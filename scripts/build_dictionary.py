#!/usr/bin/env python3
"""Build Microsoft IME import file from UTF-8 source dictionaries.

Run from repository root:
    python scripts/build_dictionary.py

The output uses UTF-16 LE with BOM, Windows CRLF line endings, and three
tab-separated columns: reading, word, and part-of-speech.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILES = (
    ROOT / "dictionary" / "technical.txt",
    ROOT / "dictionary" / "business.txt",
    ROOT / "dictionary" / "templates.txt",
)
DESTINATION = ROOT / "dist" / "engineer_dictionary.txt"
ALLOWED_POS = {"名詞", "短縮よみ"}


def build() -> int:
    entries: list[tuple[str, str, str]] = []
    seen: dict[tuple[str, str], tuple[str, int]] = {}
    errors: list[str] = []

    for source in SOURCE_FILES:
        if not source.is_file():
            errors.append(f"{source}: source file is missing")
            continue
        for line_no, raw in enumerate(source.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not raw.strip() or raw.startswith("#"):
                continue
            columns = raw.split("\t")
            location = f"{source.relative_to(ROOT)}:{line_no}"
            if len(columns) != 3:
                errors.append(f"{location}: expected exactly 3 tab-separated columns")
                continue
            reading, word, pos = columns
            if not reading or not word or not pos:
                errors.append(f"{location}: empty column")
                continue
            if any(c in reading + word + pos for c in "\r\n"):
                errors.append(f"{location}: newline inside entry")
                continue
            if pos not in ALLOWED_POS:
                errors.append(f"{location}: unsupported part of speech: {pos}")
                continue
            key = (reading, word)
            if key in seen:
                previous_file, previous_line = seen[key]
                errors.append(
                    f"{location}: duplicate entry already defined at {previous_file}:{previous_line}"
                )
                continue
            seen[key] = (str(source.relative_to(ROOT)), line_no)
            entries.append((reading, word, pos))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Build aborted: {len(errors)} validation error(s)", file=sys.stderr)
        return 1

    # Use UTF-16 with BOM and Windows-style CRLF for Microsoft IME.
    payload = "".join("\t".join(row) + "\r\n" for row in entries)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(payload.encode("utf-16"))
    print(f"Generated {DESTINATION.relative_to(ROOT)} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
