## Context

Response files saved to `responses/` currently contain no provenance metadata. A researcher opening a file weeks later cannot tell which model produced it, on what date, or from which prompt. This matters because different models have different knowledge cutoffs, reasoning styles, and failure modes — and because the research corpus may eventually need to be re-run or compared across models.

## Goals / Non-Goals

**Goals:**
- Instruct each prompt to begin its response with a standard metadata block covering model name/version, session date, and prompt template used
- Keep the metadata format consistent across all three prompts and portable across Markdown viewers

**Non-Goals:**
- Automatically capturing model metadata outside the prompt (e.g., via API wrappers or logging scripts) — this change is prompt-only
- Validating that the model accurately self-reports its version — that is a known limitation accepted here
- Changing the `search_logs/` format — session logging is a separate concern

## Decisions

### Decision: Place metadata at the top of the response as a fenced code block

The metadata block is placed as the very first element of the response, before any content sections, using a fenced YAML code block:

```yaml
model: <model name and version>
date: <YYYY-MM-DD>
prompt: <prompt template name>
```

**Rationale:** A fenced code block renders identically in all CommonMark-compatible viewers — no special syntax, no risk of being interpreted as content. YAML is human-readable and machine-parseable if needed later. Placing it first means it survives truncation and is immediately visible when opening a file.

**Alternatives considered:**
- Markdown front matter (`---` YAML block) — rejected; not supported by all viewers and some tools strip it
- A Markdown table — rejected; more verbose, harder to parse programmatically
- Inline bold text at the top — rejected; not structured, harder to extract later

### Decision: Include three fields: model, date, prompt

- **model**: identifies the AI system and version for reproducibility assessment
- **date**: allows correlation with model knowledge cutoffs and research timeline
- **prompt**: ties the response to its generating template, so the methodology is traceable

**Rationale:** These three fields answer the essential provenance questions. Additional fields (e.g., temperature, token count) are out of scope for a manual workflow.

### Decision: Instruct the model to self-report its name and version

The prompt instructs the model to fill in its own name and version in the metadata block.

**Rationale:** In a copy-paste manual workflow there is no API layer to inject metadata automatically. Self-reporting is the only viable option. The limitation (models may not always report the exact version) is acceptable and noted in Risks.

## Risks / Trade-offs

- **Model self-reporting inaccuracy** → Some models report generic names (e.g., "ChatGPT" rather than "GPT-4o") or refuse to state their version. Mitigation: the researcher can manually correct the `model` field before saving; the field is a best-effort record, not a guarantee.
- **Metadata duplication with search_logs/** → `search_logs/` already records model and date per session. Mitigation: redundancy is intentional — response files should be self-contained so they remain interpretable if detached from the log.
