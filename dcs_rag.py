"""
DCS RAG assistant - core pipeline (F-16C Viper, Chuck's Guide).

Pipeline:  PDF -> text extraction (PyMuPDF) -> chunking (page + split long pages)
           -> embeddings (sentence-transformers) -> vector DB (ChromaDB, local)
           -> retrieval -> answer with page citations

Usage:
    python dcs_rag.py build
    python dcs_rag.py ask "How do I start the engine?"
    python dcs_rag.py ask "..." --compare   # RAG vs. plain LLM side by side
"""

import re
import argparse

import fitz  # PyMuPDF
import chromadb
from sentence_transformers import SentenceTransformer

# --- Configuration ---------------------------------------------------------
PDF_PATH = "DCS_F-16C_Viper_Guide.pdf"
DB_DIR = "./chroma_db"
COLLECTION = "dcs_f16"
EMBED_MODEL = "all-MiniLM-L6-v2"   # English, light & fast (corpus is English)
MIN_CHARS = 80      # skip near-empty pages (pure photos)
MAX_CHARS = 1200    # split longer pages into sub-chunks (better retrieval)
TOP_K = 4

# Generation provider:
#   "ollama" = local model, free, offline (needs running Ollama)
#   "openai" = OpenAI API (needs OPENAI_API_KEY)
LLM_PROVIDER = "ollama"
LLM_MODEL = "llama3.1"     # ollama: llama3.1 / qwen2.5  | openai: gpt-4o-mini


# --- 1) Extraction + chunking ----------------------------------------------
def detect_section(text: str) -> str:
    m = re.search(r"PART\s+\d+\s*[–-]\s*([A-Z0-9 &/\-]{3,40})", text)
    return m.group(1).strip().title() if m else "Other"


def split_long(text: str, max_chars: int = MAX_CHARS):
    """Split a long page into smaller pieces on line boundaries."""
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


def extract_chunks(pdf_path: str = PDF_PATH):
    """Page-based chunks (long pages split). Each chunk carries page + section
    metadata -> precise citations."""
    doc = fitz.open(pdf_path)
    chunks = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if len(text) < MIN_CHARS:
            continue
        section = detect_section(text)
        for j, piece in enumerate(split_long(text)):
            chunks.append({
                "id": f"page-{i + 1}-{j}",
                "page": i + 1,
                "section": section,
                "text": piece,
            })
    doc.close()
    return chunks


# --- 2) Build index --------------------------------------------------------
def build_index():
    chunks = extract_chunks()
    print(f"Extracted {len(chunks)} chunks.")

    embedder = SentenceTransformer(EMBED_MODEL)
    embeddings = embedder.encode(
        [c["text"] for c in chunks], show_progress_bar=True, batch_size=64
    ).tolist()

    client = chromadb.PersistentClient(path=DB_DIR)
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass
    col = client.create_collection(COLLECTION)

    # add in batches (Chroma has a per-call limit)
    B = 1000
    for s in range(0, len(chunks), B):
        col.add(
            ids=[c["id"] for c in chunks[s:s + B]],
            embeddings=embeddings[s:s + B],
            documents=[c["text"] for c in chunks[s:s + B]],
            metadatas=[{"page": c["page"], "section": c["section"]}
                       for c in chunks[s:s + B]],
        )
    print(f"Index built in {DB_DIR} (collection '{COLLECTION}').")


# --- 3) Retrieval ----------------------------------------------------------
def retrieve(question: str, k: int = TOP_K):
    embedder = SentenceTransformer(EMBED_MODEL)
    q_emb = embedder.encode([question]).tolist()
    client = chromadb.PersistentClient(path=DB_DIR)
    col = client.get_collection(COLLECTION)
    res = col.query(query_embeddings=q_emb, n_results=k)
    return [
        {"text": d, "meta": m, "distance": dist}
        for d, m, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0])
    ]


# --- 4) Generation ---------------------------------------------------------
def call_llm(prompt: str) -> str:
    """Same model for RAG and plain baseline -> clean experiment."""
    if LLM_PROVIDER == "ollama":
        import ollama
        resp = ollama.chat(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1},
        )
        return resp["message"]["content"]
    elif LLM_PROVIDER == "openai":
        from openai import OpenAI
        client = OpenAI()
        resp = client.chat.completions.create(
            model=LLM_MODEL, temperature=0.1,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content
    raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")


def answer(question: str, k: int = TOP_K):
    hits = retrieve(question, k)
    context = "\n\n".join(
        f"[page {h['meta']['page']}, section {h['meta']['section']}]\n{h['text']}"
        for h in hits
    )
    prompt = (
        "You are a DCS assistant for the F-16C Viper module. Answer ONLY using the "
        "guide excerpts below. If the answer is not in the excerpts, say so clearly "
        "and do not make anything up. Cite the page number in parentheses for each claim.\n\n"
        f"=== GUIDE EXCERPTS ===\n{context}\n\n"
        f"=== QUESTION ===\n{question}\n\n=== ANSWER ==="
    )
    rag = call_llm(prompt)
    sources = ", ".join(f"p. {h['meta']['page']}" for h in hits)
    return rag, sources, hits


def answer_plain_llm(question: str) -> str:
    return call_llm(
        f"You are a DCS assistant for the F-16C Viper module. Answer the question:\n{question}"
    )


# --- CLI -------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="DCS F-16 RAG assistant")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("build")
    p_ask = sub.add_parser("ask")
    p_ask.add_argument("question")
    p_ask.add_argument("--compare", action="store_true")
    args = parser.parse_args()

    if args.cmd == "build":
        build_index()
    elif args.cmd == "ask":
        rag, sources, hits = answer(args.question)
        print("\n=== RAG ANSWER ===")
        print(rag)
        print(f"\nSources: {sources}")
        if args.compare:
            print("\n=== PLAIN LLM (no guide) ===")
            print(answer_plain_llm(args.question))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
