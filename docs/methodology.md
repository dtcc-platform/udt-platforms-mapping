# Research Methodology

## Inclusion Criteria

A platform is included in this review if it satisfies at least one of the following three criteria:

### 1. Explicit Urban Digital Twin

The platform explicitly presents itself as an urban or city-scale digital twin. This includes platforms that use the term "digital twin" in their official documentation, product descriptions, or marketing, and are scoped to urban environments (cities, districts, or built infrastructure at city scale).

### 2. City-Scale Capabilities

The platform provides capabilities commonly used to build or operate urban digital twins, even if it does not use the term. This includes platforms for city-scale 3D visualization, urban simulation, large-scale geospatial data management, or multi-domain urban analytics (buildings, transport, energy, climate).

### 3. Adjacent Architecture or Governance

The platform is a foundational building block commonly integrated into UDT systems — for example, open standards implementations (CityGML, IFC, OGC standards), enabling visualization engines (Cesium, Unity, Unreal with urban extensions), or infrastructure digital twin frameworks (iTwin). Excluded are standalone smart city IoT platforms, transport simulation tools, or standards bodies unless they are directly used as UDT building blocks.

## Scope Boundary

This review applies a **moderate** inclusion boundary. Platforms that are purely adjacent (e.g., generic IoT platforms, general-purpose GIS tools without urban twin framing) are excluded even if they could theoretically be used in a UDT context.

## Research Approach

Each platform is researched using primary sources only (see `docs/source-policy.md`). Findings are recorded in `search_logs/` and synthesized into `docs/review.md`. The canonical data record for each platform is its row in `docs/platform-inventory.md`.

For operational guidance on applying these criteria — including explicit exclusion examples, a seed list of known qualifying platforms, and a target corpus size — see [`docs/scope.md`](scope.md).

## File Naming

All filename components use only lowercase letters, digits, and hyphens (kebab-case). No spaces, underscores, or uppercase.

### Response files (`responses/`)

Pattern: `<platform>-<prompt-type>.md`

| Token | Values |
| -------------- | ----------------------------------------- |
| `<platform>` | kebab-case platform name, e.g. `cesium`, `3d-city-db` |
| `<prompt-type>` | `discovery`, `comparison`, or `license` |

Examples:

- `cesium-license.md`
- `cesium-vs-dtcc-comparison.md` — two platforms joined with `vs`
- `cesium-et-al-comparison.md` — more than two platforms
- `european-platforms-discovery.md` — broad discovery session; use a scope descriptor instead of a platform name

If a session is re-run for the same platform and prompt type, overwrite the file. Git history preserves the previous version.

### Session logs (`search_logs/`)

Pattern: `<platform>.md` — one file per platform, updated as research evolves.
