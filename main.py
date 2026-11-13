"""make.fun bounty ai-joke-03: write one joke about AI coding agents.

Spec: Python 3.13, stdlib only, no network. Run twice, must write the
same bytes to /output/entry.txt. Joke is UTF-8, 1-280 chars.
Local test: ENTRY_OUTPUT env overrides the output path.
"""
import os

JOKE = (
    "I asked my AI coding agent for bug-free code. "
    "It deleted my repo. Zero bugs, zero product — but the tests pass."
)

# Spec self-check (revision 1): the entry must be one UTF-8 joke, 1-280 chars.
JOKE_BYTES = JOKE.encode("utf-8")
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 chars"
assert JOKE_BYTES.decode("utf-8") == JOKE, "joke must round-trip as UTF-8"

OUT = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Revision 2: dirname("") raises FileNotFoundError, so guard the
    # makedirs call for a bare filename (e.g. ENTRY_OUTPUT=entry.txt).
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(JOKE_BYTES)


if __name__ == "__main__":
    main()
