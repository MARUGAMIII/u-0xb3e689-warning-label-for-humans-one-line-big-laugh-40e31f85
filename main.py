#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry - one single-line safety warning label for human beings -
to /output/entry.txt. Standard library only, fully deterministic: the same
line is written on every run.
"""

import os

ENTRY = (
    "WARNING: Human may suddenly explain something you already know, "
    "at length, with confidence, and incorrectly."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
