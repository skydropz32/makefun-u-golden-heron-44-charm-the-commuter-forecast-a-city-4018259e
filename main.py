"""Charm the Commuter: one-line weather forecast for a city that isn't.

Writes a single forecast line for the invented city Drizzlewick to
/output/entry.txt.
"""

from pathlib import Path

LINE = "Good morning, Drizzlewick: rain falling upwards, umbrellas migrating north. The 7:40 bus arrives the moment you stop checking for it."


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
