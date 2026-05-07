# Design: README manifest workflow explanation

## Root README

The root README should introduce the repository as a spec-first research workspace where expected model behavior is separated from prompt wording.

The intro should define four layers:

- specs: expected behavior and output contracts
- plan inputs: run-specific inputs
- act manifests: contract manifests that assemble specs and inputs
- resolved prompts: concrete model-facing instructions produced from manifests

The README should explicitly say that `act/*.md` files are not pasted directly into web models. They are resolved first.

## Diagrams

Use two diagrams because they answer different reader questions.

The research run flow explains how to use the repo:

```text
Specs + Plan Inputs -> Act Manifest -> Resolved Prompt -> Observe Output -> Reflect
```

The interpretation loop explains why manifests are useful:

```text
Same Manifest -> Codex / Claude / Gemini -> Compare interpretations -> Clarify specs with OpenSpec
```

## Act README

`act/README.md` should describe `act/` files as manifests for governed research, benchmarking, and reporting actions. It should point readers to `repo-act-prompt-manifest`.

## README Spec

`repo-readme` should stop requiring the old statement that `act/` prompts operationally implement contracts. It should require the README to explain manifests, resolved prompts, and multi-agent interpretation checks.
