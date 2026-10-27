# Prompts That Work

The quality of AI-written code depends heavily on the quality of your request.
This guide shows prompts that reliably produce useful, safe, beginner-friendly
code — using free AI tools.

## What makes a good prompt

Good AI coding prompts share these traits:

1. **Specific** — say what you want, what language, and what the input/output
   should be
2. **Small** — ask for one task at a time, not a whole app
3. **Contextual** — tell the AI your skill level and what you've tried
4. **Safety-aware** — say "don't use the internet" or "don't delete files" when
   that's what you want
5. **Iterative** — expect to refine the answer, not accept the first one

## Prompt templates you can copy

### "Write a small script to do X"

> Write a Python script that reads a file called `expenses.txt`, where each
> line is an amount like `12.50`, and prints the total. Keep it under 30 lines.
> Do not use the internet. Do not write to any files. Explain each part in
> plain English.

### "Explain this code"

> Explain what this code does, line by line, in plain English. Then list any
> things that could go wrong if I run it:
> 
> ```
> [paste code here]
> ```

### "Fix this error"

> I'm running this Python script and getting this error:
> 
> ```
> [paste full error message]
> ```
> 
> Here is my code:
> 
> ```python
> [paste code]
> ```
> 
> Please fix it and explain what changed. I'm a beginner, so keep the
> explanation simple.

### "Make this safer"

> Here is a script the AI wrote for me. Review it for safety problems:
> 
> 1. Does it access the internet?
> 2. Does it write, delete, or modify files?
> 3. Does it use any libraries I'd need to install?
> 
> Rewrite it to be safer if needed:
> 
> ```
> [paste code here]
> ```

### "Break this down"

> I want to build [a budget tracker / a greeting card maker / etc.]. I'm a
> beginner. Break this into tiny steps I can do one at a time. For each step,
> give me the exact code and the exact command to run it.

## Prompting for free AI tools

Free AI tiers often have limits (fewer messages per day, slower responses, no
file uploads). Work within them:

- **Keep prompts short** — saves your message limit
- **Paste code instead of uploading files** — works everywhere
- **Ask for one file at a time** — easier to copy-paste
- **Save good answers** — copy them into your own files so you don't lose them
  if you hit a message limit

## Free AI tools you can try

| Tool | Free tier | Notes |
|------|-----------|-------|
| GitHub Copilot (free tier) | Limited completions/month | Good inside VS Code |
| Claude (Anthropic) | Daily message limit | Strong at code explanation |
| ChatGPT (OpenAI) | Free model access | Good general coding help |
| Local models (Ollama, etc.) | Completely free, offline | Runs on your own computer; see local AI guides |

You do not need to pay for any of these to write code with AI as a beginner.

## Anti-prompts — what not to ask

Avoid asking the AI to:

- "Write me a full website / app" (too big; you'll get code you can't understand)
- "Find my passwords" or "log into my accounts" (never share secrets)
- "Hack into..." or "bypass..." (harmful and against most AI policies)
- "Write code with my API key hard-coded" (never put keys in code)

## Your prompting checklist

- [ ] I said what language I want
- [ ] I described the input and the expected output
- [ ] I asked for one small task
- [ ] I mentioned I'm a beginner
- [ ] I said whether internet or file access is allowed
- [ ] I read the code before running it (see reading-ai-code.md)

---

*Published by Asdale Dynamics, LLC. Plain English, step by step, never condescending.*
