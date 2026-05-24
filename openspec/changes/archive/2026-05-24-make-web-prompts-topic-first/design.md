## Context

The resolved prompt starts with `# Prompt`, then role and task text. That is readable to humans, but ChatGPT Deep Research appears to look for a specific research query or topic before starting.

The prompt should therefore start with a plain text topic line that cannot be mistaken for metadata, a heading, or a generic instruction block.

When the resolved prompt is uploaded as a file, the web runner may still treat the chat message itself as the query and ignore the attachment until instructed. The workflow therefore also needs a short launcher message for attachment-based tools.

## Goals / Non-Goals

**Goals:**

- Make resolved web prompts recognizable as a Deep Research query.
- Make attachment-based web research runs explicitly use the attached resolved prompt file.
- Keep provenance metadata and inlined contracts after the topic and task instructions.
- Preserve the governed output contract and reviewability.

**Non-Goals:**

- Remove inlined contracts.
- Change research output structure.
- Add a separate Deep Research-only artifact.

## Decisions

- Use the literal prefix `Research topic:` as the first line of saved resolved web prompts. This is clearer to target runners than a Markdown heading.
- Follow the topic line with concise task instructions, then metadata and contracts.
- Keep the entity discovery topic concrete: "Urban Digital Twin entity ecosystem, including platforms, frameworks, modules, initiatives, and excluded boundary candidates."
- Update the reviewer checklist so this class of issue is caught before execution.
- Provide a standard launcher message for attachment-based web research tools: "The attached file contains the complete research prompt. Read the file content as the query and execute it exactly. Do not ask me for another topic unless the file cannot be read."

## Risks / Trade-offs

- A topic-first line is less Markdown-structured than a heading. Mitigation: it is intentionally optimized for web research runner recognition.
- Other web tools may not need this. Mitigation: a concrete first-line topic is still harmless and improves clarity.
- Attachment launch guidance adds one extra operational step. Mitigation: keep the launcher message short and standard.
