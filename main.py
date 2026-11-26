"""Write the deterministic make.fun review entry using only the standard library."""

import os
from pathlib import Path


REVIEW = "★☆☆☆☆ Water. Got the dirt off my hands. Now I need something to get the water off."


def main() -> None:
    if not 1 <= len(REVIEW) <= 160:
        raise ValueError("Review must contain 1 to 160 characters.")
    if not REVIEW.strip():
        raise ValueError("Review must not be only whitespace.")
    if len(REVIEW.splitlines()) != 1 or REVIEW.endswith(("\n", "\r")):
        raise ValueError("Review must occupy one line with no trailing newline.")
    payload = REVIEW.encode("utf-8", errors="strict")
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
