# DCS F-16C — RAG assistant (semestral project)

RAG assistant over Chuck's Guide for the F-16C Viper module in DCS.
Pipeline: PDF → extraction (PyMuPDF) → chunking (page + split long pages) →
embeddings → vector DB (Chroma) → retrieval → answer with page citations.

Corpus: 794-page guide, ~134k words → ~1060 chunks.

## Files
- `dcs_rag.py` — core pipeline + CLI
- `app.py` — Streamlit chat UI
- `eval.py` — runs the test questions, produces `results.md` and `results.csv`
- `questions.json` — 15 test questions (12 in corpus + 3 out of corpus)
- `requirements.txt` — dependencies

## Setup in VSCode
1. Put all files **and the PDF** (`DCS_F-16C_Viper_Guide.pdf`) in one folder.
2. Open the folder in VSCode, open a terminal, create a venv:
```bash
python -m venv .venv
Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Choosing the generation model (edit top of dcs_rag.py)
- **Local, free, offline (Ollama):** install from https://ollama.com, then
  `ollama pull llama3.1`; set `LLM_PROVIDER = "ollama"`.
- **OpenAI:** set `LLM_PROVIDER = "openai"`, `LLM_MODEL = "gpt-4o-mini"`,
  and `export OPENAI_API_KEY=...`.

## Run
```bash
python dcs_rag.py build                       # build index (once)
python dcs_rag.py ask "How do I employ a JDAM?" --compare
streamlit run app.py                          # UI for the demo
python eval.py                                # evaluation -> results.md + results.csv
```
First `build` downloads the embedding model (~90 MB) and then runs offline.
Building the index over 794 pages takes a few minutes (one-time).

## Defense notes
- **Embedding model:** `all-MiniLM-L6-v2` — English, light, fast (corpus is English).
- **Chunking:** page-based, long pages split to ~1200 chars; metadata (page +
  section) gives precise citations. Near-empty pages (<80 chars) skipped.
- **Vector DB:** ChromaDB, local, zero config.
- **RAG vs plain LLM:** same model for both runs; only difference is retrieval.
- **Toward production:** larger corpus (more guides), section-aware chunking,
  reranking, hybrid search (keywords + embeddings), broader hallucination eval,
  and vision for pages where info lives only in a screenshot.
