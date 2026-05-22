"""
Concept: A graphical game using Python's built-in turtle library where multiple colorful turtles race across the screen.
Library Utilization: It introduces the turtle graphics module, which is a standard library tool for creating shapes and simple animations.
Game Setup: The script initializes the screen, creates a set of racer objects (turtles), and positions them at the starting line.
Animation Loop: It uses a loop to continuously move each turtle forward by a random distance until one crosses the finish line.
Win Condition: The program identifies the winner by checking when a turtle's coordinate exceeds the finish line threshold.
Object-Oriented Programming (OOP): Interacting with turtle objects (instantiating and calling methods like forward() or goto()).
Random Module: Using random.randrange() to give each racer a different movement increment, ensuring a fair but unpredictable race.
Event Handling: Simple loops to control the game state and display the result once a winner is declared
"""
import turtle, random
def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    screen.title("The Ultimate Turtle Race")
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ",
    )
    if user_bet:
        user_bet = user_bet.lower().strip()
    else:
        user_bet = ""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-100, -60, -20, 20, 60, 100]
    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)
    is_race_on = False
    if user_bet:
        is_race_on = True
    while is_race_on:
        for racer in all_turtles:
            if racer.xcor() > 230:
                is_race_on = False
                winning_color = racer.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                break
            random_distance = random.randint(0, 10)
            racer.forward(random_distance)
    screen.exitonclick()
if __name__ == "__main__":
    main()
