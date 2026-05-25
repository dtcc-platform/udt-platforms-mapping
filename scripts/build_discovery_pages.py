#!/usr/bin/env python3
"""Build reflected and public discovery table pages from saved observations."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSERVE = ROOT / "observe"
REFLECT_OUT = ROOT / "reflect" / "entity-discovery-tables.md"
DOCS_OUT = ROOT / "docs" / "entity-discovery.md"


@dataclass
class DiscoveryOutput:
    path: Path
    metadata: dict[str, str]
    table: list[list[str]]
    recall_table: list[list[str]]


def parse_metadata(text: str) -> dict[str, str]:
    match = re.match(r"\s*```yaml\n(?P<body>.*?)\n```\s*", text, re.DOTALL)
    if not match:
        return {}

    metadata: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def is_separator(row: str) -> bool:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_table_at(lines: list[str], index: int) -> list[list[str]]:
    if index + 1 >= len(lines) or not is_separator(lines[index + 1]):
        return []

    table: list[list[str]] = []
    cursor = index
    while cursor < len(lines):
        line = lines[cursor].strip()
        if not line.startswith("|") or not line.endswith("|"):
            break
        if not is_separator(line):
            table.append([cell.strip() for cell in line.strip("|").split("|")])
        cursor += 1
    return table


def first_markdown_table(text: str) -> list[list[str]]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().startswith("|"):
            table = parse_table_at(lines, index)
            if table:
                return table
    return []


def table_after_heading(text: str, heading: str) -> list[list[str]]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip().lower() == heading.lower():
            start = index + 1
            break
    if start is None:
        return []

    for index in range(start, len(lines)):
        if lines[index].strip().startswith("|"):
            return parse_table_at(lines, index)
        if lines[index].startswith("## ") and index > start:
            break
    return []


def discovery_files() -> list[Path]:
    files = []
    for path in OBSERVE.glob("*discovery*.md"):
        if path.name.endswith("_old.md"):
            continue
        files.append(path)
    return sorted(files)


def load_outputs() -> list[DiscoveryOutput]:
    outputs: list[DiscoveryOutput] = []
    for path in discovery_files():
        text = path.read_text()
        metadata = parse_metadata(text)
        table = first_markdown_table(text)
        recall_table = table_after_heading(text, "## Known Candidate Recall Check")
        if table:
            outputs.append(DiscoveryOutput(path, metadata, table, recall_table))
    return outputs


def render_table(table: list[list[str]]) -> list[str]:
    if not table:
        return []

    header = table[0]
    widths = [len(cell) for cell in header]
    for row in table[1:]:
        for index, cell in enumerate(row):
            if index >= len(widths):
                widths.append(0)
            widths[index] = max(widths[index], len(cell))

    def fmt(row: list[str]) -> str:
        padded = [cell.ljust(widths[index]) for index, cell in enumerate(row)]
        return "| " + " | ".join(padded) + " |"

    separator = "| " + " | ".join("-" * width for width in widths) + " |"
    return [fmt(header), separator, *[fmt(row) for row in table[1:]]]


def render_reflect(outputs: list[DiscoveryOutput]) -> str:
    lines = [
        "# Entity Discovery Tables",
        "",
        "Generated from saved discovery observations in `observe/`.",
        "",
    ]

    if not outputs:
        lines.extend(["No discovery observations were found.", ""])
        return "\n".join(lines)

    for output in outputs:
        model = output.metadata.get("model", "unknown model")
        prompt = output.metadata.get("prompt", "unknown prompt")
        date = output.metadata.get("date", "unknown date")
        rel_path = output.path.relative_to(ROOT)

        lines.extend(
            [
                f"## {model}",
                "",
                f"- Source: `{rel_path}`",
                f"- Date: `{date}`",
                f"- Prompt: `{prompt}`",
                f"- Rows: `{max(len(output.table) - 1, 0)}`",
                "",
                *render_table(output.table),
                "",
            ]
        )

        lines.append("### Known Candidate Recall Check")
        lines.append("")
        if output.recall_table:
            lines.extend(render_table(output.recall_table))
        else:
            lines.append("No recall-check table was found in this observation.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_docs(reflect_markdown: str) -> str:
    front_matter = """---
layout: default
title: Entity Discovery Tables
---

"""
    return front_matter + reflect_markdown


def main() -> None:
    outputs = load_outputs()
    reflect_markdown = render_reflect(outputs)
    REFLECT_OUT.write_text(reflect_markdown)
    DOCS_OUT.write_text(render_docs(reflect_markdown))


if __name__ == "__main__":
    main()
