#!/usr/bin/env python3
"""Entry: The GPS Swears It Was a Shortcut (make.fun one-liner)."""
import os

TEXT = (
    "Recalculating... for the fourth time. This WAS a shortcut: "
    "the road closed, the ferry left, your ETA grew two hours "
    "— but the DISTANCE was shorter. I stand by it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
