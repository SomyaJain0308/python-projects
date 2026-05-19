# 🐍 Python Projects — Tech With Tim's 21 Projects

A collection of 21 Python projects built by following [Tech With Tim's 9-hour beginner-to-advanced project series](https://www.youtube.com/watch?v=NpmFbWO6HPU). This repo is part of my journey to rebuild Python fundamentals from scratch and eventually move into AI red teaming.

---

## 📁 Projects

| # | Project | Difficulty |
|---|---------|------------|
| 01 | [Quiz Game](./01-quiz-game) | Easy |
| 02 | [Number Guessing Game](./02-number-guessing-game) | Easy |
| 03 | [Rock, Paper, Scissors](./03-rock-paper-scissors) | Easy |
| 04 | [Choose Your Own Adventure Game](./04-choose-your-own-adventure) | Easy |
| 05 | [Password Manager](./05-password-manager) | Medium |
| 06 | [PIG Dice Game](./06-pig-dice-game) | Medium |
| 07 | [Madlibs Generator](./07-madlibs-generator) | Medium |
| 08 | [Timed Math Challenge](./08-timed-math-challenge) | Medium |
| 09 | [Slot Machine](./09-slot-machine) | Medium |
| 10 | [Turtle Racing](./10-turtle-racing) | Medium |
| 11 | [WPM Typing Test](./11-wpm-typing-test) | Medium |
| 12 | [Alarm Clock](./12-alarm-clock) | Easy |
| 13 | [Password Generator](./13-password-generator) | Easy |
| 14 | [Shortest Path Finder](./14-shortest-path-finder) | Advanced |
| 15 | [NBA Stats & Current Scores](./15-nba-stats) | Medium |
| 16 | [Currency Converter](./16-currency-converter) | Medium |
| 17 | [YouTube Video Downloader](./17-youtube-downloader) | Medium |
| 18 | [Automated File Backup](./18-automated-file-backup) | Medium |
| 19 | [Mastermind / 4 Color Match](./19-mastermind) | Advanced |
| 20 | [Aim Trainer](./20-aim-trainer) | Advanced |
| 21 | [Advanced Python Scripting](./21-advanced-scripting) | Advanced |

---

## 🎯 Goal

I completed CS50P but lost most of it. This repo is me rebuilding Python through projects — hands-on, no rewatching lectures. Each project is built independently, not copied along.

The end goal is to get solid enough in Python to move into AI red teaming (prompt injection, LLM security testing, PyRIT, etc.).

---

## 🔄 My Workflow

Every project in this repo follows the same process:

1. **Never Watch** Tech With Tim's walkthrough for the project
2. **Ask Gemini** for a breakdown of the project's key features and concepts
3. **Paste that breakdown as a docstring** at the top of the Python file — so the intent is documented before a single line of code is written
4. **Build it myself from scratch** without copying Tim's code
5. **Ask Claude** to generate the project README and give an honest review of what to improve

The docstring at the top of each file (from step 3) looks like this:

```python
"""
The Quiz Game is a beginner-friendly project designed to introduce fundamental
programming concepts like input handling, string manipulation, and basic conditional logic.

User Interaction: The program prompts the user to play and collects their answers.
Logic & Flow: It checks if the user's input matches the correct answer using .lower().
Score Tracking: A score variable increments on each correct answer.
Feedback: The program provides a final score summary after all questions.
"""
```

This keeps the code self-documenting and makes it easy to see what each project was supposed to teach.

---

## 📌 Notes

- Each project folder has its own `README.md` explaining what it does, how to run it, and what I learned.
- Projects are pushed as they're completed — the repo will fill up over time.
- Credit to [Tech With Tim](https://www.youtube.com/@TechWithTim) for the original project ideas and walkthroughs.

## 🚀 Auto Git Push

If you want changes to be auto-pushed after 5 seconds of idle time, run the watcher task in VS Code:

1. Open the Command Palette.
2. Choose `Tasks: Run Task`.
3. Select `Start Auto Git Push`.

This starts `scripts/auto_git_push.py`, which:

- detects file changes in the repository,
- waits for 5 seconds of inactivity,
- stages all changes,
- creates an automatic commit,
- pushes to the current branch.

> Note: This will push directly to the current branch. If the remote branch has diverged, you may need to resolve the conflict manually.
