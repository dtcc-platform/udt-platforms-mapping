## MODIFIED Requirements

### Requirement: Platform discovery prompt file exists

The repository SHALL contain a file at `act/discovery/prompt.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `act/discovery/prompt.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt pastes plan/discovery/scope.md only

The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `plan/discovery/scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `plan/discovery/scope.md` before continuing.

The usage header SHALL direct the researcher to paste `plan/discovery/scope.md` — not any other scope file.

The discovery prompt SHALL NOT embed or reference dimension rubrics (Arch, Open, City, etc.). Those are defined in `plan/rating/scope.md` and belong to the rating phase only.

#### Scenario: Researcher runs the prompt without pasting scope

- **WHEN** a researcher pastes the discovery prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the discovery scope content before producing any output

#### Scenario: Researcher runs the prompt after pasting scope

- **WHEN** a researcher pastes `plan/discovery/scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with the Layer criteria table available and produces a complete discovery response

### Requirement: Discovery prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to paste the prompt into their AI session and save the response to `observe/discovery/<model-name>.md`. File names SHALL NOT include the cycle type prefix.

The usage header SHALL also state that the prompt can be used either in an AI web research chat or in an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `observe/discovery/`.

#### Scenario: Researcher reads the usage header before pasting the prompt

- **WHEN** a researcher reads the usage instructions at the top of `act/discovery/prompt.md`
- **THEN** they see the correct save-as path `observe/discovery/<model-name>.md` and an explicit note that web-chat sessions require manual save into `observe/discovery/`
