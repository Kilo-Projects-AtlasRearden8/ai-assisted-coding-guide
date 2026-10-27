# STATUS

## What was built

A beginner manual and static HTML site on writing code with AI for free,
published by Asdale Dynamics, LLC (Indiana, formed October 2026).

**`docs/`** — Markdown manual:
- `index.md` — welcome, page map, about Asdale Dynamics, license, no-secrets policy
- `reading-ai-code.md` — read AI-written code before running; 3-step habit; line-by-line example; red flags; pre-run checklist
- `fixing-errors.md` — read error messages bottom-up; common error table; fix-it loop; working with the AI; checklist
- `terminal-safety.md` — golden rule; cautious commands table; safe experimentation; virtualenv; checklist
- `prompts-that-work.md` — traits of good prompts; copy/paste templates; free AI tools table; anti-prompts; checklist
- `when-to-ask-human.md` — signs to ask a human; who to ask; how to ask a good question; checklist
- `first-project.md` — build `expense-total`, a Python expense totaler, step by step
- `glossary.md` — plain-English definitions

**`site/`** — Static HTML site mirroring every doc page, with shared `style.css`.
8 HTML pages, all internal links validated.

**`project/`** — First small project walkthrough (runnable, tested):
- `expense-total.py` — CLI tool that sums amounts in a text file (ignores blanks/comments/invalid lines; no file writes; no network)
- `test_expense_total.py` — 9 unittest tests using Python's built-in unittest
- `expenses.txt` — example input file
- `README.md` — how to run and test

**Root files:** `README.md`, `LICENSE` (MIT, Copyright (c) 2026 Asdale Dynamics, LLC).

## How to run it

Read the manual: open any `docs/*.md` file in a text editor, or open
`site/index.html` in a web browser.

Run the first project:

```
cd project
python3 -m venv .venv        # optional, recommended
source .venv/bin/activate    # Windows: .venv\Scripts\activate
python3 expense-total.py expenses.txt
python3 -m unittest discover -s . -v
```

## Verification results

- Project tool `expense-total.py`: runs correctly on `expenses.txt`
  (outputs `Total: $46.35` with a warning for the invalid line), returns a
  friendly error for missing files, and a usage message for no arguments.
- Project tests: `python3 -m unittest discover -s . -v` → **9 tests, 0 failures, OK.**
- Static HTML site: all 8 pages validated; every internal link resolves;
  every page references `style.css` and has a `<title>`.
- Secret scan: no API keys, passwords, tokens, or personal data in any file.
  Matches are only educational text warning users not to share secrets.

## Known gaps

- Markdown files in `docs/` are not rendered by a static-site generator; the
  HTML in `site/` is hand-written and must be kept in sync manually if docs
  change.
- The project README references `python` while this environment only has
  `python3`; users should substitute `python3` where needed.
- No lint/typecheck tooling is configured for the tiny Python project (the
  code is small and reviewed by hand).
- No `.github/workflows` files (intentionally omitted per instructions).
