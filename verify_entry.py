"""Run the entry twice and verify its output without third-party dependencies."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent


def check_output(payload: bytes) -> None:
    review = payload.decode("utf-8", errors="strict")
    if not 1 <= len(review) <= 160:
        raise ValueError("Output must contain 1 to 160 characters.")
    if not review.strip():
        raise ValueError("Output must not be only whitespace.")
    if payload.endswith((b"\n", b"\r")):
        raise ValueError("Output must not have a trailing newline.")
    if len(review.splitlines()) != 1:
        raise ValueError("Output must occupy exactly one line.")


def main() -> None:
    # Keep temporary output inside the repository and remove it automatically.
    with tempfile.TemporaryDirectory(prefix=".verify-entry-", dir=ROOT) as temp:
        outputs = []
        for name in ("first", "second"):
            output_dir = Path(temp) / name
            env = os.environ.copy()
            env["OUTPUT_DIR"] = str(output_dir)
            subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                cwd=ROOT,
                env=env,
                check=True,
                capture_output=True,
            )
            payload = (output_dir / "entry.txt").read_bytes()
            check_output(payload)
            outputs.append(payload)
        if outputs[0] != outputs[1]:
            raise ValueError("The two runs produced different bytes.")
        digest = hashlib.sha256(outputs[0]).hexdigest()
    print(f"PASS sha256={digest}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
