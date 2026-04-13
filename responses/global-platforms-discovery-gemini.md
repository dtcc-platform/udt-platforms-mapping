```yaml
model: Gemini 3 Flash (2026-04-13)
date: 2026-04-13
prompt: platform-discovery
```

| Name              | Link                                                                          | License         | Type                 | Arch | Open | City | Mature | Integ | Gov | Criterion                           |
| ----------------- | ----------------------------------------------------------------------------- | --------------- | -------------------- | ---- | ---- | ---- | ------ | ----- | --- | ----------------------------------- |
| Cesium            | [cesium.com](https://cesium.com)                                              | Apache-2.0      | Visualization engine | 5    | 5    | 5    | 5      | 5     | 4   | Adjacent Architecture or Governance |
| Bentley iTwin     | [bentley.com](https://www.bentley.com/software/itwin/)                        | MIT (open-core) | Infrastructure DT    | 5    | 4    | 5    | 5      | 4     | 3   | Explicit UDT                        |
| 3DCityDB          | [3dcitydb.org](https://www.3dcitydb.org/)                                     | Apache-2.0      | Geospatial database  | 4    | 5    | 4    | 5      | 5     | 4   | Adjacent Architecture or Governance |
| VC Map            | [vc.systems](https://vc.systems/en/solutions/vc-map/)                         | LGPL-3.0        | Web-based 3D GIS     | 4    | 5    | 4    | 4      | 4     | 2   | Explicit UDT                        |
| TerriaJS          | [terria.io](https://terria.io/)                                               | Apache-2.0      | Geospatial platform  | 4    | 5    | 5    | 5      | 4     | 4   | City-Scale Capabilities             |
| Esri ArcGIS Urban | [esri.com](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)  | Proprietary     | Urban planning DT    | 4    | 1    | 5    | 5      | 3     | 2   | Explicit UDT                        |
| SuperMap          | [supermap.com](https://www.supermap.com/en-us/)                               | Proprietary     | 3D GIS platform      | 4    | 1    | 5    | 5      | 4     | 2   | Explicit UDT                        |
| NVIDIA Omniverse  | [nvidia.com](https://www.nvidia.com/en-us/omniverse/solutions/digital-twins/) | Proprietary     | Simulation engine    | 5    | 2    | 4    | 3      | 4     | 2   | City-Scale Capabilities             |
| SUMO              | [eclipse.dev/sumo/](https://eclipse.dev/sumo/)                                | EPL-2.0         | Transport simulation | -1   | -1   | -1   | -1     | -1    | -1  | Single Domain                       |
| CityGML           | [ogc.org](https://www.ogc.org/standard/citygml/)                              | OGC License     | Data standard        | -1   | -1   | -1   | -1     | -1    | -1  | Spec or Standard                    |

## Cesium

- **Organization:** Cesium GS, Inc. ([About](https://cesium.com/about/))
- **Link:** [cesium.com](https://cesium.com)
- **License:** Apache-2.0 — open-source ([Repository](https://github.com/CesiumGS/cesium/blob/main/LICENSE.md))
- **Type:** 3D geospatial visualization engine ([Product](https://cesium.com/platform/cesiumjs/))
- **Inclusion criterion:** Adjacent Architecture or Governance

- **Technical Architecture (5/5):** Built on the 3D Tiles OGC community standard and a WebGL-based engine for high-performance rendering of massive datasets ([Architecture](https://cesium.com/platform/3d-tiles/)).
- **Openness & Licensing (5/5):** The core CesiumJS library is Apache-2.0, allowing for extensive modification and self-hosting without mandatory SaaS ties ([License](https://github.com/CesiumGS/cesium/blob/main/LICENSE.md)).
- **City-Scale Capability (5/5):** Specifically designed for global-scale terrain and city-scale 3D building data using hierarchical level-of-detail ([Capabilities](https://cesium.com/blog/2023/10/05/cesium-for-digital-twins/)).
- **Maturity & Adoption (5/5):** Highly mature with millions of downloads and mission-critical use cases in aerospace, urban planning, and defense ([Community](https://cesium.com/community/)).
- **Integration Posture (5/5):** Leading advocate for OGC standards and creator of 3D Tiles, with extensive APIs for data integration ([Interoperability](https://cesium.com/standards/)).
- **Governance (4/5):** Managed by a private entity but heavily integrated into the OGC standards process and open-source community ([OGC Partnership](https://www.ogc.org/blog/4862/)).

## Bentley iTwin

- **Organization:** Bentley Systems ([About](https://www.bentley.com/company/))
- **Link:** [bentley.com](https://www.bentley.com/software/itwin/)
- **License:** MIT — open-core ([Repository](https://github.com/iTwin/itwinjs-core/blob/master/LICENSE.md))
- **Type:** Infrastructure digital twin platform ([Product](https://www.bentley.com/software/itwin/))
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (5/5):** Uses a distributed "iModel" format that synchronizes changes from multiple BIM and GIS sources into a single unified schema ([iTwinJS Docs](https://www.itwinjs.org/learning/)).
- **Openness & Licensing (4/5):** The core client-side library (iTwin.js) is MIT licensed, though backend services and advanced synchronization require proprietary Bentley subscriptions ([License](https://github.com/iTwin/itwinjs-core)).
- **City-Scale Capability (5/5):** Optimized for large-scale infrastructure including transit networks, utility systems, and large urban districts ([Urban Applications](https://www.bentley.com/software/opencities/)).
- **Maturity & Adoption (5/5):** Widely used in professional engineering and city management, notably in the Digital Twin Victoria project ([Projects](https://www.bentley.com/software/itwin/)).
- **Integration Posture (4/5):** Strong support for IFC, LandXML, and various BIM formats through automated data "bridges" ([Integration](https://www.itwinjs.org/learning/bridges/)).
- **Governance (3/5):** Roadmap and core infrastructure are controlled by Bentley Systems, a publicly traded corporation ([Corporate](https://investors.bentley.com/)).

## 3DCityDB

- **Organization:** Technical University of Munich / 3DCityDB Project ([Project](https://www.3dcitydb.org/3dcitydb/the-project/))
- **Link:** [3dcitydb.org](https://www.3dcitydb.org/)
- **License:** Apache-2.0 — open-source ([Repository](https://github.com/3dcitydb/3dcitydb/blob/master/LICENSE.txt))
- **Type:** Geospatial database for CityGML ([Documentation](https://3dcitydb-docs.readthedocs.io/en/latest/))
- **Inclusion criterion:** Adjacent Architecture or Governance

- **Technical Architecture (4/5):** A semantic database schema implemented on Oracle or PostgreSQL/PostGIS for managing and storing virtual 3D city models ([Tech Overview](https://www.3dcitydb.org/3dcitydb/the-software/)).
- **Openness & Licensing (5/5):** Fully open-source under Apache-2.0, with no proprietary lock-in or licensing fees ([License](https://github.com/3dcitydb/3dcitydb)).
- **City-Scale Capability (4/5):** Designed specifically to store CityGML datasets at the scale of entire metropolitan areas ([Capabilities](https://www.3dcitydb.org/3dcitydb/features/)).
- **Maturity & Adoption (5/5):** Used as the backbone for major city digital twins including Berlin, Singapore, and Rotterdam ([References](https://www.3dcitydb.org/3dcitydb/references/)).
- **Integration Posture (5/5):** Deep integration with OGC standards, including native support for CityGML 2.0 and 3.0 and exports to 3D Tiles ([Interoperability](https://3dcitydb-docs.readthedocs.io/en/latest/plugins/wfs.html)).
- **Governance (4/5):** Academic and community-led governance with stable support from the Technical University of Munich and industry partners ([Governance](https://www.3dcitydb.org/3dcitydb/the-project/)).

## VC Map

- **Organization:** virtualcitysystems GmbH ([About](https://vc.systems/en/about-us/))
- **Link:** [vc.systems](https://vc.systems/en/solutions/vc-map/)
- **License:** LGPL-3.0 — open-source core ([Repository](https://github.com/virtualcitysystems/vcm-core-v4/blob/main/LICENSE))
- **Type:** Web-based 3D GIS and digital twin platform ([Product](https://vc.systems/en/solutions/vc-map/))
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (4/5):** Modular JavaScript framework that integrates Cesium, OpenLayers, and specialized urban data handling for 3D/2D visualization ([Architecture](https://vc.systems/en/technology/vc-map/)).
- **Openness & Licensing (5/5):** The "VCM Core" is available under LGPL-3.0, enabling public and private entities to build open city platforms ([License](https://github.com/virtualcitysystems/vcm-core-v4)).
- **City-Scale Capability (4/5):** Focuses on urban planning, energy simulation, and building-level detail within a city-wide context ([Use Cases](https://vc.systems/en/solutions/digital-urban-twins/)).
- **Maturity & Adoption (4/5):** Production-ready and deployed in several German cities, such as Cologne and Hamburg ([Projects](https://vc.systems/en/references/)).
- **Integration Posture (4/5):** Native support for CityGML and OGC services (WMS, WFS) with built-in tools for urban data analysis ([Standards](https://vc.systems/en/technology/)).
- **Governance (2/5):** Owned and directed by virtualcitysystems (now part of Dassault Systèmes), though the core remains open-source ([Corporate](https://www.3ds.com/newsroom/press-releases/dassault-systemes-acquires-virtualcitysystems)).

## TerriaJS

- **Organization:** Terria / Digital Science at CSIRO ([About](https://terria.io/about/))
- **Link:** [terria.io](https://terria.io/)
- **License:** Apache-2.0 — open-source ([Repository](https://github.com/TerriaJS/terriajs/blob/main/LICENSE))
- **Type:** Spatial data visualization platform ([Product](https://terria.io/products/terriajs/))
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (4/5):** A library for building web-based geospatial catalogs with a powerful data-driven cataloging engine ([Architecture](https://terria.io/products/terriajs/)).
- **Openness & Licensing (5/5):** Permissive Apache-2.0 license with a transparent development process on GitHub ([License](https://github.com/TerriaJS/terriajs)).
- **City-Scale Capability (5/5):** Proven at state and city scales, managing thousands of layers including real-time IoT and 3D urban models ([Capabilities](https://terria.io/projects/)).
- **Maturity & Adoption (5/5):** Exceptionally mature, serving as the engine for Australia's Digital Twin Victoria and NSW Spatial Digital Twin ([Deployment](https://terria.io/projects/nsw-spatial-digital-twin/)).
- **Integration Posture (4/5):** Supports a vast array of protocols including CKAN, WMS, WFS, and 3D Tiles without requiring data conversion ([Interoperability](https://terria.io/products/terriajs/)).
- **Governance (4/5):** Developed by Data61 (CSIRO), Australia's national science agency, ensuring long-term public sector alignment ([Governance](https://terria.io/about/)).

## SuperMap

- **Organization:** SuperMap Software Co., Ltd. ([Company](https://www.supermap.com/en-us/about/profile.html))
- **Link:** [supermap.com](https://www.supermap.com/en-us/)
- **License:** Proprietary — commercial ([Legal](https://www.supermap.com/en-us/support/service.html))
- **Type:** Full-stack 3D GIS and CIM platform ([Product](https://www.supermap.com/en-us/product/SuperMapGIS.html))
- **Inclusion criterion:** Explicit UDT

- **Technical Architecture (4/5):** Distributed GIS architecture with high-concurrency support and native integration for BIM, oblique photography, and point clouds ([Architecture](https://www.supermap.com/en-us/product/SuperMapGIS.html)).
- **Openness & Licensing (1/5):** Closed-source proprietary software, though they maintain some open data specifications like S3M ([Data Format](http://www.s3m.org.cn/)).
- **City-Scale Capability (5/5):** Dominant in Asian markets for City Information Modeling (CIM) and massive urban management systems ([Capabilities](https://www.supermap.com/en-us/solution/SmartCity.html)).
- **Maturity & Adoption (5/5):** Massive deployment base in China and Southeast Asia for smart city and digital twin initiatives ([References](https://www.supermap.com/en-us/news/?TypeID=44)).
- **Integration Posture (4/5):** Supports OGC standards and specialized integrations for industrial IoT and urban sensors ([Interoperability](https://www.supermap.com/en-us/product/SuperMapGIS.html)).
- **Governance (2/5):** Managed by a large commercial entity with roadmap control centralized in Beijing ([Governance](https://www.supermap.com/en-us/about/profile.html)).

## NVIDIA Omniverse

- **Organization:** NVIDIA Corporation ([About](https://www.nvidia.com/en-us/about-nvidia/))
- **Link:** [nvidia.com](https://www.nvidia.com/en-us/omniverse/solutions/digital-twins/)
- **License:** Proprietary — commercial ([License](https://www.nvidia.com/en-us/omniverse/license/))
- **Type:** Real-time 3D simulation and collaboration platform ([Product](https://www.nvidia.com/en-us/omniverse/))
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (5/5):** Built on Pixar’s Universal Scene Description (USD) for high-fidelity physics-based simulation and multi-user collaboration ([Architecture](https://docs.omniverse.nvidia.com/)).
- **Openness & Licensing (2/5):** While the USD format is open, the Omniverse platform and RTX rendering technology are proprietary and hardware-dependent ([License](https://www.nvidia.com/en-us/omniverse/license/)).
- **City-Scale Capability (4/5):** Capable of simulating complex urban environments, including autonomous vehicle testing and climate modeling at city scales ([Digital Twin Solutions](https://www.nvidia.com/en-us/omniverse/solutions/digital-twins/)).
- **Maturity & Adoption (3/5):** Rapidly growing in the industrial sector but still evolving its specific urban/geospatial toolsets compared to traditional GIS ([Maturity](https://blogs.nvidia.com/blog/2023/03/21/industrial-digital-twins-omniverse/)).
- **Integration Posture (4/5):** Strong integration with CAD and BIM tools via USD, though geospatial standard support (like CityGML) is often handled through third-party extensions ([Interoperability](https://docs.omniverse.nvidia.com/connect/latest/index.html)).
- **Governance (2/5):** Strictly controlled by NVIDIA, driven by their hardware ecosystem and AI roadmap ([Corporate](https://www.nvidia.com/en-us/)).
