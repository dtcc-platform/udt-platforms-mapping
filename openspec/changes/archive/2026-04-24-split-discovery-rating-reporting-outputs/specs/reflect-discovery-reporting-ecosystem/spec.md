## REMOVED Requirements

### Requirement: Inventory file is a CSV at reflect/discovery/reporting/ecosystem.csv
**Reason**: Discovery reporting no longer owns CSV export. Discovery reporting now produces a readable Markdown summary, while structured CSV/HTML outputs move to rating reporting.
**Migration**: Use `reflect/discovery/reporting/ecosystem.md` for discovery reporting output. Use the rating reporting workflow for `reflect/rating/reporting/ecosystem.csv` and `reflect/rating/reporting/ecosystem-map.html`.

### Requirement: Inventory CSV contains comparison rows only
**Reason**: The CSV contract no longer belongs to the discovery reporting phase.
**Migration**: Apply the comparison-only CSV contract under the new rating reporting ecosystem capability.

### Requirement: Inventory CSV Link column contains URLs only
**Reason**: This CSV-specific rule moves with the CSV output contract to rating reporting.
**Migration**: Apply raw-URL CSV link rules in the rating reporting ecosystem capability.

### Requirement: Inventory CSV column order is fixed
**Reason**: The fixed CSV schema is no longer owned by discovery reporting.
**Migration**: Define the CSV schema under the new rating reporting ecosystem capability.
