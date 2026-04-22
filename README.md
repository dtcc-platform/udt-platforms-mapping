# udt-platforms-map

A structured research repository for mapping Urban Digital Twin (UDT) platforms similar or adjacent to DTCC.

## Goal

Produce a comprehensive landscape review of existing UDT platforms — understanding their technical architecture, openness, city-scale capability, maturity, integration posture, and governance — to inform DTCC's technical and strategic direction.

## Research Workflow

```mermaid
flowchart TD
    scope["📋 01-scope.md\nInclusion criteria & seed list"]

    disc["prompts/\nplatform-discovery.md\n― global scope ―"]
    dresp["responses/\nglobal-platforms-discovery.md"]
    select["Select platforms\nfrom summary table"]
    comp["prompts/\nplatform-comparison.md"]
    cresp["responses/\n*-comparison.md"]
    inv["prompts/\nplatform-inventory.md\n― AI CLI only ―"]
    table["docs/\n05-platform-inventory.csv"]
    lic["prompts/\nlicense-analysis.md\noptional"]

    scope -->|"inclusion criteria"| disc
    disc --> dresp
    dresp --> select
    select -->|"copy selected rows"| comp
    comp --> cresp
    cresp -->|"auto-scan"| inv
    dresp -->|"auto-scan"| inv
    inv -->|"append rows"| table
    dresp -.->|"per platform"| lic
```

## Directory Layout

| Directory      | Purpose                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| `docs/`        | Scope, methodology, source policy, license review approach, and the canonical platform inventory             |
| `prompts/`     | Prompt templates for AI-assisted platform discovery, comparison, inventory curation, and license analysis    |
| `responses/`   | Raw AI responses saved for reference and verification                                                        |

## Key Documents

- [`docs/01-scope.md`](docs/01-scope.md) — inclusion and exclusion criteria, seed list
- [`docs/02-methodology.md`](docs/02-methodology.md) — research approach and file naming conventions
- [`docs/03-source-policy.md`](docs/03-source-policy.md) — acceptable sources and citation format
- [`docs/04-license-review.md`](docs/04-license-review.md) — how to evaluate platform licenses
- [`docs/05-platform-inventory.csv`](docs/05-platform-inventory.csv) — canonical platform table
