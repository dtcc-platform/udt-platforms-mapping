# Design

## Overview

Keep the contract split intact:

- `plan-udt-platforms-scope` defines the Type classification contract.
- `act-udt-platforms-prompt` defines how `act/udt-platforms.md` uses that contract.

The change only updates the prompt spec. If implementation is needed, the prompt text should use direct wording such as "Use `plan/udt-platforms-scope.md` as the authoritative Type classification contract."

## Decision

Do not duplicate the full Type table in the prompt spec. The prompt spec should reference the scope file as authoritative so the classification rules remain governed in one place.
