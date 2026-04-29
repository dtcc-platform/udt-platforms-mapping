# Proposal: reframe-calibration-as-isolated-spec-review

## Why

The current calibration model assumes a heavy loop:

1. generate prompts from the same governing spec
2. run each prompt in a web interface
3. compare research results
4. reflect on result differences

That process is expensive in both time and attention:

- each agent prompt has to be run in a web interface
- the resulting research outputs are large and noisy
- reflection mixes two different questions:
  - did the agents interpret the spec differently?
  - or did the web runs simply vary in execution and evidence?

For this repository, the primary artifact is the workflow.
That means the first calibration question should be about **spec interpretation**, not downstream research output.

The proposed change shifts calibration earlier in the chain:

- agents generate prompts from the same governing spec
- those prompts are shared as calibration artifacts
- each agent independently reviews whether the other prompts are accurate interpretations of the spec
- if not, each agent creates an isolated OpenSpec change proposal for how the spec should become more specific
- those proposals remain isolated until merge
- only after independent proposals exist do we merge them into a calibration branch and review the merged deltas directly during synthesis

This makes the calibration process:

- cheaper
- faster
- more directly about workflow quality
- more credible, because proposal generation remains independent before merge

## Why The Isolation Rule Matters

The credibility of the new calibration model depends on **isolated context**.

Each agent should see:

- the governing spec
- the generated prompts from all agents

Each agent should **not** see before merge:

- the other agents' change proposals
- any synthesis artifact

That isolation matters because it preserves independent judgment.
Without it, agents can converge socially on each other's interpretations instead of surfacing real ambiguity in the governing spec.

Independent proposals are a stronger signal:

- if several agents propose the same clarification independently, that is evidence the spec is genuinely underspecified there
- if they diverge, the divergence itself shows where the spec boundary is still too loose

## Why `c01`, `c02`, ... Still Matter

The `c01`, `c02`, ... segment is not only a way to separate rounds.
It is a way to preserve calibration history against accepted spec baselines.

That matters because the new process calibrates prompt interpretation directly.
Keeping the cycle segment makes it possible to compare, for each agent:

- how its generated prompt changed from one accepted baseline to the next
- how the common ambiguities shifted between calibration rounds
- whether spec tightening actually reduced interpretive drift over time

Without the `c01`, `c02`, ... structure, later prompt-generation rounds would be harder to compare and calibration history would lose one of its main values: showing how interpretation evolves across accepted workflow iterations.

## Proposed Calibration Flow

1. Start from an accepted spec state on `main`.
2. Generate prompts from that same spec for each agent.
3. Save those prompts under `calibration/<spec-name>/c01/<agent>/prompt.md`.
4. Only after all prompts are available, create one branch per agent.
5. On each agent branch, let the agent inspect the shared prompts and create one isolated OpenSpec change proposal.
6. Keep those proposals isolated from the other agents until merge.
7. Merge the agent branches into a dedicated calibration branch.
8. Review the merged OpenSpec proposals directly and decide what to keep while preparing the accepted follow-up change.
9. Implement the accepted follow-up change.
10. Merge accepted contract updates back to `main`.

## Impact

- calibration becomes primarily about prompt interpretation fidelity
- result-based calibration becomes optional and selective instead of the default path
- `calibration/` stores shared prompt artifacts, while the actual candidate changes are captured as isolated OpenSpec proposals
- the README can link to this proposal as the detailed rationale for the new process
