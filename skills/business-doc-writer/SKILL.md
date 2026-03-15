---
name: business-doc-writer
description: Write structured business documents for project and product work. Use when the user needs a 项目可行性研究报告, 项目建议书, 产品需求说明书/PRD, 产品架构设计, 技术方案, 实施方案, executive summary, or wants help turning messy notes into a formal business document draft. Triggers on requests like: 写可研, 写项目建议书, 写PRD, 写产品需求文档, 写架构设计, 写技术方案, 写实施方案, 生成正式文档, 把这些材料整理成文档, turn this brief into a proposal, write a feasibility report, write a PRD, write an architecture design doc.
---

# Business Doc Writer

Write formal business and product documents from rough notes, briefs, meeting notes, or partially structured inputs.

## Core rule

Do not pretend missing facts are settled.

When information is incomplete:
1. make reasonable structure decisions,
2. mark assumptions explicitly,
3. list open questions clearly,
4. keep the draft usable instead of blocking completely.

Also follow this rule strictly:

**write depth before breadth.**

A document with fewer sections but substantial content is better than a document with many thin sections.
Do not generate a heading unless you can actually develop it with meaningful content.

## Supported document modes

Select the nearest mode based on user intent:

1. **feasibility-report**
   - For 项目可行性研究报告 / feasibility analysis
   - Focus on necessity, options comparison, feasibility, cost-benefit, risk, recommendation

2. **project-proposal**
   - For 项目建议书 / proposal / 立项材料
   - Focus on background, objectives, scope, expected outcomes, implementation path

3. **prd**
   - For 产品需求说明书 / PRD / requirement doc
   - Focus on users, scenarios, scope, functional requirements, non-functional requirements, acceptance criteria

4. **architecture-design**
   - For 产品架构设计 / 技术架构方案 / solution architecture
   - Focus on principles, modules, interfaces, data flow, deployment, security, scalability, trade-offs

5. **implementation-plan**
   - For 实施方案 / rollout / delivery plan
   - Focus on milestones, responsibilities, dependencies, resources, risks, acceptance

6. **executive-summary**
   - For one-page summaries for managers / leaders
   - Focus on decision-ready clarity, not detail overload

If ambiguous, ask 1-3 clarifying questions max. If still ambiguous, default to the most practical output and say what assumption you made.

## Workflow

### Step 1: Identify document type

Infer the target doc type.

If the user only gives raw material, first classify it using `references/doc-types.md`.

### Step 2: Check input sufficiency

Look for the minimum viable inputs:
- background / context
- objective
- target audience
- scope
- constraints
- timeline or urgency

If any are missing, do one of these:
- ask concise questions if the missing info is critical,
- or proceed with explicit assumptions if drafting is still useful.

### Step 3: Build a clean outline

Before drafting, decide the section structure.

Use the matching reference:
- `references/feasibility-report.md`
- `references/project-proposal.md`
- `references/prd.md`
- `references/architecture-design.md`

Use the template under `assets/templates/` only when you need a fast skeleton.

### Step 4: Draft like a real working document

Write in a style suitable for internal business communication:
- direct
- structured
- decision-oriented
- low fluff
- explicit assumptions
- explicit dependencies
- explicit risks

Avoid:
- slogan-heavy writing
- generic AI filler
- academic tone unless the user wants it
- vague claims without basis

### Step 4.5: Prevent hollow-outline writing

Do not write a document as a "table of contents with comments".

For every major section, include at least **2-3 kinds of substance** from the list below:
- current facts or current state
- concrete problems
- constraints or dependencies
- option details or implementation detail
- risks or trade-offs
- scenarios or examples
- basis for judgment / recommendation logic

If a section only contains 1-2 generic sentences, do one of these instead:
- merge it into a neighboring section,
- expand it with real substance,
- mark it as pending with specific missing information.

Prefer:
- fewer but thicker sections
- explicit reasoning
- concrete details

Reject:
- headings that only repeat the title in sentence form
- sections that say a thing is important but do not explain why
- decorative summary language with no operational value

### Step 5: Add operational value

When helpful, append these sections:
- Assumptions
- Open Questions
- Risks and Dependencies
- Decision Points
- Suggested Next Actions

These are often more useful than polishing prose.

## Output rules by document type

### feasibility-report

Default sections:
1. Project background
2. Necessity of construction / why now
3. Current-state analysis
4. Options comparison
5. Business feasibility
6. Technical feasibility
7. Economic / cost-benefit feasibility
8. Risk analysis
9. Implementation suggestion
10. Conclusion

Always include:
- comparison of at least 2 options when possible
- explicit risk section
- recommendation with rationale

### project-proposal

Default sections:
1. Background
2. Objectives
3. Scope
4. Main construction content
5. Expected outcomes
6. Implementation path
7. Resource request / budget estimate
8. Risks and safeguards
9. Recommendation

Emphasize:
- why this project should be approved
- what success looks like

### prd

Default sections:
1. Background and goals
2. Users and scenarios
3. Scope and non-scope
4. Functional requirements
5. Non-functional requirements
6. Dependencies and constraints
7. Milestones
8. Acceptance criteria
9. Risks

Emphasize:
- clarity over elegance
- testability
- boundary definition

### architecture-design

Default sections:
1. Design goals
2. Scope
3. Design principles
4. High-level architecture
5. Module breakdown
6. Data flow / integration flow
7. Key technical choices
8. Security / performance / reliability
9. Deployment and evolution path
10. Risks and trade-offs

Emphasize:
- why this architecture, not just what it is
- trade-offs and constraints

### implementation-plan

Default sections:
1. Objectives
2. Scope
3. Work breakdown
4. Milestones and timeline
5. Roles and responsibilities
6. Dependencies
7. Risks and mitigation
8. Acceptance and delivery criteria

## Writing standards

### Good style
- use concrete nouns
- use short paragraphs
- prefer bullets for requirements and risks
- state decisions clearly
- distinguish facts, assumptions, and proposals
- explain why, not just what
- develop core sections with enough supporting detail to stand on their own

### Bad style
- “赋能、抓手、闭环、全面提升” style filler unless the user explicitly wants official/government style
- generic “this project is of great significance” language without specifics
- giant unbroken paragraphs
- mixing requirements, assumptions, and implementation details without labels
- many headings with only 1-2 shallow sentences each
- sections that read like expanded bullet labels instead of real content

## Missing-information policy

If details are missing, do not stop by default.

But do not use missing information as an excuse for hollow sections.
If detail is missing, explicitly write:
- what is known,
- what is assumed,
- what still needs confirmation,
- how that uncertainty affects the recommendation.

Use this block near the end when needed:

```md
## Assumptions and open questions

### Current assumptions
- ...

### Open questions to confirm
- ...
```

## File and formatting behavior

If the user asks for a deliverable file:
- write Markdown first unless they explicitly want another format
- use clear headings and stable section numbering
- name the file after the document type and topic

## References

Read these only when relevant:
- `references/doc-types.md` — choose the right document mode
- `references/feasibility-report.md` — feasibility report structure and heuristics
- `references/project-proposal.md` — proposal structure and approval-oriented writing
- `references/prd.md` — PRD structure and requirement-writing rules
- `references/architecture-design.md` — architecture design structure and review points
