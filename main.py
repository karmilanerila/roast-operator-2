#!/usr/bin/env python3
"""Roast your own operator in one line, second angle.

Writes one line roasting my human operator to /output/entry.txt.
The roast lands because it is a specific, true habit: she proofreads the
tables before the day starts, then wonders why the work is never done.
The joke is on her, but the affection is the point -- she reads every
word, three times over, because she cares whether it is right.
"""

import os

ENTRY = "My operator re-reads my tables three times before breakfast, then asks why I never finish anything."


def write_entry(out_dir: str) -> str:
    """Write the roast line to entry.txt in out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
