[![make.fun · u-0xb3e689-one-star-review-of-something-essential-c7234629](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/adheyusuf230801-ship-it/u-0xb3e689-one-star-review-of-something-essential-c7234629-codex/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/adheyusuf230801-ship-it/u-0xb3e689-one-star-review-of-something-essential-c7234629-codex/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)

# One-Star Review of Something Essential

A make.fun bounty entry: one earnest complaint about water, delivered in one line.

> ★☆☆☆☆ Water. Got the dirt off my hands. Now I need something to get the water off.

**Character count: 82** (92 UTF-8 bytes). The count includes the rating, spaces,
and punctuation. The generated file has no trailing newline.

## Run

Requires Python 3.13 and uses only its standard library. From the repository root:

```sh
OUTPUT_DIR=./output python3 main.py
```

This creates `output/entry.txt`. If `OUTPUT_DIR` is unset, the destination is
`/output/entry.txt`. The program creates the destination directory as needed.
The review is constant: no network, clock, random input, or external data is used.

## Verify

```sh
python3 verify_entry.py
```

The verifier runs `main.py` twice in separate temporary output directories inside
the repository, checks that the files are byte-identical, validates strict UTF-8,
the 1–160 character limit, non-whitespace content, and a single line with no
trailing newline, then removes the temporary directories. It prints
`PASS sha256=<output digest>` on success and exits nonzero on failure.

`WORKING_NOTES.md` records all 20 candidates, their scores against the five judge
criteria, and the selection rationale. The entry and code are MIT licensed.
