# 02 — Number Guessing Game

A number guessing game where the user sets a difficulty level and tries to guess a randomly generated number, receiving "too high" or "too low" feedback until they get it right.

> This project was already completed during CS50P, so the solution here is carried over from that course rather than built from scratch.

## How to Run

```bash
python game.py
```

No external dependencies — uses Python's built-in `random` module.

## Example

```
Level: 10
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 6
Just right!
```

## What I Learned

- Using the `random` module to generate a number within a user-defined range
- `while` loops for re-prompting until valid input or correct guess
- `try/except ValueError` to handle non-integer input without crashing
- Giving directional feedback (too small / too large) to guide the user

## What I'd Improve

- Wrap the level input in a `try/except` block — currently crashes if the user types a non-integer at the level prompt
- Remove the redundant `else: continue` in the level loop — the loop continues automatically without it
- Add a guess counter so the user knows how many attempts it took at the end
