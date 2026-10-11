#!/usr/bin/env python3
"""Flag typography that the course scores as zero on a whole task.

Scans markdown cells and code comments for long dashes and curly quotes.
Mathematical minus (U+2212) is left alone. The prompt log is a separate file
and is not scanned.
"""

from __future__ import annotations

import io
import json
import sys
import tokenize
from pathlib import Path

FORBIDDEN = {
    "\u2010": "hyphen",
    "\u2011": "non-breaking hyphen",
    "\u2012": "figure dash",
    "\u2013": "en dash",
    "\u2014": "em dash",
    "\u2015": "horizontal bar",
    "\u2018": "left single quote",
    "\u2019": "right single quote",
    "\u201a": "single low-9 quote",
    "\u201b": "single high-reversed-9 quote",
    "\u201c": "left double quote",
    "\u201d": "right double quote",
    "\u201e": "double low-9 quote",
    "\u201f": "double high-reversed-9 quote",
    "\u00ab": "left guillemet",
    "\u00bb": "right guillemet",
}


def code_comments(source: str) -> list[tuple[int, str]]:
    """Return comment text, including comments that follow code on the same line."""
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        return [
            (tok.start[0], tok.string)
            for tok in tokens
            if tok.type == tokenize.COMMENT
        ]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return [
            (n, line)
            for n, line in enumerate(source.splitlines(), start=1)
            if line.lstrip().startswith("#")
        ]


def lines_to_scan(kind: str, source: str) -> list[tuple[int, str]]:
    """Markdown is scanned in full. Code is scanned on comments only."""
    if kind == "markdown":
        return list(enumerate(source.splitlines(), start=1))
    if kind == "code":
        return code_comments(source)
    return []


def forbidden_in(line: str) -> list[str]:
    return [name for char, name in FORBIDDEN.items() if char in line]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_notebook.py NOTEBOOK.ipynb", file=sys.stderr)
        return 2

    path = Path(argv[1])
    notebook = json.loads(path.read_text(encoding="utf-8"))
    reports: list[str] = []

    for index, cell in enumerate(notebook.get("cells", [])):
        source = "".join(cell.get("source", []))
        kind = cell.get("cell_type", "")
        for line_no, line in lines_to_scan(kind, source):
            names = forbidden_in(line)
            if not names:
                continue
            snippet = line.strip()
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            reports.append(
                f"{path}: cell {index} ({kind}), line {line_no}: {', '.join(names)}\n  {snippet}"
            )

    if reports:
        print("\n".join(reports))
        print(f"\n{len(reports)} hit(s). Solution prose uses '-' and '\"'.")
        return 1

    print(f"{path}: no long dashes or curly quotes in markdown or comments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
