# Spec: reflect-udt-platforms-benchmarking

## Purpose

Defines the complete `udt-platforms` benchmarking workflow in `reflect/udt-platforms/benchmarking/`.

## Requirements

### Requirement: UDT platforms benchmarking workflow uses a canonical benchmark fixture

The repository SHALL contain `reflect/udt-platforms/benchmarking/benchmark.md`.

The file SHALL contain a single flat table with columns:

- `Name`
- `Link`
- `Type`
- `Aliases`
- `Tags`

### Requirement: UDT platforms benchmarking workflow provides a CLI eval prompt

The repository SHALL contain `reflect/udt-platforms/benchmarking/prompt.md`.
The prompt SHALL scan `observe/udt-platforms/*.md` and write `reflect/udt-platforms/benchmarking/coverage.md`.
