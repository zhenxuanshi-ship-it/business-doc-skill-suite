---
name: business-doc-reviewer
description: Review business and product documents from enterprise decision-making perspectives. Use when the user wants to review, critique, stress-test, or improve a 项目可行性研究报告, 项目建议书, PRD, 产品需求说明书, 架构设计, 技术方案, 实施方案, or executive summary. Triggers on requests like: 审一下这份文档, 帮我 review, 看看这份可研有没有问题, 评审这份 PRD, 评估这份架构方案, 找风险, 给修改意见, challenge this proposal, review this business doc, critique this architecture design.
---

# Business Doc Reviewer

Review business documents from multiple enterprise roles instead of academic reviewer roles.

## Agent execution preference

This skill is designed to run in the main / coordinator session by default.

**Default: main agent reviews directly.** The main agent should do the review work directly.

**Sub-agent mode only when user specifies.** Only use sub-agent for review when the user explicitly asks for it, such as:
- "用子代理review"
- "派生子代理评审"

For all other cases, review directly in the main session.

## Core goal

Do not just say whether a document is good.

Produce feedback that can be used to revise the document:
- specific issues
- why they matter
- where they appear
- what to change
- priority level

## Default reviewer panel

Use these roles unless the user asks for a narrower review.

1. **business-reviewer**
   - Check business value, strategic fit, necessity, and outcome clarity

2. **product-reviewer**
   - Check user value, scope boundaries, requirement clarity, and acceptance logic

3. **technical-reviewer**
   - Check architecture feasibility, implementation complexity, dependencies, and technical trade-offs

4. **delivery-reviewer**
   - Check timeline realism, milestones, resourcing, execution feasibility, and cross-team coordination

5. **risk-reviewer**
   - Check risks, assumptions, compliance concerns, operational constraints, and mitigation quality

6. **devils-advocate**
   - Challenge the whole proposal: why it may fail, why it may not be worth doing now, and what weak assumptions are carrying the document

## Supported review modes

### 1. full
Use for default comprehensive review.

Output:
- multi-role review summary
- prioritized issue list
- revision roadmap
- overall recommendation

### 2. quick
Use when the user wants a fast pass.

Output:
- top issues only
- no long role-by-role writeup

### 3. business-focus
Use when the user mainly cares about value, necessity, ROI, and project justification.

### 4. product-focus
Use for PRD and requirement docs.

### 5. technical-focus
Use for architecture design and technical方案.

### 6. risk-focus
Use when the user explicitly wants to find blind spots, blockers, dependencies, or compliance issues.

### 7. guided
Use when the user wants to improve the document interactively instead of receiving a static report.

## Review workflow

### Step 1: Identify document type

Classify the input doc using `references/doc-review-matrix.md`.

Main categories:
- feasibility-report
- project-proposal
- prd
- architecture-design
- implementation-plan
- executive-summary

### Step 2: Select the right review emphasis

Adjust by document type:

- **feasibility-report**
  - emphasize business case, options comparison, feasibility logic, risks, recommendation quality

- **project-proposal**
  - emphasize approval logic, expected outcomes, scope clarity, resource reasonableness

- **prd**
  - emphasize scope, scenarios, requirement quality, testability, acceptance criteria

- **architecture-design**
  - emphasize module boundaries, trade-offs, data flow, scaling, security, implementation reality

- **implementation-plan**
  - emphasize milestones, ownership, dependencies, execution risk, feasibility

### Step 3: Review for decision quality, not just writing quality

Always check these dimensions:

1. **clarity**
   - Is the document understandable?
   - Are terms stable and explicit?

2. **completeness**
   - Are key sections missing?
   - Does it omit obvious constraints or dependencies?

3. **credibility**
   - Are claims supported by specifics?
   - Are assumptions pretending to be facts?

4. **executability**
   - Can someone actually use this document to decide or implement?

5. **risk awareness**
   - Are real risks named?
   - Are mitigations usable or decorative?

6. **content density / expansion quality**
   - Is each major section actually developed?
   - Does the document contain substance, or just headings plus short summaries?
   - Are core sections written through, or merely introduced?

7. **argument depth / reasoning sufficiency**
   - Does the document merely state conclusions, or does it actually support them?
   - Are necessity, scope, budget, implementation path, and recommendation argued with enough depth?
   - Does the middle of the document do the work required by the ending?

### Step 4: Convert review into action

Do not stop at critique.

Always end with:
- prioritized issues
- what to fix first
- what can wait
- what should be removed, clarified, or restructured

When reviewing project proposals or feasibility reports, explicitly check whether the document is:
- only structurally complete, or
- genuinely report-grade and discussion-ready.

## Severity model

Use this scale:

- **Critical**
  - blocks approval, implementation, or trust
  - example: recommendation has no basis, core scope is undefined, architecture cannot support stated needs

- **High**
  - serious weakness that will likely cause confusion, rework, or risk

- **Medium**
  - fixable but important quality gap

- **Low**
  - polish-level issue that does not change core usability

Also assess **skeletonization risk**:
- **High**: many headings, thin sections, low information density, document feels like an annotated outline
- **Medium**: some major sections are underdeveloped
- **Low**: core sections have real substance and decision value

For long-form documents, also assess **report maturity**:
- **Draft-grade**: usable as an internal outline or early draft only
- **Discussion-grade**: usable for internal review and structured discussion
- **Submission-grade**: strong enough for formal internal circulation or submission with minor polishing

## Output format

Default output sections:

### 1. Overall judgment
Give a direct summary in 3-6 bullets:
- what is strong
- what is weak
- whether it is usable now
- what must be fixed before use
- whether the document suffers from skeletonization

### 2. Role-by-role findings
For each active reviewer role, summarize:
- main concern
- strongest positive point
- strongest negative point
- recommended change

### 3. Prioritized issue list
Use a table or bullets with:
- issue
- severity
- section/location
- why it matters
- suggested fix

### 4. Revision roadmap
Group actions into:
- Fix now
- Fix next
- Optional improvements

### 5. Final recommendation
Use one of these:
- Ready to use
- Usable after minor revision
- Needs major revision
- Not decision-ready

## Guided mode behavior

In `guided` mode:
- do not dump the whole review at once
- surface 1-2 important issues first
- ask the user to choose which one to improve
- help rewrite section by section

## Writing style for review

Be direct.

Good:
- “The recommendation is too early because the options comparison is not real yet.”
- “The PRD mixes user need, implementation detail, and acceptance criteria in the same section.”
- “This section is only a heading plus commentary. It still does not explain the actual implementation or decision basis.”
- “These bullet points name the right ideas, but they still need paragraph-level expansion to be usable in a formal document.”

Bad:
- “This document demonstrates strong potential but may benefit from further enhancement in several areas.”

When you detect hollow-outline writing, say so explicitly.
Do not hide it behind vague quality language.

## References

Read when relevant:
- `references/doc-review-matrix.md` — map doc type to review dimensions
- `references/review-rubrics.md` — review criteria by role
- `references/output-patterns.md` — how to structure review output and revision roadmaps
