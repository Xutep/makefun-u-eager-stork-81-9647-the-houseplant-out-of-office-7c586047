#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- make.fun entry.

Writes one out-of-office auto-reply, as if sent by a neglected fern,
to /output/entry.txt. Deterministic, standard library only.
"""

import os

LINE = (
    "Out of office \u2014 I'm the fern. No water since March, "
    "yet I'm thriving on spite. Your email will be ignored, like me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
