## 1. Update Prompt — Part 3 Output Format

- [x] 1.1 Replace the four bullet-point questions in the Part 3 section of `prompts/platform-comparison.md` with four `####` subheadings, each followed by a bullet list placeholder: `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms`
- [x] 1.2 Add an instruction note to the Part 3 section specifying that subheadings use `####` (not `###`) to avoid conflict with Part 2 platform profile headings
- [x] 1.3 Add an instruction that the model SHALL use exactly these four subheadings in this order, with no additional subheadings

## 2. Update Spec

- [x] 2.1 Apply the delta spec at `openspec/changes/structure-landscape-observations/specs/platform-comparison-prompt/spec.md` to `openspec/specs/platform-comparison-prompt/spec.md`:
  - Replace the Part 3 bullet in the three-part output list with the subheading-based description
  - Replace the "Researcher understands DTCC's position" scenario with the updated version requiring four named subheadings
  - Add the "Researcher scans Part 3 across two agent responses" scenario
