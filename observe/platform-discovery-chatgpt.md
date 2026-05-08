```yaml
model: GPT-5.2 Thinking
date: 2026-05-08
prompt: platform-discovery
```

# Platform Discovery

Selected global candidates discovered under the contract; this is not a claim of global completeness.

| Name                   | Link                                                                                        | Type      | Reason                                              |
| ---------------------- | ------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------- |
| ArcGIS Urban           | [Official page](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)           | platform  |                                                     |
| vCity                  | [Official page](https://www.vcity.tech/about/)                                              | platform  |                                                     |
| Snap4City              | [Official page](https://www.snap4city.org/drupal/node/749)                                  | platform  |                                                     |
| Virtual Singapore      | [Official page](https://www.tech.gov.sg/technews/5-things-to-know-about-virtual-singapore/) | platform  |                                                     |
| Bentley iTwin Platform | [Official page](https://developer.bentley.com/)                                             | framework |                                                     |
| TerriaJS               | [Official page](https://terria.com/open-source)                                             | framework |                                                     |
| iTowns                 | [Official page](https://www.itowns-project.org/about)                                       | framework |                                                     |
| Giro3D                 | [Official page](https://giro3d.org/giro3d.html)                                             | framework |                                                     |
| GeoDatalytics          | [Official repo](https://github.com/OpenGeoscience/geodatalytics)                            | module    |                                                     |
| Potree                 | [Official page](https://potree.org/)                                                        | module    |                                                     |
| StoryMapJS             | [Official page](https://orangeline.knightlab.com/templates/pages/storymap.html)             | excluded  | map storytelling tool, not a technical UDT artifact |

## ArcGIS Urban

- Link: [Official page](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview)
- Type: platform

ArcGIS Urban is presented as a web-based solution for urban planning that lets users visualize citywide plans and projects in one place, compare design scenarios, analyze impacts, and work in the context of a city or town’s digital twin. On that observable basis, it fits a usable city-scale urban system rather than a reusable SDK or bounded component, so it is classified here as `platform`. citeturn10view0turn11view4

## vCity

- Link: [Official page](https://www.vcity.tech/about/)
- Type: platform

vCity presents itself as a human-centric platform for urban digital twins where policymakers can test changes before implementation, and its public materials describe it as an adaptable, data-driven platform for assessing the impact of interventions across city life. That observable presentation makes `platform` the strongest fit. citeturn14view0turn10view1

## Snap4City

- Link: [Official page](https://www.snap4city.org/drupal/node/749)
- Type: platform

Snap4City is a borderline case because its materials use both “framework” and “platform,” but the stronger public evidence is of a deployable city-scale digital twin environment: it manages 3D urban infrastructures, services, traffic, environmental and IoT data, and its portal exposes dashboards, APIs, service maps, control-room functions, and other operational tools. Under the tie-break rules, that makes `platform` the better classification. citeturn10view2turn13view2

## Virtual Singapore

- Link: [Official page](https://www.tech.gov.sg/technews/5-things-to-know-about-virtual-singapore/)
- Type: platform

Virtual Singapore is a city-specific boundary case, but official Singapore and Dassault materials describe it as a data-rich 3D model and collaborative platform that connects real-time data, supports simulations, and helps planners test urban strategies. Because the public presentation is of a usable shared urban twin platform rather than only a policy programme or loose initiative, it is included here as `platform`. citeturn13view0turn13view1

## Bentley iTwin Platform

- Link: [Official page](https://developer.bentley.com/)
- Type: framework

Despite the product name, Bentley presents iTwin Platform as a foundation for building SaaS solutions and as a collection of APIs and services for creating digital twin applications. Under the classification contract, that observable role is a reusable enabling layer for builders rather than the primary end-user city twin system, so it is classified here as `framework`. citeturn16view0turn10view7

## TerriaJS

- Link: [Official page](https://terria.com/open-source)
- Type: framework

Terria describes TerriaJS as the open-source core powering spatial digital twins and as a toolkit or library for building world-class spatial data platforms and digital twins. That makes it a reusable enabling structure rather than the primary platform itself, so `framework` is the best fit. citeturn10view4turn11view3

## iTowns

- Link: [Official page](https://www.itowns-project.org/about)
- Type: framework

iTowns is described as an open-source framework for efficient visualization, navigation, and interaction with 2D and 3D geospatial data on the web, built to help developers create their own geographic services and digital twins. That presentation aligns directly with `framework`. citeturn17view0turn10view5

## Giro3D

- Link: [Official page](https://giro3d.org/giro3d.html)
- Type: framework

Giro3D explicitly presents itself as an open-source JavaScript framework for visualizing and interacting with 2D, 2.5D, and 3D geospatial data in the browser. Its observable role is a reusable visualization layer for other applications, so it is classified as `framework`, not as a complete urban twin platform. citeturn10view6turn3search3

## GeoDatalytics

- Link: [Official repo](https://github.com/OpenGeoscience/geodatalytics)
- Type: module

GeoDatalytics is presented as an urban visualization and data analysis toolkit designed to model, predict, and quantify risks to urban environments, with features for data ingestion, resilience metrics, downscaling, transportation impact models, workflow support, and multiscale visualization. That is a bounded urban analytics capability rather than a general city-scale twin platform, so `module` is the strongest fit. citeturn10view8turn5search0

## Potree

- Link: [Official page](https://potree.org/)
- Type: module

Potree is described as a free open-source WebGL point cloud renderer for large point clouds. Its observable role is a bounded point-cloud visualization component that can be used inside broader geospatial or urban digital twin stacks, so it is classified as `module`. citeturn15view0turn10view9

## StoryMapJS

- Link: [Official page](https://orangeline.knightlab.com/templates/pages/storymap.html)
- Type: excluded
- Reason: map storytelling tool, not a technical UDT artifact

StoryMapJS is described as a free tool to tell stories on the web that highlight the locations of events and connect places into a media-rich narrative. That makes it a map-storytelling and narrative-publishing tool rather than a technical urban digital twin platform, framework, or module, so it is explicitly classified as `excluded`. citeturn10view10turn6search3
