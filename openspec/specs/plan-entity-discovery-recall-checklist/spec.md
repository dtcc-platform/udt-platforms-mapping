# Spec: plan-entity-discovery-recall-checklist

## Purpose

Defines known entity recall-check cases that the entity discovery prompt must audit during each discovery run.

## Requirements

### Requirement: GeoDatalytics is a known recall-check entity

Entity discovery SHALL treat GeoDatalytics as a known recall-check entity.

The recall-check entity SHALL use `GeoDatalytics` as the canonical `Name`.

The recall-check entity SHALL use `https://github.com/OpenGeoscience/geodatalytics` as the canonical `Link`.

The recall-check entity SHALL use `module` as the expected `Type`.

The recall-check entity SHALL include `geodatalytics` as an alias.

The recall-check rationale SHALL state that GeoDatalytics is an accepted recall-miss case for adjacent geospatial or urban analytics tooling that may not use explicit digital twin wording.

#### Scenario: Discovery checks GeoDatalytics

- **WHEN** entity discovery runs with the recall checklist contract
- **THEN** it checks GeoDatalytics as a known recall-check entity
- **THEN** it reports whether GeoDatalytics was found, missed, or excluded under the governed miss categories
