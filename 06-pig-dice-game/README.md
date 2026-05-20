# 06 — PIG Dice Game

A two-player terminal dice game where players take turns rolling a die, accumulating points, and deciding when to bank their score. First to 50 wins. Rolling a 1 wipes your turn score.

## How to Run

```bash
python pig.py
```

No external dependencies — uses Python's built-in `random` and `time` modules.

## How to Play

- On your turn, roll the dice
- Any roll except 1 adds to your **turn score**
- Choose to keep rolling or bank your points
- Rolling a 1 ends your turn and wipes your turn score
- First player to reach **50 points** wins

## Example

```
Player_1's Turn!
Player_1's Score: 0
Dice Rolled: 4
Round Score: 4
Do you want to roll another time? (Enter 'y' or 'n') y
Dice Rolled: 1
Round Score: 0
Player_1's Score: 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Player_2's Turn!
...
```

## What I Learned

- Passing current score into a function and returning updated state
- Nested `while` loops — outer for the turn, inner for the y/n prompt
- Using a `rolling` boolean flag to control loop exit cleanly
- `sleep()` to add pacing and make gameplay feel natural
- Win/tie condition logic comparing two scores simultaneously

## What I'd Improve

- Add player name input instead of hardcoded Player_1 and Player_2
- Support more than 2 players using a list of scores and a loop
- Add a scoreboard display at the start of each round showing both scores
- Let players configure the winning score instead of hardcoding 50

Bruh Claude just want to find mistakes it is perfect as is if i wanted to think of other features i would never be able to complete a project.