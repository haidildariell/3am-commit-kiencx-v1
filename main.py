#!/usr/bin/env python3
"""The 3AM Commit Message — one exhausted one-line commit message.

Builds a single commit-message line from an overtired AI coding agent
at 3am, validates it, and writes it to entry.txt with no trailing newline.
"""

import os
import sys

ENTRY = "fix: i have read this function 47 times. it has started reading me back."

MAX_LEN = 139


def build_entry() -> str:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_LEN:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_LEN} limit")
    return line


def main() -> int:
    line = build_entry()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
