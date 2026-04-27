# UDT Initiatives Scope

This file defines the initiative and project mapping contract used in the `udt-initiatives` cycle.

The cycle maps city programmes, deployments, projects, and implementation efforts related to Urban Digital Twins.
It does not treat those initiatives as primary software artifacts. Technical artifacts belong in `udt-platforms`.

---

## Initiative Table Contract

The `udt-initiatives` summary table uses:

| Initiative | Link | Uses | Reason |
| ---------- | ---- | ---- | ------ |

Rules:

- `Uses` contains a comma-separated list of artifact names from `udt-platforms`, or `?` if the technical substrate is unclear.
- `Reason` is blank for in-scope rows.
- `Reason` contains a brief phrase only when an initiative is excluded from the study boundary.

## Classification Reminder

If the object is primarily:

- a software or technical artifact → classify it in `udt-platforms`
- a project, programme, or deployment effort → classify it in `udt-initiatives`
