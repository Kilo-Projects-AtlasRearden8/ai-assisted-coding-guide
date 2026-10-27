# First Project Walkthrough

This is your first real project: a tiny command-line tool that adds up a file of
expenses and prints the total. We'll build it step by step with AI help, read
the code, run it safely, and test it.

The finished project lives in `project/`. You can follow along here, or just
read the project files directly.

## What we're building

**`expense-total`** — a Python tool that:

- Reads a text file where each line is an amount (like `12.50`)
- Ignores blank lines and lines starting with `#`
- Prints the total
- Prints an error message if the file is missing or has bad data

Example:

```
$ python expense-total.py expenses.txt
Total: $47.35
```

## Step 1: Set up a safe workspace

Create a folder just for this project. Everything you do here stays here.

```bash
mkdir my-first-project
cd my-first-project
```

For Python, set up a virtual environment so installations don't touch the rest
of your computer:

```bash
python -m venv .venv
source .venv/bin/activate
# On Windows: .venv\Scripts\activate
```

## Step 2: Ask the AI for the first version

Paste this into a free AI tool:

> Write a Python script called expense-total.py that reads a text file whose
> path is given as a command-line argument. Each line of the file is an amount
> like 12.50. The script should print the total. Ignore blank lines and lines
> starting with #. If the file doesn't exist, print a friendly error. If a line
> isn't a valid number, skip it and print a warning. I'm a beginner — keep the
> code short and explain each part.

Copy the AI's answer into a file called `expense-total.py`.

## Step 3: Read the code before running it

Open `expense-total.py` and read it line by line (see reading-ai-code.md). Ask:

- Does it read the file I give it?
- Does it write or delete anything? (It shouldn't.)
- Does it use the internet? (It shouldn't.)
- Can I explain what each function does?

If anything is unclear, paste it back to the AI and ask for an explanation.

## Step 4: Create a test expenses file

Make a file called `expenses.txt`:

```
# My weekly expenses
12.50
3.75

8.00
not-a-number
22.10
```

The blank line, the comment (`#`), and the bad value (`not-a-number`) let us
test that the script handles them correctly.

## Step 5: Run it

```bash
python expense-total.py expenses.txt
```

Expected output:

```
Warning: skipping invalid line: not-a-number
Total: $46.35
```

(12.50 + 3.75 + 8.00 + 22.10 = 46.35)

## Step 6: Test error handling

Run it on a file that doesn't exist:

```bash
python expense-total.py missing.txt
```

You should get a friendly error message, not a crash.

Run it with no arguments:

```bash
python expense-total.py
```

You should get a usage message.

## Step 7: Add tests

A test is a small program that checks your code works correctly. The project
includes `test_expense_total.py` which uses Python's built-in `unittest`.

Run the tests:

```bash
python -m unittest discover -s project -v
```

All tests should pass. If one fails, read the error (see fixing-errors.md) and
fix the code.

## Step 8: Reflect

You just:

- Wrote code with AI help
- Read it before running
- Ran it in a safe folder
- Tested good input, bad input, and missing files
- Added automated tests

That's the whole loop. Every future project is the same, just bigger.

## The finished files

| File | Purpose |
|------|---------|
| `project/expense-total.py` | The tool |
| `project/test_expense_total.py` | Automated tests |
| `project/expenses.txt` | Example input file |
| `project/README.md` | How to run it |

---

*Published by Asdale Dynamics, LLC. Plain English, step by step, never condescending.*
