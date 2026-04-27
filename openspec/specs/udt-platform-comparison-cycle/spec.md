# Spec: udt-platform-comparison-cycle

## Purpose

Governs the `udt-platform-comparison` cycle and its platform-only handoff rules.

## Requirements

### Requirement: UDT platform comparison is a platform-only side-by-side evaluation cycle

Only rows from `udt-platforms` where `Type = platform` SHALL be eligible for `udt-platform-comparison`.
