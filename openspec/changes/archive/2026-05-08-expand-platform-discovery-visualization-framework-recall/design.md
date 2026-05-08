# Design: geospatial visualization framework recall

## Approach

Keep the classification contract unchanged and strengthen the discovery prompt contract.

`platform-definition` already defines `framework` as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer. Giro3D fits that definition if discovered.

The missing behavior is candidate recall: platform discovery should search beyond platform and module wording to include enabling 2D/3D geospatial visualization frameworks.

## Contract Change

Add requirements to `act-discover-platforms-prompt` that broad platform discovery SHALL include adjacent framework search language, including:

- geospatial visualization framework
- 3D web viewing library
- 3D geospatial JavaScript framework
- browser-based geospatial visualization
- 2D 2.5D 3D geospatial data viewer
- 3D Tiles viewer
- point cloud web viewer
- terrain visualization framework
- raster/vector geospatial visualization
- three.js geospatial framework
- OpenLayers 3D visualization

Add a scenario for Giro3D-style tools:

```text
WHEN broad discovery finds a technical geospatial visualization framework
THEN the prompt causes the model to include it as a candidate
THEN the model classifies it using platform-definition
```

## Expected Future Behavior

Future discovery prompts should be more likely to include Giro3D-like artifacts as `framework` rows instead of omitting them because they lack explicit "digital twin platform" phrasing.

Example expected row:

```md
| Giro3D | [Official page](https://giro3d.org/giro3d.html) | framework |  |
```
