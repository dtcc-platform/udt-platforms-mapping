# Spec Delta: ar-folder-layout

## Change Type

Modify capability

## Requirements

### Requirement: README explains the isolation rule and calibration-branch model

`README.md` SHALL explain that the credibility of calibration depends on isolated review/proposal context before merge.

It SHALL explain that:

- agents may share the governing spec and generated prompts
- agents do not see other agents' reviews or proposals before merge
- synthesis happens on a dedicated calibration branch rather than directly on `main`
