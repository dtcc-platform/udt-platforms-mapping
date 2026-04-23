# Rating Platform Selection

This file holds the platforms selected for the **current** rating cycle run. It is a required input of `act/rating/prompt.md` — the AI CLI reads it in CLI mode and inlines it into the resolved prompt in Web mode.

Unlike `scope.md`, `rubrics.md`, and `source-policy.md` — which are slow-moving **definitions** reused across cycle runs — this file is **per-run data** and is expected to change between rating cycles. Add a row to include a platform in the current comparison; remove a row to drop it. The git history of this file is the authoritative record of which platforms were compared in each cycle.

**The DTCC row MUST be present.** The rating prompt's Part 3 landscape observations orient around DTCC, so removing the DTCC row breaks Part 3 output. If DTCC is missing, the rating prompt will surface a scope error and refuse to produce output.

The `Layer` value for each row carries from the most recent discovery response's summary table and is not reassessed by the rating prompt — Layer is owned by the discovery phase.

| Name                   | Link                                                                                         | Layer         |
| ---------------------- | -------------------------------------------------------------------------------------------- | ------------- |
| DTCC Platform          | [platform.dtcc.chalmers.se](https://platform.dtcc.chalmers.se/)                              | core-platform |
| Virtual Singapore      | [nrf.gov.sg/programmes/virtual-singapore](https://www.nrf.gov.sg/programmes/virtual-singapore) | core-platform |
| ArcGIS Urban           | [esri.com/arcgis/products/arcgis-urban](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview) | core-platform |
| Bentley iTwin Platform | [bentley.com/itwin-platform](https://www.bentley.com/software/itwin-platform/)               | backbone      |
