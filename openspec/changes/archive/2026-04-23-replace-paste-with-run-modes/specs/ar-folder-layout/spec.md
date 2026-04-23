## MODIFIED Requirements

### Requirement: observe/ holds raw model responses per cycle

`observe/discovery/` SHALL contain raw discovery response files from AI models. `observe/rating/` SHALL contain raw rating response files. Response files sit directly in the cycle folder with no `responses/` subfolder. File names SHALL NOT include the cycle type — the folder provides that context.

File names SHALL be prefixed with either `cli-` or `web-` indicating the interface that produced the response, followed by a short model identifier (for example, `web-claude.md`, `cli-claude-code.md`). The prefix is the single authority on which interface produced the response; the YAML metadata block inside the file SHALL NOT carry a separate `interface` field.

#### Scenario: Researcher saves a discovery response produced in a web chat

- **WHEN** a researcher saves a model's discovery response produced in a web chat
- **THEN** it goes to `observe/discovery/web-<model-short>.md` — with the `web-` prefix identifying the interface

#### Scenario: AI saves a discovery response produced in CLI mode

- **WHEN** an AI CLI runs `act/discovery/prompt.md` in CLI mode and produces a response
- **THEN** the AI saves it to `observe/discovery/cli-<model-short>.md`

#### Scenario: Researcher scans the observe/ folder by interface

- **WHEN** a researcher lists `observe/discovery/`
- **THEN** they can tell at a glance which files came from CLI sessions and which came from web chats, without opening them
