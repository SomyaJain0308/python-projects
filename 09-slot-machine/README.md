# 09 — Slot Machine

A text-based slot machine simulator with a real banking system, weighted symbol probability, multi-line betting, and win calculation based on symbol multipliers.

## How to Run

```bash
python slot_machine.py
```

No external dependencies — uses Python's built-in `random` module.

## How to Play

- Deposit an amount to start
- Choose how many lines to bet on (1–3)
- Set your bet per line
- Spin and win if all symbols on a line match
- Cash out anytime with `q`

## Example

```
Welcome to the Python Text Slot Machine!
Enter amount to deposit ($): 100

Current Balance: $100
Enter number of lines to bet on (1-3): 2
Enter bet per line ($): 10
Betting $10 on 2 lines. Total cost: $20

--- SPIN RESULTS ---
A | B | A
D | D | D
C | A | B
--------------------
🎉 You won $40!
Winning lines: 2
```

## Symbol Configuration

| Symbol | Frequency | Payout Multiplier |
|--------|-----------|-------------------|
| A | 2 | 5x |
| B | 4 | 4x |
| C | 6 | 3x |
| D | 8 | 2x |

Rarer symbols (A) pay more. Common symbols (D) pay less.

## What I Learned

- Weighted random selection by building a pool with `extend()` and picking from it
- Matrix transposition — spinning generates columns, `get_rows()` converts them to rows for win checking
- `len(set(row)) == 1` as a clean way to check if all elements in a list are identical
- Designing functions so `play_hand()` returns a net delta, keeping `main()` as just `wallet += play_hand(wallet)`
- Separating configuration (symbol pool, payouts, grid size) from logic at the top of the file

## What I'd Improve

- Replace `val.isdigit()` with `try/except int()` for more robust input validation
- Guard against negative wallet on exit with `max(0, wallet)` in the final print
- Add session stats at the end — total spins, net profit or loss
- Let the user reconfigure grid size or symbol values at the start

This code might look best yet it's because i made it earlier before i started these projects when i was doing the cs50p course and i had just too much time that's why i just copied that here.