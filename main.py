"""The 3AM Commit Message — entry generator.

Writes the competition entry line to entry.txt inside OUTPUT_DIR.
"""

import os

ENTRY = "fix: i have read this function 47 times. it has started reading me back."

MAX_LENGTH = 139


def validate_entry(line: str) -> str:
    """Check the entry is one line of 1-139 chars; return it unchanged."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError(f"entry must be 1-{MAX_LENGTH} chars, got {len(line)}")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Write the line to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return target


def main() -> None:
    line = validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(line, out_dir)


if __name__ == "__main__":
    main()
