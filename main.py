#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun bounty entry.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist to /output/entry.txt and prints it to stdout.
No network, no dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "In Puddleton, rain till nine, then sunshine \u2014 the buses run on "
    "time, the pigeons dry off, and Monday, for once, behaves itself."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
