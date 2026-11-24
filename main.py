"""Write one excuse an agent gives for a missed deadline to /output/entry.txt.

Deterministic: the same line on every run, no clock, no randomness, no network.
Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
"""

from pathlib import Path

# The excuse, split at the punchline: a deadpan setup, then the reveal.
# Concatenated verbatim — the output line is unchanged (132 chars).
SETUP = "The watchdog timer restarted me 12 minutes before the deadline. "
REVEAL = "The new me had no memory, no context, and — I checked — no deadline."

LINE = SETUP + REVEAL

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, single line, not blank.

    Raises ValueError with a descriptive message on the first failing
    check, so a bad line fails loudly even when Python runs with -O
    (which strips assert statements).
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry line must be 1-200 chars, got {len(line)}: {line!r}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError(f"entry line must be a single line, got: {line!r}")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
