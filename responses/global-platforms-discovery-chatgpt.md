```yaml
model: ChatGPT (gpt-4)
date: 2026-03-29
prompt: platform-discovery
```

## CesiumJS

- **Organization:** CesiumGS
- **Link:** [cesium.com](https://cesium.com)
- **License:** Apache-2.0 — open-source (permissive)【29†L478-L481】
- **Type:** 3D geospatial visualization engine
- **Inclusion criterion:** Adjacent Architecture

- **Technical Architecture (4/5):** A JavaScript/WebGL library (CesiumJS) for 3D globes and maps, built on open standards (glTF, CZML, 3D Tiles) for massive data【29†L427-L432】.
- **Openness & Licensing (5/5):** Fully open-source (Apache-2.0) with no runtime fees【28†L21-L24】【29†L478-L481】. No mandatory SaaS; content sources are optional.
- **City-Scale Capability (4/5):** Scales globally with support for high-precision terrain and 3D city models (buildings, meshes, point clouds) via Cesium ion or third-party sources. Used in many city-scale twins.
- **Maturity & Adoption (5/5):** Mature and production-ready (10+ years), with large deployments (e.g. city planning tools) and an active community【28†L21-L24】.
- **Integration Posture (5/5):** Compliant with OGC/ISO (streams 3D Tiles, WMS/WMTS, etc.); rich API and plugins (Unity/Unreal bridges). Integrates with GIS and IoT.
- **Governance (3/5):** Led by CesiumGS (private company) with open governance. Funded by commercial subscriptions (open-core model) but core runtime is community-driven【29†L478-L481】.

## TwinCity3D

- **Organization:** Geosolutions & Aeronike (Italy)
- **Link:** [twincity3d.com](https://twincity3d.com)
- **License:** (Unspecified open-source) — free to use, no license fee【3†L50-L54】
- **Type:** 3D web GIS / urban digital twin platform
- **Inclusion criterion:** Explicit Urban Digital Twin

- **Technical Architecture (4/5):** Open-source web-GIS stack (based on GeoServer, Cesium, etc.) for city models. Supports OGC services (WFS, WMS, CSW) and integrates a 3D city model (CityGML/3D Tiles) alongside GIS layers【2†L72-L75】【3†L30-L33】.
- **Openness & Licensing (5/5):** Fully open-source (no licensing costs)【3†L50-L54】. Code is openly published (GitHub) and it can be self-hosted.
- **City-Scale Capability (3/5):** Focuses on 3D city model visualization/management and basic GIS analysis; does not natively cover advanced domains like transport or energy. Suitable for city-scale 3D mapping and planning.
- **Maturity & Adoption (3/5):** Production-ready and certified by partners【2†L60-L62】; deployed in demos (e.g. Bologna, Florence). Smaller user base than major GIS vendors.
- **Integration Posture (4/5):** Uses OGC standards (CityGML, WFS/WMS) and WebGIS conventions【2†L72-L75】. Provides REST APIs and web services for interoperability.
- **Governance (4/5):** Jointly maintained by two companies (Geosolutions, Aeronike); driven by consulting projects. Community-driven via GitHub; funding is commercial (EU projects, city contracts).

## Virtual City Systems (VC Map)

- **Organization:** Virtual City Systems GmbH (Germany)
- **Link:** [vc.systems](https://vc.systems)
- **License:** MIT — open-source (VC Map)【32†L27-L31】
- **Type:** Web-based 3D city planning and visualization platform
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (4/5):** Modular web platform built on CesiumJS (WebGL); back-end in Java/.NET. Extensible via plugins (VC Planner, Solar, etc.) for domain-specific analysis.
- **Openness & Licensing (4/5):** Core component (VC Map) released open-source (MIT)【32†L27-L31】. Other tools (Solar, Planner) are partially proprietary or SaaS.
- **City-Scale Capability (4/5):** Designed for municipal planning: renders city models (CityGML) with thematic layers (e.g. infrastructure, sensors) and supports scenario simulation (solar, wind)【32†L39-L42】. Web scale to tens of thousands of buildings.
- **Maturity & Adoption (4/5):** Commercial product with multiple European city deployments (Berlin, Kassel, etc.). Actively developed (10+ years in business). Some modules still evolving.
- **Integration Posture (4/5):** Supports CityGML, 3D Tiles, BIM data import. Offers REST API and GIS integrations (Shapefile, WFS). Founded on open standards (OGC, 3D Tiles) via Cesium【32†L39-L42】.
- **Governance (2/5):** Proprietary company (VC Systems); roadmap driven by business goals. They participate in OGC (3D Tiles standard) but no public consortium; funding through sales and contracts.

## 3D City Database (3DCityDB)

- **Organization:** Virtual City Systems / Fraunhofer IGD / TUM (Germany)
- **Link:** [docs.3dcitydb.org](https://docs.3dcitydb.org/latest/)
- **License:** Apache-2.0 — open-source【54†L379-L381】
- **Type:** 3D spatial database (CityGML data management)
- **Inclusion criterion:** Adjacent Architecture

- **Technical Architecture (4/5):** PostgreSQL/PostGIS database schema with CityGML mappings; includes tools to import/export CityGML (and CityJSON) data. Modular (SQL scripts, Docker, Java utilities).
- **Openness & Licensing (5/5):** Fully open-source (Apache 2.0)【54†L379-L381】, self-hosted. Community editions free; optional paid support by partners.
- **City-Scale Capability (4/5):** Handles entire city models (multi-LOD 3D), including buildings, terrain, utilities. Suited for large municipalities (tested on major cities like New York, Tokyo). Limited simulation functionality (primarily data management/analysis).
- **Maturity & Adoption (4/5):** Production-proven (in use since CityGML v1.0). Version 5 released 2024【54†L379-L381】. Known in academia and industry; multiple forks and Docker images available.
- **Integration Posture (5/5):** Native support for OGC CityGML 3.0/2.0 with ADEs. Provides OGC WFS/CSW via GeoServer integration. Can output 3D Tiles, CityJSON, etc. Strong interoperability.
- **Governance (4/5):** Overseen by a consortium of university and industry (TUM Chair of Geoinfo, Fraunhofer, Virtual City Systems)【54†L499-L508】. Community contributions guided by academic stewardship; EU project funding.

## CityJSON

- **Organization:** CityJSON (community standard, spearheaded by Delft University of Technology, NL)
- **Link:** [cityjson.org](https://www.cityjson.org/)
- **License:** MIT — open-source【49†L289-L292】
- **Type:** Data format for 3D city models (JSON schema)
- **Inclusion criterion:** Adjacent Architecture

- **Technical Architecture (3/5):** JSON encoding of CityGML data model; lightweight schema for buildings, terrain, networks. Provides Python/JavaScript libraries (cjio, citygml-tools). No runtime platform (data format only).
- **Openness & Licensing (5/5):** Fully open (official OGC standard, license MIT【49†L289-L292】). All tools and specs are open-source and community-driven【60†L66-L72】.
- **City-Scale Capability (3/5):** Supports core CityGML city models (buildings, LODs, attributes) at city scale. Lightweight for web apps but lacks certain niche CityGML features.
- **Maturity & Adoption (4/5):** Established (v2.0, OGC standard since 2022【60†L99-L100】). Used in research and some municipal projects (as alternative to CityGML). Community active (news/updates).
- **Integration Posture (5/5):** Directly interoperable with CityGML (bidirectional conversion)【60†L106-L114】. Works with common tools (QGIS, 3DCityDB). APIs available.
- **Governance (3/5):** Not a formal consortium but open governance on GitHub【60†L90-L92】. Maintained by academic/community group; funding mostly academic (no corporate owner).

## City-Scale Digital Twin Framework (CityDigitalTwin)

- **Organization:** University of Iowa (UIHILab) + academic partners (USA/Turkey)
- **Link:** [UIowa Digital Twin](https://hydroinformatics.uiowa.edu/lab/dt/)
- **License:** MIT — open-source【41†L325-L328】
- **Type:** Integrated urban simulation and analytics framework (flood/infrastructure focus)
- **Inclusion criterion:** City-Scale Capabilities

- **Technical Architecture (3/5):** Web-based front-end (CesiumJS for viz) with back-end modules (node.js, Python, PostGIS, sensor APIs). Modular microservices (traffic, hydrology, infrastructure) integrated via APIs【41†L305-L312】.
- **Openness & Licensing (5/5):** Fully open-source (MIT)【41†L325-L328】. Self-hostable and free, with code on GitHub.
- **City-Scale Capability (4/5):** Multi-domain (urban flooding, traffic, utilities) for city-wide risk analysis. Demonstrated on mid-sized cities (e.g. Simav, Turkey). Focus on resilience and disaster modeling.
- **Maturity & Adoption (2/5):** Research prototype (2025). Paper published, small pilot sites. Not a commercial product; one GitHub star.
- **Integration Posture (3/5):** Designed to ingest real-time sensor/GIS data (OGC sensor APIs, PostGIS). Exports to Cesium for 3D viz. Emphasizes open data but integrations are custom.
- **Governance (2/5):** Academic project (UIowa + partners), EU Horizon funding (101070125)【41†L343-L347】. Roadmap tied to research grants. Community-driven via GitHub issues.

## vCity

- **Organization:** Barcelona Supercomputing Center (BSC) Data Viz Group, EU (Spain)
- **Link:** [vcity.tech](https://www.vcity.tech)
- **License:** (Planned open-source) — Horizon-funded project (license TBD)
- **Type:** AI/HPC-driven urban digital twin (policy simulation platform)
- **Inclusion criterion:** Explicit Urban Digital Twin

- **Technical Architecture (3/5):** Cloud/HPC-based platform with modular microservices (data ingestion, analytics, simulation). AI models and high-performance computing (MareNostrum supercomputer) for predictive urban models【18†L81-L84】. Includes web interfaces for planners.
- **Openness & Licensing (3/5):** Aims to be open-source and transparent (EU-funded)【11†L66-L69】. Code not yet published; likely Apache or similar. Functions as SaaS for pilot cities.
- **City-Scale Capability (5/5):** Designed for full city/district scale with multi-domain coverage (mobility, air quality, energy, social factors)【18†L74-L81】【18†L98-L101】. Human-centric (citizen feedback integrated).
- **Maturity & Adoption (2/5):** Under development (2023–2025). Early prototype stage; pilots planned in Barcelona, Viladecans, Kobe. No public release yet.
- **Integration Posture (3/5):** Interacts with municipal open data and standards (CityGML, sensor data). Offers REST APIs for scenarios. Building on existing BSC projects (ASCENDER, EXTRACT)【18†L86-L94】.
- **Governance (4/5):** EU NextGen (Spain) funded project led by BSC【9†L161-L169】. Governance by public consortium (BSC, city councils, private partners). Results expected to be public-domain tools.

| Name                          | Link                                                                     | License          | Type                             | Arch | Open | City | Mature | Integ | Gov | Inclusion Criterion         |
| ----------------------------- | ------------------------------------------------------------------------ | ---------------- | -------------------------------- | ---- | ---- | ---- | ------ | ----- | --- | --------------------------- |
| CesiumJS                      | [cesium.com](https://cesium.com)                                         | Apache-2.0       | 3D visualization engine          | 4    | 5    | 4    | 5      | 5     | 3   | Adjacent Architecture       |
| TwinCity3D                    | [twincity3d.com](https://twincity3d.com)                                 | (open-source)    | 3D web GIS / Digital Twin        | 4    | 5    | 3    | 3      | 4     | 4   | Explicit Urban Digital Twin |
| Virtual City Systems (VC Map) | [vc.systems](https://vc.systems)                                         | MIT              | Web-based 3D city planning       | 4    | 4    | 4    | 4      | 4     | 2   | City-Scale Capabilities     |
| 3D City Database (3DCityDB)   | [docs.3dcitydb.org](https://docs.3dcitydb.org/latest/)                   | Apache-2.0       | 3D CityGML database              | 4    | 5    | 4    | 4      | 5     | 4   | Adjacent Architecture       |
| CityJSON                      | [cityjson.org](https://www.cityjson.org)                                 | MIT              | CityGML JSON data format         | 3    | 5    | 3    | 4      | 5     | 3   | Adjacent Architecture       |
| City-Scale DT Framework       | [hydroinformatics.uiowa.edu](https://hydroinformatics.uiowa.edu/lab/dt/) | MIT              | Flood/infra simulation framework | 3    | 5    | 4    | 2      | 3     | 2   | City-Scale Capabilities     |
| vCity                         | [vcity.tech](https://www.vcity.tech)                                     | (Horizon-funded) | Urban twin simulation platform   | 3    | 3    | 5    | 2      | 3     | 4   | Explicit Urban Digital Twin |

**Sources:** Official project sites, documentation, and published material for each platform【28†L21-L24】【32†L27-L31】【54†L379-L381】【60†L66-L70】【18†L74-L81】【41†L325-L328】.
