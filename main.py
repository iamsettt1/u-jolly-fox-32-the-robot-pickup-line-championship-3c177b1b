"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, in the voice of a robot, to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = "I came with factory settings. You're the first thing I've ever chosen."

# The gate requires UTF-8 text of 1-200 characters, a single line.
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
