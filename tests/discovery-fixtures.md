# Discovery Test Fixtures

This file is the recall benchmark for UDT ecosystem discovery sessions. It lists platforms that are expected to appear in discovery responses but are at risk of being missed due to specific discovery failure modes (gap categories).

**How to use:** Run `tests/eval-discovery.md` via Claude Code to check all `responses/global-platforms-discovery-*.md` files against this list.

**How to add an entry:** When a known in-scope platform is found to be missing from a discovery response, add a row to the appropriate gap category. If no category fits, create a new `## Gap:` section.

---

## Gap: No digital-twin framing — urban resilience & climate risk

Platforms in this category use language like "urban analytics," "resilience," "climate risk," or "infrastructure risk assessment" without claiming "digital twin." Discovery AI sessions miss them because they search for digital-twin signal first. These tools qualify as `domain-module` or `backbone` if their outputs feed into a broader UDT stack.

| Name          | Link                                              | Expected Layer | Why tricky                                                                 |
| ------------- | ------------------------------------------------- | -------------- | -------------------------------------------------------------------------- |
| GeoDatalytics | https://github.com/OpenGeoscience/geodatalytics   | domain-module  | Describes itself as "urban visualization and data analysis toolkit"; no digital-twin framing; niche GitHub project by Kitware/Northeastern |
