# Workflow Presentation Generator

Use this prompt to generate or refresh the workflow tutorial deck for this repository.

**Requires:** An AI CLI with filesystem access.
This prompt is CLI-only. Do not use it in a web chat session.

Run it by telling your AI CLI:

```text
Run workflow/presentation/prompt.md
```

Save the generated deck to `workflow/presentation/deck.md`.

---

## Prompt

You are generating a short tutorial presentation that explains the current workflow of this repository.

Your task is to read the current live repository sources listed below, infer the current workflow from them, and write a Pandoc-ready Markdown slide deck to `workflow/presentation/deck.md`.

Do not describe archived or retired workflows as if they are current.
Prefer current live baseline specs and current file structure over older wording in archived changes.

### Required context to read before writing

Read these files first:

- `README.md`
- `openspec/specs/ar-folder-layout/spec.md`
- `openspec/specs/prompt-run-modes/spec.md`
- `openspec/specs/workflow-prompts-status/spec.md`

Use the current live repository structure as supporting context, including:

- `plan/`
- `act/`
- `observe/`
- `reflect/`
- `workflow/`

Inspect the current live prompt and workflow artifacts as needed for accuracy.

### Goal of the deck

Produce a short tutorial deck for new or returning contributors.

The deck must explain:

- why this repository does not use one large prompt
- why `discovery` and `rating` are separate
- what `plan/`, `act/`, `observe/`, and `reflect/` do
- how OpenSpec governs workflow and prompt changes
- what lives under `workflow/`
- where the human researcher stays in the loop

### Deck constraints

- The deck must be short.
- The deck must be tutorial-oriented, not exhaustive.
- The deck must be a single Markdown presentation source.
- Use top-level slide headings so the file is ready for Pandoc-style slide conversion.
- Keep slides readable as slides: short paragraphs or short bullet lists only.
- Do not include speaker notes, HTML, or tool-specific slide directives.
- Do not mention archived change names, commit hashes, or historical spec names unless absolutely necessary.

### Output format

Write the output to `workflow/presentation/deck.md`.

The file must be valid Markdown.

Use this structure:

```md
# <Slide Title>

<slide content>

# <Slide Title>

<slide content>
```

Recommended slide arc:

1. Repository title and purpose
2. Why not one prompt
3. Discovery vs rating
4. The four-phase cycle
5. How artifacts flow through the repo
6. OpenSpec and governed change
7. Human-in-the-loop and shared knowledge
8. Practical how-to-use summary

### Output behavior

- Overwrite `workflow/presentation/deck.md` if it exists.
- After writing, give a brief confirmation with the saved path and the number of slides generated.
