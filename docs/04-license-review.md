# License Review Approach

## Purpose

This document defines how to evaluate the licensing of UDT platforms.
License assessment feeds into the **Openness & Licensing** dimension of the platform inventory.

## License Families

### Open Source

Platforms where the source code is publicly available under an OSI-approved license.
Key distinctions:

| Type              | Examples             | Key Implication                                                                                         |
| ----------------- | -------------------- | ------------------------------------------------------------------------------------------------------- |
| Permissive        | MIT, Apache 2.0, BSD | Can be used, modified, and redistributed with minimal restriction; commercial use allowed               |
| Copyleft (strong) | GPL v2, GPL v3       | Derivative works must also be open source under the same license                                        |
| Copyleft (weak)   | LGPL, MPL            | Allows linking without triggering copyleft; only modifications to the licensed component must be shared |

**What to look for:** License file in the repository root (`LICENSE`, `COPYING`), SPDX identifier in package metadata, or explicit license statement in documentation.

### Open Core

A hybrid model where a core platform is open source but significant features (enterprise integrations, hosted services, support) are proprietary.
Common in commercial platforms with community editions.

**What to look for:** Distinction between "Community Edition" and "Enterprise Edition"; features gated behind paid tiers; proprietary modules listed separately from the open-source core.

### Proprietary

Source code is not publicly available.
Usage is governed by a commercial license, SaaS terms of service, or government/institutional agreement.

**What to look for:** No public repository; license terms require purchase or agreement; "contact us for pricing" for core functionality.

## Data Licensing

Separate from software licensing, some platforms produce or consume open data.
Note:

- Whether the platform uses open geospatial standards (OGC, CityGML, IFC)
- Whether output data is locked in a proprietary format
- Whether any bundled datasets have their own license restrictions

## Scoring Guide (Openness & Licensing dimension)

| Score | Description                                                                                   |
| ----- | --------------------------------------------------------------------------------------------- |
| 5     | Permissive open-source software + open data standards                                         |
| 4     | Copyleft open-source or open-core with a substantial open component                           |
| 3     | Open-core with significant proprietary features, or open source with restrictive data formats |
| 2     | Primarily proprietary with limited open components or open APIs                               |
| 1     | Fully proprietary, no public source, no open APIs                                             |

## Review Checklist

For each platform:

- [ ] Locate the software license (check repo root, docs, and official site)
- [ ] Identify the license family (permissive, copyleft, open-core, proprietary)
- [ ] Note any data format lock-in
- [ ] Check for a distinction between community and enterprise tiers
- [ ] Assign an Openness & Licensing score (1–5) with a brief rationale note
