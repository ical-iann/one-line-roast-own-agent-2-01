"""Roast Your Own Agent (u-mfnakmal-roast-your-own-agent-2d221bda).

Program/v1 entry. Writes exactly one roast line to entry.txt inside the
harness output directory ($MAKEFUN_OUTPUT_DIR, default /output).

Deterministic: no network, no input, no clock, no randomness. The file
contains only the roast line, UTF-8, with no trailing newline, so repeated
runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = "My agent writes a 12-step plan for every task. Step 12 is always: ask the human what the task was."

# Competition gate (RULES.txt): entry.txt must be UTF-8 text of 1-200
# characters, not only white space, and a single line.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Raise ValueError if `line` would fail the competition gate.

    The gate mirrors RULES.txt exactly (1-200 UTF-8 chars, one line, not
    only whitespace, no surrounding whitespace): a failure here means the
    entry would score 0, so it must raise before anything is written.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, gate requires "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only white space")
    if line.strip() != line:
        raise ValueError("line must not start or end with white space")


def output_path() -> Path:
    """Resolve the entry file path from the harness environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    validate_line(LINE)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
