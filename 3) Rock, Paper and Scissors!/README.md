# 03 — Rock, Paper, Scissors

A terminal Rock, Paper, Scissors game against the computer with score tracking and continuous gameplay until the user quits.

## How to Run

```bash
python rps.py
```

No external dependencies — uses Python's built-in `random` module.

## Example

```
-----------------------------------------------------------------------
Let's play Rock, Papers and Scissors
Instructions:
1) Rock 🪨 = '1'
2) Paper 📃 = '2'
3) Scissor ✂️ = '3'
4) Quit: To Quit Press '^C'.
-----------------------------------------------------------------------
What do you choose? ['1', '2', '3'] 1
You: Rock 🪨
Computer: Scissor ✂️
You Won!
Score: 1
-----------------------------------------------------------------------
```

## What I Learned

- Breaking a program into functions (`greet_user`, `user_choice`, `computer_choice`, `calc_result`, `main`)
- Using `if __name__ == "__main__"` as an entry point guard
- Passing values into functions and returning updated state (score)
- `try/except ValueError` combined with range validation for clean input handling

## What I'd Improve

- Remove the `score = score` lines in lose/draw branches — they do nothing
- Track both `user_score` and `computer_score` separately instead of just user score
- Replace `^C` to quit with a `q` input option for a cleaner exit
- Fix double underscore variable names (`computer__choice` → `computer_choice`) — single underscore is the Python convention
