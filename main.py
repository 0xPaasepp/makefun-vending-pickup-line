"""Vending-machine pickup line entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt (the competition gate: UTF-8 text, 1-200 chars).
Pure stdlib, no network, no environment reads, deterministic.
"""

from pathlib import Path

LINE = "I've been saving slot B4 just for you \u2014 press it and I'll drop my best snack, my number, and whatever dignity I have left."

OUT = Path("/output/entry.txt")


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "entry must not be only white space"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
