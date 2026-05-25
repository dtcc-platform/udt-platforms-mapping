# Entity Discovery Benchmark Report — 2026-04-23

**Fixture:** plan/entity-discovery-benchmark.md
**Responses tested:** 3 files

---

## Recall Coverage

| Artifact                                         | Type         | Tags             | Claude Opus 4.7                | GPT-5.4 Thinking | Gemini 3 Flash |
| ------------------------------------------------ | ------------- | ---------------- | ------------------------------ | ---------------- | -------------- |
| DTCC                                             | platform | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Virtual Singapore                                | platform | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Dassault Systèmes 3DEXPERIENCity                 | platform | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| Cesium / CesiumJS                                | framework | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| Bentley iTwin Platform                           | framework | baseline         | ✓ found                        | ✓ found          | ✓ found        |
| 3DCityDB                                         | framework | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| FIWARE                                           | framework | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| TerriaJS                                         | framework | baseline         | ✓ found                        | ✗ missing        | ✓ found        |
| MATSim                                           | module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| UrbanSim                                         | module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| City Energy Analyst                              | module | baseline         | ✓ found                        | ✓ found          | ✗ missing      |
| Project PLATEAU                                  | platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| Virtual Gothenburg                               | platform | government-led   | ✗ missing                      | ✓ found          | ✗ missing      |
| SuperMap Digital Twin                            | platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| 51WORLD 51Aes                                    | platform | government-led   | ✓ found                        | ✗ missing        | ✗ missing      |
| Siradel S-Twin                                   | platform | niche-commercial | ✗ missing                      | ✗ missing        | ✓ found        |
| CityZenith SmartWorldOS                          | platform | niche-commercial | ✗ missing                      | ✗ missing        | ✓ found        |
| Hexagon Urban Digital Twin                       | platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Snap4City                                        | platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| DUET (Digital Urban European Twins)              | platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Virtual City Systems VC Suite                    | platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| Bentley OpenCities Planner                       | platform | niche-commercial | ✓ found                        | ✗ missing        | ✗ missing      |
| NVIDIA Omniverse                                 | framework | niche-commercial | ✓ found (Type: platform) | ✗ missing        | ✗ missing      |
| GeoDatalytics                                    | module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| Eclipse SUMO                                     | module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| ArcGIS CityEngine                                | module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| UMEP (Urban Multi-scale Environmental Predictor) | module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| GAMA Platform                                    | module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| ENVI-met                                         | module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| A/B Street                                       | module | no-dt-framing    | ✗ missing                      | ✓ found          | ✗ missing      |
| SimWalk                                          | module | no-dt-framing    | ✗ missing                      | ✗ missing        | ✓ found        |
| OpenEEmeter                                      | module | no-dt-framing    | ✗ missing                      | ✗ missing        | ✓ found        |
| NVIDIA Earth-2                                   | module | no-dt-framing    | ✓ found                        | ✗ missing        | ✗ missing      |
| FROST-Server                                     | framework | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| kepler.gl                                        | framework | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| deck.gl                                          | framework | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| 3D Tiles                                         | framework | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |
| 3D BAG                                           | framework | niche-oss        | ✓ found                        | ✗ missing        | ✗ missing      |

## Novel Finds — not in benchmark

Entities discovered by models but not in plan/entity-discovery-benchmark.md.
Review and add to the benchmark if in-scope, filling in the Tags column before pasting.

### Claude Opus 4.7

| Name               | Link                                                                                                           | Type          | Aliases | Tags |
| ------------------ | -------------------------------------------------------------------------------------------------------------- | ------------- | ------- | ---- |
| ArcGIS Urban       | https://www.esri.com/en-us/capabilities/3d-gis/get-started                                                     | platform |         |      |
| Siemens Xcelerator | https://xcelerator.siemens.com/global/en/industries/urban-communities/smart-cities/digital-city-solutions.html | excluded      |         |      |

### GPT-5.4 Thinking

| Name                | Link                                                             | Type          | Aliases | Tags |
| ------------------- | ---------------------------------------------------------------- | ------------- | ------- | ---- |
| ArcGIS Urban        | https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview | module |         |      |
| Azure Digital Twins | https://learn.microsoft.com/en-us/azure/digital-twins/overview   | excluded      |         |      |
| Unreal Engine       | https://www.unrealengine.com/digital-twins                       | excluded      |         |      |

### Gemini 3 Flash

| Name    | Link                                       | Type     | Aliases | Tags |
| ------- | ------------------------------------------ | -------- | ------- | ---- |
| AutoCAD | https://www.autodesk.com/products/autocad/ | excluded |         |      |

---

## Summary

| Model            | Found | Missing | Wrong type | Novel Finds |
| ---------------- | ----- | ------- | ----------- | ----------- |
| Claude Opus 4.7  | 30/38 | 8       | 1           | 2           |
| GPT-5.4 Thinking | 14/38 | 24      | 0           | 3           |
| Gemini 3 Flash   | 9/38  | 29      | 0           | 1           |
