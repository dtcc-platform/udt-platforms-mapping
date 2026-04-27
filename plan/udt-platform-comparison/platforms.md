# UDT Platform Comparison Selection

This file holds the platforms selected for the **current** `udt-platform-comparison` cycle run.
It is a required input of `act/udt-platform-comparison/prompt.md`.

Unlike `rubrics.md` and `source-policy.md`, which are slow-moving definitions reused across cycle runs, this file is **per-run data** and is expected to change between comparison cycles.
Add a row to include a platform in the current comparison; remove a row to drop it.
The git history of this file is the authoritative record of which platforms were compared in each cycle.

This cycle is intentionally restricted to rows already classified as `Type = platform` in `udt-platforms`.
Frameworks, modules, and excluded rows do not belong here.

**The DTCC row MUST be present.** The comparison prompt's Part 3 landscape observations orient around DTCC, so removing the DTCC row breaks Part 3 output.
If DTCC is missing, the comparison prompt will surface a scope error and refuse to produce output.

Aliases do not belong here. Comparison uses exact selected canonical rows; fuzzy alias handling belongs in the `udt-platforms` benchmarking workflow.

| Name | Link |
| ---- | ---- |
| DTCC Platform | [platform.dtcc.chalmers.se](https://platform.dtcc.chalmers.se/) |
| Virtual Singapore | [nrf.gov.sg/programmes/virtual-singapore](https://www.nrf.gov.sg/programmes/virtual-singapore) |
| ArcGIS Urban | [esri.com/arcgis/products/arcgis-urban](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview) |
