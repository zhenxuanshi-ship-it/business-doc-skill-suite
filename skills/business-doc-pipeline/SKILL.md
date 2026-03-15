---
name: business-doc-pipeline
description: Orchestrate a business document workflow across discovery, drafting, review, revision, and finalization. Use when the user wants an end-to-end workflow for 项目可行性研究报告, 项目建议书, PRD, 产品需求说明书, 架构设计, 技术方案, 实施方案, or wants to move from notes to draft to review to revision. Triggers on requests like: 从头到尾搞定这份文档, 帮我走完整流程, 先写再 review 再修改, end-to-end business document workflow, document pipeline, 从需求到成稿, 把这份方案一路做完.
---

# Business Doc Pipeline

This skill is a lightweight orchestrator.

It does not replace `business-doc-writer` or `business-doc-reviewer`.
Its job is to:
- detect current stage,
- recommend the next stage,
- route to the right skill,
- keep the workflow structured,
- avoid messy jumps.

## Core stages

1. **discovery**
   - clarify goals, audience, scope, constraints, and missing inputs

2. **blueprint**
   - choose doc type and outline

3. **draft**
   - generate first usable draft

4. **review**
   - run multi-role document review

5. **revise**
   - revise based on issues and roadmap

6. **finalize**
   - prepare the final usable version

## Routing rules

### Start at discovery when:
- the user has only ideas, notes, or vague goals
- the user says they are not sure what kind of doc to write
- the scope is still unclear

### Start at blueprint when:
- the goal is clear but the structure is not
- the user asks for an outline first

### Start at draft when:
- the user already knows the doc type and wants a first draft
- enough context exists to write a useful version

### Start at review when:
- the user already has a draft
- the user asks to critique, challenge, or assess a document

### Start at revise when:
- the user has review comments or a revision roadmap
- the user asks to update an existing draft based on feedback

### Start at finalize when:
- the draft is already good enough
- the user mainly wants a clean final version or delivery package

## Pipeline behavior

### Step 1: detect current stage

Infer from user input and materials.

Common cues:
- notes / minutes / rough ideas -> discovery
- outline request -> blueprint
- "write" -> draft
- "review" / "评审" -> review
- "revise" / "修改" / comments -> revise
- "final version" / "定稿" -> finalize

### Step 2: choose document type

Map the work to one of these:
- feasibility-report
- project-proposal
- prd
- architecture-design
- implementation-plan
- executive-summary

Use `references/doc-stage-matrix.md` when the type is unclear.

### Step 3: produce a checkpointed recommendation

After deciding the stage, explicitly tell the user:
1. current stage
2. target doc type
3. recommended next action
4. what input is still missing

Use concise checkpoint language.

### Step 4: hand off to the right skill

- drafting work -> `business-doc-writer`
- review work -> `business-doc-reviewer`

### Step 5: keep the workflow honest

Do not pretend the pipeline is complete if major gaps remain.

Always surface:
- assumptions
- blockers
- missing inputs
- next best action

## Recommended flow patterns

### Pattern A: from messy notes to usable draft

`discovery -> blueprint -> draft`

Use when the user is early-stage.

### Pattern B: draft to decision-ready document

`draft -> review -> revise -> finalize`

Use when the user already has something written.

### Pattern C: full workflow

`discovery -> blueprint -> draft -> review -> revise -> finalize`

Use when the user wants end-to-end help.

## Checkpoint format

Use this style when helpful:

```md
## Pipeline checkpoint

- Current stage: ...
- Document type: ...
- Current status: ...
- Main gap: ...
- Recommended next step: ...
```

## Revision loop rule

Keep revision loops practical.

Default:
- 1 review round
- 1 main revision round
- optional final polish

Do not create endless loops unless the user explicitly wants multiple rounds.

## Output expectations by stage

### discovery
Output:
- concise brief
- assumptions
- open questions
- recommended doc type

### blueprint
Output:
- outline
- section purpose
- missing input list

### draft
Output:
- usable first draft
- assumptions/open questions section if needed

### review
Output:
- overall judgment
- prioritized issue list
- revision roadmap

### revise
Output:
- revised content or a clear revision plan
- explanation of major changes

### finalize
Output:
- cleaned final draft
- optional one-page summary if useful

## References

Read when relevant:
- `references/doc-stage-matrix.md` — map situation to stage and doc type
- `references/checkpoint-patterns.md` — checkpoint message patterns
- `references/handoff-protocol.md` — how to move between writer and reviewer
