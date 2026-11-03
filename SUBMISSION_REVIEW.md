# Tresata submission review — items to finish honestly

The submitted PDF brief is clear about important limitations, but its AI-use appendix contains prompts for the author that should be completed before submission. Do not invent personal contributions or claim work that was not done.

## Suggested evidence-based update

- **Prototype changes:** added a local PDF text-extraction workflow (`pypdf`), optional local Ollama field proposals, explicit quote/value checks, reviewer confirmation before calculation preview, a 12-example manually labelled synthetic regression set, tests, and validation notes.
- **What this does not prove:** the Ollama extraction path has not yet been benchmarked; the new labels are synthetic and manually authored, not independently double-labelled; quote existence does not establish clause applicability; and the preview is not a complete accounting engine.
- **AI-use appendix:** describe which assistant/model generated which parts of the prototype and report, using the actual interaction history available to you. Distinguish generated suggestions from changes you personally reviewed, tested, or edited.
- **Personal contribution:** the author must state, in their own words, what they personally decided, implemented, tested, corrected, or learned. Replace any bracketed placeholder in the original PDF with a truthful statement.
- **References:** verify every reference and any claim about standards or vendors against the original publication before submission. Do not treat a vendor's marketing claim as independently validated evidence.

## Suggested one-sentence limitations statement

“The current prototype demonstrates a local document-to-review workflow and tests deterministic guardrails on synthetic examples; live-model accuracy, clause applicability, amendment handling, production security, and full accounting compliance remain unvalidated.”
