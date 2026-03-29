```yaml
model: gpt-4
date: 2026-03-29
prompt: platform-discovery
```

| Name                          | Link                                                                                                                                                                        | License      | Type                                | Arch | Open | City | Mature | Integ | Gov | Inclusion Criterion     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------- | ---- | ---- | ---- | ------ | ----- | --- | ----------------------- |
| Cityzenith SmartWorldPro      | [prnewswire.com](https://www.prnewswire.com/news-releases/cityzeniths-smart-world-pro-digital-twin-software-platform-selected-for-new-capital-city-in-india-300767327.html) | Proprietary  | 3D digital twin platform            | 3    | 1    | 5    | 3      | 3     | 2   | Explicit UDT            |
| Virtual Singapore             | [3ds.com](https://www.3ds.com/insights/customer-stories/virtual-singapore)                                                                                                  | Proprietary  | City-scale digital twin             | 3    | 1    | 5    | 3      | 3     | 4   | Explicit UDT            |
| CesiumJS                      | [cesium.com](https://cesium.com)                                                                                                                                            | Apache-2.0   | 3D geospatial visualization library | 5    | 5    | 5    | 5      | 5     | 4   | Adjacent Architecture   |
| iTwin.js                      | [itwinjs.org](https://www.itwinjs.org/)                                                                                                                                     | MIT          | Infrastructure digital twin library | 4    | 5    | 3    | 4      | 4     | 3   | Adjacent Architecture   |
| 3D City Database              | [3dcitydb-docs.readthedocs.io](https://3dcitydb-docs.readthedocs.io/en/latest/overview/license.html)                                                                        | Apache-2.0   | CityGML 3D model database           | 3    | 5    | 4    | 5      | 4     | 4   | Adjacent Architecture   |
| VC Map (Virtual City Systems) | [github.com/virtualcitySYSTEMS/map-ui](https://github.com/virtualcitySYSTEMS/map-ui)                                                                                        | MIT          | Web-based 3D urban GIS framework    | 4    | 5    | 4    | 4      | 4     | 3   | City-Scale Capabilities |
| Snap4City                     | [snap4city.org](https://www.snap4city.org)                                                                                                                                  | AGPL-3.0     | Smart city digital twin platform    | 4    | 4    | 5    | 3      | 5     | 2   | Explicit UDT            |
| UrbanSim                      | [github.com/UDST/urbansim](https://github.com/UDST/urbansim)                                                                                                                | BSD-3-Clause | Urban planning simulation framework | 3    | 5    | 4    | 3      | 4     | 3   | City-Scale Capabilities |
| Alto Twin (Octave)            | [octave.com](https://www.octave.com/products/geospatial-intelligence/alto/alto-twin)                                                                                        | Proprietary  | Spatial intelligence DT platform    | 3    | 1    | 3    | 5      | 4     | 2   | Explicit UDT            |

## Cityzenith SmartWorldPro

- **Organization:** Cityzenith (Chicago/London)
- **Link:** [cityzenith.com](https://www.prnewswire.com/news-releases/cityzeniths-smart-world-pro-digital-twin-software-platform-selected-for-new-capital-city-in-india-300767327.html)
- **License:** Proprietary (cloud-based SaaS)
- **Type:** Urban-scale 3D digital twin platform
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (3/5):** Built on a Unity-based engine that ingests BIM/GIS data, enabling visualization of large city models (e.g. buildings and infrastructure) in 3D.
- **Openness & Licensing (1/5):** Closed-source commercial platform (software-as-a-service) with no open-source components【62†L551-L554】.
- **City-Scale Capability (5/5):** Designed for whole-city deployment (used for Amaravati smart city) with multi-domain IoT data (traffic, environment, zoning, etc.)【62†L551-L554】.
- **Maturity & Adoption (3/5):** Commercial product (launched ~2018) with high-profile pilot (Amaravati, India)【62†L551-L554】; production-ready but limited to targeted projects.
- **Integration Posture (3/5):** Provides APIs and data import tools for BIM/GIS inputs and supports common formats (though proprietary in core); example usage is integration of real-time city services.
- **Governance (2/5):** Developed and controlled by private company Cityzenith; venture-backed, no open consortium governance.

## Virtual Singapore

- **Organization:** National Research Foundation (Singapore Govt)
- **Link:** [3ds.com – Virtual Singapore](https://www.3ds.com/insights/customer-stories/virtual-singapore)
- **License:** Proprietary (Dassault 3DEXPERIENCity platform)
- **Type:** City-scale digital twin platform
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (3/5):** Built on Dassault Systèmes’ 3DEXPERIENCity platform to integrate a high-resolution 3D city model with IoT and demographic data【64†L15-L18】.
- **Openness & Licensing (1/5):** Closed-source government platform (commercial software); core tech by Dassault (private), though city data is aggregated from public agencies.
- **City-Scale Capability (5/5):** Covers all of Singapore with fine-grained detail (buildings, infrastructure, population movement, environment) to enable multi-domain simulations【64†L15-L18】.
- **Maturity & Adoption (3/5):** Active national project (since ~2017) used by government agencies; pilot deployments (e.g. test beds) exist but system is not publicly distributed.
- **Integration Posture (3/5):** Uses open standards (CityGML, 3D geodata), and ingests diverse legacy and real-time data; access is via proprietary APIs under government control【64†L15-L18】.
- **Governance (4/5):** Led by Singapore government (NRF/Smart Nation) with private partner (Dassault); centralized roadmap set by public agencies.

## CesiumJS

- **Organization:** CesiumGS (Analytical Graphics Inc)
- **Link:** [cesium.com](https://cesium.com)
- **License:** Apache-2.0 — open-source
- **Type:** 3D geospatial visualization library
- **Inclusion criterion:** Adjacent Architecture or Governance

- **Technical Architecture (5/5):** WebGL-based JavaScript library supporting 3D Tiles, glTF, and other open formats for streaming large-scale 3D city data【20†L21-L28】.
- **Openness & Licensing (5/5):** Fully open-source (Apache 2.0) with no mandatory SaaS; the CesiumJS core is free to use or self-host【20†L43-L46】.
- **City-Scale Capability (5/5):** Designed for global city-scale visualization (buildings, terrain, imagery) and used in smart city projects and urban analytics【20†L15-L18】.
- **Maturity & Adoption (5/5):** Mature, production-ready library with wide adoption (industry, government, research); active development and large user community.
- **Integration Posture (5/5):** Supports open standards (3D Tiles, CZML, KML/GeoJSON, OGC services) and provides rich APIs, enabling interoperability in UDT systems【20†L21-L28】.
- **Governance (4/5):** Led by CesiumGS with open governance; community contributions are welcomed, and development roadmaps are transparent.

## iTwin.js

- **Organization:** Bentley Systems (iTwin platform team)
- **Link:** [itwinjs.org](https://www.itwinjs.org/)
- **License:** MIT — open-source
- **Type:** Infrastructure digital twin library/framework
- **Inclusion criterion:** Adjacent Architecture or Governance

- **Technical Architecture (4/5):** TypeScript/JavaScript monorepo designed to aggregate BIM, CAD, GIS, and IoT data for infrastructure digital twins【66†L14-L23】.
- **Openness & Licensing (5/5):** Open-source (MIT) with no SaaS requirement for core library; Bentley’s cloud services are optional (iModelHub)【66†L14-L23】.
- **City-Scale Capability (3/5):** Focused on building/infrastructure assets (bridges, buildings, utilities) rather than entire cities; applicable to urban projects within Bentley’s ecosystem.
- **Maturity & Adoption (4/5):** Production-ready; used in Bentley’s infrastructure projects (e.g. YII awards) and has an active developer ecosystem and enterprise backing.
- **Integration Posture (4/5):** Rich interoperability (supports OpenBIM/IFC, iModel formats, REST/GraphQL APIs) and integrates with engineering and GIS data.
- **Governance (3/5):** Governance by Bentley (open-source but company-driven); roadmaps set by Bentley with community input.

## 3D City Database

- **Organization:** 3DCityDB Team (TUM / Virtual City Systems)
- **Link:** [3dcitydb-docs.readthedocs.io](https://3dcitydb-docs.readthedocs.io/en/latest/overview/license.html)
- **License:** Apache-2.0 — open-source
- **Type:** CityGML 3D city model database
- **Inclusion criterion:** Adjacent Architecture or Governance

- **Technical Architecture (3/5):** Relational DB schema and tools for storing/analyzing CityGML city models (buildings, terrain, etc.) on PostGIS/Oracle【68†L39-L42】.
- **Openness & Licensing (5/5):** Fully open-source (Apache 2.0) implementation of the CityGML standard【68†L39-L42】; free to use with no licensing fees.
- **City-Scale Capability (4/5):** Designed for large-scale urban 3D data (multi-LOD city models); used by cities to manage municipal building and terrain data.
- **Maturity & Adoption (5/5):** Established (over a decade); widely adopted in industry and academia (Hamburg, Helsinki, Singapore, etc.)【68†L39-L42】.
- **Integration Posture (4/5):** Implements CityGML 3.0 fully; supports WFS and CityJSON import/export; often integrated with GIS platforms.
- **Governance (4/5):** Open development by university consortium (TUM, etc.) and Virtual City Systems; community-driven with formal releases.

## VC Map (Virtual City Systems)

- **Organization:** Virtual City Systems (Germany)
- **Link:** [github.com/virtualcitySYSTEMS/map-ui](https://github.com/virtualcitySYSTEMS/map-ui)
- **License:** MIT — open-source
- **Type:** Web-based 3D urban GIS framework
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (4/5):** JavaScript framework using Vue.js, OpenLayers, and Cesium to render synchronized 2D/3D/oblique city views in the browser【70†L354-L362】.
- **Openness & Licensing (5/5):** Open-source (MIT); fully free and self-hostable, with all code available on GitHub【70†L354-L362】.
- **City-Scale Capability (4/5):** Built for interactive exploration and analysis of full-city 3D models (buildings, point clouds, terrain) in the browser【70†L354-L362】.
- **Maturity & Adoption (4/5):** Actively developed (900+ commits) and used by European cities (e.g. Rostock); supported by Virtual City Systems.
- **Integration Posture (4/5):** Supports OGC standards and formats (CityGML, CityJSON, 3D Tiles); provides plugin API for extensions【70†L354-L362】.
- **Governance (3/5):** Company-managed (Virtual City Systems) but open to contributions; commercial support available.

## Snap4City

- **Organization:** DISIT Lab, University of Florence
- **Link:** [snap4city.org](https://www.snap4city.org)
- **License:** AGPL-3.0 — open-source
- **Type:** Smart city digital twin and analytics platform
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (4/5):** Microservice-based IoT/GIS platform using Apache NiFi, Node-RED, and containerized components for city data ingestion and analytics.
- **Openness & Licensing (4/5):** Fully open-source (AGPL-3.0) with all code on GitHub; self-hostable without licensing fees【72†L59-L63】.
- **City-Scale Capability (5/5):** Designed for large-scale urban deployments; manages data for dozens of European cities (flows for sensors, dashboards, etc.)【72†L59-L63】.
- **Maturity & Adoption (3/5):** Research-driven but operational; used in multiple smart city pilots (Firenze, Helsinki, etc.); moderate adoption.
- **Integration Posture (5/5):** Interfaces with FIWARE and IoT standards (MQTT, NGSI-LD) and provides public APIs; strong support for open data and interoperability.
- **Governance (2/5):** Developed by university lab (DISIT) with EU project funding; open collaboration but no formal consortium.

## UrbanSim

- **Organization:** Urban Data Science Toolkit (UDST, nonprofit)
- **Link:** [github.com/UDST/urbansim](https://github.com/UDST/urbansim)
- **License:** BSD-3-Clause — open-source
- **Type:** Urban planning and simulation framework
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (3/5):** Python library (with Orca orchestration) offering modular components for land-use, housing, and transportation modeling of cities/regions【75†L284-L292】.
- **Openness & Licensing (5/5):** BSD open-source; core code freely available for research and planning applications【75†L278-L283】.
- **City-Scale Capability (4/5):** Models broad city/regional dynamics (development, demographics, travel demand); used to simulate urban policies at scale.
- **Maturity & Adoption (3/5):** Established research tool; applied by public agencies and academics in dozens of cities worldwide【75†L302-L305】.
- **Integration Posture (4/5):** Works with GIS and transport libraries (via Orca, Pandana, Synthpop); input data often drawn from standard urban datasets.
- **Governance (3/5):** Community-driven (UDST nonprofit); contributions by academics and practitioners, with periodic releases.

## Alto Twin (Octave)

- **Organization:** Octave (Hexagon)
- **Link:** [octave.com](https://www.octave.com/products/geospatial-intelligence/alto/alto-twin)
- **License:** Proprietary
- **Type:** Industrial/spatial intelligence digital twin platform
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (3/5):** Enterprise spatial platform combining GIS, BIM/CAD, and real-time IoT streams to create a 3D operational twin; GPU-accelerated 2D/3D rendering【77†L80-L87】.
- **Openness & Licensing (1/5):** Closed-source proprietary software (site-licensed, subscription model)【77†L206-L209】.
- **City-Scale Capability (3/5):** Targets complex facilities (industrial plants, airports, hospitals) but also used in urban projects (e.g. City of Genoa case); merges infrastructure data into a single view【77†L178-L184】.
- **Maturity & Adoption (5/5):** Mature commercial product (formerly HxGN Smart Sites); deployed globally in enterprise and public sectors.
- **Integration Posture (4/5):** Connects to enterprise systems, GIS, sensors, and CAD/BIM via built-in connectors; supports open data inputs (e.g. point clouds, GIS layers).
- **Governance (2/5):** Controlled by Octave/Hexagon (corporate roadmap); development driven by market demands.
