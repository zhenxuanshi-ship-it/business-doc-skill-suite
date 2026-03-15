# Architecture Design Guide

## Default structure

1. Design goals
2. Scope
3. Design principles
4. High-level architecture
5. Module breakdown
6. Data flow / interaction flow
7. Key technical choices
8. Security, performance, reliability
9. Deployment and evolution path
10. Risks and trade-offs

## What makes a good architecture doc

- explains why this design was chosen
- makes module boundaries clear
- states trade-offs honestly
- identifies dependencies and constraints
- is readable by both engineers and adjacent stakeholders

## Common weak patterns

- only talks about components, not interactions
- names technologies without reasons
- no trade-offs section
- no failure scenarios or risk thinking
- mixes target state and current state without labels

## Review checklist

- are responsibilities of each module clear?
- are interfaces/data flows explicit enough?
- are scalability and security discussed concretely?
- is there a migration/evolution path?
- are major trade-offs documented?
