# Validation note

## What was tested

### A. Original fixture engine

The original dashboard includes 12 synthetic lease snippets and predefined proposals. Its current evaluation reports 35/36 field decisions correct for the verified pipeline, zero wrong values silently accepted, one withheld value, and 12/12 expected statuses. The original Node test suite also checks the deterministic present-value calculation and rejection of missing/mismatched quotes.

**Interpretation:** these tests provide functional evidence for the hand-authored cases and control logic. They do not estimate how well a language model extracts real contracts, because no model generated those proposals. The expected statuses and proposal fixtures were authored by the project builder. The simple regex baseline is not a strong production comparator.

### B. New labelled synthetic set

`tests/data/labelled_examples.json` contains 12 short, synthetic excerpts with manually assigned labels for term months, base monthly rent, and explicitly stated annual escalation (36 field decisions). The test script evaluates a transparent regex baseline and checks quote-verification guardrails. The latest local run exact-matched 29/36 field decisions (80.6%): term 11/12, monthly rent 6/12, escalation 12/12.

This result is deliberately reported as a small regression-set result. It is not independently double-labelled, is not based on real contracts, and does not validate the LLM proposal path. The regex extractor is intentionally small and misses several rent phrasings. It is a baseline to improve, not evidence that AI outperforms current systems.

## What is not yet validated

- The local Ollama model's extraction precision/recall or hallucination rate.
- Scanned PDFs/OCR, tables, handwritten material, amendments, conflicting clauses, currency, commencement dates, extension options, or applicability of a clause to the current contract.
- Whether a quote is from the governing clause or a superseded amendment.
- The accounting correctness of the full lease liability under a particular policy; the calculator covers only a simplified payment pattern.
- Comparative performance against a strong rule-based baseline or a commercial product.

## Recommended next experiment

1. Obtain permission to use a small de-identified or public contract set.
2. Have two reviewers independently label fields and exact evidence spans; resolve disagreements with an accounting subject-matter expert.
3. Freeze the labels before running any model. Track term/rent/escalation exact-match accuracy, quote validity, unsupported-value acceptance, missing-value rate, and reviewer correction time.
4. Compare (a) strong regex/rule baseline, (b) local model alone, and (c) local model plus evidence verification.
5. Include hard negatives: amendments, conflicting rent clauses, renewal options, annual-vs-monthly amounts, CPI-linked rent, missing terms, irrelevant monetary figures, and malicious instructions inside documents.
6. Have a qualified accountant independently recompute a sample of liabilities and verify the payment convention and discount-rate policy.
7. Do not claim production readiness until privacy, access control, audit integrity, retention, OCR, and amendment handling have been designed and tested.
