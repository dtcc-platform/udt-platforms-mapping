## REMOVED Requirements

### Requirement: Discovery prompt uses a parameterized search scope token

**Reason:** The placeholder's fallback already defaulted to a global scope, making manual replacement redundant. Hardcoding the global scope removes a required user action with no loss of functionality.

**Migration:** Researchers who previously used `[SEARCH_SCOPE]` to target a specific region or technology focus should now run the prompt as-is (global scope) and filter results manually, or create a separate scoped prompt file if a narrower scope is needed.

## MODIFIED Requirements

### Requirement: Discovery prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to paste the prompt into their AI session and save the response as `responses/global-platforms-discovery.md`. The reference to `docs/methodology.md` SHALL be updated to `docs/02-methodology.md`. The step to replace `[SEARCH_SCOPE]` SHALL be removed.

#### Scenario: Researcher reads the usage header before pasting the prompt

- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see two numbered steps (paste, save) with no placeholder replacement step, and the correct save-as filename `responses/global-platforms-discovery.md`
