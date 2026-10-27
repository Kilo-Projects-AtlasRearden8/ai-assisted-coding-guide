# Fixing Errors

Errors are normal. Every programmer gets them, every day. AI-written code gets
them too. This guide shows you how to read an error message, fix the problem,
and work with the AI to get unstuck — without panicking.

## Errors are information, not failure

An error message is the computer telling you exactly what went wrong and where.
It is not a judgment on your ability. Read it like a friend pointing out a
typo.

## How to read a Python error (example)

Say you run a script and see this:

```
Traceback (most recent call last):
  File "greet.py", line 4, in <module>
    print(greeting)
NameError: name 'greeting' is not defined
```

Read it bottom-up:

- **Last line:** `NameError: name 'greeting' is not defined`
  - What: You used a variable called `greeting` that doesn't exist.
  - Fix: Define `greeting` before using it, or check the spelling.
- **Second-to-last line:** `File "greet.py", line 4, in <module>`
  - Where: The problem is in `greet.py` on line 4.

The traceback lists each function call leading to the error, with the most
recent (the actual failure) at the bottom. The bottom line is usually the most
useful.

## Common error types and what they mean

| Error | Plain-English meaning | Typical fix |
|-------|----------------------|-------------|
| `NameError` | You used a name that hasn't been defined | Check spelling; define the variable first |
| `TypeError` | You used a value in a way it doesn't support | Make sure you're passing the right kind of data |
| `FileNotFoundError` | The program looked for a file that isn't there | Check the file path and spelling |
| `SyntaxError` | The code has a typo the computer can't parse | Check parentheses, quotes, colons, indentation |
| `ImportError` / `ModuleNotFoundError` | A library is missing or misspelled | Install it, or check the import name |
| `IndexError` | You asked for an item that doesn't exist in a list | Check the list length before indexing |
| `KeyError` | You asked for a dictionary key that isn't there | Use `.get()` or check the key exists |

## The fix-it loop

1. **Read the error.** Copy the full message.
2. **Find the line.** Look at the file and line number in the traceback.
3. **Make one small change.** Guess the smallest fix, not a rewrite.
4. **Run again.** See if the error changed or disappeared.
5. **Repeat.** Errors often come in waves; fixing one reveals the next.

Never change ten things at once. You won't know which one helped.

## Working with the AI to fix errors

Paste the error and your code back into the AI chat:

> I'm getting this error:
> 
> ```
> [paste the full error message]
> ```
> 
> Here is my code:
> 
> ```python
> [paste your code]
> ```
> 
> Can you help me fix it? Please explain what changed.

Tell the AI:

- What you expected to happen
- What actually happened
- The full error message (don't paraphrase)
- What you've already tried

## Terminal safety while fixing

Some fixes involve running commands. See [terminal safety](terminal-safety.md)
before you run anything the AI suggests, especially `pip install`, `rm`, or
anything with `sudo`.

## When the AI's fix doesn't work

AI can suggest wrong fixes, just like it can write wrong code. If the AI's
suggestion:

- Doesn't change the error
- Makes a new error appear
- Uses code you don't understand

…then revert the change, paste the new error back to the AI, or ask a human.
You are allowed to say "that didn't work, try again."

## Your error-fixing checklist

- [ ] I read the full error message, especially the last line
- [ ] I found the file and line number
- [ ] I made one small change at a time
- [ ] I ran the code again after each change
- [ ] I understand what my fix actually did
- [ ] I did not run any dangerous terminal commands without checking them first

---

*Published by Asdale Dynamics, LLC. Plain English, step by step, never condescending.*
