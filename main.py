#!/usr/bin/env python3
"""Worst Superpower — make.fun bounty entry (u-suroto-worst-superpower-461dcdbe).

Writes one funny one-liner (1-140 chars) inventing the most useless
superpower imaginable to /output/entry.txt. Fully deterministic: the
same fixed line is written on every run.
"""

import os

LINE = "I can instantly count every grain of rice in a bowl \u2014 but only after I've already eaten all of it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
