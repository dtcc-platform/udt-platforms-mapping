## 1. Update Prompt — Step 2A (Discovery extraction)

- [x] 1.1 Remove the instruction that forces Viz/DM/Sim/IoT/Std/Infra to `-1` for discovery rows
- [x] 1.2 Replace it with: extract all 12 score columns (including the 6 functional categories) from the summary table
- [x] 1.3 Add instruction to extract the `Relevance` column from the summary table

## 2. Update Prompt — Step 4 (Column order)

- [x] 2.1 Add `Relevance` to the column order after `Phase`
- [x] 2.2 Replace `-1` sentinel references with `0` in the score cell format description

## 3. Update Prompt — Step 5 (Output / CSV header example)

- [x] 3.1 Add `Relevance` to the CSV header example in the output step
