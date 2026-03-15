# Feedback Normalization

For each piece of feedback, normalize into:

- source
- priority
- target section
- problem type
- requested action

## Priority buckets

### Must fix
Blocks trust, approval, or implementation.

### Should fix
Improves quality materially, but not a hard blocker.

### Optional
Polish or nice-to-have improvement.

## Problem type buckets

- clarity
- scope
- logic
- structure
- inconsistency
- unsupported claim
- risk gap
- technical gap
- delivery gap

## Example normalization

Raw comment:
“这份 PRD 的验收标准太虚了，而且功能边界不清楚。”

Normalized:
- source: reviewer
- priority: must fix
- target section: requirements / acceptance
- problem type: scope + clarity
- requested action: define feature boundaries and rewrite acceptance criteria
