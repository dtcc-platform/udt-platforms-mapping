# Spec Delta: prompt-run-modes

## Change Type

Retire capability

## Rationale

The repository no longer wants a governed prompt capability for choosing between CLI and Web execution.
That behavior adds interface complexity without improving the research contract.

## Retirement

The baseline capability `prompt-run-modes` SHALL be retired.

Act prompts SHALL no longer be required to:

- ask `Run as CLI or Web?`
- support two execution branches
- save outputs with `cli-` or `web-` filename prefixes
