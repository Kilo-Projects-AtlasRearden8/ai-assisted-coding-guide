# Reading AI-Written Code

AI can write code fast, but it can also write code that looks right and does
something subtle you didn't intend. This guide teaches you how to read
AI-written code before you run it, so you stay in control.

## Why read the code at all?

You are the author. The AI is a typing assistant that happens to be very fast
and very confident. Confident is not the same as correct.

AI-written code can:

- Use libraries you don't have installed
- Reference files or folders that don't exist on your computer
- Contain subtle bugs that only show up with certain inputs
- Do things you didn't ask for (like reaching out to the internet)

Reading the code first is how you catch these problems before they become
your problems.

## A three-step reading habit

Use these steps every time the AI hands you code.

### 1. Skim the whole file first

Read from top to bottom without trying to understand every line. Ask:

- What is this program supposed to do?
- Does it mention any file names, folder names, or website addresses?
- Does it import or install anything?
- How long is it? (A 500-line file for "hello world" is a red flag.)

### 2. Read it line by line

Look at each line and translate it into plain English in your head. If you
can't explain what a line does, don't run it yet.

Look specifically for:

- **Imports / `require` / `include`** — what outside code is being pulled in?
- **File operations** — `open`, `write`, `delete`, `remove`. What files will it touch?
- **Network calls** — `fetch`, `requests.get`, `urllib`. Is it contacting the internet?
- **Loops and conditions** — does the logic match what you asked for?
- **Hard-coded values** — passwords, API keys, specific usernames, file paths

### 3. Run it in a safe place first

Never run AI-written code on your main computer for the first time. See the
[terminal safety guide](terminal-safety.md) for how to test code safely.

## Line-by-line example

Here is a tiny AI-written script, and how to read it.

```python
import os
import requests

filename = "notes.txt"
with open(filename, "w") as f:
    f.write("Hello from AI")

response = requests.get("https://example.com")
print(response.text)
```

Reading it line by line:

| Line | What it does | Question to ask |
|------|--------------|-----------------|
| `import os` | Pulls in the operating-system module | Do we actually need this? (Here, no.) |
| `import requests` | Pulls in a library to fetch web pages | Is `requests` installed? Will it reach the internet? |
| `filename = "notes.txt"` | Picks a file name | Will this overwrite a file I care about? |
| `open(filename, "w")` | Opens `notes.txt` for writing | `"w"` erases existing content. Is that okay? |
| `f.write("Hello from AI")` | Writes text into the file | Fine, harmless. |
| `requests.get(...)` | Downloads a web page | Does it need internet? Is that expected? |
| `print(response.text)` | Prints the page content | Fine, just display. |

This script creates a file and downloads a web page. If you only wanted a
local note, the internet call is unexpected. You would ask the AI to remove it.

## Questions to ask the AI about its code

You can paste the AI's code back into the chat and ask:

- "What does this line do?"
- "Does this code access the internet?"
- "Does this code write or delete any files?"
- "What could go wrong if I run this with bad input?"
- "Can you explain this without using jargon?"

A good AI will explain itself. If it can't, that's a sign not to run the code.

## Red flags — stop and ask

Stop and get a second opinion (from a friend, a forum, or a more experienced
coder) if you see:

- Passwords, API keys, or tokens pasted into the code
- `eval(`, `exec(`, or `compile(` with user input
- A command that deletes files (`rm`, `del`, `os.remove`, `shutil.rmtree`)
- A web address you don't recognize
- Code that installs other programs (`pip install`, `apt install`, `npm install`) without explaining why

## Your checklist before running AI code

- [ ] I can explain what each line does
- [ ] I know what files it will read, write, or delete
- [ ] I know whether it uses the internet
- [ ] I have tested it in a safe, isolated place
- [ ] I know how to undo what it does (delete the output file, etc.)

If you can't check every box, don't run it yet. Ask for help.

---

*Published by Asdale Dynamics, LLC. Plain English, step by step, never condescending.*
