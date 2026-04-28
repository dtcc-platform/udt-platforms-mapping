# Spec: udt-platforms-cycle

## Purpose

Governs the `udt-platforms` thread and its technical-artifact output contract.

## Requirements

### Requirement: UDT platforms thread maps technical artifacts through broad discovery

The `udt-platforms` thread SHALL classify technical artifacts only.
Its summary table SHALL use `Name`, `Link`, `Type`, and `Reason`.
`Type` SHALL be one of `platform`, `framework`, `module`, or `excluded`.
The thread SHALL be framed as broad global discovery that prioritizes recall and stable classification over strict source-policy filtering.

### Requirement: UDT platforms thread owns the scope-table contract

The repository SHALL contain a file at `plan/udt-platforms/scope.md`.

That file SHALL contain exactly one classification table with these columns:

- `Type`
- `Definition`
- `Observable Criteria`

The rows SHALL be:

- `platform`
- `framework`
- `module`
- `excluded`

The file SHALL explain that initiatives and projects are tracked separately in `udt-initiatives`.
