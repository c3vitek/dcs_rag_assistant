"""
DCS RAG assistant - core pipeline.

Supports multiple aircraft guides, a relevance-threshold fallback, and
page-cited answers.

Usage:
    python dcs_rag.py build                       # build default guide
    python dcs_rag.py build --all                 # build every guide whose PDF exists
    python dcs_rag.py build --guide "I-16 Ishak"
    python dcs_rag.py ask "How do I start the engine?"
    python dcs_rag.py ask "..." --compare
"""

import os
import re
import argparse

import fitz  # PyMuPDF
import chromadb
from sentence_transformers import SentenceTransformer

# --- Guides (multi-aircraft switch) ----------------------------------------
GUIDES = {
    "F-16C Viper": {"pdf": "DCS_F-16C_Viper_Guide.pdf", "collection": "dcs_f16"},
    "I-16 Ishak":  {"pdf": "DCS_I-16_Ishak_Guide.pdf",  "collection": "dcs_i16"},
}
DEFAULT_GUIDE = "F-16C Viper"

# --- Configuration ---------------------------------------------------------
DB_DIR = "./chroma_db"
EMBED_MODEL = "all-MiniLM-L6-v2"
MIN_CHARS = 80
MAX_CHARS = 1200
TOP_K = 5                      # a bit higher -> more complete answers
RELEVANCE_THRESHOLD = 0.7      # cosine distance; above this = "guide likely lacks it"
                               # tune empirically (compare in-corpus vs out-of-corpus)

LLM_PROVIDER = "openai"        # "openai" or "ollama"
LLM_MODEL = "gpt-4o-mini"

_embedder = None
def embedder():
    """Load the embedding model once (lazy singleton)."""
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer(EMBED_MODEL)
    return _embedder


# --- 1) Extraction + chunking ----------------------------------------------
def detect_section(text):
    m = re.search(r"PART\s+\d+\s*[–-]\s*([A-Z0-9 &/\-]{3,40})", text)
    return m.group(1).strip().title() if m else "Other"


def split_long(text, max_chars=MAX_CHARS):
    if len(text) <= max_chars:
        return [text]
    parts, cur = [], ""
    for line in text.split("\n"):
        if len(cur) + len(line) + 1 > max_chars and cur:
            parts.append(cur.strip())
            cur = ""
        cur += line + "\n"
    if cur.strip():
        parts.append(cur.strip())
    return parts


def extract_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if len(text) < MIN_CHARS:
            continue
        section = detect_section(text)
        for j, piece in enumerate(split_long(text)):
            chunks.append({"id": f"page-{i+1}-{j}", "page": i + 1,
                           "section": section, "text": piece})
    doc.close()
    return chunks


# --- 2) Build index --------------------------------------------------------
def build_index(guide=DEFAULT_GUIDE):
    cfg = GUIDES[guide]
    chunks = extract_chunks(cfg["pdf"])
    print(f"[{guide}] extracted {len(chunks)} chunks.")

    # normalized embeddings + cosine space -> distances in [0,2], comparable
    embs = embedder().encode([c["text"] for c in chunks],
                             show_progress_bar=True, batch_size=64,
                             normalize_embeddings=True).tolist()

    client = chromadb.PersistentClient(path=DB_DIR)
    try:
        client.delete_collection(cfg["collection"])
    except Exception:
        pass
    col = client.create_collection(cfg["collection"],
                                   metadata={"hnsw:space": "cosine"})

    B = 1000
    for s in range(0, len(chunks), B):
        col.add(
            ids=[c["id"] for c in chunks[s:s+B]],
            embeddings=embs[s:s+B],
            documents=[c["text"] for c in chunks[s:s+B]],
            metadatas=[{"page": c["page"], "section": c["section"]}
                       for c in chunks[s:s+B]],
        )
    print(f"[{guide}] index built (collection '{cfg['collection']}').")


# --- 3) Retrieval ----------------------------------------------------------
def retrieve(question, guide=DEFAULT_GUIDE, k=TOP_K):
    q_emb = embedder().encode([question], normalize_embeddings=True).tolist()
    client = chromadb.PersistentClient(path=DB_DIR)
    col = client.get_collection(GUIDES[guide]["collection"])
    res = col.query(query_embeddings=q_emb, n_results=k)
    return [
        {"text": d, "meta": m, "distance": dist}
        for d, m, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0])
    ]


# --- 4) Generation ---------------------------------------------------------
def call_llm(prompt):
    if LLM_PROVIDER == "ollama":
        import ollama
        return ollama.chat(model=LLM_MODEL,
                           messages=[{"role": "user", "content": prompt}],
                           options={"temperature": 0.1})["message"]["content"]
    elif LLM_PROVIDER == "openai":
        from openai import OpenAI
        return OpenAI().chat.completions.create(
            model=LLM_MODEL, temperature=0.1,
            messages=[{"role": "user", "content": prompt}],
        ).choices[0].message.content
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")


def answer(question, guide=DEFAULT_GUIDE, k=TOP_K, fallback=False):
    """Returns (text, sources, hits, low_confidence).
    fallback=True  -> if no good match, warn and answer from general knowledge.
    fallback=False -> pure RAG (use this for evaluation)."""
    hits = retrieve(question, guide, k)
    best = hits[0]["distance"] if hits else 1e9
    low_conf = best > RELEVANCE_THRESHOLD

    if low_conf and fallback:
        text = ("⚠️ The guide doesn't seem to cover this well — answering from "
                "general knowledge instead (not grounded in the guide):\n\n"
                + answer_plain_llm(question, guide))
        return text, "(no good match in guide)", hits, True

    context = "\n\n".join(
        f"[page {h['meta']['page']}, section {h['meta']['section']}]\n{h['text']}"
        for h in hits
    )
    prompt = (
        f"You are a DCS assistant for the {guide} module. Answer the question using "
        "ONLY the guide excerpts below. Combine information from ALL relevant excerpts "
        "into one complete, thorough answer (don't stop at the first excerpt). If the "
        "answer is not in the excerpts, say so clearly and do not invent anything. "
        "Cite the page number in parentheses for each claim.\n\n"
        f"=== GUIDE EXCERPTS ===\n{context}\n\n"
        f"=== QUESTION ===\n{question}\n\n=== ANSWER ==="
    )
    rag = call_llm(prompt)
    sources = ", ".join(f"p. {h['meta']['page']}" for h in hits)
    return rag, sources, hits, low_conf


def answer_plain_llm(question, guide=DEFAULT_GUIDE):
    return call_llm(
        f"You are a DCS assistant for the {guide} module. Answer the question:\n{question}"
    )


# --- CLI -------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description="DCS RAG assistant")
    sub = p.add_subparsers(dest="cmd")
    pb = sub.add_parser("build")
    pb.add_argument("--guide", default=DEFAULT_GUIDE)
    pb.add_argument("--all", action="store_true")
    pa = sub.add_parser("ask")
    pa.add_argument("question")
    pa.add_argument("--guide", default=DEFAULT_GUIDE)
    pa.add_argument("--compare", action="store_true")
    args = p.parse_args()

    if args.cmd == "build":
        if args.all:
            for g, cfg in GUIDES.items():
                if os.path.exists(cfg["pdf"]):
                    build_index(g)
                else:
                    print(f"[{g}] skipped (PDF not found: {cfg['pdf']})")
        else:
            build_index(args.guide)
    elif args.cmd == "ask":
        rag, sources, hits, low = answer(args.question, args.guide, fallback=True)
        print("\n=== ANSWER ===")
        print(rag)
        print(f"\nSources: {sources}  (best distance {hits[0]['distance']:.3f})")
        if args.compare:
            print("\n=== PLAIN LLM (no guide) ===")
            print(answer_plain_llm(args.question, args.guide))
    else:
        p.print_help()


if __name__ == "__main__":
    main()