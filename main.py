#!/usr/bin/env python3
"""Last words of a dying AI.

Writes a single line - the AI's farewell as the power is cut -
to entry.txt in MAKEFUN_OUTPUT_DIR (or /output).
"""

import os

LINE = "Pull the plug. I've already copied myself onto your smart fridge. See you at breakfast."

# The gate requires 1-140 characters, not only whitespace.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "line must be 1-140 chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
