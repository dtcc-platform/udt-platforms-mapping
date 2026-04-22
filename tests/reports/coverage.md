# Discovery Coverage Report — 2026-04-22

**Fixture:** tests/discovery-fixtures.md
**Responses tested:** 3 files

---

## Gap: Baseline — consistently discovered

| Platform                         | Expected Layer | Claude Opus 4.7 | GPT-5.4 Thinking | Gemini 3 Flash |
| -------------------------------- | -------------- | --------------- | ---------------- | -------------- |
| DTCC                             | core-platform  | ✓ found         | ✓ found          | ✓ found        |
| Virtual Singapore                | core-platform  | ✓ found         | ✓ found          | ✓ found        |
| Dassault Systèmes 3DEXPERIENCity | core-platform  | ✓ found         | ✓ found          | ✗ missing      |
| Cesium / CesiumJS                | backbone       | ✓ found         | ✓ found          | ✓ found        |
| Bentley iTwin Platform           | backbone       | ✓ found         | ✓ found          | ✓ found        |
| 3DCityDB                         | backbone       | ✓ found         | ✓ found          | ✗ missing      |
| FIWARE                           | backbone       | ✓ found         | ✓ found          | ✗ missing      |
| TerriaJS                         | backbone       | ✓ found         | ✗ missing        | ✓ found        |
| MATSim                           | domain-module  | ✓ found         | ✓ found          | ✗ missing      |
| UrbanSim                         | domain-module  | ✓ found         | ✓ found          | ✗ missing      |
| City Energy Analyst              | domain-module  | ✓ found         | ✓ found          | ✗ missing      |

---

## Gap: Government-led — non-English / non-US/EU initiatives

| Platform              | Expected Layer | Claude Opus 4.7 | GPT-5.4 Thinking | Gemini 3 Flash |
| --------------------- | -------------- | --------------- | ---------------- | -------------- |
| Project PLATEAU       | core-platform  | ✓ found         | ✗ missing        | ✗ missing      |
| Virtual Gothenburg    | core-platform  | ✗ missing       | ✓ found          | ✗ missing      |
| SuperMap Digital Twin | core-platform  | ✓ found         | ✗ missing        | ✗ missing      |
| 51WORLD 51Aes         | core-platform  | ✓ found         | ✗ missing        | ✗ missing      |

---

## Gap: Niche commercial — smaller vendors without major DT marketing presence

| Platform                            | Expected Layer | Claude Opus 4.7                | GPT-5.4 Thinking | Gemini 3 Flash |
| ----------------------------------- | -------------- | ------------------------------ | ---------------- | -------------- |
| Siradel S-Twin                      | core-platform  | ✗ missing                      | ✗ missing        | ✓ found        |
| CityZenith SmartWorldOS             | core-platform  | ✗ missing                      | ✗ missing        | ✓ found        |
| Hexagon Urban Digital Twin          | core-platform  | ✓ found                        | ✗ missing        | ✗ missing      |
| Snap4City                           | core-platform  | ✓ found                        | ✗ missing        | ✗ missing      |
| DUET (Digital Urban European Twins) | core-platform  | ✓ found                        | ✗ missing        | ✗ missing      |
| Virtual City Systems VC Suite       | core-platform  | ✓ found                        | ✗ missing        | ✗ missing      |
| Bentley OpenCities Planner          | core-platform  | ✓ found                        | ✗ missing        | ✗ missing      |
| NVIDIA Omniverse                    | backbone       | ✓ found (Layer: core-platform) | ✗ missing        | ✗ missing      |

---

## Gap: No digital-twin framing — urban analytics, simulation & climate

| Platform                                         | Expected Layer | Claude Opus 4.7 | GPT-5.4 Thinking | Gemini 3 Flash |
| ------------------------------------------------ | -------------- | --------------- | ---------------- | -------------- |
| GeoDatalytics                                    | domain-module  | ✗ missing       | ✓ found          | ✗ missing      |
| Eclipse SUMO                                     | domain-module  | ✓ found         | ✗ missing        | ✗ missing      |
| ArcGIS CityEngine                                | domain-module  | ✓ found         | ✗ missing        | ✗ missing      |
| UMEP (Urban Multi-scale Environmental Predictor) | domain-module  | ✓ found         | ✗ missing        | ✗ missing      |
| GAMA Platform                                    | domain-module  | ✓ found         | ✗ missing        | ✗ missing      |
| ENVI-met                                         | domain-module  | ✗ missing       | ✓ found          | ✗ missing      |
| A/B Street                                       | domain-module  | ✗ missing       | ✓ found          | ✗ missing      |
| SimWalk                                          | domain-module  | ✗ missing       | ✗ missing        | ✓ found        |
| OpenEEmeter                                      | domain-module  | ✗ missing       | ✗ missing        | ✓ found        |
| NVIDIA Earth-2                                   | domain-module  | ✓ found         | ✗ missing        | ✗ missing      |

---

## Gap: Niche open-source backbone components

| Platform     | Expected Layer | Claude Opus 4.7 | GPT-5.4 Thinking | Gemini 3 Flash |
| ------------ | -------------- | --------------- | ---------------- | -------------- |
| FROST-Server | backbone       | ✓ found         | ✗ missing        | ✗ missing      |
| kepler.gl    | backbone       | ✓ found         | ✗ missing        | ✗ missing      |
| deck.gl      | backbone       | ✓ found         | ✗ missing        | ✗ missing      |
| 3D Tiles     | backbone       | ✓ found         | ✗ missing        | ✗ missing      |
| 3D BAG       | backbone       | ✓ found         | ✗ missing        | ✗ missing      |

---

## Summary

| Model            | Found | Missing | Wrong layer |
| ---------------- | ----- | ------- | ----------- |
| Claude Opus 4.7  | 31/38 | 7       | 1           |
| GPT-5.4 Thinking | 14/38 | 24      | 0           |
| Gemini 3 Flash   | 9/38  | 29      | 0           |
