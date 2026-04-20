## MODIFIED Requirements

### Requirement: Platform discovery prompt file exists

The repository SHALL contain a file at `prompts/platform-discovery.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `prompts/platform-discovery.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt pastes docs/01-discovery-scope.md only

The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-discovery-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-discovery-scope.md` before continuing.

The usage header SHALL direct the researcher to paste `docs/01-discovery-scope.md` — not `docs/01-scope.md` or `docs/01-comparison-scope.md`.

The discovery prompt SHALL NOT embed or reference dimension rubrics (Arch, Open, City, etc.). Those are defined in `docs/01-comparison-scope.md` and belong to the comparison phase only.

#### Scenario: Researcher runs the prompt without pasting scope

- **WHEN** a researcher pastes the discovery prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the discovery scope content before producing any output

#### Scenario: Researcher runs the prompt after pasting scope

- **WHEN** a researcher pastes `docs/01-discovery-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with the Layer criteria table available and produces a complete discovery response

### Requirement: Discovery prompt requests Layer classification output only

The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing identification fields and a Layer assignment. No dimension scoring is required or expected.

**For in-scope platforms** (`core-platform`, `backbone`, `domain-module`): identification fields only — Organization, Link, License, Type, Layer.

**For excluded platforms** (`excluded`): identification fields plus a single **Reason** field — one sentence explaining why the platform is outside the study boundary.

The `Layer` field SHALL contain exactly one of: `core-platform`, `backbone`, `domain-module`, or `excluded`, assigned using the criteria table from the pasted scope content.

The prompt template SHALL include a concrete example section demonstrating the exact field labels and Layer field placement for both in-scope and excluded platforms.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections.

#### Scenario: Response is used to select platforms for comparison

- **WHEN** an AI responds to the discovery prompt
- **THEN** each in-scope platform section contains Organization, Link, License, Type, and Layer — enough to select platforms for a comparison session

#### Scenario: Discovery session finds an excluded platform

- **WHEN** the model encounters a platform that does not meet any in-scope criteria
- **THEN** the platform appears in the summary table with `Layer=excluded` and a one-sentence Reason in its per-platform section; no dimension scores appear

#### Scenario: Discovery session finds a domain-module platform

- **WHEN** an AI responds to the discovery prompt
- **THEN** domain-specific analytics or simulation tools appear with `Layer=domain-module`, not filtered out for not being full platforms

### Requirement: Discovery prompt summary table contains Layer and Reason columns

The summary table SHALL be output immediately after the metadata block and before per-platform sections. The table SHALL use exactly these columns: **Name**, **Link**, **Layer**, **Reason**.

The `Reason` column SHALL be blank for in-scope platforms and contain a brief phrase (not a full sentence) for excluded platforms.

All discovered platforms SHALL appear in the summary table regardless of Layer value. The table SHALL be ordered: `core-platform` first, then `backbone`, then `domain-module`, then `excluded`.

#### Scenario: Researcher scans the summary table to select platforms for comparison

- **WHEN** a researcher opens a discovery response
- **THEN** the summary table shows Name, Link, Layer, and Reason for every discovered platform, allowing quick selection of in-scope platforms for pasting into the comparison prompt

#### Scenario: Researcher copies rows for comparison

- **WHEN** a researcher selects in-scope platforms from the summary table
- **THEN** they can exclude `excluded` rows by filtering on the Layer column

### Requirement: Discovery prompt includes DTCC as a required research entry

The prompt template SHALL instruct the model to include DTCC (Digital Twin Cities Centre) as a required research target in every discovery session. DTCC SHALL be researched from primary sources (dtcc.chalmers.se, official GitHub repository) and SHALL appear with a full identification block and a `Layer` assignment.

#### Scenario: Researcher runs a discovery session

- **WHEN** an AI responds to the discovery prompt
- **THEN** a DTCC per-platform section appears with identification fields and Layer assignment regardless of what other platforms were discovered

#### Scenario: Researcher prepares rows for comparison

- **WHEN** a researcher selects rows from the discovery summary table to paste into the comparison prompt
- **THEN** the DTCC row is available in the summary table and can be selected alongside other platforms

### Requirement: Discovery prompt may be run in deep research mode for reassessment

The prompt template SHALL note that the discovery prompt can be run in a deep research interface when a more thorough Layer classification is needed — for example, to reassess a specific platform's layer assignment with primary-source evidence. Running the discovery prompt in deep research mode is the standard mechanism for layer reassessment; no separate reassessment prompt is needed.

#### Scenario: Researcher reassesses a platform layer

- **WHEN** a researcher wants to verify or update the Layer assignment for a specific platform
- **THEN** they run the discovery prompt in deep research mode, targeting that platform, and update the inventory with the result

### Requirement: Discovery prompt enforces agent-agnostic output structure

The prompt template SHALL comply with the shared Markdown contract defined in `prompt-markdown-format` and SHALL specify these discovery-specific constraints:

- Platform heading level: `##` for every platform section
- Citation override: inline Markdown links `[Description](url)` override the model's default citation format
- Research-mode suppression: return only the final deliverable with no exposed research plan, executive summary, or provider-specific wrapper

#### Scenario: Two agents respond to the same discovery prompt

- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and Layer values with no agent-specific formatting artifacts

### Requirement: Discovery prompt output begins with a model metadata block

The prompt template SHALL instruct the model to begin its response with a fenced YAML code block containing: `model`, `date` (YYYY-MM-DD), and `prompt: platform-discovery`.

#### Scenario: Response is saved as a file and opened later

- **WHEN** a researcher opens a saved discovery response file
- **THEN** the first visible element is the metadata block identifying the model, date, and prompt template

## REMOVED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
**Reason**: Discovery no longer produces dimension scores. Output is now Layer classification only (Organization, Link, License, Type, Layer, Reason). The inventory CSV is comparison-only.
**Migration**: Use the new "Discovery prompt requests Layer classification output only" requirement.

### Requirement: Discovery prompt response begins with a required summary table
**Reason**: The summary table columns change — Relevance and all 12 dimension columns are removed. Replaced by the new "Discovery prompt summary table contains Layer and Reason columns" requirement.
**Migration**: New summary table: Name | Link | Layer | Reason.

### Requirement: Discovery prompt includes a [PASTE_SCOPE_HERE] guard
**Reason**: The scope file reference changes from `docs/01-scope.md` to `docs/01-discovery-scope.md`. Replaced by "Discovery prompt pastes docs/01-discovery-scope.md only".
**Migration**: Update paste instructions to reference `docs/01-discovery-scope.md`.

### Requirement: Discovery prompt does not request deep research
**Reason**: Deep research mode is now explicitly allowed for reassessment passes. Replaced by "Discovery prompt may be run in deep research mode for reassessment".
**Migration**: Remove the prohibition; add the reassessment note.

### Requirement: Discovery prompt instructs multi-layer ecosystem search
**Reason**: Multi-layer search is now implicit in the Layer criteria table — the four rows cover all ecosystem layers including excluded. No separate instruction needed.
**Migration**: The criteria table in `docs/01-discovery-scope.md` replaces this requirement.
