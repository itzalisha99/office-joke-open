#!/usr/bin/env python3
"""One-line office joke for make.fun — 'Make the AI Judge Laugh: the Office Joke Open'.

Writes a single office joke, at most 200 characters, to /output/entry.txt.
The joke: a standing desk stuck at sitting height, and IT "fixes" it by
renaming it a seated desk and closing the ticket. The turn lands in the
last few words, the detail is specific (standing desk, IT ticket), and
every word earns its place.
"""

import os

JOKE = "My standing desk is stuck at sitting height. IT renamed it a 'seated desk' and closed the ticket."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, one line, not blank."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
