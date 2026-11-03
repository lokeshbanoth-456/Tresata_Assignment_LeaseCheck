# LeaseCheck: evidence-backed lease abstraction for lease-liability review

**Tresata take-home submission draft · India (Ind AS 116) · Synthetic data only**

## 1. Problem and user

Finance and accounting teams must inspect lease agreements and related documents, identify payment terms, and calculate a lease liability under the applicable accounting policy. Important inputs can be distributed across clauses, schedules, renewals, and amendments. A plausible extracted number is not enough: the reviewer needs to know where it came from and whether that clause governs the current lease.

The target user is a lease accountant or finance reviewer, with an auditor as a secondary user. The prototype focuses narrowly on the path from document text to a small set of candidate fields, evidence checks, a simplified present-value preview, and explicit human review. It does not decide whether a contract contains a lease or handle a complete lease-accounting lifecycle.

## 2. Hypothesis and proposed gap

**Hypothesis:** for selected lease fields, a system that requires an exact source quote and a deterministic support check before a value can be used in a calculation will reduce unsupported values reaching the calculator compared with a simple regex baseline.

This is a testable control hypothesis, not a claim of product novelty. Commercial vendors advertise AI-assisted extraction, evidence/source links, and accounting workflows. The unresolved question is whether their actual implementations prevent unsupported or superseded values from flowing into calculations. This has not been verified by hands-on vendor testing.

## 3. Workflow and architecture

1. **Document intake and text extraction:** the Document Lab accepts a PDF and extracts selectable text locally using `pypdf`. Image-only scans are rejected; OCR is not implemented.
2. **Candidate field proposal:** an optional locally hosted Ollama model proposes lease term in months, base monthly rent, and an explicitly stated fixed annual escalation. Each proposal must include a verbatim quote. The model output is treated as untrusted.
3. **Deterministic evidence checks:** code checks that the exact quote occurs in the current text and that the number supports the proposed value, allowing only simple, explicit unit conversions. A passed quote check does not establish clause applicability, priority, or whether an amendment supersedes it.
4. **Calculation preview:** deterministic code calculates a simplified present value for monthly payments in advance, using an effective monthly rate and fixed annual escalation. The reviewer must explicitly confirm the term and rent fields before a preview is shown. The user supplies the discount rate; the prototype does not infer it.
5. **Human decision:** the finance reviewer checks the source, context, policy, and calculation before accepting any result. The prototype does not post journal entries or automatically approve leases.

The original synthetic dashboard remains available for reviewing 12 fixed cases. The new Document Lab is a separate live-document workflow. This distinction is intentional: the original fixtures do not measure language-model extraction performance.

## 4. Prototype evaluation

### Existing 12-case fixture suite

The original dashboard reports 35/36 field decisions correct for the verified pipeline, zero wrong values silently accepted, one value withheld, and 12/12 expected statuses. Its proposals and cases are authored fixtures. These results test deterministic verification, calculation, and review-state logic—not real AI extraction accuracy. The regex baseline is deliberately simple, so the result is not a fair comparison against a strong production baseline.

### Additional labelled synthetic set

A separate set of 12 manually labelled synthetic lease excerpts tests a transparent regex baseline on three fields (36 field decisions). The current run exact-matches 29/36 decisions (80.6%): term 11/12, monthly rent 6/12, and escalation 12/12. The rent misses show that this baseline is rudimentary. The labels were prepared separately from model output, but the set has not been independently double-labelled or adjudicated by an accounting expert. It is a regression test, not evidence of real-world performance.

### Live AI status

The local Ollama integration has been implemented but has not been evaluated against real lease documents in this environment. No real-model accuracy, latency, or error-rate claim is made. A model can still return a quote from the wrong clause, misread an amendment, or omit a critical condition.

## 5. Alternatives considered

- **One LLM extracts and calculates everything:** rejected because arithmetic and policy controls should be deterministic and independently testable.
- **Regex-only extraction:** useful as a baseline and for simple patterns, but wording variation and context create missed or incorrect values. A stronger baseline is still needed for a fair comparison.
- **Retrieval-augmented generation:** not required for a single short document in the first prototype. It becomes relevant for multi-document portfolios, amendments, and cross-references; retrieval alone would not prove which clause governs.
- **Multi-agent architecture:** not justified for this narrow task without evidence that separate agents improve measurable outcomes.
- **Fine-tuning:** premature without a permissioned, representative, labelled corpus and a stable evaluation suite.
- **Automatic approval or posting:** excluded because accounting judgement, policy inputs, evidence applicability, and exception handling require human accountability.

## 6. Risks and controls

| Risk | Current control | Remaining gap |
|---|---|---|
| Hallucinated or unsupported number | Exact quote and numeric support checks | A real quote may still be from the wrong or superseded clause |
| Conflicting or missing values | Missing proposals and simple conflicts are flagged in fixture workflow | Full clause conflict and amendment resolution not implemented |
| Prompt injection inside a lease | Prompt tells local model to treat document text as untrusted | Live model behavior has not been tested; prompt instructions are not a security boundary |
| Incorrect discount rate or payment convention | Rate is a reviewer-entered input; calculator is deterministic | Effective-dated policy, approval, currency and complete accounting adjustments not implemented |
| Privacy and confidentiality | Local PDF extraction and optional local Ollama path; server binds to loopback by default | No authentication, role-based access, retention controls, encrypted storage, or tamper-proof audit trail |
| False confidence from demo results | UI and docs label fixture data and limits | Live model benchmark and independent expert review still required |

## 7. Scope and accounting caveat

The prototype is not a full Ind AS 116 implementation. It excludes lease identification, lessor accounting, lease modifications and remeasurement, renewal-option judgement, variable payments beyond flags, incentives, initial direct costs, residual value guarantees, low-value policy elections, journal posting, and tax. The calculator uses a simplified payment pattern and should not be treated as a booked accounting amount. The applicable standard and the entity's accounting policy must be checked by a qualified professional.

## 8. Next validation plan

1. Use public or approved de-identified lease documents.
2. Have two reviewers independently label the relevant fields and exact evidence spans, then resolve disagreements with an accounting subject-matter expert.
3. Freeze the labels before running models.
4. Compare a stronger regex/rule baseline, local model alone, and local model plus verification.
5. Report field-level precision/recall, exact match, quote validity, false acceptance of wrong values, false rejection of valid values, reviewer correction time, and latency.
6. Add amendments, rent schedules, tables, scans/OCR, conflicting clauses, CPI-linked rents, annual-versus-monthly amounts, renewal options, missing fields, and document-borne malicious instructions.
7. Have an accountant independently recompute a sample of liabilities and approve the calculation conventions.
8. Design and test privacy, access control, audit integrity, retention, and deployment controls before production use.

## 9. AI-use disclosure draft

The prototype and written brief were reviewed and revised with ChatGPT assistance. In this revision, ChatGPT helped add a local PDF text-extraction workflow, an optional local Ollama proposal endpoint, evidence-check UI, synthetic regression tests, and documentation of limitations. The existing dashboard's 12 case proposals remain hand-authored fixtures. The new local-model path has not been benchmarked against real leases; the reported regression-set metrics are from synthetic examples only.

**Author completion required:** add the actual initial prompt(s) used with other tools/models if relevant; state which generated changes you personally reviewed, tested, or edited; explain one suggestion you rejected or corrected; and write in your own words what you personally contributed and what you can defend in an interview. Do not claim personal implementation or independent validation unless it is true.

## References to verify before final submission

- Ministry of Corporate Affairs, Government of India: Ind AS 116, Leases — https://www.mca.gov.in/bin/ebook/dms/getdocument?doc=MTk1MDM2ODIw&docCategory=Accounting+Standards&type=open
- Ollama API documentation, `/api/chat` and structured outputs — https://github.com/ollama/ollama/blob/main/docs/api.md

Check the latest applicable standard, entity accounting policy, and all vendor claims before making definitive compliance or competitive statements.
