## ADDED Requirements

### Requirement: UDT platforms prompt applies the scope classification contract

The prompt SHALL instruct the model to use `plan/udt-platforms-scope.md` as the authoritative classification contract for assigning each artifact's `Type`.

The prompt SHALL instruct the model to apply the scope file's criteria before assigning `platform`, `framework`, `module`, or `excluded`.

#### Scenario: Model classifies discovered artifacts

- **WHEN** the model evaluates a discovered technical artifact
- **THEN** it uses `plan/udt-platforms-scope.md` as the source of truth for Type classification
- **THEN** it applies the scope criteria before assigning `platform`, `framework`, `module`, or `excluded`
