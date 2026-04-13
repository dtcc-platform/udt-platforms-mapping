## Context

The other prompts in this project (`platform-discovery.md`, `platform-comparison.md`) are designed to be pasted into any AI chat session. They work because they are self-contained: the user provides all necessary data inline via placeholders.

The inventory prompt is different — it needs to *read* files from `responses/` rather than receive data from the user. This creates a fundamental design constraint: the prompt requires an AI session with filesystem access (Claude Code or equivalent tool-enabled session), not a generic chat window.

The `responses/` directory currently contains comparison responses from multiple models (Claude, Gemini, ChatGPT), each with a YAML metadata block identifying the model, date, and prompt type. These are the source of truth for the inventory table.

## Goals / Non-Goals

**Goals:**
- Produce a GFM table of inventory rows ready to paste into `docs/05-platform-inventory.md`
- Extract all platform rows from all comparison response files automatically
- Attach model and date provenance to every row
- Require zero user input beyond pasting the prompt

**Non-Goals:**
- Cross-referencing discovery responses for additional metadata (Org, License, Type) — out of scope per design decision (Option A)
- Deduplicating rows for the same platform — multiple rows per platform are intentional
- Sorting or ranking output rows — insertion order is sufficient
- Validating or correcting scores from source files

## Decisions

### Filesystem access is required — prompt targets AI CLI tools, not web chat

**Decision:** The prompt is designed for AI CLI tools with filesystem access (Claude Code, Codex CLI, Gemini CLI), not generic web chat sessions.

**Rationale:** Auto-scanning `responses/` is the core value of this prompt. A fallback that asks the user to paste file contents would reduce it to a reformatting task with manual effort comparable to the current workflow. Accepting the CLI constraint keeps the prompt simple and honest about its requirements.

**Alternative considered:** Add a placeholder where the user pastes all comparison file contents. Rejected — files are large and multiple, making this impractical. It also defeats the purpose of "auto-scan".

**How to signal this:** The prompt usage header explicitly states it requires an AI CLI with file access (Claude Code, Codex CLI, Gemini CLI) and cannot be used in a web chat session.

### Output is data rows only, no header row

**Decision:** The model outputs only data rows, not the table header.

**Rationale:** `docs/05-platform-inventory.md` already has the correct header. Outputting rows-only lets the researcher paste directly below it without risk of duplicating or misaligning the header.

**Alternative considered:** Output the full table including header. Rejected — the researcher would need to replace the existing header, introducing an error surface.

### No structural wrapper around output

**Decision:** The model outputs the GFM table rows as the entire response body, with a brief preamble noting which files were processed and how many rows were extracted.

**Rationale:** Keeps the output paste-ready. A brief preamble (not a table row) gives the researcher confidence the scan ran correctly before they paste.

### Files are identified by YAML `prompt` field, not filename

**Decision:** Qualifying files are identified by `prompt: platform-comparison` in their YAML metadata block, not by filename pattern.

**Rationale:** Filename conventions can drift (e.g., `global-platforms-comparison-claude.md` uses a scope descriptor prefix rather than a platform name). The YAML field is authoritative and was specifically designed for this purpose.

## Risks / Trade-offs

- **CLI dependency** — researchers who prefer to run prompts in a web chat session cannot use this prompt as-is. Mitigation: document the CLI requirement clearly in the usage header, and list the supported tools (Claude Code, Codex CLI, Gemini CLI).
- **YAML parsing reliability** — the model must correctly parse fenced YAML blocks. Mitigation: the spec requires that files without a YAML block are skipped silently, so malformed files degrade gracefully.
- **Part 1 table format drift** — if the comparison prompt's Part 1 table schema changes in future, the inventory prompt's column-reordering instruction may produce misaligned output. Mitigation: the spec requires the model to reorder columns to match the inventory schema, which isolates it from source format changes.

## Open Questions

_(none — design is fully resolved)_
