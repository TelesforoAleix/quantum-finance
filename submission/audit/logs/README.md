# `audit/logs/` — Pipeline execution logs (full LLM call audit trail)

Timestamped JSONL logs from every pipeline phase that invoked the LLM client (Azure OpenAI). Provides a complete audit trail of model calls, prompts, responses, timing, and configuration for every phase that produced an artifact.

## Provenance

These logs are the **union of both researchers' local execution histories**:

- Files dated when each researcher actively ran the pipeline on their machine.
- Two researchers ran independent sessions; both contributions are merged here.
- One conflicting filename (`2026-04-22_llm_client.jsonl`) is preserved as two distinct files: the curator's copy under the original name, and the collaborator's copy with the suffix `__<user>`.
- In the operational repository these logs are gitignored; they are materialised here for examiner reproducibility.

## File patterns

`<DATE>` is `YYYY-MM-DD` of the run.

### Phase 1 — framework synthesis

| Pattern | Purpose |
|---------|---------|
| `<DATE>_phase1_batch.jsonl` | Per-batch ingestion / Zotero pull events |
| `<DATE>_phase1_extraction.jsonl` | Per-paper extraction events |

### Phase 2 — systematic review and classification

| Pattern | Purpose |
|---------|---------|
| `<DATE>_run_classification.jsonl` | Phase 2 classification orchestrator |
| `<DATE>_step_runner.jsonl` | Step-by-step runner state |
| `<DATE>_processing_log.jsonl` | Pipeline-wide processing events |
| `<DATE>_text_chunker.jsonl` | Text-chunker tokenisation log |
| `<DATE>_ab_test.jsonl` | Prompt/model A/B comparisons |
| `<DATE>_test.jsonl`, `<DATE>___main__.jsonl` | Smoke / harness runs |

### Phase 3 — thematic synthesis

| Pattern | Purpose |
|---------|---------|
| `<DATE>_b1_calls.jsonl`, `b2_calls.jsonl`, `l3_calls.jsonl` | B1 batch themes, B2 silo themes, L3 adversarial review LLM calls (per-stage prompt + response metadata) |
| `<DATE>_c3_per_silo.jsonl` | C3 cross-silo crosswalk runs |
| `<DATE>_batch_api.jsonl` | Azure OpenAI batch-API submissions |
| `<DATE>_benchmark_batch.jsonl`, `extract_benchmarks.jsonl`, `aggregate_benchmarks.jsonl` | S2 quantitative benchmark extraction batches |
| `<DATE>_build_indices.jsonl`, `build_citation_graph.jsonl`, `report_missing_papers.jsonl` | S2/S3 corpus-wide index builders |
| `<DATE>_detect_contradictions.jsonl` | Cross-paper contradiction scan |
| `<DATE>_chapter_lit_notes.jsonl` | Manuscript-side per-paper literature notes |
| `<DATE>_openalex_client.jsonl` | OpenAlex metadata lookups (no LLM) |

### Phase 4 — experiments and resource estimation

| Pattern | Purpose |
|---------|---------|
| `<DATE>_audit_phase8_F21.log`, `audit_phase8d.log`, `audit_phase8e.log`, `audit_phase9.log` | Per-phase audit script stdout |
| `<DATE>_phase8b_*.log`, `phase8c_F21.log`, `phase8d_*.log` | Phase-8 sweep runner stdout |
| `<DATE>_aggregate_F21.log`, `phase11_cleanup.log` | Phase 8/11 maintenance runs |

### Cross-cutting

| Pattern | Purpose |
|---------|---------|
| `<DATE>_llm_client.jsonl` | Raw LLM API call / response bodies (any phase) |
| `<DATE>_llm_client__<user>.jsonl` | Same shape; collaborator-attributed copy when filenames collide |

## How to use

- **Reproduce a specific result**: locate the `<DATE>` of the pipeline run that produced the artifact (cross-reference with `processing_log.json` in each phase folder), then read the corresponding `*_calls.jsonl` for that date.
- **Audit a specific LLM call**: search by `paper_id` or `git_sha` field across the JSONL files.
- **Re-run with the same prompts**: the prompt templates live in `<phase>/prompts/`; the version logs live in `<phase>/prompts/VERSION_LOG.md`.

## Cross-references

- Companion in-phase logs: `p3_thematic_synthesis/s6_silo_framing/logs/`, `p2_systematic_review/processing_log.json`
- Audit policy: project root `FAIR_USE.md` and `manuscript` Annex H (AI-Use Declaration)
