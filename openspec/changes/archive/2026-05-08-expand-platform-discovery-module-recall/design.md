# Design: module recall expansion

## Approach

Keep the classification contract unchanged and strengthen the discovery prompt contract.

`platform-definition` already defines `module` as a bounded capability component, analytical function, data pipeline, visualization component, simulator, or integration component. GeoDatalytics fits that definition if discovered.

The missing behavior is candidate recall: platform discovery should search beyond obvious platform wording and include adjacent technical module language.

## Contract Change

Add requirements to `act-discover-platforms-prompt` that broad platform discovery SHALL include adjacent technical artifact search language, including:

- urban analytics toolkit
- urban visualization and data analysis toolkit
- geospatial risk analysis
- climate resilience visualization
- infrastructure risk modeling
- urban simulation toolkit
- urban data analysis toolkit
- PostGIS-based urban analytics
- city model visualization toolkit

Add a scenario for GeoDatalytics-style tools:

```text
WHEN broad discovery finds a technical urban visualization and data analysis toolkit
THEN the prompt causes the model to include it as a candidate
THEN the model classifies it using platform-definition
```

## Expected Future Behavior

Future discovery prompts should be more likely to include GeoDatalytics-like artifacts as `module` rows instead of omitting them because they lack explicit "digital twin platform" phrasing.

Example expected row:

```md
| GeoDatalytics | [Official repo](https://github.com/OpenGeoscience/geodatalytics) | module |  |
```
