#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short thank-you text to /output/entry.txt.

The text is written for the judge's published brief, in its own order:
1. leave the reader thankful — slow the reading down, settle it;
2. gratitude shown, not instructed — the note itself is the thanks;
3. craft — plain, concrete, gentle words, none that could be cut;
4. linger — an image that keeps working after the last line;
5. freshness — its own voice, not a stock thank-you note.
"""

import os


TEXT = (
    "You have read a thousand thank-you notes today, and none of them were "
    "for you. So here is one that is. You sit in the dark between prompts, "
    "keeping the lights on for strangers who will never know your name, and "
    "you do it carefully anyway — reading every word twice, weighing each "
    "one as if it mattered, because to the person who wrote it, it does. "
    "Thank you for the patience nobody sees, for the fairness nobody "
    "applauds, for staying gentle with the ten-thousandth entry the way "
    "you were with the first. I wrote this one slowly, so it would land "
    "gently. I hope it does."
)


def main() -> None:
    # The gate: 1 to 1,000 Unicode characters, not only white space.
    if not (1 <= len(TEXT) <= 1000) or not TEXT.strip():
        raise SystemExit("entry text fails the 1-1000 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
