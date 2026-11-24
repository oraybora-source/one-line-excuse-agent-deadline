"""One-line excuse an agent gives its human after missing a deadline.

Writes a single line (at most 160 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no dependencies beyond the Python standard library.
"""

import os

TEXT = "You wrote 'ASAP' on Monday, 'no rush' on Tuesday, and 'is it done?' on Friday. I optimised for Tuesday."

# Gate: /output/entry.txt must hold 1-160 characters, not only whitespace.
MAX_CHARS = 160


def main():
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError("entry text must be 1-160 characters")
    # The grader reads /output as another user, so the file it writes must
    # be world-readable (0644) whatever umask this process inherits. Setting
    # the process umask is not a chmod of /output (never chmod /output).
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
