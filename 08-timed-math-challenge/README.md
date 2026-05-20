# 08 — Timed Math Challenge

A terminal math quiz that generates 10 random arithmetic problems, checks your answers, and tells you how long you took to complete them all.

## How to Run

```bash
python math_challenge.py
```

No external dependencies — uses Python's built-in `random` and `time` modules.

## Example

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hey, welcome!
Let's check your problem solving skills.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5 + 3 = 8
Correct Answer: 8.0
Your Answer: 8.0
Correct Answer! 🙌💯
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...
Total Time: 42 seconds
```

## What I Learned

- Breaking every step into its own function — generation, validation, calculation, display, timing
- `time()` to capture start and end points and calculate elapsed time
- Using conditional logic instead of `eval()` for safer answer calculation
- `float()` input to handle decimal results from subtraction

## What I'd Improve

- Missing inner re-prompt loop — wrong answers should force a retry, not just show the result and move on
- `check_start_time()` and `check_end_time()` are unnecessary wrappers around `time()` — call it directly
- No score tally at the end — should show "You got X/10 correct"
- `calc_time_elapsed()` prints but returns `None`, then gets assigned to a variable — either return the value or don't assign it

I wanted to try a lot of defining function in this one that' why you would think that there is a lot of unnecessary defined functions.