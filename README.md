# udt-platforms-map

A structured research repository for mapping Urban Digital Twin (UDT) platforms similar or adjacent to DTCC.

## Goal

Produce a comprehensive landscape review of existing UDT platforms — understanding their technical architecture, openness, city-scale capability, maturity, integration posture, and governance — to inform DTCC's technical and strategic direction.

## Directory Layout

| Directory | Purpose |
|-----------|---------|
| `prompts/` | Prompt templates for AI-assisted platform discovery, comparison, and license analysis |
| `search_logs/` | Session logs recording date, model, prompt, response, sources, and notes — one file per platform per session |
| `responses/` | Raw AI responses saved for reference and verification |
| `docs/` | Methodology, source policy, license review approach, and the canonical platform inventory |
| `sources/` | Raw research material — license files, screenshots, exports, downloaded docs |
| `notes/` | Freeform researcher notes, observations, and working drafts |

## Research Workflow

Each platform is researched following this five-step process:

1. **Research** — investigate using primary sources (official sites, repositories, documentation, papers)
2. **Log** — record the session in `search_logs/YYYY-MM-DD-<platform>.md` using the logging template
3. **Write** — add or update the platform profile and analysis in `docs/review.md`
4. **Inventory** — update the platform's row in `docs/platform-inventory.md`
5. **Source** — store raw material (license files, screenshots, exports) in `sources/`

## Key Documents

- [`docs/methodology.md`](docs/methodology.md) — platform inclusion criteria and research approach
- [`docs/source-policy.md`](docs/source-policy.md) — acceptable sources and citation format
- [`docs/license-review.md`](docs/license-review.md) — how to evaluate platform licenses
- [`docs/platform-inventory.md`](docs/platform-inventory.md) — canonical platform table
