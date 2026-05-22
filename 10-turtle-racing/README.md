# The Ultimate Turtle Race

A graphical racing game where six colorful turtles compete across the screen. Place your bet on a turtle and watch the race unfold with randomized movements.

## How to Run

```bash
python turtle_race.py
```

No external dependencies — uses Python's built-in `turtle` and `random` modules.

## How to Play

- Enter the color of the turtle you think will win (red, orange, yellow, green, blue, purple)
- Watch as all six turtles race across the screen
- Each turtle moves forward by a random distance (0-10 pixels) each turn
- First turtle to cross the finish line (x-coordinate > 230) wins
- Check the console to see if you won your bet
- Click anywhere on the screen to exit

## Example

```
Make your bet
Which turtle will win the race? Enter a color: blue

[Race happens on screen]

You've won! The blue turtle is the winner!
```

## What I Learned

- Using the `turtle` module for graphical output and animations
- Creating multiple turtle objects and storing them in a list
- Using `textinput()` for GUI-based user input
- Coordinate system in turtle graphics (x and y positioning)
- Breaking out of nested loops with flags (`is_race_on`)
- Comparing object attributes (`.pencolor()`, `.xcor()`) for game logic

## What I'd Improve

- Draw a visible finish line on the screen instead of using invisible coordinates
- Display win/loss message on the GUI window instead of console
- Add a visual starting countdown (3, 2, 1, GO!)
- Show a scoreboard or betting odds before the race starts
