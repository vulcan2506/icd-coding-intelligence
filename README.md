# ICD-10-CM Coding Intelligence Pipeline

Turns a folder of multi-version regulatory guideline PDFs into a retrieval-augmented
chatbot that is measurably better than a plain vector-search baseline — and proves it,
on every change, against three other retrieval methods.

This is a domain-generalization showcase: the same pipeline and retrieval stack
originally built for HealthRules Payer release notes, run unmodified against a
completely different domain — the CMS ICD-10-CM Official Guidelines for Coding
and Reporting (FY25 vs. October 2025). Every prompt, role, and worked example the
LLM sees is derived at build time from the actual document content (see
`Stage 1/context_profiler.py`), not hardcoded to either domain.

## What's in here

```
Stage 1/           offline ingestion pipeline — PDFs -> chunked, labeled, taxonomy-aware
                   knowledge base (run once per corpus update)
retrieval_layer/   the serving layer — routing, reranking, confidence-gated retrieval,
                   evaluation harness, Redis-cached chatbot CLI
```

Two phases, one venv. `Stage 1/` reads raw PDFs and writes structured JSON/CSV artifacts.
`retrieval_layer/` reads those artifacts, builds a vector index, and answers questions.

The pre-built corpus (`Stage 1/data/`, `retrieval_layer/chroma_db/`, `retrieval_layer/index/`)
ships committed in this repo — both source PDFs are public CMS documents, so unlike the
original HealthRules corpus there's nothing proprietary to exclude. Chat works immediately
without re-running the pipeline.

## Quick start

```bash
cd "Stage 1"
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You'll also need two things running locally (not pip-installable):

```bash
bash start_server.sh                # local Qwen3.5-9B LLM via llama.cpp, port 8080
sudo systemctl start redis-server   # response cache for the demo
```

### Re-run the pipeline (only needed if you swap in different PDFs)

```bash
cd "Stage 1"
python main.py         # ingest -> label -> group -> build taxonomy
python run_tail.py     # cross-version analysis -> evolution cards -> index -> ChromaDB -> eval
```

### Ask it questions

```bash
cd retrieval_layer
python cli.py                              # interactive chat — gated, cached, sessioned
python cli.py "What changed in sepsis coding guidance between versions?"
python cli.py --raw --compare "..."        # see pipeline vs naive vs traditional RAG
```

Any flag can also be typed inline as part of the question itself, e.g.
`--detailed what changed in excludes1 notes?`.

## What makes this more than a basic RAG demo

- **Self-comparing.** Every retrieval path (pipeline, naive, traditional RAG, and two pooled
  ensembles) is measured head-to-head on the same query set, on both retrieval quality
  and generated-answer quality (faithfulness, correctness, completeness).
- **Dynamic confidence gating, not a fixed router.** The production path runs the cheap
  method first, measures its own confidence live, and only escalates to a more expensive
  pooled method when a specific query actually needs it.
- **Version-aware.** Detects when an answer would blend facts from two different document
  versions and injects the actual delta report instead of silently merging them.
- **Domain-adaptive prompting.** A one-time content-profiling pass derives the domain,
  analyst persona, terminology, and worked examples used by every downstream prompt
  (labeling, delta analysis, Q&A generation, evolution/value-add synthesis, and the live
  chat system prompt) — swap the PDFs and every prompt re-derives itself, no hardcoded
  domain vocabulary.
- **Redis-backed caching** for instant, zero-token demo answers, side by side with the real
  live path for comparison.

## Where to look next

- `Stage 1/requirements.txt` — pinned dependencies for the whole project (both folders
  share one venv).
- `DEPLOY.md` — HF Spaces (backend) + Vercel (frontend) deploy instructions.
