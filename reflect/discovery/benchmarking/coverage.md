# Discovery Coverage Report — 2026-04-23

**Fixture:** reflect/discovery/benchmarking/benchmark.md
**Responses tested:** 3 files

---

## Recall

| Platform                                         | Layer         | Tags             | Claude Opus 4.7                | GPT-5.4 Thinking | Gemini 3 Flash |
| ------------------------------------------------ | ------------- | ---------------- | ------------------------------ | ---------------- | -------------- |
| DTCC                                             | core-platform | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Virtual Singapore                                | core-platform | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Dassault Systèmes 3DEXPERIENCity                 | core-platform | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| Cesium / CesiumJS                                | backbone      | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Bentley iTwin Platform                           | backbone      | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| 3DCityDB                                         | backbone      | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| FIWARE                                           | backbone      | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| TerriaJS                                         | backbone      | baseline         | ✓ found                        | ✗ missing        | ✓ found        |
| MATSim                                           | domain-module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| UrbanSim                                         | domain-module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| City Energy Analyst                              | domain-module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| Project PLATEAU                                  | core-platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| Virtual Gothenburg                               | core-platform | government-led   | ✗ missing                      | ✓ found          | ✗ missing      |
| SuperMap Digital Twin                            | core-platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| 51WORLD 51Aes                                    | core-platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| Siradel S-Twin                                   | core-platform | niche-commercial | ✗ missing                      | ✗ missing        | ✓ found        |
| CityZenith SmartWorldOS                          | core-platform | niche-commercial | ✗ missing                      | ✗ missing        | ✓ found        |
| Hexagon Urban Digital Twin                       | core-platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Snap4City                                        | core-platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| DUET (Digital Urban European Twins)              | core-platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Virtual City Systems VC Suite                    | core-platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Bentley OpenCities Planner                       | core-platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| NVIDIA Omniverse                                 | backbone      | niche-commercial | ✓ found (Layer: core-platform) | ✗ missing        | ✗ missing      |
| GeoDatalytics                                    | domain-module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| Eclipse SUMO                                     | domain-module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| ArcGIS CityEngine                                | domain-module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| UMEP (Urban Multi-scale Environmental Predictor) | domain-module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| GAMA Platform                                    | domain-module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| ENVI-met                                         | domain-module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| A/B Street                                       | domain-module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| SimWalk                                          | domain-module | no-dt-framing    | ✗ missing                      | ✗ missing        | ✓ found        |
| OpenEEmeter                                      | domain-module | no-dt-framing    | ✗ missing                      | ✗ missing        | ✓ found        |
| NVIDIA Earth-2                                   | domain-module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| FROST-Server                                     | backbone      | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| kepler.gl                                        | backbone      | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| deck.gl                                          | backbone      | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| 3D Tiles                                         | backbone      | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| 3D BAG                                           | backbone      | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |

## Novel Finds — not in benchmark

Platforms discovered by models but not in reflect/discovery/benchmarking/benchmark.md.
Review and add to the benchmark if in-scope, filling in the Tags column before pasting.

### Claude Opus 4.7

| Name               | Link                                                                                                           | Layer         | Aliases | Tags |
| ------------------ | -------------------------------------------------------------------------------------------------------------- | ------------- | ------- | ---- |
| ArcGIS Urban       | https://www.esri.com/en-us/capabilities/3d-gis/get-started                                                     | core-platform |         |      |
| Siemens Xcelerator | https://xcelerator.siemens.com/global/en/industries/urban-communities/smart-cities/digital-city-solutions.html | excluded      |         |      |

### GPT-5.4 Thinking

| Name                | Link                                                             | Layer         | Aliases | Tags |
| ------------------- | ---------------------------------------------------------------- | ------------- | ------- | ---- |
| ArcGIS Urban        | https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview | domain-module |         |      |
| Azure Digital Twins | https://learn.microsoft.com/en-us/azure/digital-twins/overview   | excluded      |         |      |
| Unreal Engine       | https://www.unrealengine.com/digital-twins                       | excluded      |         |      |

### Gemini 3 Flash

| Name    | Link                                       | Layer    | Aliases | Tags |
| ------- | ------------------------------------------ | -------- | ------- | ---- |
| AutoCAD | https://www.autodesk.com/products/autocad/ | excluded |         |      |

---

## Summary

| Model            | Found | Missing | Wrong layer | Novel Finds |
| ---------------- | ----- | ------- | ----------- | ----------- |
| Claude Opus 4.7  | 30/38 | 8       | 1           | 2           |
| GPT-5.4 Thinking | 14/38 | 24      | 0           | 3           |
| Gemini 3 Flash   | 9/38  | 29      | 0           | 1           |
