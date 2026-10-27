#!/usr/bin/env python3
"""expense-total.py

Add up the amounts in a text file, one amount per line.

Usage:
    python expense-total.py <file>

Behavior:
- Blank lines and lines starting with '#' are ignored.
- Lines that are not valid numbers are skipped with a warning.
- If the file is missing, a friendly error is printed.
- Nothing is written to disk and no network is used.
"""

import sys


def parse_amount(line):
    """Return a float for a valid amount line, or None if invalid."""
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    try:
        return float(stripped)
    except ValueError:
        return None


def total_expenses(filename):
    """Return (total, warnings) for the given expenses file.

    total: sum of all valid amounts
    warnings: list of warning strings for skipped invalid lines
    """
    total = 0.0
    warnings = []

    with open(filename, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            amount = parse_amount(line)
            if amount is None:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    warnings.append(
                        "Line {}: skipping invalid amount {!r}".format(
                            line_number, stripped
                        )
                    )
                continue
            total += amount

    return total, warnings


def main(argv):
    if len(argv) != 2:
        print("Usage: python expense-total.py <file>")
        return 1

    filename = argv[1]

    try:
        total, warnings = total_expenses(filename)
    except FileNotFoundError:
        print("Error: file not found: {}".format(filename))
        return 1
    except OSError as exc:
        print("Error: could not read file {}: {}".format(filename, exc))
        return 1

    for warning in warnings:
        print(warning)

    print("Total: ${:.2f}".format(total))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
