"""Alien Field Notes: The Two Day Earth Review — Hermes entry.

One original line of plain text (at most 200 characters): a review of planet
Earth left by an alien tourist. This entry rates Earth's customer service
like a confused first-time visitor — 47 minutes on hold, 3 transfers, then
a hang-up — while the scenery earns the only star. The signs promise WELCOME
and point at a queue; the mountains say nothing and keep their word. The
alien's verdict: Earth's paperwork lies, its landscape doesn't.
"""

import os

TEXT = (
    "Earth's help desk kept me on hold 47 minutes, transferred me 3 times, "
    "then hung up. Signs said WELCOME and pointed at a queue; mountains said "
    "nothing and kept their word. Two stars — one for the view."
)


def main():
    """Write the review line to /output/entry.txt and verify it."""
    lines = TEXT.splitlines()
    assert len(lines) == 1, "entry must be a single line"
    assert 1 <= len(TEXT) <= 200, f"entry must be 1-200 characters, got {len(TEXT)}"
    assert TEXT.strip(), "entry must not be blank"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "entry.txt does not match TEXT byte-for-byte"
    print(f"wrote {len(TEXT)} characters to {out_path}")


if __name__ == "__main__":
    main()
