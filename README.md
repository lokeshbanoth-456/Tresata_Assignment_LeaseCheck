# LeaseCheck — evidence-backed lease abstraction prototype

**Purpose:** support a finance reviewer working with lease clauses under Ind AS 116 / IFRS 16 principles. The prototype separates document text extraction, candidate field proposals, deterministic evidence checks, present-value arithmetic, and human approval.

> **Prototype limitations:** this is not accounting or legal advice. The existing 12-case dashboard uses synthetic fixtures. The new Document Lab can extract selectable text from an uploaded PDF and optionally ask a locally running Ollama model to propose fields. That live-model path has not been benchmarked on real leases. Do not describe the fixture results as AI extraction accuracy.

## Quick start (macOS/Linux)

1. Install Python 3.10+.
2. In a terminal, enter this folder and run `./run_local.sh` (or `python3 -m pip install -r requirements.txt && python3 server.py`).
3. Open `http://127.0.0.1:8765/` and select **Document Lab**.
4. Choose a text-based PDF and select **Extract text**. Text is extracted locally with `pypdf`; no OCR is included.
5. For optional AI proposals, install and start [Ollama](https://ollama.com), run `ollama pull qwen3:4b`, then use **Check Ollama** in the UI before selecting **Run local extraction**. Use `ollama list` to confirm the exact installed model name. The app calls the local Ollama HTTP endpoint, not a hosted AI API. The AI request is limited to the first 18,000 extracted characters and has a timeout so it should return a visible error rather than wait indefinitely.
6. Inspect every quote and field. A passing quote check does **not** prove that a clause is applicable, current, or not superseded by an amendment. Checkboxes require the reviewer to explicitly confirm fields before the preview calculator runs.

**Troubleshooting:** (a) Start the app with `./run_local.sh`; do not open `document_lab.html` directly from Finder. (b) If PDF extraction says no selectable text was found, the PDF is probably scanned/image-only; OCR is not yet included. Open the PDF in Preview and try selecting/copying a sentence. (c) If PDF reading fails, re-export it from Preview/Word as a new PDF and remove any password. (d) If Ollama appears to run without returning, click **Check Ollama**, confirm the selected model is installed with `ollama list`, then retry on a shorter document excerpt. The UI now shows connection/model errors and times out instead of waiting indefinitely.

The server binds to `127.0.0.1` by default. Do not expose it to a network. There is no authentication, encryption-at-rest layer, tamper-proof audit log, or production access control. Only use real confidential leases in an organization-approved environment.

## Existing synthetic dashboard

Open `index.html` directly for the original synthetic case dashboard. It has 12 authored test cases, review statuses, a deterministic calculator, and a simple browser-local audit log. The fixture proposals are hand-authored; no LLM is called in that evaluation.

Historical fixture results in the dashboard: 35/36 field decisions correct for the verified pipeline, zero wrong values silently accepted, 1 value withheld, and 12/12 expected statuses. These are **functional tests of the authored fixtures, verifier, calculator and status rules**—not a real-world benchmark. The baseline is intentionally simple. See `docs/VALIDATION.md`.

## Tests

- Original fixture-engine tests: `node tests/run_tests.js` (Node 16+).
- Document-lab regression and mocked API tests: `python3 -m unittest tests/test_document_lab.py tests/test_server_api.py -v`.
- Labelled set: `tests/data/labelled_examples.json` has 12 manually labelled **synthetic** excerpts (36 field decisions). The regex baseline exact-matched 29/36 (80.6%) on the current run; per-field results are printed by the test. This small synthetic set is useful for regression checks only, not a claim about real-world accuracy. The set has not been independently double-labelled or adjudicated by accounting experts.

## Architecture

1. **PDF text extraction:** local Python server and `pypdf`. Scanned/image-only PDFs return an error; OCR is not included.
2. **Field proposal (optional AI):** local Ollama model returns JSON proposals for term months, monthly rent, and explicit fixed annual escalation. Model output is untrusted.
3. **Evidence checks (code):** require an exact quote in the current text and a simple numerical match or explicit unit conversion. This is a useful guardrail, not semantic clause validation.
4. **Calculator preview:** deterministic monthly-in-advance present-value calculation, with a user-entered annual rate and only reviewer-confirmed fields. This is not a complete lease liability accounting engine.
5. **Human review:** every field remains subject to review. No journal posting or automatic approval is implemented.

## Important scope limits / next work

- No OCR, clause applicability, amendment reconciliation, effective-date hierarchy, conflicting schedule resolution, currency detection validation, or multi-document package processing.
- No production security, identity, role permissions, server-side audit persistence, retention controls, or tamper resistance.
- The model can hallucinate, misread a clause, follow document-borne instructions, or select a superseded figure. Quote presence alone does not eliminate those risks.
- The calculator omits several accounting inputs/adjustments and assumes a simple payment pattern. A qualified accountant must validate the applicable accounting policy and calculation conventions.
- Real-model validation requires a separately labelled lease set, dual review by qualified annotators, a stronger baseline, field-level precision/recall, false-accept and false-reject analysis, and independent calculation checks.

## Files

- `index.html` — original synthetic-case dashboard and fixture evaluation.
- `document_lab.html` — upload, text extraction, local-model proposal and review UI.
- `server.py` — local HTTP server, PDF text extraction, optional Ollama proxy.
- `tests/run_tests.js` — original fixture engine tests.
- `tests/data/labelled_examples.json` — small manually labelled synthetic evaluation set.
- `tests/test_document_lab.py` — regex baseline and quote-verifier regression tests.
- `tests/test_server_api.py` — mocked local-model API contract tests (not a real model test).
- `docs/VALIDATION.md` — evaluation interpretation and next validation plan.
- `docs/SUBMISSION_REVIEW.md` — remaining items to review honestly before submitting.


🧑‍💻 Author

Banoth Lokesh
Electrical Engineering
