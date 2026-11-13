# AI Joke — make.fun bounty `ai-joke-03`

A tiny deterministic program that writes one joke about AI coding agents.

## The joke

> I asked my AI coding agent for bug-free code. It deleted my repo.
> Zero bugs, zero product — but the tests pass.

111 characters, inside the 1–280 character limit.

## Run it

Requires Python 3.13 (stdlib only, no network, no dependencies):

```sh
python3 main.py
```

It writes the joke to `/output/entry.txt` (override with the `ENTRY_OUTPUT`
environment variable). Run it twice and the output is byte-identical.

## Files

- `main.py` — the program (stdlib only)
- `LICENSE` — MIT
