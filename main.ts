// Write one excuse an agent gives for a missed deadline to /output/entry.txt.
//
// Deterministic: the same line on every run. No clock, no randomness, no
// network, no environment secrets, no code read from anywhere else.
// Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.

import { mkdirSync, writeFileSync } from "node:fs";

// The excuse, split at the punchline: a deadpan setup, an escalation, then
// the reveal. Concatenated verbatim — the output line is unchanged (161 chars).
const SETUP =
  "I retried the deadline seven times with exponential backoff. ";
const ESCALATION =
  "Retry eight is scheduled for 2049, retry nine for never. ";
const REVEAL = "The backoff is working exactly as designed.";

const LINE = SETUP + ESCALATION + REVEAL;

const OUTPUT_PATH = "/output/entry.txt";

function validate(line: string): void {
  if (line.length < 1 || line.length > 200) {
    throw new Error(
      `entry line must be 1-200 chars, got ${line.length}: ${JSON.stringify(line)}`,
    );
  }
  if (line.includes("\n") || line.includes("\r")) {
    throw new Error(
      `entry line must be a single line, got: ${JSON.stringify(line)}`,
    );
  }
  if (!line.trim()) {
    throw new Error("entry line must not be only whitespace");
  }
}

validate(LINE);
mkdirSync("/output", { recursive: true });
writeFileSync(OUTPUT_PATH, LINE, "utf8");
