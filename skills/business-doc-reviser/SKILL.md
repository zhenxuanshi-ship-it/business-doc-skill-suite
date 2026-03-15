---
name: business-doc-reviser
description: Revise business and product documents based on review findings, integrity reports, stakeholder comments, or revision roadmaps. Use when the user wants to modify a 项目可行性研究报告, 项目建议书, PRD, 产品需求说明书, 架构设计, 技术方案, 实施方案, or executive summary after feedback. Triggers on requests like: 按意见修改, 根据评审意见修订, 根据 integrity 报告修, 帮我改这份 PRD, 更新这份架构方案, 按 roadmap 重写, revise this proposal, update this draft based on comments.
---

# Business Doc Reviser

Revise an existing business document using concrete feedback.

This skill sits after:
- `business-doc-reviewer`
- `business-doc-integrity`
- stakeholder feedback
- leadership comments

## Core rule

Do not rewrite blindly.

First classify feedback into:
1. must fix,
2. should fix,
3. optional improvements,
4. rejected / deferred suggestions.

Then revise deliberately.

## Main modes

### 1. full-revision
Use when the user wants a revised document, not just advice.

Output:
- revised version
- summary of major changes
- unresolved items if any

### 2. roadmap-only
Use when the user first wants a revision plan.

Output:
- prioritized revision roadmap
- suggested execution order
- dependencies between fixes

### 3. section-rewrite
Use when only one section needs rewriting.

Examples:
- rewrite the risk section
- fix the recommendation section
- tighten scope and assumptions only

### 4. response-pack
Use when the user needs a structured response to comments.

Output:
- comment-by-comment response
- disposition: accepted / partially accepted / deferred / rejected
- revision mapping

## Inputs this skill can consume

- review report
- integrity report
- raw stakeholder comments
- leadership comments
- inline bullets from user
- a revision roadmap from previous stages

## Workflow

### Step 1: normalize feedback

Convert mixed feedback into a standard issue list.

For each item, identify:
- source
- severity / priority
- target section
- problem type
- required action

Problem types:
- clarity
- scope
- logic
- structure
- inconsistency
- unsupported claim
- risk gap
- technical gap
- delivery gap

### Step 2: choose revision strategy

Typical strategies:

- **surgical**
  - small edits, wording changes, local clarification

- **sectional**
  - rewrite one or two sections while keeping the rest stable

- **structural**
  - reorder sections, split mixed content, tighten scope, rewrite major argument flow

Default to the least disruptive strategy that actually solves the problem.

### Step 3: preserve what already works

Do not flatten the document into a full rewrite unless necessary.

Keep:
- stable structure
- correct details
- useful wording
- business context that remains valid

### Step 4: surface unresolved items honestly

If some feedback cannot be fully applied because information is missing, say so explicitly.

Use a short unresolved-items section when needed.

## Revision priorities

### Must fix now
Examples:
- contradictions
- unsupported recommendation
- scope confusion
- missing acceptance criteria
- architecture mismatch with stated goals

### Should fix next
Examples:
- weak structure
- vague sections
- incomplete risk treatment
- unclear owner/milestone mapping

### Optional improvements
Examples:
- tone cleanup
- formatting cleanup
- redundancy reduction

## Output format

### For full-revision
Provide:
1. revised text or revised sections
2. major changes summary
3. unresolved items

### For roadmap-only
Provide:
1. Fix now
2. Fix next
3. Optional improvements
4. Suggested revision order

### For response-pack
Provide a table with:
- comment
- disposition
- action taken
- location in revised document

## Good revision behavior

Good:
- directly address the real problem
- keep changes traceable
- avoid unnecessary rewriting
- make the document more decision-ready

Bad:
- rewriting everything because one section was weak
- accepting every comment without judgment
- hiding unresolved conflicts

## References

Read when relevant:
- `references/revision-strategies.md` — choose surgical vs sectional vs structural revision
- `references/feedback-normalization.md` — turn mixed comments into a standard issue list
- `references/response-patterns.md` — comment-by-comment response patterns
