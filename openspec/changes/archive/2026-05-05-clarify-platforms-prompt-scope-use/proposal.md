# Clarify Platforms Prompt Scope Use

## Why

`act-udt-platforms-prompt` currently requires `act/udt-platforms.md` to include and resolve `plan/udt-platforms-scope.md`, but it does not explicitly state how the model must use that scope input. The intended behavior is that the scope file is the authoritative classification contract for assigning `Type`.

Making that explicit closes a contract gap without moving the Type definitions out of the scope spec.

## What Changes

- Add a requirement to `act-udt-platforms-prompt` that the prompt applies `plan/udt-platforms-scope.md` as the authoritative Type-classification contract.
- Clarify that the prompt must instruct the model to apply the scope file's criteria before assigning `platform`, `framework`, `module`, or `excluded`.

## Impact

- The scope spec remains responsible for defining the classification criteria.
- The prompt spec becomes responsible for requiring the prompt to operationalize those criteria.
