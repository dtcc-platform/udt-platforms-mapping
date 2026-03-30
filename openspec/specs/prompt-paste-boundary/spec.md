### Requirement: Prompt files contain a cut-line separating usage instructions from AI prompt body

Each prompt template file in `prompts/` that contains human-facing usage instructions SHALL include a cut-line that visually and structurally separates those instructions from the AI-facing prompt body. The cut-line SHALL be a Markdown blockquote on its own line in the form:

> Paste into your AI session from this line onwards.

The cut-line SHALL appear immediately before the start of the AI-facing prompt body and after all human-facing usage instructions.

#### Scenario: Researcher identifies where to start copying

- **WHEN** a researcher opens a prompt file in any text editor or Markdown viewer
- **THEN** a prominent blockquote line makes it immediately clear where the AI-facing content begins

#### Scenario: Model receives content starting from the cut-line

- **WHEN** a researcher copies from the cut-line onwards and pastes into a fresh AI session
- **THEN** the model receives only the AI-facing prompt body, with no human workflow steps or usage instructions present

#### Scenario: Model receives the full file including usage instructions

- **WHEN** a researcher accidentally pastes the entire file including the usage header
- **THEN** the cut-line blockquote is present in the pasted content and serves as a visible signal that content above it was not intended for the model

### Requirement: Usage instructions in prompt files reference the cut-line

The human-facing usage instructions in each prompt file SHALL explicitly direct researchers to paste from the cut-line onwards, not from the top of the file. The instruction SHALL appear as a numbered step in the usage block and SHALL name the cut-line by its exact blockquote wording.

#### Scenario: Researcher reads the usage steps before their first session

- **WHEN** a researcher reads the numbered steps at the top of a prompt file
- **THEN** one step says to paste into their AI session starting from the cut-line, so they know not to include the usage instructions themselves
