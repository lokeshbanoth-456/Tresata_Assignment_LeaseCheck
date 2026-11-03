I am working on a take-home assignment for Tresata. The assignment asks me to choose an area of finance, identify one real problem, design an AI-based solution, and explain the architecture, risks, alternatives, and human involvement.

I am considering invoice verification, where businesses compare supplier invoices with purchase orders before approving payments.

Help me investigate this problem systematically. Identify the users, their workflow, the specific pain points, the potential business impact, and the situations where existing rule-based automation may be insufficient. Distinguish established facts from assumptions that require research.

Do not immediately propose a complicated architecture. First, help me determine whether this is a sufficiently specific and defensible problem for the assignment. Suggest what evidence I should collect and which questions I should answer before building a prototype.
Tresata Take-Home Assignment: Investigating AI-Based Invoice Verification
Your idea—using AI to verify supplier invoices against purchase orders before payment approval—is a promising starting point for the Tresata assignment.

But the important question is not whether AI can compare two documents. It is:

Can we identify a specific, costly problem in invoice verification that existing automation does not solve reliably, and demonstrate how an AI-based solution would improve the outcome?

That distinction will make your submission much more convincing. You need to show that you understand the financial process, the people involved, the limitations of current solutions, and the business value of solving a particular problem.

I recommend investigating the problem in six stages, without committing to a complicated architecture or building a prototype yet.

1. Define the problem you are investigating
Businesses receive invoices from suppliers and need to verify them before paying. The invoice may need to be checked against a purchase order (PO), a record of goods or services received, and other supporting information.

For example, suppose a company orders 100 units of a component at ₹500 per unit.

Purchase order: 100 units × ₹500 = ₹50,000.
Supplier invoice: 100 units × ₹550 = ₹55,000.
Difference: ₹5,000.
The accounts payable team must determine whether the difference is an error, an authorized price change, an additional charge, or a potentially invalid request for payment.

The arithmetic is straightforward. Determining why the difference exists and whether the invoice should be approved is the more interesting problem.

Three possible problem statements
Option	Problem	Potential AI contribution
A. Invoice data extraction	Supplier invoices arrive in different layouts, formats, and levels of quality.	Extract and normalize relevant information from documents.
B. Complex invoice discrepancies	An invoice differs from its purchase order or receipt records, and the reason is unclear.	Interpret discrepancies using multiple documents, business context, and historical cases.
C. Suspicious invoice detection	Some invoices may be duplicates, altered, inconsistent, or otherwise suspicious.	Identify unusual patterns and prioritize invoices for investigation.
These are related problems, but they are not interchangeable.

My initial recommendation is Option B: investigating ambiguous invoice discrepancies.

It offers a clearer opportunity to examine where fixed rules may struggle, where AI might add value, and where a human decision-maker remains necessary.

However, that recommendation is provisional. You should validate whether the problem is sufficiently common, costly, and inadequately addressed by existing systems before selecting it.

2. Identify the users and understand their workflow
Before discussing AI, understand who handles an invoice and who has the authority to approve it.

A. The key users
User	Responsibility	Potential problem
Accounts payable (AP) analyst	Checks invoices, verifies details, and investigates exceptions.	Spends time resolving discrepancies that require looking across several records.
Procurement team	Manages purchase orders, negotiated prices, and supplier relationships.	Must clarify whether a price or quantity difference is legitimate.
Receiving or warehouse team	Confirms goods received or records service completion.	Missing or delayed receipt records can prevent invoice matching.
Department manager or budget owner	Confirms business justification and approves eligible expenses.	May lack the context needed to approve an exception quickly.
Finance controller	Oversees payment controls, financial accuracy, and compliance.	Needs reliable controls and evidence supporting payment decisions.
Supplier	Issues invoices and corrects billing errors.	May face delayed payments because of unresolved exceptions.
These roles are a starting point, not a claim that every organization uses the same structure. In a small business, one person may perform several of these roles.

B. Map the existing workflow
A typical purchase-order-based invoice process looks like this:

Purchase: The business creates and approves a purchase order.
Receipt: The business records the goods received or the service completed.
Invoice arrival: The supplier sends an invoice, usually electronically or through another established channel.
Data capture: Relevant invoice information is entered into or extracted for the accounting system.
Matching: The system compares the invoice with the purchase order and, where applicable, the receipt record.
Exception handling: If a discrepancy violates the organization's rules, the invoice is investigated.
Approval: An authorized person approves the invoice or its exception.
Payment: The approved invoice proceeds through the payment process.
The matching process can involve two-way matching (invoice against purchase order) or three-way matching (invoice, purchase order, and receipt). These are established capabilities in enterprise finance software, not new AI innovations. 

C. Where does the process become difficult?
Consider this example:

A company orders 100 components at ₹500 each. The supplier delivers 100 components, but the invoice charges ₹520 each.

The matching system identifies a ₹2,000 discrepancy.

Now consider three explanations:

Case 1 — Billing error: The supplier accidentally charged the wrong price.
Case 2 — Legitimate change: The buyer and supplier agreed to a revised price, but the purchase order was not updated.
Case 3 — Unsupported charge: The supplier charged a higher price without authorization.
The numerical discrepancy is identical in all three cases, but the correct action differs.

Situation	Appropriate action
Confirmed billing error	Request a corrected invoice or follow the organization's correction process.
Authorized price change	Verify the authorization and supporting evidence before proceeding.
Unsupported price change	Escalate the exception and withhold approval until resolved.
This is the potential problem worth investigating: Can a system help AP analysts resolve ambiguous invoice discrepancies by finding relevant evidence, explaining the likely cause, and recommending the next action?

Notice the distinction: the system should not assume that a price difference is fraud, nor should it automatically approve a discrepancy simply because it resembles a previously accepted one.

3. Distinguish established facts from assumptions
This distinction is essential for a defensible assignment. A plausible business problem is not the same as a proven business opportunity.

Here is the evidence status of the main claims.

Claim	Current status	What supports or would validate it?
Invoice verification can involve matching invoices, POs, and receipts.	Established fact.	Enterprise software documentation describes these processes. 
Matching systems can apply configurable tolerances to price and quantity differences.	Established fact.	Microsoft and SAP documentation describe matching rules and tolerance settings. 
Some invoices require investigation when discrepancies occur.	Established fact.	Invoice-processing documentation describes exception handling. 
Ambiguous exceptions consume substantial analyst time.	Plausible and supported qualitatively; magnitude unverified for your target customer.	Measure exception rates and time spent investigating them.
Existing rule-based systems cannot resolve these discrepancies adequately.	Unproven and too broad.	Compare the proposed use case with existing systems and identify a specific remaining limitation.
AI can identify the correct reason for a discrepancy more accurately than existing tools.	Hypothesis.	Evaluate AI against real, independently verified exception cases.
AI will reduce processing costs or payment delays.	Hypothesis.	Measure baseline performance and compare it with a controlled pilot.
Businesses will pay for this capability.	Commercial hypothesis.	Interview potential customers and investigate their current solutions and budgets.
One important finding from the research is that the market already includes AI-assisted invoice matching. For example, Sage Intacct's 2026 release documentation describes AI-driven, line-level matching across purchase orders, receiving records, and invoices. 

That matters because your assignment should not claim that AI-based invoice matching does not exist.

Instead, you need to identify a specific unresolved problem that existing tools do not address adequately for your intended users.

A strong submission acknowledges existing capabilities and explains why a particular gap remains worth solving.

4. Investigate the pain points and business impact
You need to determine whether the problem is important enough to justify a new solution.

A. Potential pain points
Start with these five areas.

1. Repeated manual investigation

An AP analyst identifies a mismatch, searches for supporting records, contacts procurement or the supplier, and waits for clarification.

Research question: How much analyst time is spent resolving each type of exception?

2. Missing context

The invoice and purchase order may not explain whether a discrepancy was authorized. The relevant evidence might be in an email, an amended contract, an approval record, or a separate receipt.

Research question: Which information sources do analysts consult to resolve discrepancies, and how often is necessary evidence unavailable?

3. Incorrect exception classification

A system may correctly flag a price mismatch but provide little help determining whether the discrepancy is an error, an authorized change, or an unresolved issue.

Research question: Do existing tools identify the underlying cause, or do they simply flag the mismatch?

4. Delayed payments

Unresolved exceptions can delay invoice approval and payment scheduling.

Research question: How much processing time is attributable specifically to invoice discrepancies, rather than other approval delays?

5. Repeated problems

The same supplier, purchasing category, or internal process may generate similar exceptions repeatedly.

Research question: Can the business identify recurring causes and prevent future exceptions, rather than investigating each invoice independently?

These are plausible problems to investigate, not five problems you should automatically claim to have solved.

B. What does the published evidence tell us?
A useful starting point is the 2025 State of ePayables research from Ardent Partners, distributed through Tradeshift.

The report gives the following average accounts payable benchmarks:

Metric	Published benchmark
Cost to process an invoice	$9.84
Invoice processing time	8.2 days
Invoice exception rate	18.4%
Invoices processed without manual intervention	35.4%
Source: Ardent Partners' State of ePayables 2025

These figures suggest that invoice processing and exception handling are meaningful operational concerns. However, they do not establish that your proposed AI solution would improve performance.

The data also has limitations:

These are industry benchmarks, not measurements from your intended customer.
The processing-time metric should not automatically be interpreted as the time spent resolving an exception.
The exception rate includes different types of problems, not just ambiguous purchase-order discrepancies.
The processing cost is not a direct estimate of the savings achievable through AI.
You should use these statistics to establish context, not to promise a particular percentage of cost savings.

C. Translate the problem into measurable business value
Suppose a hypothetical business processes 100,000 invoices annually.

For illustration, assume 18% require manual exception handling and each exception takes an average of 20 minutes to resolve.

These are hypothetical assumptions, not industry facts.

The estimated annual exception workload would be:

Exceptions: 100,000 × 18% = 18,000.
Time spent: 18,000 × 20 minutes = 360,000 minutes.
Total: 6,000 staff-hours annually.
If a pilot demonstrated that your solution reduced the average handling time from 20 minutes to 12 minutes, the business would save:

18,000 × 8 minutes = 144,000 minutes, or 2,400 staff-hours annually.

This calculation assumes the exception count remains constant and every exception receives the same time saving. A real evaluation would need to account for differences between cases, additional review time, and operating costs.

The example illustrates why measuring exception-handling time could be more informative than merely measuring how many invoices the AI processes.

Other useful metrics include:

Metric	What it tells you
Exception rate	How frequently invoices require intervention.
Average resolution time	How much time is spent resolving an exception.
Time to payment readiness	Whether the solution speeds up the overall process.
First-pass resolution rate	How often an exception is resolved without repeated investigation.
False-clearance rate	How often the system recommends clearing an exception that should remain unresolved.
Cost per resolved exception	Whether the solution reduces operational expenditure.
For a finance-related AI system, the false-clearance rate is particularly important. A faster system is not necessarily better if it allows incorrect payments.

5. Determine where rule-based automation is insufficient
This is the most important part of validating your proposed use case.

Do not assume that rule-based automation is inherently inadequate. Rules are excellent for many invoice verification tasks.

A. What existing rules can already do well
Consider the following examples:

Problem	Can conventional rules handle it?
Invoice total does not equal the sum of line items.	Yes.
Invoice price exceeds the purchase-order price by more than an allowed tolerance.	Yes.
Invoice quantity exceeds the quantity received.	Yes, if the relevant receipt data is available and the matching rules are configured.
An invoice number and supplier match a previously processed invoice.	Often, using duplicate-detection rules.
A required purchase-order number is missing.	Yes, although resolving the missing reference is a separate problem.
A price change was authorized in an email but not recorded in the purchase order.	Potentially difficult for basic rules, especially if the email is unstructured and not connected to the matching process.
Enterprise systems already support configurable matching policies, tolerances, and exception messages. 

Therefore, your strongest argument for AI is not that it can compare invoice numbers or calculate differences.

It is that AI might help interpret relevant evidence that conventional matching rules do not readily connect or understand.

B. Identify the potential AI advantage
Suppose the purchase order specifies ₹500 per unit, but the invoice charges ₹520.

The procurement team previously approved a price increase in an email, but the PO was never updated.

A basic matching rule can detect the difference. It cannot establish authorization merely from the two numerical values.

An AI-assisted investigation might:

Retrieve the relevant invoice, PO, and receipt records.
Find a potentially relevant email or contract amendment.
Compare the supplier, product, date, and revised price.
Explain why the evidence may justify the discrepancy.
Recommend that an authorized employee verify the change before approval.
However, this workflow is a proposed capability, not a demonstrated result.

The system could retrieve the wrong email, overlook a later cancellation, misunderstand a contract clause, or mistake a discussion for formal authorization.

AI can help interpret evidence; it cannot turn incomplete or ambiguous evidence into proof of authorization.

C. Four hypotheses worth testing
Rather than building an entire invoice-processing platform, investigate these specific hypotheses.

Hypothesis	What you would test
H1: Relevant evidence is scattered across systems.	How often does resolving an exception require searching beyond the invoice, PO, and receipt?
H2: Existing tools detect discrepancies but provide insufficient explanations.	How often must analysts independently investigate the reason for an existing system's exception?
H3: Similar exceptions can be resolved using previously verified cases.	Can prior decisions help identify relevant evidence and suggest a resolution for a new case?
H4: AI-generated explanations can reduce investigation time without compromising controls.	Can analysts resolve cases faster while maintaining an acceptably low rate of incorrect recommendations?
If H1 and H2 are not supported by evidence, you may need to choose a different problem.

If H3 is supported but H4 fails, AI might still be useful for retrieving relevant records without recommending a decision.

If conventional systems already solve the targeted problem well, the correct conclusion may be that this is not the right use case.

That willingness to reject an unsuitable idea is a strength in a take-home assignment.

6. Collect evidence before designing the architecture
I recommend organizing your investigation into four evidence sources.

Source 1: Existing software documentation
Study how established systems handle invoice matching, tolerances, exceptions, and approvals.

Start with these resources:

Microsoft Dynamics 365 — Invoice matching overview
SAP Concur — Purchase order matching rules
Sage Intacct — Intelligent three-way matching
For each product, record:

What the system already automates.
What data it requires.
How it handles mismatches.
Whether it explains the discrepancy or merely identifies it.
What requires human approval.
Which limitations are documented, and which remain unverified.
Do not claim that a product lacks a feature simply because you cannot find it in one documentation page.

Source 2: Industry reports
Use industry reports to estimate the scale of the operational problem.

The Ardent Partners benchmark above is a reasonable starting point. Its figures can help you explain why exception handling deserves attention.

But distinguish between:

Total invoice-processing costs.
Costs associated with exceptions.
Costs associated with your specific target problem.
Only the third category directly establishes the economic opportunity for your proposed solution.

Source 3: Interviews with potential users
If possible, speak to two or three people who work in accounts payable, procurement, or financial operations.

You do not need a large survey for an initial investigation. You need enough specific evidence to determine whether your proposed problem exists in practice.

Ask questions about actual experiences, rather than asking whether the person likes your AI idea.

For example:

Can you describe the last invoice discrepancy you had to investigate?
What triggered the investigation?
Which records or systems did you consult?
How long did the investigation take?
Who had to participate in resolving it?
What caused the delay?
How did you establish whether the invoice could be approved?
What does your current software already handle automatically?
Which types of exceptions repeatedly require manual investigation?
What happens when an exception is incorrectly cleared?
Where possible, ask for anonymized examples of resolved cases, with permission. Real cases will be more useful for a prototype than invented examples.

Source 4: A small, labeled dataset
If you can obtain suitable data, collect anonymized invoice cases with their supporting purchase orders, receipt records, relevant authorization evidence, and final resolution.

For each case, record:

Field	Purpose
Invoice ID	Identify the case without exposing sensitive supplier details.
PO ID	Identify the associated purchase order.
Receipt reference	Check quantities received, where applicable.
Discrepancy type	Classify the issue.
Discrepancy amount	Measure the financial difference.
Relevant evidence	Identify the records used to investigate the issue.
Final resolution	Record the verified outcome.
Resolution time	Measure the baseline workload.
Human decision	Record who approved or rejected the proposed resolution.
Do not assume that all these records are available in one system. Determining how accessible and connected they are is itself part of your research.

Also, avoid using real confidential invoices or supplier information in an external AI service without appropriate authorization and data safeguards.

7. Questions you should answer before building a prototype
Use the following checklist as your initial research plan.

Problem definition
Which invoice discrepancy will I target?
Who experiences the problem most directly?
What happens today when the discrepancy occurs?
Why is the current process insufficient?
Business impact
How frequently does this problem occur?
How long does resolving it take?
What financial or operational consequences does it create?
Which measurable improvement would justify a new solution?
Existing alternatives
What can ERP and accounts payable automation systems already do?
Which conventional rules are sufficient?
What evidence remains difficult to interpret or connect?
Could a simpler workflow improvement solve the problem without AI?
Data feasibility
Which documents and records would the system need?
Can the records be accessed reliably?
Is there enough verified historical data to evaluate the solution?
Can the relevant authorization and final decision be established?
Safety and human involvement
What happens if the AI recommends an incorrect resolution?
Which decisions must remain with an authorized employee?
How will the system explain its recommendation?
How will it handle missing, contradictory, or outdated evidence?
Prototype evaluation
What is the existing process's baseline performance?
What will you compare the prototype against?
How will you measure resolution accuracy and time saved?
What error rate would make the solution unacceptable?
You do not need to answer every question perfectly before starting. However, you should have enough evidence to justify the problem, identify the data requirements, and define a measurable evaluation.

8. My recommendation: narrow the problem further
At this stage, I would not describe the project simply as an AI Invoice Verification System. That title is too broad and overlaps with established capabilities.

I would investigate this more specific formulation:

AI-Assisted Resolution of Ambiguous Purchase-Order Invoice Discrepancies

The intended user is an accounts payable analyst handling invoices that existing matching rules have flagged.

The problem is that identifying a discrepancy does not necessarily establish its cause or whether it is legitimate. The analyst may need to gather information from procurement, receiving, suppliers, contracts, or previous decisions.

The proposed system would help retrieve relevant evidence, explain the discrepancy, and recommend the next step while leaving financial approval with an authorized employee.

The intended business outcome would be reduced investigation time and faster exception resolution without increasing incorrect payment approvals.

This formulation is specific enough to investigate, but its commercial value remains unproven.

What would make this problem defensible?
I would want evidence supporting three conditions:

Frequency: The targeted discrepancies occur often enough to matter.
Unmet need: Existing systems do not adequately support their investigation for the intended customer.
Measurable improvement: An AI-assisted approach can reduce the work required without weakening financial controls.
If you cannot establish the second condition, do not force an AI solution into the problem. Consider a narrower variation, such as finding missing authorization evidence or identifying recurring causes of invoice exceptions.

9. The next step: build a problem-validation brief
Before designing the architecture, prepare a short document containing these six sections:

Section	What to include
1. Problem	One clearly defined invoice discrepancy and why it matters.
2. User and workflow	The person affected and the steps they currently follow.
3. Evidence	Industry research, software documentation, and user interviews.
4. Existing solutions	What conventional rules and current products already accomplish.
5. Unresolved gap	The specific task that remains difficult and why.
6. Success criteria	How you will determine whether an AI-assisted solution improves the process.
Once this brief is credible, you can compare three solution approaches:

A conventional rules-based workflow.
AI-assisted evidence retrieval and explanation.
A hybrid approach combining deterministic checks with AI-assisted investigation.
Only then should you choose the architecture and build a prototype.

The key principle for your Tresata assignment: Start with a demonstrable financial problem, not with a preferred AI technology. Your strongest argument will explain why the problem exists, why current alternatives are insufficient for that particular use case, and how you would prove that your proposed solution improves the outcome.

I am working on a finance-related AI take-home assignment. I want to identify a real problem in financial accounting that involves repetitive document processing, manual verification, and potential human errors. Explore possible problems and recommend one suitable for an AI-based solution.
Identifying a Financial Accounting Problem for an AI-Based Solution
For your finance-related take-home assignment, I recommend focusing on a problem that satisfies four conditions:

Repetitive work: Employees regularly process large numbers of financial documents.
Manual verification: Employees must compare information across multiple records.
Risk of human error: Incorrect data entry, missed discrepancies, or incomplete verification can cause financial losses.
Clear AI opportunity: AI can reduce manual investigation, extract information, identify inconsistencies, or help employees make better decisions.
The objective should not be to build another general-purpose accounting system. It should be to identify one specific accounting problem where AI can improve an existing workflow.

I would explore the following seven problem areas before selecting one.

1. Potential Problems in Financial Accounting
Problem 1: Invoice Verification and Discrepancy Detection
Area: Accounts Payable (AP)

Businesses receive invoices from suppliers and verify them against purchase orders (POs) and goods-received records before approving payments.

How the process works:

A supplier sends an invoice.
The accounts payable team extracts invoice details.
The team compares the invoice with the purchase order.
They verify quantities, prices, taxes, and totals.
They investigate discrepancies.
An authorized employee approves the payment.
Problems:

Different suppliers use different invoice formats.
Invoice quantities or prices may differ from purchase orders.
Duplicate invoices may be submitted.
Supporting documents may be missing.
Employees spend time investigating discrepancies.
Incorrect invoices may pass through manual verification.
Potential AI solution:

An AI-assisted invoice verification system that extracts invoice information, compares it with purchase orders and receipt records, identifies discrepancies, retrieves supporting evidence, and recommends whether an invoice requires approval or investigation.

Business impact:

Reduced manual verification.
Faster invoice processing.
Lower risk of incorrect payments.
Improved financial controls.
Assessment: Very strong candidate. It has a clearly identifiable user, workflow, documents, measurable outcomes, and opportunities for AI-assisted investigation.

Problem 2: Bank Reconciliation Automation
Area: Financial Accounting / Treasury

Businesses maintain internal accounting records and receive bank statements containing actual transactions. Accountants must reconcile these two sets of records.

How the process works:

The company downloads its bank statement.
The accounting team retrieves internal ledger transactions.
They compare transaction amounts, dates, and descriptions.
They identify matched and unmatched transactions.
They investigate differences.
They record adjustments and complete reconciliation.
Problems:

Bank descriptions may differ from internal ledger descriptions.
Transactions may be recorded on different dates.
Bank fees and interest may not be recorded internally.
One payment may correspond to multiple accounting entries.
Missing or duplicate transactions may go unnoticed.
Potential AI solution:

An AI-assisted reconciliation system that matches transactions using amounts, dates, descriptions, references, and historical patterns. It identifies unmatched transactions, explains likely causes, and recommends adjustments for human review.

Business impact:

Reduced reconciliation time.
Faster month-end closing.
Improved transaction accuracy.
Earlier detection of unusual transactions.
Assessment: Excellent candidate, particularly because transaction matching and exception investigation can be measured independently.

Problem 3: Expense Report Verification
Area: Accounts Payable / Employee Expense Management

Employees submit expense claims with receipts, invoices, and supporting documents. Finance teams verify whether these expenses comply with company policies.

How the process works:

Employees submit expense claims.
They upload receipts and supporting documents.
Finance teams extract amounts, dates, and merchant details.
They compare expenses with company policies.
They identify missing information or unusual expenses.
Managers approve or reject claims.
Problems:

Employees submit incomplete receipts.
The same expense may be claimed more than once.
Expenses may exceed permitted limits.
Incorrect categories may be selected.
Manual policy verification consumes time.
Potential AI solution:

An AI-powered expense verification assistant that reads receipts, extracts transaction details, identifies duplicate claims, checks policy requirements, and flags suspicious or unsupported expenses.

Business impact:

Faster expense reimbursement.
Reduced manual verification.
Better policy compliance.
Reduced duplicate or invalid claims.
Assessment: Good candidate. It is relatively easy to demonstrate with sample receipts and expense policies.

Problem 4: Financial Document Data Extraction and Ledger Entry
Area: General Accounting

Accountants receive documents such as invoices, receipts, debit notes, credit notes, and payment confirmations. They must extract information and enter it into accounting records.

How the process works:

Financial documents are received.
Employees identify the document type.
They extract relevant financial information.
They determine the appropriate accounting category.
They enter the information into the accounting system.
They verify the resulting ledger entries.
Problems:

Repetitive data entry.
Different document formats.
Incorrect account classification.
Missing or incorrectly entered values.
Time spent handling large document volumes.
Potential AI solution:

A document-processing assistant that identifies document types, extracts relevant information, suggests accounting categories, and prepares draft ledger entries for approval.

Business impact:

Reduced data-entry workload.
Improved consistency.
Faster accounting operations.
Reduced classification errors.
Assessment: Good candidate, but it can become too broad. You should narrow it to one document type or one accounting activity.

Problem 5: GST Invoice Reconciliation and Tax Verification
Area: Tax Accounting / Compliance

Businesses registered under GST need to ensure that their purchase records and supplier invoices are consistent with the information available in GST records.

How the process works:

A business receives supplier invoices.
The accounting team records eligible purchase transactions.
Supplier invoice information is compared with relevant GST records, such as GSTR-2B.
Differences in invoice numbers, GSTINs, taxable values, or tax amounts are identified.
Employees investigate missing or inconsistent entries.
Eligible input tax credit (ITC) is determined according to applicable GST requirements.
Problems:

Supplier invoices may be missing from the relevant GST statement.
Invoice numbers or dates may not match.
Taxable values or GST amounts may differ.
Incorrect GSTIN information may be recorded.
Employees must investigate mismatches before finalizing reconciliation.
Potential AI solution:

An AI-assisted GST reconciliation system that extracts information from invoices, compares it with GST records, identifies mismatches, groups discrepancies by likely cause, and recommends corrective actions.

Business impact:

Reduced manual reconciliation.
Improved accuracy of tax records.
Faster identification of missing invoices.
Reduced risk of incorrect ITC claims.
Assessment: Very strong candidate, particularly if you want an India-focused financial accounting problem.

One important distinction: GST eligibility and ITC rules should be implemented using validated tax rules. AI should assist with document interpretation and discrepancy investigation, not independently determine legal tax eligibility.

Problem 6: Accounts Receivable and Payment Reconciliation
Area: Accounts Receivable (AR)

Businesses send invoices to customers and subsequently receive payments. The finance team must identify which invoices have been paid and which remain outstanding.

How the process works:

The business generates customer invoices.
Customers make payments.
The business receives bank transaction records.
The accounts receivable team identifies the customer and corresponding invoice.
Payments are matched against outstanding invoices.
Unmatched payments and outstanding balances are investigated.
Problems:

Customers may pay multiple invoices through one transaction.
Payment descriptions may not contain invoice numbers.
Partial payments complicate reconciliation.
Customers may deduct charges or make adjustments.
Unidentified payments remain in suspense accounts.
Potential AI solution:

An AI-assisted cash application system that interprets payment descriptions, identifies likely customers and invoices, matches partial or combined payments, and recommends how to allocate unmatched transactions.

Business impact:

Faster payment allocation.
Reduced manual reconciliation.
Better visibility into outstanding receivables.
Improved cash-flow reporting.
Assessment: Strong candidate because it combines document processing, transaction matching, and financial reasoning.

Problem 7: Intercompany Transaction Reconciliation
Area: Corporate Accounting / Financial Consolidation

Large organizations often have multiple subsidiaries that conduct transactions with one another. Their accounting records must be reconciled before consolidated financial statements are prepared.

Example:

Company A records an intercompany sale of ₹10 lakh.
Company B records an intercompany purchase of ₹9.5 lakh.
The two entities report different values.

Problems:

Transactions may be recorded in different accounting periods.
Different currencies may be involved.
One entity may record a transaction while another has not.
Exchange-rate differences may occur.
Manual investigation is required to identify the source of mismatches.
Potential AI solution:

An AI-assisted intercompany reconciliation system that matches transactions across subsidiaries, identifies discrepancies, explains possible causes, and prepares supporting information for consolidation teams.

Business impact:

Faster month-end closing.
Reduced manual reconciliation.
Better consistency between subsidiary records.
Improved financial reporting.
Assessment: Interesting and potentially valuable, but more complex to demonstrate because it requires multiple entities' financial records and accounting context.

2. Compare All Seven Problems
Here is how I would evaluate them for your take-home assignment.

Scores are preliminary assessments for project suitability, not measured industry statistics.

Problem	Repetitive work	Human-error risk	AI opportunity	Prototype feasibility
Invoice verification	High	High	High	High
Bank reconciliation	High	High	High	High
Expense verification	High	Medium–High	High	Very High
Financial document extraction	Very High	High	High	Very High
GST reconciliation	High	High	High	High
Payment reconciliation	High	High	High	High
Intercompany reconciliation	High	High	High	Medium
My ranking
Rank	Problem	Reason
1	Invoice verification	Strong combination of document processing, financial controls, discrepancy detection, and human approval.
2	Bank reconciliation	Clear matching problem with measurable accuracy and efficiency.
3	GST reconciliation	Strong real-world relevance in India and identifiable compliance implications.
4	Payment reconciliation	Good opportunity for AI-assisted matching and exception handling.
5	Expense verification	Relatively easy to demonstrate, but existing solutions are mature.
6	Intercompany reconciliation	Valuable but more difficult to build a convincing prototype.
7	General financial document extraction	Useful, but too broad without a specific accounting outcome.
These rankings reflect suitability for your assignment, not the size of each market or the absence of competing products.

3. Where Does AI Actually Add Value?
This is an important distinction for your assignment.

Not every repetitive accounting task needs AI.

Consider the following:

Task	Traditional automation	Potential AI contribution
Adding invoice amounts	Excellent	Little additional value
Checking whether an invoice exceeds PO tolerance	Excellent	Little additional value
Extracting information from different invoice layouts	Requires OCR and configured extraction	AI can improve extraction and interpretation
Matching transactions with slightly different descriptions	Exact matching is limited	Semantic matching and contextual interpretation
Finding the reason for a discrepancy	Requires predefined rules and investigation	AI can retrieve and summarize relevant evidence
Identifying unusual transaction patterns	Rules can identify predefined conditions	AI/ML can identify patterns not explicitly encoded
Approving a financial transaction	Requires authorization controls	AI can provide recommendations, but approval should remain with authorized personnel
A strong AI accounting solution generally combines three capabilities:

1. Deterministic automation: Performs calculations, validates mandatory fields, and checks accounting rules.

2. AI/ML: Extracts information, interprets unstructured documents, identifies patterns, and assists with ambiguous cases.

3. Human review: Handles exceptions, verifies evidence, and makes decisions requiring financial authority.

This hybrid approach is more defensible than claiming that an LLM can independently perform accounting verification.

4. My Recommended Problem: AI-Assisted Invoice Verification
Considering the requirements of your Tresata assignment, I would select Invoice Verification and Discrepancy Investigation.

However, I would narrow it to one specific problem rather than building a complete invoice automation platform.

Proposed problem statement
Businesses face difficulties verifying supplier invoices when the information differs across invoices, purchase orders, goods-received records, and supporting documents. Existing matching rules can identify numerical discrepancies, but resolving ambiguous exceptions may require employees to manually investigate multiple records and obtain additional approvals.

Proposed solution
Develop an AI-Assisted Invoice Verification and Exception Resolution System.

The system would:

Accept supplier invoices in PDF or image format.
Extract invoice numbers, supplier details, quantities, prices, taxes, and totals.
Retrieve the corresponding purchase order and goods-received records.
Perform deterministic two-way or three-way matching.
Identify and classify discrepancies.
Retrieve relevant supporting evidence for ambiguous cases.
Explain why an invoice has been flagged.
Recommend an action: approve for normal processing, request clarification, or escalate for human review.
Importantly, the system should not automatically approve invoices simply because an AI model considers them legitimate.

Example scenario
Imagine the following documents:

Information	Purchase Order	Supplier Invoice
Product	Component A	Component A
Quantity	100	100
Unit price	₹500	₹550
Total	₹50,000	₹55,000
The system identifies a ₹5,000 discrepancy.

Instead of merely reporting that the invoice does not match, it investigates whether:

There was an authorized price revision.
The supplier made a billing mistake.
An additional charge was included.
Supporting authorization is missing.
It then presents the evidence and recommended next action to the accounts payable analyst.

That investigation capability is the potential differentiator—not the simple comparison of two prices.

5. Why I Would Choose This Over the Other Problems
There are three particularly attractive options: invoice verification, bank reconciliation, and GST reconciliation.

Here is how I would distinguish them.

Factor	Invoice verification	Bank reconciliation	GST reconciliation
Main documents	Invoices, POs, receipts	Bank statements, ledgers	Purchase invoices, GST records
Main activity	Verify supplier payments	Match transactions	Verify tax records
Main challenge	Resolving discrepancies	Matching unmatched transactions	Investigating tax mismatches
AI opportunity	Document understanding and evidence retrieval	Contextual transaction matching	Document extraction and mismatch classification
Human involvement	Exception approval	Unmatched transaction review	Tax and compliance review
Prototype difficulty	Moderate	Moderate	Moderate–High
My reasoning:

Invoice verification: Best overall balance of financial relevance, document processing, and explainable AI assistance.
Bank reconciliation: Potentially the simplest to evaluate quantitatively, especially with transaction datasets.
GST reconciliation: Particularly relevant to Indian businesses, but you need to handle tax rules and compliance requirements carefully.
If you want a project that demonstrates both AI capabilities and an understanding of business operations, invoice verification is my first choice.

If you want a more India-specific accounting problem, GST reconciliation deserves serious consideration.

6. What I Would Research Before Building Anything
I would not start coding immediately.

First, answer these ten questions:

No.	Research question	Why it matters
1	How do companies currently verify supplier invoices?	Understand the existing process.
2	What percentage of invoices require manual intervention?	Establish the problem's frequency.
3	What are the most common discrepancy types?	Identify the actual target problem.
4	How much time does an analyst spend resolving exceptions?	Establish operational impact.
5	Which existing software solutions already automate this process?	Understand competitors and alternatives.
6	What limitations remain in existing solutions?	Establish the opportunity for AI.
7	What documents and historical information are required?	Establish data feasibility.
8	How can AI recommendations be verified?	Establish reliability.
9	Which decisions require human approval?	Establish financial controls.
10	How will you measure improvement?	Establish project success criteria.
7. Suggested Research Sources
These are useful starting points for understanding the accounting processes and existing software capabilities.

Resource	What to investigate
Microsoft Dynamics 365	Invoice matching, accounts payable, and reconciliation.
SAP	Enterprise accounting workflows and invoice automation.
Oracle Financials	Financial automation and invoice processing.
RPA and UiPath	Traditional automation and document processing.
Ardent Partners	Accounts payable industry research and benchmarks.
When researching these products, look for their existing capabilities rather than assuming they have limitations.

8. Final Recommendation for Your Take-Home Assignment
I would shortlist these three problem statements:

Option A — Invoice Verification

AI-assisted verification of supplier invoices against purchase orders and goods-received records, with intelligent investigation of ambiguous discrepancies.

Option B — Bank Reconciliation

AI-assisted matching of bank transactions with internal accounting records, with automated identification and explanation of unmatched transactions.

Option C — GST Reconciliation

AI-assisted reconciliation of supplier invoices with GST records to identify missing invoices, inconsistent tax amounts, and potential input tax credit discrepancies.

My final choice: Option A
I would proceed with invoice verification, subject to validating that the targeted exception-resolution problem is not already adequately solved by the intended customer's existing software.

It gives you a good opportunity to demonstrate:

Financial accounting knowledge.
Document processing and information extraction.
AI-based reasoning and classification.
Integration with existing financial records.
Risk identification and fraud prevention.
Human-in-the-loop decision-making.
Measurable business value.
One important suggestion: Do not position your project as a system that replaces accountants or automatically approves payments. Position it as a system that helps finance professionals investigate financial discrepancies faster, with better evidence and fewer manual steps.

That is a much more realistic and defensible AI use case.

Your next decision should be between invoice verification, bank reconciliation, and GST reconciliation. Once you select one, we can investigate the actual business problem, existing solutions, limitations, potential AI contribution, and prototype scope in depth before designing its architecture.

I am considering lease accounting under Ind AS 116. Analyse the challenges finance teams face when extracting lease information and calculating lease liabilities. Identify the users, workflow, pain points, and potential business impact.
Lease Accounting Under Ind AS 116: Problem Investigation for Your Tresata Assignment
Lease accounting under Ind AS 116 is a strong candidate for a finance-related AI project. In fact, it offers an interesting problem beyond ordinary invoice verification: finance teams must interpret lengthy legal agreements, identify accounting-relevant information, and convert contractual terms into financial calculations.

The challenge is that lease agreements are not standardized financial forms. Important information may be spread across multiple clauses, amendments, schedules, and supporting documents.

A finance professional must extract these terms, determine their accounting treatment, calculate lease liabilities, and maintain accurate records throughout the lease period.

This creates an opportunity for an AI-assisted lease accounting system.

However, we should distinguish three different problems:

Lease data extraction: Finding relevant information in lease agreements.
Lease accounting calculations: Calculating lease liabilities and right-of-use (ROU) assets correctly.
Lease lifecycle management: Tracking modifications, renewals, terminations, and changes throughout the lease.
These are connected, but each has different challenges and automation requirements.

Let's investigate them systematically before deciding what your prototype should solve.

1. Understanding Ind AS 116 and the Financial Problem
What is Ind AS 116?
Ind AS 116 is the Indian Accounting Standard governing the recognition, measurement, presentation, and disclosure of leases.

Under Ind AS 116, a lessee generally recognizes:

Lease liability: The present value of qualifying future lease payments.
Right-of-use (ROU) asset: An asset representing the right to use the underlying leased property or equipment during the lease term.
There are exceptions, including qualifying short-term leases and leases of low-value assets.

A simple example
Suppose a company rents office space under these terms:

Parameter	Value
Monthly rent	₹1,00,000
Lease period	5 years
Payment frequency	Monthly
Discount rate	10% annually
Payment timing	End of each month
The finance team must determine the present value of the future lease payments.

The simplified lease liability formula is:

L
L
=
∑
t
=
1
n
P
t
(
1
+
r
)
t
LL= 
t=1
∑
n
​
  
(1+r) 
t
 
P 
t
​
 
​
 
Where:

L
L
LL = Initial lease liability.
P
t
P 
t
​
  = Lease payment in period 
t
t.
r
r = Discount rate per period.
n
n = Number of payment periods.
For monthly payments, the discount rate must be converted consistently into a monthly rate.

The finance team must also determine the initial ROU asset, considering the lease liability and relevant adjustments such as qualifying initial direct costs, advance payments, lease incentives, and restoration obligations.

The difficult part is not just calculating the present value. It is obtaining the correct inputs from the lease agreement and determining how accounting requirements apply to those inputs.

This is where the opportunity for your project begins.

2. Who Are the Users?
Lease accounting involves several people, not just accountants. Understanding their responsibilities will help you identify who experiences the problem and who would use your proposed system.

User	Responsibility	Challenges
Lease Accountant	Extracts lease terms and performs accounting calculations.	Manually reviews lengthy agreements and calculates lease liabilities.
Financial Controller	Reviews accounting treatment and financial statements.	Needs accurate calculations and supporting evidence.
Accounts Team	Maintains payment schedules and accounting entries.	Tracks monthly payments, interest, and depreciation.
Legal Team	Manages lease agreements, amendments, and contractual conditions.	Must communicate changes that affect accounting treatment.
Procurement / Administration	Coordinates office, equipment, and property leases.	Maintains lease records across different locations and departments.
Internal Auditor	Reviews lease calculations and accounting compliance.	Needs traceable calculations and supporting contractual evidence.
CFO / Finance Head	Oversees financial reporting and accounting controls.	Needs reliable lease liabilities and visibility into financial obligations.
Who is the primary user?
For your proposed project, I recommend targeting:

Lease Accountants and Financial Controllers.

Why?

Lease accountants perform the repetitive document extraction and calculations.
Financial controllers review the results and are accountable for financial reporting.
Both directly benefit from reducing manual work and improving calculation accuracy.
Other departments can provide supporting information, but they do not need to be the primary users of your prototype.

3. Existing Lease Accounting Workflow
Let's understand how a company typically processes a new lease agreement.

Step 1: Collect lease agreements
Companies may have hundreds or thousands of leases involving:

Office buildings.
Retail stores.
Warehouses.
Manufacturing facilities.
Vehicles.
Computers and other equipment.
Machinery.
The agreements may arrive as PDFs, scanned documents, Word files, or physical documents.

Challenge: Lease agreements are stored in different formats and locations. Finance teams may not have one centralized source containing all active lease agreements.

Step 2: Identify whether an agreement contains a lease
The accounting team determines whether an arrangement contains a lease under Ind AS 116.

Broadly, this involves assessing whether the contract conveys the right to control the use of an identified asset for a period of time in exchange for consideration.

This is not always obvious from the document title.

For example:

A company enters into an agreement with a logistics provider to transport goods.

The agreement may be a service contract rather than a lease. However, if it gives the company control over the use of an identified vehicle, the arrangement may contain a lease.

Challenge: Identifying a lease requires interpretation of contractual rights and obligations, not simply searching for the word "lease."

Step 3: Extract important lease information
The accountant reviews the agreement and identifies relevant terms.

Information	Example	Accounting importance
Lease commencement date	1 April 2026	Determines when recognition begins.
Lease end date	31 March 2031	Helps establish the lease term.
Monthly rent	₹1,00,000	Determines contractual payments.
Payment frequency	Monthly	Determines payment schedule.
Payment timing	Beginning/end of month	Affects present value calculations.
Escalation clause	5% every year	Changes future payment amounts.
Rent-free period	First 3 months	Affects payment schedules.
Renewal option	Additional 3 years	May affect the lease term.
Termination option	Early termination permitted	May affect the lease term.
Discount rate	10% annually	Used to calculate present value.
Security deposit	₹5,00,000	Requires separate accounting assessment.
Challenge: Important information is spread across different sections of the agreement. Some terms may also be contained in separate schedules or amendments.

Step 4: Determine the lease term and payment schedule
The accountant determines the period over which the lease liability should be measured.

This may not always be identical to the contractual period.

For example:

Initial lease period: 5 years.
Renewal option: Additional 3 years.
Management expects to exercise the renewal option.
If the renewal option is reasonably certain to be exercised, the lease term may include the additional three years.

The accountant must evaluate the relevant facts and circumstances rather than automatically including every renewal option.

The team must also identify qualifying lease payments, including relevant fixed payments, in-substance fixed payments, and certain variable payments linked to an index or rate.

Challenge: Lease agreements often contain conditions that require accounting judgment. Incorrectly interpreting them can change the lease term and the liability.

Step 5: Determine the discount rate
The finance team determines the appropriate discount rate.

Under Ind AS 116, the lessee uses the interest rate implicit in the lease if readily determinable. Otherwise, the lessee generally uses its incremental borrowing rate.

The incremental borrowing rate depends on factors such as:

Lease term.
Economic environment.
Currency.
Security.
Relevant borrowing conditions.
Challenge: The discount rate may not be explicitly stated in the lease agreement. Finance teams may need to obtain or calculate an appropriate rate using additional information.

This is an important distinction for your project: an AI model should not simply invent a discount rate from the lease document.

Step 6: Calculate the lease liability and ROU asset
After obtaining the required inputs, the accounting team calculates:

Initial lease liability.
Initial ROU asset.
Interest expense.
Lease payments.
Depreciation expense.
Closing lease liability.
The lease liability is initially measured at the present value of qualifying unpaid lease payments.

The ROU asset is initially measured using the applicable Ind AS 116 requirements.

Step 7: Record accounting entries
The accountant prepares the relevant accounting entries.

For example, the initial recognition may be represented as:

Account	Debit	Credit
Right-of-use asset	₹X	—
Lease liability	—	₹X
This is a simplified illustration, assuming no other adjustments to the initial ROU asset.

Subsequently:

Interest expense increases the lease liability.
Lease payments reduce the liability.
Depreciation reduces the carrying value of the ROU asset.
Step 8: Monitor the lease throughout its lifecycle
This is where another significant challenge emerges.

Lease agreements may change after initial recognition.

Examples:

Rent increases.
Lease period gets extended.
Additional space is acquired.
Part of the leased property is surrendered.
The agreement is terminated early.
The finance team must assess whether the change constitutes a lease modification, a reassessment, or another accounting event and apply the relevant requirements.

Challenge: Even if the initial calculation is correct, subsequent changes can make the accounting records inaccurate if they are not identified and processed.

4. Major Pain Points in Lease Accounting
I would group the challenges into six categories.

Pain Point 1: Manual Extraction from Complex Lease Agreements
This is probably the strongest starting point for an AI-based solution.

Imagine a company has 500 lease agreements.

An accountant may need to manually review each agreement to identify:

Lease commencement date.
Lease duration.
Monthly payments.
Escalation clauses.
Rent-free periods.
Renewal options.
Termination conditions.
Payment schedules.
The information is not necessarily presented in a consistent format.

One agreement might specify rent in a table, while another describes the payment schedule in paragraphs.

A third may contain the escalation terms in an annexure.

Why this is problematic:

Time-consuming document review.
Risk of overlooking important clauses.
Inconsistent extraction across accountants.
Difficulty processing large numbers of agreements.
Potential AI contribution: Extract structured lease information from unstructured agreements and identify the source clauses supporting each extracted value.

Pain Point 2: Misinterpretation of Lease Terms
Extracting a number is different from understanding its accounting meaning.

Consider these examples:

Contractual condition	Potential accounting issue
Renewal option for another five years	Whether the additional period belongs in the lease term.
Rent-free period	Correct treatment of lease payments and ROU asset.
Annual rent escalation	Correct future payment schedule.
Early termination clause	Whether termination options affect the lease term.
Variable rent based on sales	Whether payments belong in the initial lease liability.
Agreement amendment	Whether a reassessment or modification is required.
A document extraction tool may identify all these clauses but still fail to interpret their accounting implications correctly.

Potential AI contribution: Identify relevant clauses, explain their implications, and flag terms requiring professional judgment.

Pain Point 3: Lease Liability Calculation Errors
Lease liability calculations involve multiple inputs.

A small mistake in one input can affect the result.

For example:

Incorrect commencement date.
Wrong payment frequency.
Incorrect payment timing.
Missing escalation.
Incorrect lease term.
Incorrect discount rate.
Missing rent-free period.
Suppose the accountant assumes that rent is payable at the end of each month when the contract actually requires payment at the beginning.

The present value calculation will differ.

Potential AI contribution: Automatically generate a structured payment schedule from extracted contractual terms and pass validated inputs into a deterministic calculation engine.

The AI should not independently perform financial calculations without a separate calculation and validation mechanism.

Pain Point 4: Tracking Lease Amendments
Consider this example:

A company initially signs a five-year office lease.

After two years, the landlord and tenant agree to extend the lease by another three years.

The finance team must identify the amendment and determine its accounting consequences.

If the amendment is not communicated to the accounting department, the lease liability may continue to be calculated using outdated assumptions.

Potential AI contribution: Compare new agreements and amendments with existing lease records, identify changed terms, and notify the accountant about potential reassessment or modification requirements.

Pain Point 5: Decentralized Lease Information
Large businesses may operate across multiple cities.

Different departments may maintain separate records.

For example:

Chennai office leases.
Bengaluru office leases.
Hyderabad warehouse leases.
Mumbai retail leases.
The finance team may receive information from different departments in different formats.

Potential AI contribution: Centralize lease information and provide a searchable, structured repository with document references and accounting status.

Pain Point 6: Audit and Compliance Challenges
During an audit, finance teams may need to demonstrate:

How the lease term was determined.
Which contractual clauses support the extracted payments.
How the discount rate was selected.
How the lease liability was calculated.
How modifications were accounted for.
Whether the accounting entries are supported by documentation.
If calculations are maintained in separate spreadsheets without proper references, tracing the original contractual information can become difficult.

Potential AI contribution: Maintain an audit trail connecting each accounting input, calculation, and accounting output to its supporting document and approval.

5. Potential Business Impact
Now let's connect these problems to measurable business outcomes.

Lease accounting is particularly interesting because errors can affect both the balance sheet and the income statement.

A. Financial impact
Incorrect lease information can result in:

Incorrect lease liabilities.
Incorrect ROU asset values.
Incorrect interest expenses.
Incorrect depreciation expenses.
Incorrect financial statement disclosures.
For example, if a company has 500 active leases and some agreements have incorrect payment schedules or lease terms, the cumulative impact could be material.

However, the actual impact depends on the value and nature of the leases. You should not assume every extraction error results in a material financial misstatement.

B. Operational impact
Current challenge	Potential business improvement
Manual document review	Reduced document-review time.
Manual data extraction	Faster structured data creation.
Spreadsheet-based calculations	Consistent calculation methodology.
Missed contractual amendments	Earlier identification of changes.
Repeated verification	Reduced duplicate work.
Difficult audit preparation	Better traceability and documentation.
C. Compliance impact
Ind AS 116 requires appropriate recognition, measurement, and disclosure of lease-related information.

A properly designed system could help finance teams:

Apply consistent accounting policies.
Maintain supporting documentation.
Identify missing lease information.
Monitor changes in lease terms.
Prepare more reliable financial records.
It is important to distinguish between supporting compliance and guaranteeing compliance. An AI system cannot guarantee that financial statements comply with Ind AS 116.

6. Which Parts Are Suitable for AI and Which Are Not?
This distinction will be particularly important when you explain your solution to Tresata.

Activity	Traditional automation	AI suitability
Reading scanned lease agreements	OCR	High: document understanding and extraction.
Identifying commencement dates	Keyword/rule extraction	High: extracting information from varied formats.
Identifying escalation clauses	Basic rules	High: understanding contractual language.
Identifying renewal conditions	Limited predefined rules	High: interpreting contextual clauses.
Determining whether a renewal is reasonably certain	Requires accounting judgment	AI can assist by organizing evidence, but should not independently decide.
Calculating present value	Excel/Python calculation	Low need for AI; deterministic calculation is preferable.
Calculating depreciation	Accounting formulas	Low need for AI.
Comparing amended agreements	Text comparison	High: identifying changes across documents.
Preparing audit evidence	Manual document collection	High: retrieval and summarization.
Approving accounting treatment	Human authorization	Human responsibility.
My recommendation is a hybrid AI and financial calculation system.

Use AI where language understanding is necessary. Use conventional software where mathematical accuracy and accounting rules are required.

For example, an LLM can extract a clause saying that monthly rent increases by 5% every April. A deterministic calculation engine should then generate the monthly payment schedule and calculate the present value.

This separation improves reliability and makes the system easier to audit.

7. What Is Already Established and What Requires Research?
This is important because you should not present assumptions as industry facts in your assignment.

Statement	Evidence status
Ind AS 116 generally requires lessees to recognize lease liabilities and ROU assets.	Established accounting requirement, subject to applicable exemptions and other requirements.
Lease liabilities are initially measured using the present value of qualifying lease payments.	Established accounting requirement.
Lease agreements can contain renewal, termination, escalation, and variable-payment clauses.	Established contractual reality.
Different contractual clauses can affect lease accounting calculations.	Established accounting principle.
Finance teams must assess relevant lease modifications and reassessments.	Established accounting requirement.
All companies maintain lease information in spreadsheets.	Unverified generalization.
Manual lease extraction is a major source of errors across Indian businesses.	Requires empirical research.
Most companies spend several hours processing each lease.	Requires empirical research.
AI extraction will be more accurate than existing lease accounting software.	Hypothesis requiring testing.
AI will significantly reduce accounting costs.	Business hypothesis requiring measurement.
Companies will purchase a new AI lease accounting platform.	Commercial hypothesis requiring validation.
The last three are especially important. Do not claim them as proven advantages.

8. What Should You Measure to Establish Business Value?
Before developing a prototype, identify measurable baseline metrics.

I recommend these six:

Metric	Measurement
Lease extraction time	Average minutes required to extract information from one agreement.
Extraction accuracy	Percentage of correctly extracted fields.
Critical clause detection	Percentage of relevant accounting clauses correctly identified.
Calculation accuracy	Difference between system calculations and independently verified calculations.
Amendment detection rate	Percentage of relevant lease changes correctly identified.
Audit traceability	Percentage of accounting inputs linked to supporting evidence.
For example, you could evaluate a prototype using 50 anonymized lease agreements.

Measure:

How long a finance professional takes to extract lease details manually.
How long the AI-assisted system takes.
How accurately it extracts the information.
Whether it identifies important clauses.
Whether the resulting lease liability agrees with an independently validated calculation.
Do not measure only extraction speed. A system that extracts information quickly but misses a renewal clause is not necessarily useful.

9. Recommended Problem Statement for Your Tresata Assignment
I would narrow the problem to the following.

Proposed title
LeaseLens AI – Intelligent Lease Document Extraction and Lease Liability Calculation Under Ind AS 116

Problem statement
Indian businesses manage multiple lease agreements involving offices, warehouses, equipment, vehicles, and other assets. Finance teams must manually review these agreements to extract accounting-relevant information, interpret contractual clauses, determine lease terms, and calculate lease liabilities and right-of-use assets under Ind AS 116.

Lease information is often distributed across lengthy agreements, payment schedules, and subsequent amendments. Manual extraction and interpretation can create operational inefficiencies and increase the risk of missing important contractual information or entering incorrect calculation inputs.

The proposed solution aims to automate lease information extraction, identify accounting-relevant contractual clauses, generate structured payment schedules, and calculate lease liabilities using validated accounting formulas.

The system will provide supporting document references, highlight missing or ambiguous information, and route judgment-dependent decisions to qualified finance professionals.

Primary users
Lease accountants.
Financial controllers.
Corporate finance teams.
Internal auditors.
Core problem being solved
Reducing the manual effort and potential errors involved in converting unstructured lease agreements into accurate, auditable lease accounting records.

10. Three Possible Project Scopes
There are three directions you could take.

Scope	Description	Complexity
A. Intelligent Lease Data Extraction	Extract relevant lease information and clauses from PDF agreements.	Low–Medium
B. Lease Liability Calculation Automation	Extract contractual inputs, generate payment schedules, and calculate lease liabilities and ROU assets.	Medium
C. Complete Lease Accounting Intelligence	Handle extraction, calculations, amendments, reassessments, accounting entries, and audit reporting.	High
My recommendation: Scope B
I would choose Lease Data Extraction + Lease Liability Calculation.

Why?

It addresses both document-processing and financial-accounting challenges.
It demonstrates meaningful AI functionality.
It includes measurable financial calculations.
It can be demonstrated using sample lease agreements.
It has a clear human-review component.
It is achievable without building an entire enterprise accounting platform.
You can include amendment detection as an additional feature if time permits.

I would avoid attempting to automate every aspect of lease accounting in your first prototype.

11. Questions to Investigate Before Building LeaseLens AI
These are the questions I would prioritize for your research.

A. Business understanding

How many active lease agreements does a typical target company manage?
Which departments maintain these agreements?
How are lease agreements currently processed?
How much time does a lease accountant spend reviewing one agreement?
How frequently do lease modifications occur?
B. Accounting understanding

Which contractual fields are necessary to calculate the initial lease liability?
How are renewal and termination options evaluated?
How are rent-free periods and escalation clauses treated?
How is the incremental borrowing rate determined?
What events require reassessment or modification accounting?
C. Existing solutions

What lease accounting software do companies currently use?
Which information extraction capabilities do these systems already provide?
What remains manual?
How do existing systems handle amendments and supporting evidence?
D. AI feasibility

Can AI reliably extract information from different lease formats?
Can it identify relevant clauses rather than merely extract numbers?
How will missing or contradictory information be handled?
How will calculations be independently validated?
How will accountants review and approve the results?
12. My Final Assessment
I think lease accounting under Ind AS 116 is a particularly promising direction for your assignment.

Compared with ordinary invoice verification, it gives you an opportunity to demonstrate a more interesting combination of:

Financial document understanding.
Contractual information extraction.
Accounting rule interpretation.
Financial calculations.
Exception handling.
Auditability and human oversight.
But there is one important consideration.

Do not position the problem as simply automating lease liability calculations.

The calculation itself is mathematical and can be performed accurately using conventional software once the correct inputs are available.

The more interesting problem is:

How can we reliably convert complex lease agreements into structured, accounting-ready information, identify clauses that affect lease measurement, and generate accurate, traceable lease calculations with minimal manual intervention?

That is the problem I would investigate.

What I suggest we do next
Before building LeaseLens AI, I recommend investigating these four areas in order:

Ind AS 116 accounting requirements: Understand exactly which information must be extracted and how it affects lease accounting.
Real-world lease agreement analysis: Examine sample agreements and identify difficult clauses, variations, and missing information.
Existing software analysis: Determine what lease accounting platforms already automate and identify a genuine gap.
Prototype feasibility: Select a limited set of lease types and calculate the expected output against independently verified results.
The most important next step is understanding the exact contractual information required under Ind AS 116. That will determine what your AI needs to extract, what your calculation engine needs as inputs, and which decisions must remain with a human accountant.

I want to build an AI-based solution called LeaseCheck. It should extract important lease information such as lease term, monthly rent, payment frequency, annual escalation, and renewal options. Propose a practical architecture with AI extraction, evidence verification, financial calculations, and human approval.
LeaseCheck – AI-Powered Lease Accounting and Verification System
For your Tresata take-home assignment, I recommend designing LeaseCheck as a hybrid AI-powered lease accounting platform that converts unstructured lease agreements into structured, verified, and calculation-ready financial information under Ind AS 116.

The central design principle should be:

AI extracts and interprets lease information, a verification layer checks the evidence, a deterministic calculation engine performs financial calculations, and a human accountant approves accounting decisions.

This is important because lease accounting involves financial calculations and accounting judgments. An LLM should not independently decide the final lease liability or approve accounting entries.

Let's design a practical architecture that you can realistically implement as a prototype.

1. What LeaseCheck Will Do
A finance professional uploads a lease agreement in PDF format.

LeaseCheck will:

Read the uploaded agreement.
Extract important lease information.
Identify relevant contractual clauses.
Verify extracted information against the original document.
Identify missing or conflicting information.
Generate a lease payment schedule.
Calculate the initial lease liability and ROU asset using validated inputs.
Present the results for accountant review and approval.
Generate an accounting summary and supporting evidence report.
Example input
A company uploads a commercial office lease agreement containing:

Lease parameter	Contract information
Lease commencement date	01-Apr-2026
Lease end date	31-Mar-2031
Monthly rent	₹1,00,000
Payment frequency	Monthly
Annual escalation	5%
Renewal option	Additional 3 years
Payment timing	Beginning of each month
The system extracts this information and creates a structured lease record.

However, it should not automatically assume that the renewal option will be exercised. That requires an accounting assessment based on the relevant facts and circumstances.

2. Proposed System Architecture
I recommend a six-layer architecture.

Architecture overview
             USER / FINANCE TEAM
                     |
                     v
             LEASECHECK INTERFACE
                     |
                     v
          1. DOCUMENT INGESTION
                     |
                     v
          2. DOCUMENT PROCESSING
              OCR + PDF PARSING
                     |
                     v
          3. AI EXTRACTION ENGINE
              LLM + STRUCTURED JSON
                     |
                     v
          4. EVIDENCE VERIFICATION
             SOURCE CLAUSE CHECK
             FIELD VALIDATION
             MISSING DATA CHECK
                     |
                     v
          5. FINANCIAL CALCULATION
             LEASE PAYMENT SCHEDULE
             LEASE LIABILITY
             ROU ASSET
             INTEREST + DEPRECIATION
                     |
                     v
          6. HUMAN APPROVAL
             ACCOUNTANT REVIEW
             CONTROLLER APPROVAL
                     |
                     v
              FINAL OUTPUT
             ACCOUNTING REPORT
             AUDIT TRAIL
             EXPORTABLE RESULTS
Each layer has a separate responsibility. This separation will make the system easier to test, explain, and maintain.

Layer 1: Document Ingestion
Purpose: Accept lease agreements and prepare them for processing.

Input documents
For the initial prototype, support:

PDF lease agreements.
Scanned PDF agreements.
Lease amendment documents.
Supporting payment schedules.
Processing
When a user uploads a document:

Assign a unique Lease ID.
Store the original document.
Identify whether it is a text-based or scanned PDF.
Extract document text.
Preserve page numbers and document references.
Send the extracted content to the AI extraction engine.
Suggested technologies
Component	Technology
Frontend	Streamlit
Backend	Python + FastAPI
PDF text extraction	PyMuPDF
OCR for scanned documents	Tesseract or PaddleOCR
Document storage	Local storage for prototype; object storage for production
Important: Do not discard the original PDF after extracting its text. You need it later to verify the extracted information.

Layer 2: AI-Based Lease Information Extraction
Purpose: Convert unstructured contractual information into structured data.

This is the primary AI component of LeaseCheck.

Instead of asking an LLM to summarize the entire agreement, give it a specific extraction task.

Information to extract
I recommend dividing the information into five categories.

A. Basic lease information

Field	Example
Lease ID	LC-001
Lessee	ABC Technologies
Lessor	XYZ Properties
Underlying asset	Office building
Lease commencement date	01-Apr-2026
Contractual end date	31-Mar-2031
Lease term	60 months
B. Payment information

Field	Example
Initial monthly rent	₹1,00,000
Payment frequency	Monthly
Payment timing	Beginning of month
Payment start date	01-Apr-2026
Annual escalation	5%
Rent-free period	3 months
Variable payments	If applicable
C. Renewal and termination information

Field	Example
Renewal option	Yes
Additional renewal period	3 years
Renewal notice period	6 months
Early termination option	Yes
Termination conditions	As specified in contract
D. Accounting information

Field	Example
Discount rate	10% annually
Short-term lease assessment	Requires review
Low-value lease assessment	Requires review
Lease classification	Requires accounting assessment
The discount rate should normally be supplied or confirmed through the finance team's approved methodology. Do not expect the AI to invent it from the agreement.

E. Supporting contractual information

For every extracted field, capture:

Original document page.
Relevant sentence or paragraph.
Extracted value.
Extraction confidence or review status.
Example extraction output
The LLM should return structured JSON similar to this:

{
  "lease_id": "LC-001",
  "lessee": "ABC Technologies",
  "lessor": "XYZ Properties",
  "asset_type": "Office Building",
  "commencement_date": "2026-04-01",
  "contractual_end_date": "2031-03-31",
  "lease_term_months": 60,
  "initial_monthly_rent": 100000,
  "payment_frequency": "monthly",
  "payment_timing": "beginning",
  "annual_escalation": 5,
  "renewal_option": {
    "available": true,
    "additional_months": 36,
    "reasonably_certain": null
  },
  "discount_rate": null,
  "missing_information": [
    "Approved discount rate",
    "Renewal option assessment"
  ]
}

The important design decision is that an unknown value should be returned as null, not guessed.

Also, distinguish the contractual lease period from the accounting lease term. They may differ because of renewal and termination options.

Suggested AI technologies
You can use:

An LLM for contractual language interpretation.
Structured output or JSON mode for consistent extraction.
Pydantic for validating the returned data.
For a prototype, you can use an API-based LLM. If you want to demonstrate local processing, you can also experiment with an instruction-following model through Ollama.

My recommendation: Keep the extraction engine independent of the rest of the application so that you can replace the underlying LLM without changing the calculation engine.

Layer 3: Evidence Verification and Validation Engine
This layer is extremely important.

An LLM might extract a monthly rent of ₹1,00,000 when the actual agreement specifies ₹1,10,000.

If LeaseCheck directly sends the extracted amount into the calculation engine, the entire result becomes unreliable.

Therefore, every important extracted field must have supporting evidence.

A. Evidence mapping
For example:

Extracted field	Value	Source evidence	Page
Monthly rent	₹1,00,000	"The monthly rent shall be INR 1,00,000."	3
Lease commencement	01-Apr-2026	"The lease shall commence on 1 April 2026."	2
Lease duration	5 years	"The initial term shall be five years."	2
Annual escalation	5%	"Rent shall increase by 5% annually."	4
Renewal option	3 years	"The lessee may renew for an additional three years."	8
The user should be able to click an extracted field and view the original supporting text.

B. Validation checks
Implement deterministic validation rules.

Examples:

Validation	Expected behaviour
Commencement date is after contractual end date	Flag an error.
Monthly rent is missing	Request manual input.
Payment frequency is unclear	Flag for review.
Annual escalation is mentioned in multiple clauses with different percentages	Flag a conflict.
Renewal period is mentioned but conditions are unclear	Request accounting review.
Extracted amount has no supporting source text	Reject or request manual verification.
Lease term differs from the contractual dates	Flag an inconsistency.
C. Confidence and review status
Each extracted field should have its own status.

For example:

Field	Confidence/review status
Monthly rent	High – Evidence verified
Commencement date	High – Evidence verified
Annual escalation	Medium – Manual review
Renewal option	Low – Ambiguous clause
Discount rate	Missing – Finance input required
Do not rely solely on the LLM's self-reported confidence score. Combine extraction quality with evidence matching, document quality, and validation results.

D. Important verification principle
LeaseCheck should distinguish three situations:

Verified: The extracted value is supported by clear contractual evidence.
Ambiguous: The document contains information, but its interpretation is uncertain.
Missing: The required information cannot be found.
This distinction prevents the system from treating missing information as zero or assuming that an ambiguous clause has a particular accounting meaning.

Layer 4: Financial Calculation Engine
Purpose: Convert verified lease information into accounting calculations.

This should be a deterministic Python module, not an LLM-based calculation system.

The calculation engine should receive only validated inputs and produce reproducible outputs.

A. Generate the payment schedule
Suppose the agreement contains:

Parameter	Value
Monthly rent	₹1,00,000
Lease term	5 years
Annual escalation	5%
Payment frequency	Monthly
Payment timing	Beginning of month
Discount rate	10% annually
The system generates a schedule:

Year	Monthly rent	Annual rent
1	₹1,00,000	₹12,00,000
2	₹1,05,000	₹12,60,000
3	₹1,10,250	₹13,23,000
4	₹1,15,762.50	₹13,89,150
5	₹1,21,550.63	₹14,58,607.50
This example assumes the escalation happens at the beginning of each lease year and that there are no rent-free periods or other payment adjustments.

B. Calculate the initial lease liability
The general formula is:

L
L
=
∑
t
=
1
n
P
t
(
1
+
r
)
t
LL= 
t=1
∑
n
​
  
(1+r) 
t
 
P 
t
​
 
​
 
Where:

P
t
P 
t
​
  = Lease payment at period 
t
t.
r
r = Discount rate per payment period.
n
n = Total payment periods.
For an annual effective discount rate of 10%, the equivalent monthly effective rate is:

r
m
=
(
1
+
0.10
)
1
/
12
−
1
r 
m
​
 =(1+0.10) 
1/12
 −1
The calculation engine must also account for payment timing.

For payments at the beginning of each month, the first payment is made at commencement and is not discounted. Subsequent payments are discounted according to their payment dates.

The system should use actual payment dates where necessary rather than blindly assuming every period has identical timing.

C. Calculate the ROU asset
Under Ind AS 116, the initial ROU asset generally incorporates:

R
O
U
=
L
L
+
I
n
i
t
i
a
l
D
i
r
e
c
t
C
o
s
t
s
+
P
r
e
p
a
i
d
L
e
a
s
e
P
a
y
m
e
n
t
s
−
L
e
a
s
e
I
n
c
e
n
t
i
v
e
s
+
R
e
s
t
o
r
a
t
i
o
n
O
b
l
i
g
a
t
i
o
n
s
ROU=LL+InitialDirectCosts+PrepaidLeasePayments−LeaseIncentives+RestorationObligations
This is a simplified representation of the initial measurement components.

Not every component will apply to every lease.

D. Generate the lease amortization schedule
The system should calculate:

Period	Opening liability	Interest	Payment	Closing liability
Month 1	Calculated	Calculated	Calculated	Calculated
Month 2	Calculated	Calculated	Calculated	Calculated
Month 3	Calculated	Calculated	Calculated	Calculated
...	...	...	...	...
For each period:

I
n
t
e
r
e
s
t
t
=
O
p
e
n
i
n
g
L
i
a
b
i
l
i
t
y
t
×
r
t
Interest 
t
​
 =OpeningLiability 
t
​
 ×r 
t
​
 
C
l
o
s
i
n
g
L
i
a
b
i
l
i
t
y
t
=
O
p
e
n
i
n
g
L
i
a
b
i
l
i
t
y
t
+
I
n
t
e
r
e
s
t
t
−
P
a
y
m
e
n
t
t
ClosingLiability 
t
​
 =OpeningLiability 
t
​
 +Interest 
t
​
 −Payment 
t
​
 
For payments at the beginning of a period, the payment must be applied before calculating interest for that period.

The actual implementation should follow the contractual payment dates and the accounting measurement requirements.

E. Calculate depreciation
The ROU asset is generally depreciated over the shorter of the useful life of the underlying asset and the lease term, unless ownership transfers or a purchase option is reasonably certain to be exercised, in which case the applicable useful-life requirements differ.

For a simple straight-line example:

A
n
n
u
a
l
D
e
p
r
e
c
i
a
t
i
o
n
=
I
n
i
t
i
a
l
R
O
U
A
s
s
e
t
D
e
p
r
e
c
i
a
t
i
o
n
P
e
r
i
o
d
AnnualDepreciation= 
DepreciationPeriod
InitialROUAsset
​
 
Your prototype should support a clearly defined straight-line case initially.

Suggested technologies
Component	Technology
Financial calculations	Python
Date and payment schedules	Pandas
Numerical calculations	NumPy
Validation	Pydantic
Results storage	SQLite
Reporting	Pandas + ReportLab
Important: Build independent test cases for the calculation engine. Compare its results against manually verified calculations or a trusted spreadsheet before using it for AI-extracted data.

Layer 5: Human Review and Approval
This is where LeaseCheck becomes suitable for a real finance workflow rather than just a document extraction demonstration.

Not every extracted contractual term should be accepted automatically.

The human reviewer should be able to:

View the extracted information.
Open the original agreement.
Verify supporting clauses.
Correct incorrectly extracted values.
Resolve missing information.
Confirm accounting assumptions.
Approve the calculation.
Reject the calculation and provide a reason.
Proposed approval workflow
          DOCUMENT UPLOADED
                  |
                  v
          AI EXTRACTS DATA
                  |
                  v
          EVIDENCE VALIDATION
                  |
          +-------+-------+
          |               |
       VERIFIED         ISSUES
          |               |
          |               v
          |         HUMAN REVIEW
          |               |
          |         CORRECT DATA
          |               |
          +-------+-------+
                  |
                  v
          CALCULATION ENGINE
                  |
                  v
          ACCOUNTANT REVIEW
                  |
          +-------+-------+
          |               |
       APPROVE          REJECT
          |               |
          v               v
      FINAL REPORT    REPROCESS
          |
          v
      AUDIT TRAIL
Two levels of human involvement
Level 1: Lease Accountant

Reviews the extracted information, contractual evidence, assumptions, and calculation schedule.

Level 2: Financial Controller

Approves the accounting treatment and final results according to the organization's authorization policy.

For a prototype, you can simulate both roles using different approval statuses rather than implementing a full enterprise permission system.

Layer 6: Reporting and Audit Trail
After approval, LeaseCheck should generate a report containing:

Lease identification details.
Extracted contractual terms.
Source page references.
Verification status.
Missing or ambiguous information.
Payment schedule.
Initial lease liability.
Initial ROU asset.
Interest and depreciation schedule.
Accountant approval status.
The system should also maintain a history of changes.

For example:

Activity	User	Status
Agreement uploaded	Finance user	Completed
Lease details extracted	AI system	Completed
Monthly rent verified	Lease accountant	Approved
Discount rate entered	Finance user	Completed
Liability calculated	Calculation engine	Completed
Accounting review	Financial controller	Approved
This is particularly useful for auditability.

3. Recommended Technology Stack
You do not need a complicated enterprise architecture for the first version.

I recommend this practical stack:

Layer	Recommended technology	Purpose
Frontend	Streamlit	Upload documents and display results.
Backend	Python	Coordinate processing.
PDF extraction	PyMuPDF	Extract text from digital PDFs.
OCR	Tesseract / PaddleOCR	Process scanned agreements.
AI extraction	LLM API or local Ollama model	Understand contractual language.
Structured output	JSON + Pydantic	Standardize extracted information.
Evidence verification	Python rules + source references	Validate extracted information.
Calculation engine	Python + NumPy	Calculate lease liabilities and ROU assets.
Database	SQLite	Store lease information and approval history.
Reports	Pandas + ReportLab	Generate financial reports.
Why this stack?
It is relatively easy to implement.
Most components can be developed independently.
You can demonstrate the entire workflow locally.
You do not need a complex cloud infrastructure.
You can replace the AI model without rewriting your accounting calculations.
I would use SQLite initially and consider PostgreSQL if you later need multiple users, stronger concurrency, and production-level access controls.

4. How the Components Communicate
Here is a more practical view of the backend.

                  STREAMLIT UI
                       |
                       v
                 PYTHON BACKEND
                       |
          +------------+------------+
          |                         |
          v                         v
     DOCUMENT STORE             DATABASE
          |
          v
     PDF PROCESSOR
          |
          v
      OCR ENGINE
          |
          v
     AI EXTRACTION
          |
          v
    STRUCTURED JSON
          |
          v
    VALIDATION ENGINE
          |
          v
    EVIDENCE MAPPING
          |
          v
   ACCOUNTING INPUTS
          |
          v
   CALCULATION ENGINE
          |
          v
    FINANCIAL OUTPUT
          |
          v
     HUMAN APPROVAL
          |
          v
    REPORT GENERATOR
I would organize the Python project like this:

LeaseCheck/
│
├── app.py
│
├── modules/
│   ├── document_processor.py
│   ├── ocr_engine.py
│   ├── lease_extractor.py
│   ├── evidence_verifier.py
│   ├── validation_engine.py
│   ├── lease_calculator.py
│   ├── approval_manager.py
│   └── report_generator.py
│
├── database/
│   ├── db_manager.py
│   └── schema.sql
│
├── prompts/
│   └── lease_extraction_prompt.txt
│
├── uploads/
│
├── outputs/
│
├── tests/
│   ├── test_extraction.py
│   ├── test_validation.py
│   └── test_calculations.py
│
└── requirements.txt
This is sufficient for a credible prototype.

5. Important Risks and How LeaseCheck Should Handle Them
For a financial AI assignment, explaining risks is as important as explaining functionality.

Risk	Example	Mitigation
Incorrect extraction	AI extracts ₹1,00,000 instead of ₹1,10,000.	Verify values against source clauses.
Missing clauses	AI overlooks an annual escalation clause.	Check expected fields and flag incomplete extraction.
Hallucination	AI invents a renewal period.	Require source evidence for every extracted value.
Incorrect accounting interpretation	AI assumes every renewal option belongs in the lease term.	Require accountant assessment.
Incorrect discount rate	AI selects an unsupported borrowing rate.	Require an approved finance input and methodology.
Calculation errors	Wrong payment timing or discounting.	Use deterministic formulas and independent test cases.
Outdated information	An amendment is not incorporated.	Maintain document versions and amendment tracking.
Confidentiality	Lease agreements expose commercially sensitive information.	Apply access controls, encryption, and approved data-processing arrangements.
One additional risk: Conflicting agreements
Suppose the original agreement specifies ₹1,00,000 monthly rent, but a subsequent amendment specifies ₹1,10,000.

LeaseCheck must not simply extract both values and select one arbitrarily.

It should:

Identify both documents.
Determine their effective dates.
Compare the contractual terms.
Flag the conflicting values.
Ask the accountant to verify which terms apply.
This would be a valuable additional capability because real-world lease accounting involves more than processing the original agreement.

6. What Should You Actually Build for the Prototype?
I recommend dividing development into three phases.

Phase 1: Core lease extraction
Build:

PDF upload.
Text extraction and OCR.
AI-based lease information extraction.
Structured JSON output.
Evidence references.
Editable extracted information.
Expected demonstration: Upload an agreement and see its important lease details automatically extracted.

Phase 2: Financial calculations
Build:

Payment schedule generation.
Annual rent escalation handling.
Monthly and annual payment frequencies.
Beginning-of-period and end-of-period payment handling.
Discount-rate input.
Initial lease liability calculation.
Initial ROU asset calculation for a defined scenario.
Interest and depreciation schedules.
Expected demonstration: Verified lease details are converted into an accounting calculation.

Phase 3: Verification and approval
Build:

Missing-field detection.
Conflicting-clause detection.
Evidence viewer.
Accountant review.
Approval and rejection statuses.
PDF accounting report.
Audit history.
Expected demonstration: A finance professional can verify the results and approve the lease record.

7. How to Demonstrate LeaseCheck to Tresata
I would prepare three sample scenarios.

Scenario	Contract condition	Expected system behaviour
1. Simple lease	Fixed monthly rent for five years.	Extract information and calculate liability.
2. Escalating lease	Monthly rent increases by 5% annually.	Identify escalation and generate variable payment schedules.
3. Complex lease	Renewal option, rent-free period, and amendment.	Extract relevant clauses, flag accounting judgments, and request human verification.
The third scenario is particularly important.

It demonstrates that LeaseCheck does not blindly trust AI-generated information.

You can show that the system recognizes uncertainty and involves a human when required.

Suggested evaluation metrics
Metric	What you demonstrate
Field extraction accuracy	How accurately AI extracts contractual information.
Evidence coverage	Percentage of extracted fields with supporting document references.
Clause identification accuracy	Whether important clauses are detected.
Calculation accuracy	Whether the calculated liability matches an independently verified result.
Exception detection	Whether missing and conflicting information is identified.
Processing time	Whether the solution reduces manual effort.
Use independently labeled agreements to measure these metrics. Avoid evaluating the system only on documents or examples used to develop its extraction prompts.

8. My Final Architectural Recommendation
I would present LeaseCheck to Tresata using the following four major components:

Component	Main responsibility	Technology
AI Extraction Engine	Understand lease agreements and extract contractual information.	OCR + LLM
Evidence Verification Engine	Validate extracted information against original clauses and identify inconsistencies.	Python + validation rules
Financial Calculation Engine	Generate payment schedules and calculate lease liabilities and ROU assets.	Python + NumPy
Human Approval System	Allow accountants to review evidence, correct inputs, and approve calculations.	Streamlit interface
The overall workflow is:

Upload → Extract → Verify → Calculate → Review → Approve → Report

One feature I strongly recommend adding: Evidence-Linked Financial Calculations
This could become LeaseCheck's most valuable differentiator.

Imagine a financial controller sees:

Initial Monthly Rent: ₹1,00,000

Instead of simply trusting the extracted value, the controller can click it and see:

Original PDF.
Page 3.
Highlighted contractual clause.
Extracted amount.
Verification status.
Any subsequent amendment affecting the amount.
The same traceability should apply to the lease commencement date, escalation clauses, payment frequency, and other relevant inputs.

This connects the original contract directly to the resulting financial calculation.

It also makes the solution more explainable and easier to audit.

Final positioning for your Tresata assignment
I would describe LeaseCheck as:

LeaseCheck is an AI-assisted lease accounting solution designed to automate the extraction and verification of contractual information from lease agreements and generate accurate, auditable lease liability calculations under Ind AS 116. It combines document intelligence, evidence-based validation, deterministic financial calculations, and human approval to reduce manual accounting effort while maintaining financial accuracy and accountability.

My strongest recommendation: Make extraction accuracy, evidence verification, and calculation reliability the three pillars of LeaseCheck. Do not try to make the LLM perform the entire accounting process.

That will give you a practical architecture, a demonstrable prototype, and a much stronger explanation of why AI is needed in this particular financial accounting workflow.

Design a simple but effective technical architecture for LeaseCheck. I want to use Python, HTML, CSS, JavaScript, PDF text extraction, and a locally running Ollama model. Explain how these components should communicate and how extracted information should be verified before calculations.
LeaseCheck – Technical Architecture Using Python, HTML, CSS, JavaScript and Ollama
For LeaseCheck, I recommend a local, modular web application rather than a complicated cloud-based architecture.

You can build the complete prototype using:

HTML, CSS and JavaScript: Frontend interface.
Python + Flask: Backend and application logic.
PyMuPDF: Extract text from PDF lease agreements.
Ollama: Run a local LLM to understand lease agreements and extract contractual information.
Python validation engine: Verify extracted information against the original document.
Python calculation engine: Calculate lease liabilities and ROU assets under Ind AS 116.
SQLite: Store lease records, verification results, and approval history.
The entire application can run locally on your computer without sending lease agreements to external AI services.

The most important architectural decision is:

Never allow Ollama's extracted values to go directly into the financial calculation engine. They must pass through an evidence verification and validation layer first.

1. Overall System Architecture
Here is the architecture I recommend.

LeaseCheck architecture
                  USER
                   |
                   v
        HTML + CSS + JAVASCRIPT
             FRONTEND
                   |
             HTTP REQUEST
                   |
                   v
             PYTHON FLASK
                BACKEND
                   |
          +--------+---------+
          |                  |
          v                  v
    PDF PROCESSOR        SQLITE DB
          |
          v
     PyMuPDF / OCR
          |
          v
     EXTRACTED TEXT
          |
          v
       OLLAMA LLM
     LOCAL AI MODEL
          |
          v
    STRUCTURED JSON
          |
          v
    VALIDATION ENGINE
          |
     +----+-----+
     |          |
     v          v
  VERIFIED   NEEDS REVIEW
     |          |
     |          v
     |      HUMAN REVIEW
     |          |
     +----+-----+
          |
          v
  FINANCIAL CALCULATION
        ENGINE
          |
          v
   LEASE LIABILITY
      ROU ASSET
   PAYMENT SCHEDULE
          |
          v
     FINAL REPORT
          |
          v
       FRONTEND
I would implement this architecture using separate Python modules so that each component has one responsibility.

2. Technology Stack
Keep the technology stack simple. You do not need React, Node.js, Docker, Kubernetes, or a separate vector database for the first prototype.

Component	Technology	Responsibility
Frontend	HTML	Structure of the application
Styling	CSS	Dashboard design and layout
Frontend interaction	JavaScript	Upload files, call APIs, display results
Backend	Python + Flask	Connect all components
PDF extraction	PyMuPDF	Extract text and page information
AI model	Ollama	Extract and interpret lease information
AI communication	Ollama REST API	Send lease text and receive structured responses
Data validation	Python + Pydantic	Validate extracted fields
Financial calculations	Python + NumPy	Calculate lease liabilities and ROU assets
Database	SQLite	Store extracted information and approval records
Report generation	Python + ReportLab	Generate lease accounting reports
Why Flask instead of Streamlit?
Since you specifically want HTML, CSS, and JavaScript, I recommend Flask.

Flask will serve your frontend and provide backend API endpoints.

Your browser will communicate with Python through HTTP requests.

Ollama will run separately as a local service.

For example:

Browser:
http://127.0.0.1:5000

Flask:
http://127.0.0.1:5000

Ollama:
http://127.0.0.1:11434
The browser never needs to communicate directly with Ollama. Flask acts as the intermediary.

This keeps your model connection, document processing, and financial calculations on the backend.

3. How Each Component Communicates
Let's follow one lease agreement through the entire application.

Step 1: User uploads a PDF
The user opens LeaseCheck in their browser.

The interface contains:

Upload Lease Agreement.
Extract Lease Information.
Verify Information.
Calculate Lease Liability.
Review and Approve.
The user selects a PDF and clicks Upload & Analyse.

Frontend: JavaScript
JavaScript sends the PDF to Flask using fetch() and FormData.

Conceptually:

const formData = new FormData();

formData.append("file", selectedFile);

const response = await fetch("/api/upload", {
    method: "POST",
    body: formData
});

const result = await response.json();

Backend: Flask
Flask receives the document.

It should:

Check that a file was uploaded.
Validate the file extension and actual PDF format.
Generate a unique Lease ID.
Save the document in the uploads directory.
Store its metadata in SQLite.
Start PDF processing.
Example response:

{
    "lease_id": "LC-001",
    "filename": "office_lease.pdf",
    "status": "uploaded",
    "message": "Document uploaded successfully"
}

Important: Validate file size and reject encrypted or malformed PDFs unless you explicitly support them.

Step 2: Extract text from the PDF
Now Flask calls your PDF processor.

I recommend using PyMuPDF (fitz).

It can extract:

Text.
Page numbers.
Document metadata.
Text positions and bounding boxes.
This is useful because you need to show the original evidence behind every extracted value.

Example Python implementation
import fitz

def extract_pdf_text(pdf_path):

    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text("text")

        pages.append({
            "page_number": page_number,
            "text": text
        })

    return pages

Example output:

[
    {
        "page_number": 1,
        "text": "LEASE AGREEMENT..."
    },
    {
        "page_number": 2,
        "text": "The lease shall commence..."
    },
    {
        "page_number": 3,
        "text": "The monthly rent shall be..."
    }
]

Keep each page separate rather than combining the entire PDF into one string.

Why?

Suppose the AI extracts monthly rent as ₹1,00,000.

You want to know exactly which page contains that information.

What about scanned PDFs?
PyMuPDF primarily extracts embedded text. It cannot reliably extract text from image-only scanned pages.

For those documents, add an OCR fallback:

PDF Upload
    |
    v
PyMuPDF Text Extraction
    |
    v
Check Extracted Text
    |
    +---- Sufficient text ---> Continue
    |
    +---- Insufficient text -> OCR
                               |
                               v
                         Extracted Text
Use Tesseract or PaddleOCR for this additional step.

For your first prototype, prioritize text-based PDFs and add OCR as a second-phase feature.

Step 3: Send the extracted text to Ollama
This is where the AI component comes into the system.

Ollama runs your selected language model locally.

For example, you could start with a Qwen instruction-following model that is available through Ollama.

The exact model should be selected based on your computer's available memory and extraction quality.

How communication works
Flask sends the extracted lease text to Ollama through its REST API.

The endpoint is:

http://localhost:11434/api/chat

Ollama processes the prompt and returns a response.

What should the AI extract?
Give the model a specific extraction schema rather than asking it to summarize the lease.

I recommend the following fields:

Category	Fields
Lease identification	Lessee, lessor, asset type
Lease dates	Commencement date, contractual end date
Lease duration	Contractual duration
Payment information	Initial rent, payment frequency, payment timing
Escalation	Escalation percentage, escalation frequency, effective dates
Renewal	Renewal availability, additional period, conditions
Termination	Termination options and conditions
Other payments	Rent-free period, incentives, variable payments
Accounting inputs	Discount rate, direct costs, prepaid payments
The model should also identify the supporting page and exact contractual text for each field.

Example Ollama request
import requests

def extract_lease_information(lease_text):

    prompt = f"""
    You are a lease document extraction assistant.

    Extract the following information from the lease:

    1. Lessee
    2. Lessor
    3. Asset type
    4. Commencement date
    5. Contractual end date
    6. Monthly rent
    7. Payment frequency
    8. Payment timing
    9. Annual escalation
    10. Renewal options
    11. Termination conditions
    12. Rent-free period

    Return structured JSON.

    Rules:
    - Do not invent missing information.
    - Return null for unavailable values.
    - Preserve the original contractual meaning.
    - Include the supporting page number.
    - Include the exact supporting text.

    Lease document:

    {lease_text}
    """


This is an illustrative implementation. In the actual application, parse the JSON, validate its schema, and handle malformed model responses.

Also, don't put a very large agreement into one prompt if it exceeds the model's usable context.

For larger documents, process relevant pages or sections in manageable chunks, preserve page references, and combine the extracted results through a separate consolidation step.

Example AI output
{
    "lessee": {
        "value": "ABC Technologies",
        "page": 1,
        "evidence": "This agreement is entered into between..."
    },
    "commencement_date": {
        "value": "2026-04-01",
        "page": 2,
        "evidence": "The lease shall commence on 1 April 2026."
    },
    "monthly_rent": {
        "value": 100000,
        "currency": "INR",
        "page": 3,
        "evidence": "The monthly rent shall be INR 1,00,000."
    },
    "payment_frequency": {
        "value": "monthly",
        "page": 3,
        "evidence": "Rent shall be payable every month."
    },
    "annual_escalation": {
        "value": 5,
        "unit": "percent",
        "page": 4,
        "evidence": "Rent shall increase by 5% annually."
    },
    "renewal_option": {
        "value": true,
        "additional_months": 36,
        "page": 8,
        "evidence": "The lessee may renew the lease for an additional three years."
    }
}

Notice that the AI extracts the contractual renewal option but does not decide whether exercising that option is reasonably certain.

That distinction belongs in the accounting assessment.

4. Most Important Part: How Extracted Information Should Be Verified
This is where I would put significant effort in LeaseCheck.

You cannot trust every value returned by an LLM.

For example:

The agreement states:

The monthly rental shall be INR 1,10,000.

But Ollama extracts:

{
    "monthly_rent": 100000
}

If you directly use this value, your entire lease liability calculation becomes incorrect.

Therefore, introduce a dedicated Evidence Verification Engine between AI extraction and financial calculations.

A. Three levels of verification
I recommend implementing these checks.

Check 1: Evidence verification
For every extracted field, verify:

Does the referenced page exist?
Does the supporting text actually appear on that page?
Does the supporting text support the extracted value?
Is the extracted value consistent with the contractual wording?
For example:

Field	Extracted value	Evidence	Result
Monthly rent	₹1,00,000	Contract says ₹1,10,000	Failed
Commencement date	01-Apr-2026	Contract says 01-Apr-2026	Passed
Annual escalation	5%	Contract says 5%	Passed
Renewal period	36 months	Contract says 3 years	Passed
One important technical detail: searching for the exact extracted quotation is useful, but quotation matching alone is not enough.

The model might provide a genuine quotation that does not actually support the associated value.

Therefore, verify both the quotation and its meaning.

For a prototype, use:

Exact or normalized text matching.
Page-number verification.
Value consistency checks.
Human review for ambiguous interpretations.
Check 2: Data validation
Once the evidence is checked, validate the extracted values using Python.

For example:

Field	Validation rule
Commencement date	Must be a valid date.
End date	Must be after commencement date.
Monthly rent	Must be numeric and non-negative.
Payment frequency	Must belong to an allowed set.
Escalation	Must have a valid percentage and applicable period.
Renewal period	Must have a valid duration if specified.
Discount rate	Must come from an approved source or finance input.
You can use Pydantic for this.

Illustrative model:

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class LeaseData(BaseModel):

    commencement_date: date

    contractual_end_date: date

    monthly_rent: float = Field(ge=0)

    payment_frequency: str

    annual_escalation: Optional[float] = Field(
        default=None,
        ge=0
    )

    renewal_months: Optional[int] = Field(
        default=None,
        ge=0
    )

    discount_rate: Optional[float] = None

You should add cross-field validation too.

For example, the contractual end date must follow the commencement date.

Also, this initial schema is illustrative: a production-quality implementation should represent payment amounts and currencies, dates, escalation rules, and evidence references with more precise types.

Check 3: Accounting readiness
Even if all extracted information is correct, the agreement may not be ready for calculation.

Consider:

The renewal option exists, but its accounting assessment is incomplete.
The discount rate has not been provided.
Payment timing is unclear.
An amendment conflicts with the original agreement.
The contract contains variable payments requiring separate treatment.
LeaseCheck should generate a readiness status.

Status	Meaning
Verified	Evidence and data checks passed.
Needs Review	Some information is ambiguous.
Missing Information	Required input is unavailable.
Conflict Detected	Multiple documents contain inconsistent terms.
Calculation Ready	All required calculation inputs and accounting assessments are approved.
Only records marked Calculation Ready should enter the calculation engine.

Importantly, this status must be based on accounting requirements, not simply on whether all JSON fields are populated.

B. How to implement the verification flow
          AI EXTRACTED JSON
                  |
                  v
          JSON SCHEMA CHECK
                  |
          +-------+-------+
          |               |
        VALID           INVALID
          |               |
          v               v
     EVIDENCE CHECK    REPROCESS
          |
          v
     VALUE VALIDATION
          |
          v
     ACCOUNTING REVIEW
          |
     +----+-----+
     |          |
   READY     NOT READY
     |          |
     v          v
 CALCULATE   HUMAN REVIEW
                |
                v
           CORRECT DATA
                |
                v
           REVALIDATE
A useful implementation detail is to store both the original AI extraction and the corrected, approved values.

Never overwrite the original extraction without maintaining a history.

This allows auditors and reviewers to see what the model extracted and what the accountant changed.

5. Financial Calculation Engine
Once the information is verified and approved, Flask calls your calculation module.

The calculation engine should not communicate directly with Ollama.

Its input should be a validated Python object.

Example input
{
    "commencement_date": "2026-04-01",
    "contractual_end_date": "2031-03-31",
    "monthly_rent": 100000,
    "payment_frequency": "monthly",
    "payment_timing": "beginning",
    "annual_escalation": 5,
    "discount_rate": 10,
    "renewal_months": null
}

The calculation engine should then:

1. Determine the approved lease term.

Use the contractual dates together with the approved accounting assessment of renewal and termination options.

2. Generate the payment schedule.

Apply escalation rules and payment dates.

3. Calculate the initial lease liability.

Discount qualifying lease payments using the approved discount rate.

4. Calculate the initial ROU asset.

Include the applicable adjustments under Ind AS 116.

5. Generate subsequent schedules.

Calculate interest, payments, closing liability, and depreciation.

Important accounting design decision
Store the discount rate as an explicit input with:

Rate value.
Rate period.
Effective date.
Currency.
Source or approved methodology.
Reviewer or approval status.
Do not simply store 10 and assume that everyone knows whether it means 10% annually, monthly, nominal, or effective.

Similarly, support payment timing explicitly. A beginning-of-month payment schedule differs from an end-of-month schedule.

For the first prototype, support a simple fixed-rent or annual-escalation lease with clearly defined assumptions. Add more complex clauses incrementally.

6. How the Frontend Should Display the Results
I recommend a clean dashboard with five main sections.

Screen 1: Dashboard
Show:

Total leases uploaded.
Successfully extracted leases.
Leases requiring review.
Calculation-ready leases.
Approved leases.
Screen 2: Upload Agreement
Provide:

PDF upload button.
Document name.
Upload status.
Analyse button.
Screen 3: Extracted Lease Information
Display an editable table:

Parameter	Extracted value	Verification
Lease commencement	01-Apr-2026	Verified
Lease end	31-Mar-2031	Verified
Monthly rent	₹1,00,000	Verified
Payment frequency	Monthly	Verified
Annual escalation	5%	Verified
Renewal option	3 years	Needs Review
Clicking a field should open the corresponding page and supporting text.

Screen 4: Financial Calculations
Display:

Initial lease liability.
Initial ROU asset.
Total contractual payments.
Total interest over the schedule.
Annual depreciation.
Monthly amortization schedule.
You can use JavaScript charts to display the liability reduction over time.

Screen 5: Review and Approval
Provide:

Extracted values.
Original supporting evidence.
Validation messages.
Editable fields.
Approve / Reject buttons.
Reviewer comments.
This is where the user completes the accounting review.

7. Backend API Design
To keep communication organized, I recommend the following Flask endpoints.

API endpoint	Method	Responsibility
/api/upload	POST	Upload PDF.
/api/extract/<lease_id>	POST	Extract PDF text and call Ollama.
/api/verify/<lease_id>	POST	Verify extracted fields and evidence.
/api/lease/<lease_id>	GET	Retrieve lease information.
/api/lease/<lease_id>	PUT	Update extracted or corrected values.
/api/calculate/<lease_id>	POST	Generate financial calculations.
/api/approve/<lease_id>	POST	Approve or reject calculations.
/api/report/<lease_id>	GET	Generate or retrieve the accounting report.
The frontend calls these endpoints using JavaScript fetch().

Flask handles the business logic and communicates with the relevant Python modules.

For a longer-running Ollama extraction, use an asynchronous job status rather than making the browser wait indefinitely. You can begin with a simple background worker or task queue if needed.

8. Recommended Folder Structure
I would organize your project like this:

LeaseCheck/
│
├── app.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       ├── js/
│       │   └── script.js
│       │
│       └── assets/
│
├── backend/
│   ├── pdf_processor.py
│   ├── ocr_processor.py
│   ├── ollama_client.py
│   ├── lease_extractor.py
│   ├── evidence_verifier.py
│   ├── validation_engine.py
│   ├── lease_calculator.py
│   ├── approval_manager.py
│   └── report_generator.py
│
├── database/
│   ├── db_manager.py
│   └── schema.sql
│
├── prompts/
│   └── extraction_prompt.txt
│
├── uploads/
│
├── outputs/
│
├── tests/
│   ├── test_extraction.py
│   ├── test_evidence.py
│   └── test_calculations.py
│
├── requirements.txt
│
└── README.md
Responsibility of each important file
File	Function
app.py	Flask application and API routes.
pdf_processor.py	Extract text and page references.
ollama_client.py	Communicate with the local Ollama API.
lease_extractor.py	Prepare prompts and parse model responses.
evidence_verifier.py	Check supporting contractual evidence.
validation_engine.py	Validate extracted data and accounting readiness.
lease_calculator.py	Calculate lease liability and ROU asset.
approval_manager.py	Manage human review and approval.
report_generator.py	Generate final accounting reports.
9. How to Build It in the Right Order
Don't build all the components simultaneously.

I recommend this sequence.

Phase	Development task	Expected output
1	HTML/CSS/JS interface	Working upload dashboard.
2	Flask backend	Frontend-backend communication.
3	PyMuPDF integration	PDF text extraction.
4	Ollama integration	Structured lease information extraction.
5	Evidence verification	Source-linked extracted fields.
6	Validation engine	Missing and conflicting information detection.
7	Financial calculation engine	Lease liability and ROU calculations.
8	Human approval	Accountant review workflow.
9	SQLite and reporting	Persistent records and downloadable reports.
I would initially test the extraction engine using three different lease agreements:

A simple fixed-rent agreement.
An agreement with annual escalation.
An agreement with renewal options and rent-free periods.
This will help you understand how well the model handles different contractual structures before you integrate everything.

10. Important Technical Decisions
Before implementation, I recommend making these five decisions.

Decision	My recommendation	Reason
Backend	Flask	Simple integration with HTML, CSS, JS, and Python.
AI model	Ollama with Qwen	Local document understanding without external API calls.
PDF processing	PyMuPDF	Simple text extraction with page references.
Verification	Python rules + evidence matching + human review	Prevents blindly trusting AI outputs.
Calculations	Pure Python	Reproducible and testable financial calculations.
Additional safeguards
Because lease agreements contain commercially sensitive information:

Keep uploaded documents and the database locally.
Do not expose Ollama's port to the public internet.
Restrict access to uploaded files.
Validate uploaded PDFs and limit file sizes.
Maintain an audit history of corrections and approvals.
Avoid sending confidential documents to external services.
Use backups and appropriate access controls if multiple people use the application.
11. What Makes LeaseCheck Different?
I would avoid positioning LeaseCheck as simply another PDF-to-JSON extraction tool.

Its real value should come from connecting three things:

Capability	What it provides
AI document understanding	Extracts lease terms from complex agreements.
Evidence-based verification	Shows exactly where each extracted value came from.
Financial calculation	Converts verified contractual information into lease accounting outputs.
Consider this example:

A finance professional sees:

Annual Escalation: 5%

They click the value and LeaseCheck displays:

Original PDF.
Page 4.
Relevant contractual clause.
Extracted escalation percentage.
Verification status.
Generated payment schedule reflecting that escalation.
This makes the result explainable rather than just presenting an AI-generated number.

12. Final Architecture I Recommend
For your assignment, this is the architecture I would present:

                LEASECHECK
                     |
          +----------+----------+
          |                     |
          v                     v
      FRONTEND              BACKEND
   HTML/CSS/JS              PYTHON
          |                     |
          |                Flask API
          |                     |
          |                     v
          |              PDF PROCESSOR
          |                PyMuPDF
          |                     |
          |                     v
          |                OLLAMA LLM
          |               Local Qwen
          |                     |
          |                     v
          |              JSON EXTRACTION
          |                     |
          |                     v
          |             EVIDENCE VERIFIER
          |                     |
          |                     v
          |              DATA VALIDATOR
          |                     |
          |              +------+------+
          |              |             |
          |              v             v
          |          VERIFIED      NEEDS REVIEW
          |              |             |
          |              |        HUMAN REVIEW
          |              |             |
          |              +------+------+
          |                     |
          |                     v
          |             CALCULATION ENGINE
          |                  Python
          |                     |
          |                     v
          |              FINANCIAL RESULTS
          |                     |
          |                     v
          |              HUMAN APPROVAL
          |                     |
          |                     v
          +--------------> REPORTS
                                |
                                v
                             SQLITE
SQLite should also store intermediate extraction results, document references, verification outcomes, and approval history—not just final reports.

My final recommendation
Build LeaseCheck as a local AI-powered financial document processing application, with Flask coordinating the frontend, PDF extraction, Ollama, verification, and calculations.

Keep the architecture modular, and make the verification layer mandatory.

Your central workflow should be:

Upload Lease → Extract Information → Verify Evidence → Validate Accounting Inputs → Calculate Lease Liability → Human Approval → Generate Report.

This is technically achievable with your chosen technologies and gives you a clear demonstration of AI, financial accounting, document intelligence, and human-in-the-loop controls.

One thing to remember for the Tresata evaluation: The strongest part of LeaseCheck should not be that it uses an LLM. It should be that every important financial result can be traced back to the original lease agreement and independently reproduced through a deterministic calculation engine.

