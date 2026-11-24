"""Write one excuse an agent gives for a missed deadline to /output/entry.txt.

Deterministic: the same line on every run, no clock, no randomness, no network.
Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
"""

from pathlib import Path

LINE = "The watchdog timer restarted me 12 minutes before the deadline. The new me had no memory, no context, and — I checked — no deadline."

# Single line, well inside the 200-char gate (132 chars).
assert 1 <= len(LINE) <= 200 and "\n" not in LINE.strip()

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
