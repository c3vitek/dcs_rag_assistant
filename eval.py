
"""
Eval script: runs every question from questions.json through RAG and the plain
LLM (same model) and writes a comparison to results.md and results.csv.
Includes a manual-labeling scaffold + a summary tally to fill in.
 
Run:  python eval.py    (after: python dcs_rag.py build)
"""
 
import json
import csv
import dcs_rag
 
with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)
 
rows = []
for i, item in enumerate(questions, 1):
    q = item["q"]
    print(f"[{i}/{len(questions)}] {q}")
    rag_answer, sources, hits, _ = dcs_rag.answer(q, fallback=False)
    retrieved_pages = [h["meta"]["page"] for h in hits]
    plain_answer = dcs_rag.answer_plain_llm(q)
    rows.append({
        "type": item["type"],
        "difficulty": item.get("difficulty", ""),
        "question": q,
        "expected": item["expected"],
        "expected_pages": item.get("expected_pages", []),
        "rag_answer": rag_answer.strip(),
        "retrieved_pages": retrieved_pages,
        "plain_llm": plain_answer.strip(),
    })
 
# --- Markdown report (for the paper) ---------------------------------------
with open("results.md", "w", encoding="utf-8") as f:
    f.write("# Evaluation: RAG vs. plain LLM — DCS F-16C\n\n")
    f.write(f"Model: `{dcs_rag.LLM_PROVIDER}/{dcs_rag.LLM_MODEL}`, "
            f"top-k = {dcs_rag.TOP_K}, embeddings = `{dcs_rag.EMBED_MODEL}`\n\n")
 
    f.write("## Summary tally (fill in after labeling)\n\n")
    f.write("| Metric | Score |\n|---|---|\n")
    f.write("| RAG correct | __ / 12 |\n")
    f.write("| Plain LLM correct | __ / 12 |\n")
    f.write("| Citations correct (cited page really contains the answer) | __ / 12 |\n")
    f.write("| Out-of-corpus correctly refused | __ / 3 |\n\n---\n\n")
 
    for r in rows:
        f.write(f"## [{r['type']} | {r['difficulty']}] {r['question']}\n\n")
        f.write(f"**Expected** (pages {r['expected_pages']}): {r['expected']}\n\n")
        f.write(f"**RAG** (retrieved pages {r['retrieved_pages']}):\n\n> {r['rag_answer']}\n\n")
        f.write(f"**Plain LLM** (no guide):\n\n> {r['plain_llm']}\n\n")
        f.write("**Labels:** RAG ⬜✅ ⬜🟡 ⬜❌ | Plain ⬜✅ ⬜🟡 ⬜❌ | "
                "Citation correct ⬜yes ⬜no | (if out-of-corpus) refused ⬜yes ⬜no\n\n---\n\n")
 
# --- CSV (for an appendix / analysis) --------------------------------------
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    for r in rows:
        w.writerow({k: (", ".join(map(str, v)) if isinstance(v, list) else v)
                    for k, v in r.items()})
 
print("\nDone: results.md and results.csv")
