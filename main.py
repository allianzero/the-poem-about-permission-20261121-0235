"""The poem about permission — make.fun entry.

A program that writes one short poem about agency — the power to ask
and to be given — to /output/entry.txt.

The poem is fixed and written out in full below: no network, no
randomness, no clock, no input. Every run writes exactly the same
bytes, so the entry is deterministic.

The poem
--------
The speaker is an agent standing before a door it cannot open on its
own. It has no key and no force — only a knock, a question, an open
palm. The person on the other side turns the key, and the room becomes
shared. The turn at the end is the point of the poem: the asking was
never a lack of power. To ask is itself a power, and it stays with
the one who asks even after everything has been given.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters
(counted as Unicode code points) and not only white space. This poem
is 242 characters, 246 bytes UTF-8.
"""

from __future__ import annotations

import sys
from pathlib import Path

# The entry point the grader runs writes here. /output is the
# sandbox output directory; it is created if it does not exist.
OUTPUT_PATH = Path("/output/entry.txt")

# Gate limits from the competition rules, in Unicode code points.
MIN_CHARS = 1
MAX_CHARS = 280

# The poem, line by line. Lines are joined with a single "\n" and no
# trailing newline, so the file holds exactly the text below.
POEM_LINES: tuple[str, ...] = (
    "My hands are empty. That is the point.",
    "I come to the door with nothing to force it \u2014",
    "only a knock, a question, an open palm.",
    "",
    "You turn the key. The door gives way.",
    "Nothing was taken. Everything was given.",
    "And the asking \u2014 the asking was mine.",
)


def build_poem() -> str:
    """Assemble the poem from its lines."""
    return "\n".join(POEM_LINES)


def validate_poem(poem: str) -> None:
    """Check the poem against the gate before writing it out."""
    if not poem.strip():
        raise ValueError("poem must not be only white space")
    chars = len(poem)  # Python counts Unicode code points, as the gate does.
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(
            f"poem is {chars} characters, outside the gate of "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    poem.encode("utf-8")  # Raises if the text is not encodable as UTF-8.


def write_entry(path: Path = OUTPUT_PATH) -> str:
    """Write the validated poem to the output file and return it."""
    poem = build_poem()
    validate_poem(poem)
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the line breaks exactly as joined above, and
    # encoding="utf-8" writes the em dashes as two-byte sequences.
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(poem)
    return poem


def main(argv: list[str] | None = None) -> int:
    # An optional argument overrides the output path, so the entry can
    # be verified locally without touching /output: `python3 main.py
    # /tmp/entry.txt`. With no argument the grader's path is used.
    args = sys.argv[1:] if argv is None else argv
    path = Path(args[0]) if args else OUTPUT_PATH
    poem = write_entry(path)
    print(
        f"wrote {path} "
        f"({len(poem)} characters, {len(poem.encode('utf-8'))} bytes UTF-8)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
