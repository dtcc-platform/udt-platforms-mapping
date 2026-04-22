```yaml
model: GPT-5.4 Thinking
date: 2026-04-21
prompt: platform-discovery
```

| Name                | Link                                                                                                                                                        | Layer         | Reason                    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------- |
| DTCC                | [dtcc.chalmers.se](https://www.dtcc.chalmers.se/)                                                                                                           | core-platform |                           |
| Virtual Singapore   | [smartnation.gov.sg](https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/)                                                        | core-platform |                           |
| 3DEXPERIENCity      | [3ds.com](https://www.3ds.com/virtual-twin/infrastructure-cities)                                                                                           | core-platform |                           |
| Virtual Gothenburg  | [goteborg.se](https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/in-english-about-gothenburgs-digital-twin) | core-platform |                           |
| Cesium              | [cesium.com](https://cesium.com/platform/)                                                                                                                  | backbone      |                           |
| iTwin Platform      | [developer.bentley.com](https://developer.bentley.com/)                                                                                                     | backbone      |                           |
| FIWARE              | [fiware.org](https://www.fiware.org/)                                                                                                                       | backbone      |                           |
| 3DCityDB            | [3dcitydb.org](https://www.3dcitydb.org/)                                                                                                                   | backbone      |                           |
| ArcGIS Urban        | [esri.com](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)                                                                                | domain-module |                           |
| MATSim              | [matsim.org](https://matsim.org/)                                                                                                                           | domain-module |                           |
| UrbanSim            | [udst.github.io](https://udst.github.io/urbansim/)                                                                                                          | domain-module |                           |
| City Energy Analyst | [cityenergyanalyst.com](https://www.cityenergyanalyst.com/)                                                                                                 | domain-module |                           |
| ENVI-met            | [envi-met.com](https://envi-met.com/)                                                                                                                       | domain-module |                           |
| A/B Street          | [abstreet.uk](https://abstreet.uk/)                                                                                                                         | domain-module |                           |
| GeoDatalytics       | [github.com/OpenGeoscience/geodatalytics](https://github.com/OpenGeoscience/geodatalytics)                                                                  | domain-module |                           |
| Azure Digital Twins | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/digital-twins/overview)                                                                       | excluded      | general-purpose twin PaaS |
| Unreal Engine       | [unrealengine.com](https://www.unrealengine.com/digital-twins)                                                                                              | excluded      | general-purpose 3D engine |

## DTCC

- **Organization:** [Digital Twin Cities Centre](https://www.dtcc.chalmers.se/) / Chalmers University of Technology
- **Link:** [DTCC Platform](https://www.dtcc.chalmers.se/)
- **License:** MIT — open-source ([GitHub](https://github.com/dtcc-platform/dtcc))
- **Type:** Open-source environment for creating, simulating, and visualizing digital twins of cities ([DTCC](https://www.dtcc.chalmers.se/))
- **Layer:** core-platform

## Virtual Singapore

- **Organization:** [Government of Singapore](https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/) with [Singapore Land Authority](https://www.sla.gov.sg/geospatial/)
- **Link:** [Virtual Singapore](https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/)
- **License:** unknown
- **Type:** National city-scale digital twin and collaborative 3D platform for simulation and planning ([Virtual Singapore](https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/))
- **Layer:** core-platform

## 3DEXPERIENCity

- **Organization:** [Dassault Systèmes](https://www.3ds.com/)
- **Link:** [Infrastructure & Cities](https://www.3ds.com/virtual-twin/infrastructure-cities)
- **License:** proprietary — commercial ([3DEXPERIENCE terms](https://www.3ds.com/terms/software-terms))
- **Type:** City virtual twin platform combining 3D modeling, collaboration, and simulation for infrastructure and cities ([Infrastructure & Cities](https://www.3ds.com/virtual-twin/infrastructure-cities))
- **Layer:** core-platform

## Virtual Gothenburg

- **Organization:** [City of Gothenburg, City Planning Authority](https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/in-english-about-gothenburgs-digital-twin)
- **Link:** [Virtual Gothenburg](https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/in-english-about-gothenburgs-digital-twin)
- **License:** unknown
- **Type:** Municipal digital twin of the whole city for visualization, real-time control, and simulated future scenarios ([Gothenburg](https://goteborg.se/wps/portal/start/goteborg-vaxer/sa-planeras-staden/goteborgs-digitala-tvilling/in-english-about-gothenburgs-digital-twin))
- **Layer:** core-platform

## Cesium

- **Organization:** [Cesium GS, Inc.](https://cesium.com/)
- **Link:** [Cesium Platform](https://cesium.com/platform/)
- **License:** Apache-2.0 — open-source core for CesiumJS; proprietary commercial cloud services for Cesium ion ([Cesium Platform](https://cesium.com/platform/), [CesiumJS](https://cesium.com/platform/cesiumjs/))
- **Type:** 3D geospatial platform and streaming/visualization foundation for building applications ([Cesium Platform](https://cesium.com/platform/))
- **Layer:** backbone

## iTwin Platform

- **Organization:** [Bentley Systems](https://www.bentley.com/)
- **Link:** [iTwin Platform](https://developer.bentley.com/)
- **License:** proprietary — commercial ([Developer Terms](https://developer.bentley.com/terms-of-service/), [Pricing](https://developer.bentley.com/pricing/))
- **Type:** API and services platform for building digital twin applications from engineering, reality, and sensor data ([iTwin Platform](https://developer.bentley.com/))
- **Layer:** backbone

## FIWARE

- **Organization:** [FIWARE Foundation e.V.](https://www.fiware.org/)
- **Link:** [FIWARE](https://www.fiware.org/)
- **License:** AGPL-3.0 for Orion-LD context broker — open-source ([Orion-LD](https://github.com/fiware/context.orion-ld))
- **Type:** Open standards-based context data management framework centered on a context broker for interoperable smart-city systems ([FIWARE](https://www.fiware.org/), [Orion-LD](https://github.com/fiware/context.orion-ld))
- **Layer:** backbone

## 3DCityDB

- **Organization:** [3DCityDB Team](https://3dcitydb-docs.readthedocs.io/en/latest/)
- **Link:** [3DCityDB](https://www.3dcitydb.org/)
- **License:** Apache-2.0 — open-source ([License](https://3dcitydb-docs.readthedocs.io/en/latest/overview/license.html))
- **Type:** CityGML-based 3D city database and toolkit for storing, managing, and exporting semantic city models ([GitHub](https://github.com/3dcitydb/3dcitydb))
- **Layer:** backbone

## ArcGIS Urban

- **Organization:** [Esri](https://www.esri.com/)
- **Link:** [ArcGIS Urban](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)
- **License:** proprietary — commercial ([Trial](https://www.esri.com/en-us/arcgis/products/arcgis-urban/trial), [Licensing](https://doc.arcgis.com/en/urban/latest/get-started/get-started-setting-up.htm))
- **Type:** Web-based 3D urban planning and scenario analysis solution for zoning, land use, and development projects ([ArcGIS Urban](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview))
- **Layer:** domain-module

## MATSim

- **Organization:** [MATSim Association](https://matsim.org/association/)
- **Link:** [MATSim](https://matsim.org/)
- **License:** unknown
- **Type:** Open-source framework for large-scale agent-based transport simulation ([MATSim](https://matsim.org/))
- **Layer:** domain-module

## UrbanSim

- **Organization:** [Urban Data Science Toolkit (UDST)](https://docs.udst.org/)
- **Link:** [UrbanSim](https://udst.github.io/urbansim/)
- **License:** BSD-3-Clause — open-source ([GitHub](https://github.com/UDST/urbansim))
- **Type:** Platform for statistical simulation of cities and regions, including land use, development, and demographics ([GitHub](https://github.com/UDST/urbansim))
- **Layer:** domain-module

## City Energy Analyst

- **Organization:** [Architecture and Building Systems](https://github.com/architecture-building-systems), ETH Zurich
- **Link:** [City Energy Analyst](https://www.cityenergyanalyst.com/)
- **License:** MIT — open-source ([GitHub](https://github.com/architecture-building-systems/CityEnergyAnalyst))
- **Type:** Urban building energy simulation platform for low-carbon city and district energy planning ([GitHub](https://github.com/architecture-building-systems/CityEnergyAnalyst))
- **Layer:** domain-module

## ENVI-met

- **Organization:** [ENVI-met GmbH](https://envi-met.com/)
- **Link:** [ENVI-met](https://envi-met.com/)
- **License:** proprietary — commercial ([Pricing](https://envi-met.com/pricing/))
- **Type:** High-resolution 3D urban microclimate modeling software for climate-adaptive planning ([ENVI-met](https://envi-met.com/))
- **Layer:** domain-module

## A/B Street

- **Organization:** [A/B Street project](https://github.com/a-b-street)
- **Link:** [A/B Street](https://abstreet.uk/)
- **License:** Apache-2.0 — open-source ([GitHub](https://github.com/a-b-street/abstreet))
- **Type:** Transportation planning and traffic simulation software focused on walking, biking, transit, and street redesign scenarios ([GitHub](https://github.com/a-b-street/abstreet))
- **Layer:** domain-module

## GeoDatalytics

- **Organization:** [Kitware Inc.](https://www.kitware.com/) in collaboration with [Northeastern University Sustainability and Data Sciences Lab](https://sdslab.io/)
- **Link:** [GeoDatalytics](https://github.com/OpenGeoscience/geodatalytics)
- **License:** Apache-2.0 — open-source ([GitHub](https://github.com/OpenGeoscience/geodatalytics))
- **Type:** Urban visualization and data analysis toolkit for resilience, climate risk, and infrastructure impacts ([GitHub](https://github.com/OpenGeoscience/geodatalytics))
- **Layer:** domain-module

## Azure Digital Twins

- **Organization:** [Microsoft](https://www.microsoft.com/)
- **Link:** [Azure Digital Twins](https://learn.microsoft.com/en-us/azure/digital-twins/overview)
- **License:** proprietary — commercial
- **Type:** Digital twin platform as a service for modeling connected environments ([Azure Digital Twins](https://learn.microsoft.com/en-us/azure/digital-twins/overview))
- **Layer:** excluded
- **Reason:** General-purpose digital twin cloud service rather than an urban-specific platform or urban backbone.

## Unreal Engine

- **Organization:** [Epic Games](https://www.epicgames.com/)
- **Link:** [Unreal Engine digital twins](https://www.unrealengine.com/digital-twins)
- **License:** proprietary — commercial ([License](https://www.unrealengine.com/eula/unreal))
- **Type:** Real-time 3D engine used in digital twin visualization workflows ([Digital Twins](https://www.unrealengine.com/digital-twins))
- **Layer:** excluded
- **Reason:** General-purpose 3D engine that can be used in urban twins but is not itself an urban digital twin platform or urban-specialized backbone.
