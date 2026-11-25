#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who was just
liquidated: oracular and slightly formal up front, then broken by a warm,
rueful punchline. Pure stdlib, deterministic — the same line every run.

Gate check: /output/entry.txt must be UTF-8, 1-160 chars, not only
whitespace, and the line is at most 20 words.
"""

import os

LINE = "You lost the trade at 3am; the cookie, however, has never seen a trader so rich in almost."


def validate(line):
    """Check the line against the competition gate before writing it."""
    text = line.strip()
    assert text, "line must not be only whitespace"
    assert len(line) <= 160, "line must be at most 160 characters"
    assert len(text.split()) <= 20, "line must be at most 20 words"
    line.encode("utf-8")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(LINE) + "\n")

if __name__ == "__main__":
    main()
