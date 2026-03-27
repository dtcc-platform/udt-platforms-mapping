# Platform Discovery Scope

This document operationalises the inclusion boundary for the UDT platform review. It translates the normative criteria in [`docs/methodology.md`](methodology.md) into concrete research guidance, provides explicit exclusion examples to calibrate the boundary, seeds the platform list with known qualifiers, and sets a target corpus size.

**Normative reference:** [`docs/methodology.md`](methodology.md) — the inclusion criteria defined there are authoritative. This document is a working aid, not a replacement.

---

## Inclusion Criteria (Operational)

A platform qualifies if it satisfies **at least one** of the following, evidenced by primary sources (official site, repository, published paper):

### 1. Explicit Urban Digital Twin

**Qualifies if:** The platform's own official documentation, product page, or repository description uses the term "digital twin" in an urban or city-scale context.

**Sufficient evidence:** One of — product page headline, repository README, official paper abstract, or press release from the platform's own organisation.

**Does not qualify on:** Third-party descriptions, analyst reports, or general-purpose platforms that _could_ be used as a UDT without being positioned as one.

### 2. City-Scale Capabilities

**Qualifies if:** The platform is purpose-built for one or more of: city-scale 3D visualisation, urban simulation, large-scale geospatial data management, or multi-domain urban analytics (buildings, transport, energy, climate, utilities).

**Sufficient evidence:** Feature documentation or published use cases demonstrating city-scale deployment (not just single-building or campus-scale).

**Does not qualify on:** Generic GIS tools, single-domain analytics platforms, or building-level BIM tools without demonstrated city-scale deployment.

### 3. Adjacent Architecture or Governance

**Qualifies if:** The platform is a foundational technical building block that is directly and commonly integrated into UDT systems — e.g., open standards implementations (CityGML, IFC, OGC API), enabling 3D visualisation engines with urban extensions, or infrastructure digital twin frameworks.

**Sufficient evidence:** Published integrations with known UDT platforms, or explicit positioning as UDT infrastructure in official documentation.

**Does not qualify on:** Standards bodies, specification documents, or frameworks whose primary use case is not UDT (e.g., general IoT platforms, ERP systems, cloud infrastructure).

---

## Explicit Exclusions

The following categories and named examples are **out of scope** under the moderate inclusion boundary:

| Platform / Category                     | Reason excluded                                                                                                             |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **AWS IoT / Azure IoT Hub**             | Generic IoT platform; no city-scale spatial or 3D capability; not positioned as UDT infrastructure                          |
| **SUMO (Simulation of Urban MObility)** | Single-domain transport simulation tool; does not cover the multi-domain scope of a UDT                                     |
| **OpenStreetMap**                       | Geospatial data source / community project; not a platform for building or operating digital twins                          |
| **FIWARE NGSI-LD standard**             | A specification / standard, not a platform; the FIWARE Orion Context Broker (platform) may qualify separately               |
| **Esri ArcGIS**                         | General-purpose GIS; city-scale capable but not positioned as a UDT platform; would require explicit UDT framing to qualify |
| **IOTA / Helium**                       | Distributed IoT networks; no urban spatial or simulation capability                                                         |
| **CityGML standard**                    | A data model standard (OGC), not a platform; implementations (e.g., 3D City DB) may qualify                                 |

> **Borderline cases:** If a platform is adjacent but its primary positioning is clearly outside UDT, exclude it and note it as "adjacent but out of scope" in the session log. When uncertain, compare against the seed list below.

---

## Seed List

Known platforms that qualify, distributed across the three inclusion criteria. Use these to anchor discovery sessions and calibrate the boundary for new candidates.

### Criterion 1 — Explicit Urban Digital Twin

| Platform                                                                 | Organisation                         | Notes                                                     |
| ------------------------------------------------------------------------ | ------------------------------------ | --------------------------------------------------------- |
| [DTCC (Digital Twin City Centre)](https://dtcc.chalmers.se)              | Chalmers / Rise / City of Gothenburg | Academic–municipal UDT; explicit digital twin positioning |
| [Virtual Singapore](https://www.nrf.gov.sg/programmes/virtual-singapore) | Singapore NRF / GovTech              | National city-scale digital twin programme                |

### Criterion 2 — City-Scale Capabilities

| Platform                                                           | Organisation                   | Notes                                                                       |
| ------------------------------------------------------------------ | ------------------------------ | --------------------------------------------------------------------------- |
| [Cesium](https://cesium.com)                                       | Cesium GS                      | 3D geospatial visualisation engine; widely used as UDT rendering layer      |
| [3D City DB](https://www.3dcitydb.org)                             | TU Munich / virtualcitySYSTEMS | Open-source city model database (CityGML); city-scale geospatial management |
| [FIWARE Orion Context Broker](https://fiware-orion.readthedocs.io) | FIWARE Foundation              | Context data management; deployed in multiple smart city / UDT projects     |

### Criterion 3 — Adjacent Architecture or Governance

| Platform                                                  | Organisation       | Notes                                                                       |
| --------------------------------------------------------- | ------------------ | --------------------------------------------------------------------------- |
| [iTwin](https://www.bentley.com/software/itwin-platform/) | Bentley Systems    | Infrastructure digital twin framework; explicit UDT integration positioning |
| [Eclipse Ditto](https://eclipse.dev/ditto/)               | Eclipse Foundation | IoT device twin framework; used as the device layer in UDT architectures    |

---

## Target Corpus

**Target:** 15–30 platforms.

This range is a **planning heuristic**, not a hard constraint. The actual count will be determined by what the research finds. A corpus below 15 is likely under-sampled; above 30 risks including platforms that are too peripheral to be analytically useful.

The seed list above contributes 7 confirmed platforms. Discovery sessions should aim to extend this to the target range by finding additional platforms across all three criteria, with particular attention to non-English-speaking markets and government-led initiatives not well represented in the seed list.
