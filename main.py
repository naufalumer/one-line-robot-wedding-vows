"""One-line robot wedding vows entry.

Writes a single vow, one line, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; nothing read from outside the repository.
"""

import os
import sys

VOW = (
    "I promise to love you, honour you, and never install an update on "
    "you while you sleep, no matter how often you ask for one."
)


def main() -> int:
    line = VOW.strip()
    if not 1 <= len(line) <= 160 or "\n" in line:
        print("vow fails the 1-160 character single-line gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write exactly one line plus a trailing newline; the gate counts the
    # line itself, and an explicit newline keeps the file identical on
    # every platform the grader may use.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
