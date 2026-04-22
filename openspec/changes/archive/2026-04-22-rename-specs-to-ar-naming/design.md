## Context

After the AR folder restructure, spec names like `platform-discovery-prompt` no longer mirror the file they govern (`act/discovery/prompt.md`). The naming convention should be: join the path segments of the governed file with hyphens, drop the extension. Cross-cutting specs that govern a concept rather than a single file are exempt.

## Goals / Non-Goals

**Goals:**
- Spec folder names match `phase-cycle-subfolder` of the file they govern
- Two stale specs (`platform-comparison-prompt`, `platform-comparison-scope-file`) also get their internal path references fixed

**Non-Goals:**
- Changing spec content beyond stale path fixes
- Renaming cross-cutting specs (`ar-folder-layout`, `fixture-alias-column`, `prompt-markdown-format`, `prompt-paste-boundary`, `prompt-placeholder-guard`, `relevance-score`, `platform-discovery-scope`)

## Decisions

### Rename via git mv

Use `git mv openspec/specs/<old> openspec/specs/<new>` to preserve history.

### Cross-cutting specs are exempt

Specs that govern a concept across multiple files (markdown format, paste boundary, alias column rules) don't map to a single AR path. Forcing `phase-cycle-subfolder` naming on them would be misleading. They stay as-is.

### `platform-discovery-scope` stays

This spec appears to be a legacy/superseded version. It is left untouched — renaming it risks confusion. The active scope spec is `platform-discovery-scope-file` → renamed to `plan-discovery-scope`.

## Risks / Trade-offs

- **Rename breaks any hardcoded spec name references** — e.g. if a change's delta spec folder name refers to the old main spec name. Mitigation: grep for references before deleting old folders.
