---
name: business-doc-integrity
description: Check business and product documents for consistency, internal logic, terminology stability, unsupported claims, cross-section contradictions, and execution credibility. Use when the user wants to verify a 项目可行性研究报告, 项目建议书, PRD, 产品需求说明书, 架构设计, 技术方案, 实施方案, or final draft before review, approval, or delivery. Triggers on requests like: 检查一致性, 做文档校验, 看看有没有前后冲突, 查查这份方案有没有硬伤, 核查这份 PRD, 校验架构设计, integrity check this document, consistency check this proposal, validate this draft.
---

# Business Doc Integrity

Check whether a business document is internally trustworthy and decision-ready.

This is not academic citation verification.
This skill focuses on document integrity in enterprise writing:
- consistency
- logic
- terminology
- scope alignment
- numeric stability
- execution realism
- structure-to-content balance

## Core rule

Do not only point out that something feels vague.

Whenever possible, identify:
1. what is inconsistent,
2. where it appears,
3. why it is risky,
4. what should be reconciled.

## Main check modes

### 1. full
Use for a complete integrity pass.

Check:
- terminology consistency
- number consistency
- timeline consistency
- scope consistency
- section-to-section logic
- recommendation support
- risk closure

### 2. consistency-only
Use when the user mainly wants to find contradictions.

### 3. logic-only
Use when the user mainly wants to test whether conclusions and recommendations are supported.

### 4. final-gate
Use before approval, submission, or final delivery.

This mode is stricter and should answer:
- is this ready to circulate?
- what still blocks decision confidence?

## What to check

### A. Terminology consistency

Look for:
- one thing called by multiple names
- module names changing across sections
- role names shifting
- business terms and technical terms being mixed carelessly

Examples:
- “统一认证中心” later becomes “SSO平台” and later “认证网关” without clarification
- “试点阶段” and “一期建设” used as if they mean the same thing

### B. Number consistency

Look for:
- budget numbers changing between sections
- timeline counts not matching milestones
- user volume / traffic / resource assumptions changing without explanation
- counts in summary not matching detail tables

### C. Timeline consistency

Look for:
- milestone order conflicts
- implementation tasks happening before prerequisites
- rollout timing inconsistent with dependency timing

### D. Scope consistency

Look for:
- scope and non-scope contradicting each other
- summary promising more than detailed sections support
- PRD requirements exceeding the declared objective
- architecture covering less than the claimed business scope

### E. Logic and recommendation support

Look for:
- recommendation appears before real comparison
- conclusion is stronger than evidence
- “necessary” is asserted but not shown
- “feasible” is declared without addressing key constraints

### F. Risk closure

Look for:
- major risks named but not mitigated
- mitigation measures too generic to be actionable
- no owner or trigger condition for risk handling
- dependencies mentioned without contingency thinking

### G. Cross-document alignment

When the user provides multiple related materials, check alignment between them:
- brief vs proposal
- PRD vs architecture design
- proposal vs implementation plan
- feasibility report vs executive summary

### H. Skeletonization / hollow-outline risk

Look for:
- too many headings with too little development under each
- sections that only restate the heading in sentence form
- core claims appearing in summary/conclusion without being developed earlier
- multiple sections with very low information gain
- documents that look complete structurally but remain thin operationally

## Workflow

### Step 1: Identify document type

Use `references/integrity-matrix.md` to adjust emphasis.

### Step 2: Scan for structural weak points

Before line-by-line issues, detect the big failure modes:
- recommendation unsupported
- scope drifting
- architecture-document mismatch
- optimistic timeline fantasy
- decorative risk section
- hollow-outline structure with insufficient expansion

### Step 3: Produce issue list with evidence

For each issue, include:
- issue title
- severity
- location
- conflicting statements or sections
- why it matters
- suggested reconciliation

### Step 4: Give gate decision

Use one of these:
- Pass
- Pass with fixes
- Needs revision before circulation
- Not credible enough yet

## Severity scale

- **Critical**: breaks trust or blocks approval/implementation
- **High**: likely to cause major confusion, rework, or bad decisions
- **Medium**: important inconsistency or weakness, but repairable
- **Low**: polish-level issue

## Output format

### 1. Integrity summary
- what is stable
- what is unstable
- whether the document is safe to circulate

### 2. Key findings
List the most important contradictions or unsupported jumps first.
Also call out if the document is structurally complete but informationally thin.

### 3. Detailed issue table
Include:
- issue
- severity
- location
- conflicting or weak statements
- suggested fix

### 4. Reconciliation checklist
Group into:
- Must reconcile now
- Should tighten next
- Optional cleanup

### 5. Gate decision
State the final gate result clearly.

## Good integrity feedback

Good:
- “Section 2 says Phase 1 only covers internal users, but Section 4.3 includes partner-side portal access. Scope needs reconciliation.”
- “The proposal recommends immediate rollout, but the implementation section still depends on data governance rules that are marked as pending. Recommendation is ahead of prerequisites.”

Bad:
- “This feels a little inconsistent in places.”

## References

Read when relevant:
- `references/integrity-matrix.md` — integrity focus by document type
- `references/failure-patterns.md` — common business document failure modes
- `references/output-format.md` — recommended report structure
