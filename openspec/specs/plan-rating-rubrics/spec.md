# Spec: plan-rating-rubrics

## Purpose

Defines the requirements for `plan/rating/rubrics.md`, the scope reference file for rating sessions. Researchers paste its full content into the `[PASTE_SCOPE_HERE]` slot in the rating prompt before running a session.

## Requirements

### Requirement: plan/rating/rubrics.md exists and contains the 12 dimension rubrics

The repository SHALL contain a file at `plan/rating/rubrics.md`. This file is the sole scope reference for rating sessions — researchers paste its full content into the `[PASTE_SCOPE_HERE]` slot in the rating prompt before running a session.

The file SHALL contain the 12 dimension and functional category rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra) as the canonical source for rating scoring. Each rubric SHALL define criteria for scores 0–5.

The file SHALL NOT contain the Layer criteria table, the Relevance rubric, a seed list, or target corpus size. Those belong in `plan/discovery/scope.md` or are retired.

The file SHALL include a brief header explaining its purpose: it defines the dimension scoring rubrics used in the rating phase.

#### Scenario: Researcher prepares a rating session

- **WHEN** a researcher is about to run a rating session
- **THEN** they paste the full content of `plan/rating/rubrics.md` into the `[PASTE_SCOPE_HERE]` slot in the rating prompt — not the discovery scope

#### Scenario: Rating AI scores a platform dimension

- **WHEN** a rating AI reads the rubrics and assesses a platform's Technical Architecture
- **THEN** it assigns a score 1–5 per the Arch rubric criteria from the pasted scope content

#### Scenario: Researcher updates a dimension rubric

- **WHEN** a researcher needs to refine the criteria for a dimension score level
- **THEN** they edit `plan/rating/rubrics.md` only; the rating prompt receives the updated rubric at run time via the paste step

#### Scenario: Researcher runs discovery after updating rating scope

- **WHEN** a researcher updates `plan/rating/rubrics.md`
- **THEN** discovery sessions are unaffected — discovery pastes `plan/discovery/scope.md` which is unchanged
