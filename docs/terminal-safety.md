# Terminal Safety

The terminal (also called the command line, console, or shell) is where you
type commands to your computer. It is powerful, and power means you can hurt
things by mistake. This guide shows beginners how to use the terminal safely,
especially when running AI-suggested commands.

## The golden rule

Never paste and run a terminal command you don't understand. If the AI gives
you a command, read it first. Ask the AI what each part does if you're unsure.

## Commands that deserve extra caution

Treat these as "stop and think" commands:

| Command | What it can do | Why to be careful |
|---------|---------------|-------------------|
| `rm` / `del` | Deletes files or folders | Deleted files usually don't go to trash |
| `rm -rf` | Deletes a folder and everything inside it | Can wipe your documents in one keystroke |
| `sudo` / `runas` | Runs a command as administrator | Gives the command full system access |
| `pip install` / `npm install` | Downloads and installs code from the internet | Runs other people's code on your machine |
| `curl ... \| sh` / `wget ... \| sh` | Downloads a script and runs it immediately | You can't review the script before it runs |
| `chmod +x` | Makes a file executable | Combined with running it, can launch anything |
| `format` / `diskpart` | Erases a disk | Permanent data loss |

If you see any of these in an AI suggestion, slow down and verify.

## Safe ways to experiment

### Use a folder just for experiments

Create a folder you don't care about, and do your AI coding inside it:

```bash
mkdir ai-experiments
cd ai-experiments
```

If something goes wrong, delete the whole folder. Your important files are
untouched.

### Use a virtual environment (Python)

Python projects can install libraries without touching your whole computer:

```bash
python -m venv .venv
source .venv/bin/activate
# On Windows: .venv\Scripts\activate
```

Now `pip install` only affects this folder, not your system.

### Read before you run

If the AI says "run this command," ask:

> What does this command do? Will it change or delete any files? Will it use the internet?

Only run it when the answer makes sense to you.

### Undo plans

Before you run something that writes or deletes files, ask yourself: "How do I
undo this?" If you can't answer, don't run it yet.

## A safe first command session

Try these harmless commands to get comfortable:

```bash
pwd          # shows where you are
ls           # lists files in the current folder
cd ai-experiments  # moves into that folder
mkdir test   # creates a folder called test
```

None of these can hurt your data.

## If something goes wrong

- **Don't panic.** Most terminal mistakes are recoverable.
- **Don't run more commands to "fix it" blindly.** That often makes it worse.
- **Close the terminal** if you're unsure. Nothing running in it will continue.
- **Ask a human** or search for the exact error message.

## Your terminal safety checklist

- [ ] I understand what the command does
- [ ] I know whether it will delete, overwrite, or install anything
- [ ] I know whether it uses the internet
- [ ] I am working in an experiment folder, not among my important files
- [ ] I know how to undo what the command does

If any box is unchecked, stop and ask.

---

*Published by Asdale Dynamics, LLC. Plain English, step by step, never condescending.*
