# Integrity Matrix

## feasibility-report

Focus on:
- whether recommendation matches analysis
- whether option comparison is real
- whether feasibility dimensions are complete
- whether costs, benefits, and risks are internally consistent

Common integrity failures:
- recommendation not supported by comparison
- risks acknowledged but ignored in conclusion
- economics section uses assumptions that differ from earlier scope

## project-proposal

Focus on:
- whether objectives, scope, outcomes, and budget align
- whether the ask matches the body
- whether implementation path supports expected outcomes

Common integrity failures:
- scope too big for stated resources
- expected outcomes stronger than implementation plan supports
- summary and detailed sections describe different projects

## prd

Focus on:
- whether goals, scenarios, requirements, and acceptance criteria line up
- whether scope and non-scope stay stable
- whether non-functional requirements match the product ambition

Common integrity failures:
- feature list drifts beyond the stated goal
- acceptance criteria do not test the requirement
- requirements refer to undefined actors or systems

## architecture-design

Focus on:
- whether architecture covers the promised scope
- whether modules, interfaces, and data flow align
- whether stated performance/security/reliability claims match the design

Common integrity failures:
- high-level claims not reflected in module design
- deployment assumptions conflict with security or scaling claims
- module names change across sections

## implementation-plan

Focus on:
- milestone dependency order
- resource plan vs scope
- risks vs mitigation
- sequencing realism

Common integrity failures:
- task sequence ignores prerequisites
- milestone timing conflicts with external dependencies
- ownership is unclear where risk is highest
