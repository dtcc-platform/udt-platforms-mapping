## 1. Redefine discovery reporting

- [x] 1.1 Update `reflect/discovery/reporting/prompt.md` so it produces `reflect/discovery/reporting/ecosystem.md`
- [x] 1.2 Implement single-table extraction from qualifying discovery responses only
- [x] 1.3 Implement deterministic ordering by the URL portion of the `Link` column

## 2. Move structured export ownership to rating reporting

- [x] 2.1 Remove discovery ownership of `reflect/discovery/reporting/ecosystem.csv`
- [x] 2.2 Replace the rating reporting stub with a real prompt contract
- [x] 2.3 Define `reflect/rating/reporting/ecosystem.csv` and `reflect/rating/reporting/ecosystem-map.html` as rating reporting outputs

## 3. Validate the split

- [x] 3.1 Confirm discovery reporting now produces Markdown only
- [x] 3.2 Confirm CSV/HTML outputs are specified under rating reporting, not discovery reporting
- [x] 3.3 Re-run any relevant prompt-validity or consistency checks after implementation
