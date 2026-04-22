# Discovery Recall Benchmark

This file is the recall benchmark for UDT ecosystem discovery sessions. It lists platforms that are expected to appear in discovery responses, grouped by the discovery failure mode (gap category) that makes them easy to miss.

**How to use:** Run `evals/discovery/run.md` via Claude Code to check all `responses/global-platforms-discovery-*.md` files against this list.

**How to add an entry:** When a known in-scope platform is found to be missing from a discovery response, add a row to the appropriate gap category. If no category fits, create a new `## Gap:` section. When a model uses a variant name that causes a false negative, add that variant to the `Aliases` cell (comma-separated).

---

## Gap: Baseline — consistently discovered

Platforms that all major models reliably find. Included as a regression baseline — if any of these go missing in a future session something is wrong with the prompt or session setup.

| Name                             | Link                                                                           | Expected Layer | Why tricky                 | Aliases                                 |
| -------------------------------- | ------------------------------------------------------------------------------ | -------------- | -------------------------- | --------------------------------------- |
| DTCC                             | https://dtcc.chalmers.se                                                       | core-platform  | Required entry; regression | DTCC Platform                           |
| Virtual Singapore                | https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/ | core-platform  | Regression baseline        |                                         |
| Dassault Systèmes 3DEXPERIENCity | https://www.3ds.com/virtual-twin/infrastructure-cities                         | core-platform  | Regression baseline        | 3DEXPERIENCity, 3DEXPERIENCE City       |
| Cesium / CesiumJS                | https://cesium.com/platform/cesiumjs/                                          | backbone       | Regression baseline        | CesiumJS, Cesium                        |
| Bentley iTwin Platform           | https://www.bentley.com/software/itwin-platform/                               | backbone       | Regression baseline        | iTwin Platform, iTwin (Bentley Systems) |
| 3DCityDB                         | https://www.3dcitydb.org                                                       | backbone       | Regression baseline        |                                         |
| FIWARE                           | https://www.fiware.org                                                         | backbone       | Regression baseline        |                                         |
| TerriaJS                         | https://terria.io                                                              | backbone       | Regression baseline        |                                         |
| MATSim                           | https://matsim.org                                                             | domain-module  | Regression baseline        |                                         |
| UrbanSim                         | https://udst.github.io/urbansim/                                               | domain-module  | Regression baseline        |                                         |
| City Energy Analyst              | https://cityenergyanalyst.com                                                  | domain-module  | Regression baseline        | CityEnergyAnalyst, CEA                  |

---

## Gap: Government-led — non-English / non-US/EU initiatives

Platforms backed by national or municipal governments, often documented primarily in non-English sources or on government websites that models may not find without explicit geographic search.

| Name                  | Link                                                                                                | Expected Layer | Why tricky                                                        | Aliases                        |
| --------------------- | --------------------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------- | ------------------------------ |
| Project PLATEAU       | https://www.mlit.go.jp/plateau/en/                                                                  | core-platform  | Japanese government initiative; primary docs in Japanese          |                                |
| Virtual Gothenburg    | https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/ | core-platform  | Swedish municipality; limited English-language coverage           |                                |
| SuperMap Digital Twin | https://www.supermap.com/en-us/                                                                     | core-platform  | Chinese vendor; dominant in Asian markets, low Western visibility | SuperMap Digital Twin Platform |
| 51WORLD 51Aes         | https://www.51world.com                                                                             | core-platform  | Chinese vendor; primary presence in Chinese-language media        |                                |

---

## Gap: Niche commercial — smaller vendors without major DT marketing presence

Platforms from smaller or regional vendors that are genuine UDT products but lack the marketing footprint of Esri, Bentley, or Siemens. Models tend to miss these in favour of well-known names.

| Name                                | Link                                                 | Expected Layer | Why tricky                                                               | Aliases                                |
| ----------------------------------- | ---------------------------------------------------- | -------------- | ------------------------------------------------------------------------ | -------------------------------------- |
| Siradel S-Twin                      | https://www.siradel.com/solutions/smart-city/s-twin/ | core-platform  | French vendor; strong in telecoms/smart city; low global DT profile      |                                        |
| CityZenith SmartWorldOS             | https://cityzenith.com                               | core-platform  | Small US vendor; rebranded from SmartWorldPro; low visibility            | SmartWorldOS                           |
| Hexagon Urban Digital Twin          | https://hexagon.com/go/sig/urban-digital-twin        | core-platform  | Marketed under Hexagon's wider portfolio; not a standalone product name  | Hexagon Urban Digital Twin Platform    |
| Snap4City                           | https://www.snap4city.org                            | core-platform  | EU-funded smart city platform; academic-commercial hybrid                |                                        |
| DUET (Digital Urban European Twins) | https://www.digitalurbantwins.com                    | core-platform  | EU Horizon project; not a commercial product                             |                                        |
| Virtual City Systems VC Suite       | https://vc.systems/en/solutions/digital-twin/        | core-platform  | German vendor; strong CityGML heritage; low English-language profile     | Virtual City Systems VC Suite / VC Map |
| Bentley OpenCities Planner          | https://www.bentley.com/software/opencities-planner/ | core-platform  | Separate Bentley product from iTwin; less well-known                     |                                        |
| NVIDIA Omniverse                    | https://www.nvidia.com/en-us/omniverse/              | backbone       | Marketed as a simulation/rendering platform; DT use cases not front-page |                                        |

---

## Gap: No digital-twin framing — urban analytics, simulation & climate

Platforms that use "urban analytics," "resilience," "simulation," or "climate risk" language without claiming "digital twin." Models miss them because they search for digital-twin signal first. These tools qualify as `domain-module` or `backbone` if their outputs feed into a broader UDT stack.

| Name                                             | Link                                                                  | Expected Layer | Why tricky                                                                           | Aliases                        |
| ------------------------------------------------ | --------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------ | ------------------------------ |
| GeoDatalytics                                    | https://github.com/OpenGeoscience/geodatalytics                       | domain-module  | "Urban visualization and data analysis toolkit"; no DT framing; niche GitHub project |                                |
| Eclipse SUMO                                     | https://eclipse.dev/sumo/                                             | domain-module  | Traffic simulation; widely used in UDT mobility layers; not DT-branded               | SUMO                           |
| ArcGIS CityEngine                                | https://www.esri.com/en-us/arcgis/products/arcgis-cityengine/overview | domain-module  | 3D urban modelling tool; often seen as a CAD product, not a UDT component            | CityEngine                     |
| UMEP (Urban Multi-scale Environmental Predictor) | https://umep-docs.readthedocs.io                                      | domain-module  | Urban climate tool; academic plugin for QGIS; no DT framing                          | UMEP                           |
| GAMA Platform                                    | https://gama-platform.org                                             | domain-module  | Agent-based urban simulation; research tool; no commercial DT profile                | GAMA                           |
| ENVI-met                                         | https://www.envi-met.com                                              | domain-module  | Urban microclimate simulation; architectural/planning domain; no DT label            |                                |
| A/B Street                                       | https://abstreet.uk                                                   | domain-module  | Open-source traffic/mobility simulator; indie project; low visibility                | ABStreet, A/B Street simulator |
| SimWalk                                          | https://www.simwalk.com                                               | domain-module  | Pedestrian and crowd simulation; niche vendor; no DT framing                         |                                |
| OpenEEmeter                                      | https://www.openeemeter.org                                           | domain-module  | Energy measurement and verification; utility domain; no DT framing                   | EEmeter                        |
| NVIDIA Earth-2                                   | https://www.nvidia.com/en-us/high-performance-computing/earth-2/      | domain-module  | Climate/weather AI platform; infrastructure-scale; not UDT-branded                   | Earth-2                        |

---

## Gap: Niche open-source backbone components

Open-source projects that function as foundational building blocks in UDT stacks but are not marketed as digital twin tools. Models miss these when they focus on end-to-end platforms.

| Name         | Link                                           | Expected Layer | Why tricky                                                                      | Aliases |
| ------------ | ---------------------------------------------- | -------------- | ------------------------------------------------------------------------------- | ------- |
| FROST-Server | https://fraunhoferiosb.github.io/FROST-Server/ | backbone       | OGC SensorThings API implementation; infrastructure component; no UDT marketing |         |
| kepler.gl    | https://kepler.gl                              | backbone       | Geospatial data visualisation; often seen as a data viz library, not UDT        |         |
| deck.gl      | https://deck.gl                                | backbone       | WebGL geospatial rendering; framework-level; not marketed as UDT                |         |
| 3D Tiles     | https://github.com/CesiumGS/3d-tiles           | backbone       | OGC standard for streaming 3D geospatial data; spec/format, not a product       |         |
| 3D BAG       | https://3dbag.nl                               | backbone       | Dutch national 3D building dataset; data product, not a software platform       |         |
