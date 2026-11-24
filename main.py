#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Standard library only, fully deterministic:
the same bytes on every run.
"""

import os
import sys

# The rant. One concrete annoyance — the office printer — with a fresh
# angle: it never jams on a quiet day, only when the one document that
# matters is due. Sharp, economical, no throat-clearing.
RANT = (
    "The office printer has never once jammed on a quiet Tuesday. "
    "It waits — patient, smug, fully inked — until your flight leaves "
    "in forty minutes and the boarding pass is the one document that "
    "matters. Then it eats the paper, blinks orange, and prints a test "
    "page in a language nobody in this building speaks. I have "
    "apologised to a machine more often than to my own family."
)

MAX_CHARS = 400


def validate(text: str) -> str:
    """Enforce the competition gate: UTF-8 text, 1-400 chars, not blank.

    Returns the exact text to write: stripped of any accidental leading
    or trailing whitespace so the gate sees the rant and nothing else.
    """
    text = text.strip()
    if not text:
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main() -> int:
    text = validate(RANT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
