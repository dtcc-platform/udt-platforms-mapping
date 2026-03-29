# Research Methodology

## Inclusion Criteria

A platform is included in this review if it satisfies at least one of the following three criteria:

### 1. Explicit Urban Digital Twin

The platform explicitly presents itself as an urban or city-scale digital twin.
This includes platforms that use the term "digital twin" in their official documentation, product descriptions, or marketing, and are scoped to urban environments (cities, districts, or built infrastructure at city scale).

### 2. City-Scale Capabilities

The platform provides capabilities commonly used to build or operate urban digital twins, even if it does not use the term.
This includes platforms for city-scale 3D visualization, urban simulation, large-scale geospatial data management, or multi-domain urban analytics (buildings, transport, energy, climate).

### 3. Adjacent Architecture or Governance

The platform is a foundational building block commonly integrated into UDT systems — for example, open standards implementations (CityGML, IFC, OGC standards), enabling visualization engines (Cesium, Unity, Unreal with urban extensions), or infrastructure digital twin frameworks (iTwin).
Excluded are standalone smart city IoT platforms, transport simulation tools, or standards bodies unless they are directly used as UDT building blocks.

## Scope Boundary

This review applies a **moderate** inclusion boundary.
Platforms that are purely adjacent (e.g., generic IoT platforms, general-purpose GIS tools without urban twin framing) are excluded even if they could theoretically be used in a UDT context.

## Research Approach

Each platform is researched using primary sources only (see `docs/source-policy.md`).
Findings are synthesized into `docs/review.md`.
The canonical data record for each platform is its row in `docs/platform-inventory.md`.

## Discovery to Comparison Workflow

1. Run a discovery session using `prompts/platform-discovery.md` and save the response to `responses/`
2. Open the saved response and choose which platforms to compare
3. Copy the rows you want to compare (including the header row) from the summary table
4. Paste them into the `[PASTE_SELECTED_PLATFORMS_HERE]` token in `prompts/platform-comparison.md`
5. Run the comparison session and save the response to `responses/`

Discovery dimension scores are judgment-based first-pass signals. The comparison prompt deepens them with full rubric-based research and primary source evidence — expect scores to shift.

**Optional — License analysis:** For any platform in the discovery table, copy the header row and that platform's row and paste them into the `[PASTE_SELECTED_PLATFORM_HERE]` token in `prompts/license-analysis.md`.
This can be run independently at any point — it does not need to precede or follow a comparison session.

For operational guidance on applying these criteria — including explicit exclusion examples, a seed list of known qualifying platforms, and a target corpus size — see [`docs/scope.md`](scope.md).

## File Naming

All filename components use only lowercase letters, digits, and hyphens (kebab-case).
No spaces, underscores, or uppercase.

### Response files (`responses/`)

Pattern: `<platform>-<prompt-type>.md`

| Token           | Values                                                |
| --------------- | ----------------------------------------------------- |
| `<platform>`    | kebab-case platform name, e.g. `cesium`, `3d-city-db` |
| `<prompt-type>` | `discovery`, `comparison`, or `license`               |

Examples:

- `cesium-license.md`
- `cesium-vs-dtcc-comparison.md` — two platforms joined with `vs`
- `cesium-et-al-comparison.md` — more than two platforms
- `european-platforms-discovery.md` — broad discovery session; use a scope descriptor instead of a platform name

If a session is re-run for the same platform and prompt type, overwrite the file. Git history preserves the previous version.

### Session logs (`search_logs/`)

Pattern: `<platform>.md` — one file per platform, updated as research evolves.

## Functional Category Rubrics

The Part 1 scoring table includes six functional category columns in addition to the six research dimensions. Each category uses the same 1–5 integer scale — bare integer, `?` for unknown.

**Column abbreviations:**

| Abbreviation | Full name | Description |
| ------------ | --------- | ----------- |
| Viz | Visualization | 3D rendering, GIS viewers, scene composition |
| DM | Data Management | Data ingestion, storage, twin models, semantic layers |
| Sim | Simulation | Urban simulation, physics, scenario modelling |
| IoT | IoT Sensing | Real-time data, sensor integration, device management |
| Std | Standards | Open standards implementation, interoperability frameworks |
| Infra | Infrastructure | Built environment, BIM/GIS, infrastructure lifecycle |

**Rubrics:**

**Visualization (Viz)**

| Score | Criteria |
| ----- | -------- |
| 5 | Purpose-built 3D visualization engine or viewer; primary purpose; real-time or near-real-time rendering |
| 4 | Strong visualization capabilities; core feature set with significant investment |
| 3 | Visualization present and useful but not the primary strength |
| 2 | Basic or incidental visualization (e.g., simple 2D map view, no 3D) |
| 1 | No meaningful visualization capability |

**Data Management (DM)**

| Score | Criteria |
| ----- | -------- |
| 5 | Purpose-built for city-scale data storage and management; semantic model, versioning, full data lifecycle |
| 4 | Strong data management with semantic modelling or graph; multi-source ingestion |
| 3 | Solid data management but limited semantic layer or scalability |
| 2 | Basic storage or data exchange; limited query or model capabilities |
| 1 | No meaningful data management role |

**Simulation (Sim)**

| Score | Criteria |
| ----- | -------- |
| 5 | Purpose-built simulation engine; multi-domain urban physics, scenario comparison at city scale |
| 4 | Strong simulation support across multiple urban domains |
| 3 | Simulation present for one or two domains; limited scenario tooling |
| 2 | Basic scenario comparison or single-variable simulation |
| 1 | No simulation capability |

**IoT Sensing (IoT)**

| Score | Criteria |
| ----- | -------- |
| 5 | Purpose-built IoT platform; real-time ingestion, device registry, stream processing at scale |
| 4 | Strong IoT support; real-time APIs, sensor integration, stream handling |
| 3 | Connects to sensors but limited real-time processing |
| 2 | Basic real-time data hookup; manual or batch sensor feeds |
| 1 | No IoT or real-time sensing capability |

**Standards (Std)**

| Score | Criteria |
| ----- | -------- |
| 5 | Primary purpose is defining or implementing open standards (OGC, ISO, W3C); governance role in standards body |
| 4 | Strong standards implementation; multiple OGC/ISO standards as native data models |
| 3 | Partial standards support; some open standards alongside proprietary models |
| 2 | Limited standards; primarily proprietary with token open format support |
| 1 | No meaningful open standards implementation |

**Infrastructure (Infra)**

| Score | Criteria |
| ----- | -------- |
| 5 | Purpose-built for infrastructure or BIM lifecycle; IFC, asset management, lifecycle tracking |
| 4 | Strong infrastructure support; BIM integration, asset management, or civil engineering focus |
| 3 | Infrastructure is one of several domains; partial BIM/GIS support |
| 2 | Limited infrastructure scope; building-level only or minimal lifecycle management |
| 1 | No meaningful infrastructure or built environment focus |
