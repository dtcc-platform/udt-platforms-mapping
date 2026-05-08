# Design: seed-list recall for platform discovery

## Approach

Keep `platform-definition` unchanged and strengthen the discovery behavior contract.

The prompt should treat curated lists as discovery inputs, not as classification authorities. A seed-list entry should only be included when it satisfies `platform`, `framework`, `module`, or useful `excluded` boundary behavior under `platform-definition`.

## Seed-List Domains

The discovery prompt should consider adjacent ecosystem seed lists covering:

- frontend GIS
- geospatial visualization
- 3D Tiles
- point-cloud and LiDAR web viewers
- web mapping libraries
- spatial data processing tools
- geospatial analytics tools
- browser-based 2D/3D mapping frameworks

## Expected Behavior

When the prompt uses an `awesome-frontend-gis`-style seed list:

- TerriaJS, iTowns, ArcGIS Maps SDK for JavaScript, deck.gl, MapLibre GL JS, OpenLayers, and MapTalks.js can be considered as `framework` candidates.
- Potree, Plasio, Kepler.gl, geojson.io, and mapshaper can be considered as `module` candidates.
- StoryMapJS can be considered as an `excluded` boundary candidate.

The prompt should not imply that every seed-list entry belongs in the output.

## Relationship to Existing Recall Changes

This generalizes the GeoDatalytics and Giro3D recall fixes. Those fixes add term families; this change adds curated seed-list use as another recall strategy.
