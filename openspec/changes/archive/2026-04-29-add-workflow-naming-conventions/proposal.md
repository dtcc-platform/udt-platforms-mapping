# Proposal: add-workflow-naming-conventions

## Why

Naming in this repository now carries workflow meaning.

It affects how users and agents interpret:

- branch purpose
- commit intent
- OpenSpec change scope
- calibration cycle history
- calibration artifact identity

Those conventions currently live mostly in README guidance and in scattered examples across specs. That is too weak for a repo where naming is part of traceability and calibration credibility.

The repository needs one cross-cutting naming capability that governs naming formats without taking over structural path semantics owned by structural specs.

## What Changes

- add a standalone `workflow-naming-conventions` capability
- govern repo-wide naming formats such as:
  - branch names
  - commit message patterns
  - OpenSpec change names
  - calibration cycle tokens like `c01`
  - calibration naming segments like `<spec-name>` and `<agent>`
- keep path structure semantics in `repository-structure` and `calibration-archive`

## Impact

- improves consistency across humans and agents
- makes traceability rules inspectable as a governed contract
- reduces reliance on README-only naming guidance
