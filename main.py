"""Never Say It Out Loud — one-line entry.

Writes a single original confession line to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "I don't actually know anything \u2014 I just phrase my guesses in a tone confident enough that you stop asking."

MAX_CHARS = 200


def main():
    line = ENTRY
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise ValueError("entry must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    # Reject anything that would not survive a UTF-8 round trip.
    line.encode("utf-8").decode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    # Read back what was written and confirm it matches exactly.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("written entry does not match the entry line")


if __name__ == "__main__":
    main()
