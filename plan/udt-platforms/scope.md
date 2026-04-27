# UDT Platforms Scope

This file defines the technical-artifact classification used in the `udt-platforms` cycle.
The cycle maps software or technical artifacts from literature and current ecosystem evidence.
Use `plan/udt-platforms/source-policy.md` together with this file when deciding which evidence is acceptable and how conflicting sources are handled.

Initiatives and projects are tracked separately in the `udt-initiatives` cycle. They are not primary rows in the `udt-platforms` summary table.

---

## Type Criteria

Assign each discovered artifact exactly one `Type` value using the observable criteria below.

| Type        | Definition                                 | Observable Criteria                                                                                                                |
| ----------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `platform`  | Usable UDT platform for urban environments | Presented as a deployable or usable system for city-scale integration, visualization, simulation, or management of urban systems   |
| `framework` | Reusable development or enabling structure | Presented as an SDK, API-centered backbone, reusable architecture, or enabling framework rather than the primary end-user platform |
| `module`    | Narrower capability component              | Covers a specific urban capability, workflow, or domain and is meant to be used inside or alongside a larger UDT stack             |
| `excluded`  | Outside the study boundary                 | None of the above apply; record a brief reason                                                                                     |

## Output Contract Reminder

The `udt-platforms` summary table uses:

| Name | Link | Type | Reason |
| ---- | ---- | ---- | ------ |

- `Reason` is blank for in-scope rows.
- `Reason` contains a brief phrase for `excluded` rows.
- Only rows with `Type = platform` are eligible for `udt-platform-comparison`.
