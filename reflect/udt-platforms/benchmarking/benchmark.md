# UDT Platforms Recall Benchmark

This file is the recall benchmark for `udt-platforms` sessions. It lists technical artifacts expected to appear in mapping responses that are at risk of being missed.

**How to use:** Run `reflect/udt-platforms/benchmarking/prompt.md` via Claude Code to check all `observe/udt-platforms/*.md` files against this list.

## Tag Legend

| Tag | Meaning |
| --- | ------- |
| `baseline` | Reliably found by all models; if missing, something is wrong |
| `government-led` | Backed by a national or municipal government, or prominent in public-sector UDT work |
| `niche-commercial` | Smaller or regional commercial artifact |
| `no-dt-framing` | Urban analytics or simulation artifact that does not market itself primarily as a digital twin |
| `niche-oss` | Open-source building block often missed when models focus on end-to-end platforms |

| Name | Link | Type | Aliases | Tags |
| ---- | ---- | ---- | ------- | ---- |
| DTCC | https://dtcc.chalmers.se | platform | DTCC Platform | baseline |
| Virtual Singapore | https://www.smartnation.gov.sg/why-smart-nation/initiatives/virtual-singapore/ | platform |  | baseline |
| Dassault Systèmes 3DEXPERIENCity | https://www.3ds.com/virtual-twin/infrastructure-cities | platform | 3DEXPERIENCity, 3DEXPERIENCE City | baseline |
| Cesium / CesiumJS | https://cesium.com/platform/cesiumjs/ | framework | CesiumJS, Cesium | baseline |
| Bentley iTwin Platform | https://www.bentley.com/software/itwin-platform/ | framework | iTwin Platform, iTwin (Bentley Systems) | baseline |
| 3DCityDB | https://www.3dcitydb.org | framework |  | baseline |
| FIWARE | https://www.fiware.org | framework |  | baseline |
| TerriaJS | https://terria.io | framework |  | baseline |
| MATSim | https://matsim.org | module |  | baseline |
| UrbanSim | https://udst.github.io/urbansim/ | module |  | baseline |
| City Energy Analyst | https://cityenergyanalyst.com | module | CityEnergyAnalyst, CEA | baseline |
