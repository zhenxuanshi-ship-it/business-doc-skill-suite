---
name: biz-discovery
description: Clarify messy business inputs into structured project briefs before formal document writing. Use when the user has rough ideas, meeting notes, chat logs, leadership instructions, project fragments, or unclear requirements and wants to turn them into a usable brief for 项目可行性研究报告, 项目建议书, PRD, 架构设计, 技术方案, or实施方案. Triggers on requests like: 帮我梳理这个项目, 把会议纪要整理成项目输入, 先澄清需求, 帮我拆项目边界, 整理这些想法, turn these notes into a brief, clarify this project, organize these requirements.
---

# Biz Discovery

Turn messy business input into a structured, decision-usable project brief.

This skill is the front-end of the business-doc workflow.

Use it before formal drafting when the user has:
- vague goals,
- mixed stakeholder input,
- scattered notes,
- unclear scope,
- incomplete assumptions.

## Core rule

Do not over-formalize too early.

The goal is not to write the final document.
The goal is to produce a clean intermediate artifact that makes writing easier and less fake.

## Primary outputs

Choose the right combination based on the situation:

- `project-brief.md`
- `scope-definition.md`
- `stakeholder-map.md`
- `requirements-seed.md`
- `risk-list.md`
- `open-questions.md`
- `recommended-next-doc.md`

## Main modes

### 1. brief
Use when the user wants a clean summary of a project idea.

Output:
- project background
- objective
- target audience/stakeholders
- scope
- constraints
- suggested next step

### 2. notes-to-brief
Use when the user provides meeting notes, raw bullets, or chat logs.

Output:
- structured brief
- extracted decisions
- unresolved questions
- action items

### 3. scope-clarification
Use when the problem is mainly boundary confusion.

Output:
- in-scope
- out-of-scope
- assumptions
- dependencies
- unresolved boundary items

### 4. requirements-seed
Use before PRD writing.

Output:
- goals
- user roles
- scenarios
- rough functional requirements
- rough non-functional requirements
- open product questions

### 5. proposal-intake
Use before project proposal / feasibility report writing.

Output:
- business context
- why now
- expected outcomes
- constraints
- initial options / direction
- risk prompts

## Workflow

### Step 1: classify the input material

Typical input types:
- meeting notes
- leadership message / high-level instruction
- rough idea description
- fragmented requirements
- chat screenshots copied as text
- old document excerpts

Use `references/input-patterns.md` if needed.

### Step 2: find the real center of gravity

Identify:
- what problem is being solved
- for whom
- why now
- what success might look like
- what constraints are already present

Do not assume the loudest detail is the most important one.

### Step 3: separate facts from assumptions from wishes

Always distinguish these three categories:

1. **Known facts**
2. **Working assumptions**
3. **Open questions / unknowns**

This separation is critical.

### Step 4: define scope and stakeholders

At minimum, try to extract:
- target users / stakeholders
- owner / sponsor if known
- main business scope
- non-scope if inferable
- external dependencies

### Step 5: recommend the next document type

Map the result into the next best document:
- feasibility-report
- project-proposal
- prd
- architecture-design
- implementation-plan

Use `references/next-doc-mapping.md`.

## Output structure

Default output sections:

### 1. Project brief
Include:
- background
- objective
- target stakeholders
- expected outcomes

### 2. Scope snapshot
Include:
- in scope
- likely out of scope
- dependencies
- constraints

### 3. Assumptions and unknowns
Split clearly:
- known facts
- assumptions
- open questions

### 4. Risks / ambiguity points
List the biggest uncertainty sources.

### 5. Recommended next step
State:
- which document should be written next
- what information is still missing

## When to ask questions

Ask concise questions only when they materially change the direction.

Good clarifying questions:
- “This is closer to a project proposal or a PRD. Which one do you want first?”
- “Is the primary goal approval, implementation, or requirement clarification?”
- “Who is the main audience: leadership, product team, or engineering team?”

Bad clarifying questions:
- long interviews up front
- asking for every detail before producing anything useful

## Good discovery behavior

Good:
- compress messy input into structure
- expose ambiguity instead of hiding it
- preserve useful raw intent
- identify missing decision points

Bad:
- immediately writing polished formal prose
- inventing business context
- forcing certainty where none exists

## References

Read when relevant:
- `references/input-patterns.md` — map messy input to discovery mode
- `references/brief-structure.md` — standard project brief structure
- `references/next-doc-mapping.md` — decide the next document type
- `references/question-strategy.md` — ask fewer, better clarification questions
