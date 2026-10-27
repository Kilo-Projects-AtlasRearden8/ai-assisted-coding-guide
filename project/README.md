# expense-total

A tiny command-line tool that adds up a file of expenses, one amount per line.
Built as the first project in the *AI-Assisted Coding: A Beginner's Manual*.

## What it does

Reads a text file of amounts and prints the total. Blank lines and comment
lines (starting with `#`) are ignored. Invalid lines are skipped with a
warning. Nothing is written to disk and no network is used.

## How to run

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate
# On Windows: .venv\Scripts\activate

# Run the tool
python expense-total.py expenses.txt
```

Example output:

```
Warning: skipping invalid amount 'not-a-number'
Total: $46.35
```

## Example input

`expenses.txt`:

```
# My weekly expenses
12.50
3.75

8.00
not-a-number
22.10
```

## How to test

Uses Python's built-in `unittest` — nothing to install.

```bash
python -m unittest discover -s . -v
```

## Files

- `expense-total.py` — the tool
- `test_expense_total.py` — automated tests
- `expenses.txt` — example input file

## About

Published by **Asdale Dynamics, LLC**. Plain English, step by step, never
condescending. MIT License — see the repository `LICENSE`.
