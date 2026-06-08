"""
Eval skript: projede vsechny otazky z questions.json pres RAG i holy LLM
(stejny model) a ulozi srovnani do results.md a results.csv.

Spusteni:  python eval.py
(Predtim:  python dcs_rag.py build)
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

    rag_answer, sources, hits = dcs_rag.answer(q)
    retrieved_pages = [h["meta"]["page"] for h in hits]
    plain_answer = dcs_rag.answer_plain_llm(q)

    rows.append({
        "typ": item["type"],
        "otazka": q,
        "ocekavano": item["expected"],
        "ocekavane_strany": item.get("expected_pages", []),
        "rag_odpoved": rag_answer.strip(),
        "nalezene_strany": retrieved_pages,
        "holy_llm": plain_answer.strip(),
    })

# --- Markdown tabulka (do reportu) -----------------------------------------
with open("results.md", "w", encoding="utf-8") as f:
    f.write("# Vyhodnocení RAG vs. holý LLM — DCS I-16\n\n")
    f.write(f"Model: `{dcs_rag.LLM_PROVIDER}/{dcs_rag.LLM_MODEL}`, "
            f"top-k = {dcs_rag.TOP_K}, embeddings = `{dcs_rag.EMBED_MODEL}`\n\n")
    for r in rows:
        f.write(f"## [{r['typ']}] {r['otazka']}\n\n")
        f.write(f"**Očekáváno** (strany {r['ocekavane_strany']}): {r['ocekavano']}\n\n")
        f.write(f"**RAG** (našel strany {r['nalezene_strany']}):\n\n> {r['rag_odpoved']}\n\n")
        f.write(f"**Holý LLM** (bez příručky):\n\n> {r['holy_llm']}\n\n")
        f.write("**Hodnocení** (doplň ručně): citace sedí? ⬜  RAG lepší? ⬜  "
                "u 'mimo korpus' odmítl? ⬜\n\n---\n\n")

# --- CSV (na analyzu / prilohu) --------------------------------------------
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    for r in rows:
        w.writerow({k: (v if not isinstance(v, list) else ", ".join(map(str, v)))
                    for k, v in r.items()})

print("\nHotovo: results.md a results.csv")
