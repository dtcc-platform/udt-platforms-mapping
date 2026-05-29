## Context

`docs/` currently contains static publication output generated with Pandoc, including a simple index page and an entity discovery page. Research outputs live in `observe/`, while synthesized artifacts live in `reflect/`. There is no repeatable command that publishes those Markdown artifacts into browsable HTML or updates the public home page.

## Goals / Non-Goals

**Goals:**

- Provide one repository-local script for publishing direct Markdown files from `observe/` and `reflect/` into matching publication folders under `docs/`.
- Generate `docs/index.html` as a home page with separate `Observations` and `Reflections` link groups.
- Preserve `observe/` and `reflect/` as the canonical source locations for research artifacts.
- Keep publication output static and usable from GitHub Pages or direct file browsing.

**Non-Goals:**

- Publish nested files below `observe/` or `reflect/`.
- Change research artifact naming rules beyond the publication mapping.
- Add a site generator beyond Pandoc and shell scripting.
- Validate the research quality of published artifacts.

## Decisions

- Use `scripts/publish.sh` as the command location. This keeps operational automation outside the research phase folders while making it easy to discover from the repository root.
- Generate one HTML file per direct Markdown source file using the source basename under the matching category folder, such as `observe/platform-discovery-chatgpt.md` to `docs/observations/platform-discovery-chatgpt.html`.
- Generate `docs/index.md` during publication and then run Pandoc to produce `docs/index.html`. Keeping the Markdown intermediate makes the home page easy to inspect and review.
- Use `docs/assets/site.css` for all generated HTML so existing public styling remains shared.
- Exclude phase-local `README.md` files from publication lists because they document repository structure rather than research artifacts.

## Risks / Trade-offs

- Generated `docs/*.html` can become stale if contributors edit `observe/` or `reflect/` without running the script. Mitigation: document and verify the publish command.
- Pandoc availability is an environment dependency. Mitigation: the script checks for `pandoc` and exits with a clear error.
