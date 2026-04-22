# Discovery Recall Benchmark

This file is the recall benchmark for UDT ecosystem discovery sessions. It lists platforms expected to appear in discovery responses that are at risk of being missed.

**How to use:** Run `reflect/discovery/benchmarking/prompt.md` via Claude Code to check all `observe/discovery/*.md` files against this list.

**How to add an entry:** Add a row to the table. Fill in `Tags` with one or more comma-separated tags from the tag legend below. Add known name variants to `Aliases` (comma-separated) when a model uses a different name and causes a false negative.

## Tag Legend

| Tag                | Meaning                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `baseline`         | Reliably found by all models — regression guard; if missing, something is wrong                                   |
| `government-led`   | Backed by a national or municipal government; often documented in non-English sources                             |
| `niche-commercial` | Smaller or regional vendor; lacks the marketing footprint of Esri, Bentley, or Siemens                            |
| `no-dt-framing`    | Uses urban analytics / simulation / climate language without claiming "digital twin"                              |
| `niche-oss`        | Open-source building block; not marketed as a digital twin tool; missed when models focus on end-to-end platforms |

---

| Name                                             | Link                                                                                                | Layer         | Aliases                                 | Tags             |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------- | ---------------- |
| DTCC                                             | https://dtcc.chalmers.se                                                                            | core-platform | DTCC Platform                           | baseline         |
| Virtual Singapore                                | https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/                      | core-platform |                                         | baseline         |
| Dassault Systèmes 3DEXPERIENCity                 | https://www.3ds.com/virtual-twin/infrastructure-cities                                              | core-platform | 3DEXPERIENCity, 3DEXPERIENCE City       | baseline         |
| Cesium / CesiumJS                                | https://cesium.com/platform/cesiumjs/                                                               | backbone      | CesiumJS, Cesium                        | baseline         |
| Bentley iTwin Platform                           | https://www.bentley.com/software/itwin-platform/                                                    | backbone      | iTwin Platform, iTwin (Bentley Systems) | baseline         |
| 3DCityDB                                         | https://www.3dcitydb.org                                                                            | backbone      |                                         | baseline         |
| FIWARE                                           | https://www.fiware.org                                                                              | backbone      |                                         | baseline         |
| TerriaJS                                         | https://terria.io                                                                                   | backbone      |                                         | baseline         |
| MATSim                                           | https://matsim.org                                                                                  | domain-module |                                         | baseline         |
| UrbanSim                                         | https://udst.github.io/urbansim/                                                                    | domain-module |                                         | baseline         |
| City Energy Analyst                              | https://cityenergyanalyst.com                                                                       | domain-module | CityEnergyAnalyst, CEA                  | baseline         |
| Project PLATEAU                                  | https://www.mlit.go.jp/plateau/en/                                                                  | core-platform |                                         | government-led   |
| Virtual Gothenburg                               | https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/ | core-platform |                                         | government-led   |
| SuperMap Digital Twin                            | https://www.supermap.com/en-us/                                                                     | core-platform | SuperMap Digital Twin Platform          | government-led   |
| 51WORLD 51Aes                                    | https://www.51world.com                                                                             | core-platform |                                         | government-led   |
| Siradel S-Twin                                   | https://www.siradel.com/solutions/smart-city/s-twin/                                                | core-platform |                                         | niche-commercial |
| CityZenith SmartWorldOS                          | https://cityzenith.com                                                                              | core-platform | SmartWorldOS                            | niche-commercial |
| Hexagon Urban Digital Twin                       | https://hexagon.com/go/sig/urban-digital-twin                                                       | core-platform | Hexagon Urban Digital Twin Platform     | niche-commercial |
| Snap4City                                        | https://www.snap4city.org                                                                           | core-platform |                                         | niche-commercial |
| DUET (Digital Urban European Twins)              | https://www.digitalurbantwins.com                                                                   | core-platform |                                         | niche-commercial |
| Virtual City Systems VC Suite                    | https://vc.systems/en/solutions/digital-twin/                                                       | core-platform | Virtual City Systems VC Suite / VC Map  | niche-commercial |
| Bentley OpenCities Planner                       | https://www.bentley.com/software/opencities-planner/                                                | core-platform |                                         | niche-commercial |
| NVIDIA Omniverse                                 | https://www.nvidia.com/en-us/omniverse/                                                             | backbone      |                                         | niche-commercial |
| GeoDatalytics                                    | https://github.com/OpenGeoscience/geodatalytics                                                     | domain-module |                                         | no-dt-framing    |
| Eclipse SUMO                                     | https://eclipse.dev/sumo/                                                                           | domain-module | SUMO                                    | no-dt-framing    |
| ArcGIS CityEngine                                | https://www.esri.com/en-us/arcgis/products/arcgis-cityengine/overview                               | domain-module | CityEngine                              | no-dt-framing    |
| UMEP (Urban Multi-scale Environmental Predictor) | https://umep-docs.readthedocs.io                                                                    | domain-module | UMEP                                    | no-dt-framing    |
| GAMA Platform                                    | https://gama-platform.org                                                                           | domain-module | GAMA                                    | no-dt-framing    |
| ENVI-met                                         | https://www.envi-met.com                                                                            | domain-module |                                         | no-dt-framing    |
| A/B Street                                       | https://abstreet.uk                                                                                 | domain-module | ABStreet, A/B Street simulator          | no-dt-framing    |
| SimWalk                                          | https://www.simwalk.com                                                                             | domain-module |                                         | no-dt-framing    |
| OpenEEmeter                                      | https://www.openeemeter.org                                                                         | domain-module | EEmeter                                 | no-dt-framing    |
| NVIDIA Earth-2                                   | https://www.nvidia.com/en-us/high-performance-computing/earth-2/                                    | domain-module | Earth-2                                 | no-dt-framing    |
| FROST-Server                                     | https://fraunhoferiosb.github.io/FROST-Server/                                                      | backbone      |                                         | niche-oss        |
| kepler.gl                                        | https://kepler.gl                                                                                   | backbone      |                                         | niche-oss        |
| deck.gl                                          | https://deck.gl                                                                                     | backbone      |                                         | niche-oss        |
| 3D Tiles                                         | https://github.com/CesiumGS/3d-tiles                                                                | backbone      |                                         | niche-oss        |
| 3D BAG                                           | https://3dbag.nl                                                                                    | backbone      |                                         | niche-oss        |
