#!/usr/bin/env python3
"""Build reflected and public discovery table pages from saved observations."""

from __future__ import annotations

import re
from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSERVE = ROOT / "observe"
REFLECT_OUT = ROOT / "reflect" / "entity-discovery-tables.md"
DOCS_OUT = ROOT / "docs" / "entity-discovery.md"
DOCS_HTML_OUT = ROOT / "docs" / "entity-discovery.html"
INDEX_HTML_OUT = ROOT / "docs" / "index.html"


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


def markdown_links_to_html(value: str) -> str:
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def replace(match: re.Match[str]) -> str:
        label = escape(match.group(1))
        href = escape(match.group(2), quote=True)
        return f'<a href="{href}">{label}</a>'

    return pattern.sub(replace, escape(value))


def render_html_table(table: list[list[str]]) -> str:
    if not table:
        return ""

    header = table[0]
    rows = table[1:]
    lines = ["<div class=\"table-wrap\">", "<table>", "<thead>", "<tr>"]
    lines.extend(f"<th>{escape(cell)}</th>" for cell in header)
    lines.extend(["</tr>", "</thead>", "<tbody>"])
    for row in rows:
        lines.append("<tr>")
        for cell in row:
            lines.append(f"<td>{markdown_links_to_html(cell)}</td>")
        lines.append("</tr>")
    lines.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(lines)


def render_entity_html(outputs: list[DiscoveryOutput]) -> str:
    sections: list[str] = []
    for output in outputs:
        model = output.metadata.get("model", "unknown model")
        prompt = output.metadata.get("prompt", "unknown prompt")
        date = output.metadata.get("date", "unknown date")
        rel_path = output.path.relative_to(ROOT)
        row_count = max(len(output.table) - 1, 0)

        recall = (
            render_html_table(output.recall_table)
            if output.recall_table
            else "<p>No recall-check table was found in this observation.</p>"
        )
        sections.append(
            f"""
<section class="run">
  <h2>{escape(model)}</h2>
  <dl class="metadata">
    <div><dt>Source</dt><dd><code>{escape(str(rel_path))}</code></dd></div>
    <div><dt>Date</dt><dd>{escape(date)}</dd></div>
    <div><dt>Prompt</dt><dd>{escape(prompt)}</dd></div>
    <div><dt>Rows</dt><dd>{row_count}</dd></div>
  </dl>
  {render_html_table(output.table)}
  <h3>Known Candidate Recall Check</h3>
  {recall}
</section>
"""
        )

    body = "\n".join(sections) if sections else "<p>No discovery observations were found.</p>"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Entity Discovery Tables</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f8fa;
      --panel: #ffffff;
      --text: #20242a;
      --muted: #5d6673;
      --line: #d8dde5;
      --accent: #0b6bcb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font: 15px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background: var(--bg);
    }}
    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }}
    h1 {{ margin: 0 0 8px; font-size: 2rem; }}
    h2 {{ margin: 0 0 12px; font-size: 1.35rem; }}
    h3 {{ margin: 24px 0 10px; font-size: 1rem; }}
    .intro {{ margin: 0 0 24px; color: var(--muted); }}
    .run {{
      margin: 24px 0;
      padding: 20px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .metadata {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 10px 16px;
      margin: 0 0 18px;
    }}
    .metadata div {{ min-width: 0; }}
    dt {{ font-size: 0.78rem; color: var(--muted); text-transform: uppercase; }}
    dd {{ margin: 2px 0 0; overflow-wrap: anywhere; }}
    code {{
      padding: 2px 4px;
      background: #eef1f5;
      border-radius: 4px;
      font-size: 0.9em;
    }}
    .table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 6px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      background: #fff;
    }}
    th, td {{
      padding: 8px 10px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
      white-space: nowrap;
    }}
    th {{
      position: sticky;
      top: 0;
      background: #eef3f8;
      font-weight: 650;
    }}
    tr:last-child td {{ border-bottom: 0; }}
    a {{ color: var(--accent); }}
    @media (max-width: 720px) {{
      main {{ padding: 20px 12px 40px; }}
      .run {{ padding: 14px; }}
      th, td {{ padding: 7px 8px; }}
    }}
  </style>
</head>
<body>
  <main>
    <h1>Entity Discovery Tables</h1>
    <p class="intro">Generated from saved discovery observations in <code>observe/</code>.</p>
    {body}
  </main>
</body>
</html>
"""


def render_index_html() -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>UDT Platforms Map</title>
  <style>
    body {
      margin: 0;
      font: 16px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #20242a;
      background: #f7f8fa;
    }
    main {
      max-width: 760px;
      margin: 0 auto;
      padding: 48px 20px;
    }
    a { color: #0b6bcb; }
  </style>
</head>
<body>
  <main>
    <h1>Urban Digital Twin Platforms Map</h1>
    <p><a href="./entity-discovery.html">Entity Discovery Tables</a></p>
  </main>
</body>
</html>
"""


def main() -> None:
    outputs = load_outputs()
    reflect_markdown = render_reflect(outputs)
    REFLECT_OUT.write_text(reflect_markdown)
    DOCS_OUT.write_text(render_docs(reflect_markdown))
    DOCS_HTML_OUT.write_text(render_entity_html(outputs))
    INDEX_HTML_OUT.write_text(render_index_html())


if __name__ == "__main__":
    main()
