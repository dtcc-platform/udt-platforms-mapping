## Context

The repository currently defines platform discovery and initiative discovery with separate behavior specs. Those specs repeat boundary language: technical artifacts belong in platform discovery, projects and deployments belong in initiative discovery, and unclear substrate should preserve uncertainty.

The maintenance problem is that boundary changes must be made in more than one place and discovery has to be split across platform and initiative runs. The desired shape is one canonical definition for UDT entities and one discovery prompt that uses it.

## Goals / Non-Goals

**Goals:**

- Establish `entity-definition` as the single canonical behavior contract for platform artifacts, initiatives, and exclusions.
- Establish `act/discover-entities.md` as the single canonical discovery prompt.
- Establish `observe/entity-discovery-<model-short>.md` as the single saved discovery response pattern.
- Preserve the existing distinction between technical artifacts and real-world initiatives.
- Keep the discovery summary table compact with only `Name`, `Type`, and `Link`, with `Link` as the last column.
- Put `Uses`, exclusion reasons, and uncertainty details in per-entity paragraphs or sections.
- Keep prompt bodies lightweight by moving classification and boundary rules into the unified spec.

**Non-Goals:**

- Do not remove the canonical `platforms` and `initiatives` research objects from the repository.
- Do not rewrite existing observed outputs as part of proposal creation.
- Do not change platform comparison scoring in this change.

## Decisions

- Use `entity-definition` as the merged spec name.
  - Rationale: repository naming conventions avoid a redundant `udt-` prefix, and the spec covers more than platforms.
  - Alternative considered: `udt-entity-definition`. That is more explicit outside this repo but conflicts with the existing naming direction.

- Model `initiative` as both an entity kind and a platform discovery `Type` value.
  - Rationale: the user wants a fifth category while merging discovery. A unified search can discover a project or programme that has no separable technical artifact; representing it as `Type = initiative` is clearer than forcing it into `excluded`.
  - Alternative considered: only use `EntityKind = initiative` and remove Type-level initiative rows. That is cleaner semantically but would not satisfy the fifth-category workflow.

- Keep `EntityKind` and `Type` distinct in the definition, but expose only `Type` in the summary table.
  - Rationale: `platform`, `framework`, and `module` describe technical artifact role, while `initiative` describes entity kind. The merged definition must make that distinction visible to avoid future confusion.
  - Alternative considered: make all categories a single flat enum. That is simpler, but it hides cases where an initiative uses a platform artifact.

- Retire separate platform and initiative discovery prompt/output contracts after implementation.
  - Rationale: one discovery prompt and one output shape is easier to maintain and review.
  - Alternative considered: keep two prompts that share `entity-definition`. That reduces duplicated definitions but still leaves duplicated discovery prompt and output maintenance.

- Use `Name`, `Type`, and `Link` as the only summary table columns, in that order.
  - Rationale: the table should stay scannable, with classification visible before the URL, while `Uses`, exclusion reasons, and uncertainty are better expressed in prose where they can be nuanced.
  - Alternative considered: include `Uses` and `Reason` columns. That is more structured but makes the table wider and duplicates details that belong in entity paragraphs.

## Risks / Trade-offs

- `Type = initiative` mixes technical-role and entity-kind categories -> Mitigate by documenting `EntityKind` separately in `entity-definition`.
- Existing platform discovery coverage counts may need interpretation updates -> Keep coverage targets focused on technical artifact recall unless explicitly changed later.
- Older observed outputs will not contain `initiative` rows -> Treat this as a forward contract change and avoid rewriting historical observations.
- Prompt consumers may expect separate discovery prompts -> Update prompt specs, output specs, and repository structure guidance in the same change.

## Migration Plan

1. Add `openspec/specs/entity-definition/spec.md`.
2. Add `openspec/specs/act-discover-entities-prompt/spec.md`.
3. Add `openspec/specs/observe-entity-discovery/spec.md`.
4. Add `act/discover-entities.md` and update repository guidance to make it canonical.
5. Retire separate platform and initiative discovery prompts, output contracts, and definition specs after active consumers move.
