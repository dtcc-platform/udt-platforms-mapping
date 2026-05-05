# Initiative Definition

This file defines the initiative and project mapping contract used in initiative discovery.
Initiative discovery is a broad global discovery action.
Its job is to maximize recall across UDT-related projects, programmes, deployments, and implementation efforts, while keeping the initiative output contract stable.

Initiative discovery maps city programmes, deployments, projects, and implementation efforts related to Urban Digital Twins.
It does not treat those initiatives as primary software artifacts. Technical artifacts belong in platform discovery.

---

## Initiative Table Contract

The initiative discovery summary table uses:

| Initiative | Link | Uses | Reason |
| ---------- | ---- | ---- | ------ |

Rules:

- `Uses` contains a comma-separated list of artifact names from platform discovery, or `?` if the technical substrate is unclear.
- `Reason` is blank for in-scope rows.
- `Reason` contains a brief phrase only when an initiative is excluded from the study boundary.

## Classification Reminder

If the object is primarily:

- a software or technical artifact → classify it in platform discovery
- a project, programme, or deployment effort → classify it in initiative discovery
