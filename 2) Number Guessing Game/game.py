"""
The Basic Idea:
Randomization: The program uses the random module to select a secret number within a range defined by the user (e.g., 1 to 10).
Looping: It employs a while loop to allow the user to keep guessing until they hit the correct number.
Conditional Feedback: The program provides helpful feedback by telling the user if their guess was too high or too low, helping them narrow down the answer.
Input Validation: It teaches you how to handle user input securely, specifically ensuring the input is a valid number before comparing it to the secret value.
"""

#I already built something like this in my cs50p course so i will just paste that here!


"""
In a file called game.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random
while True:
    n=int(input("Level: "))
    if n>0:
        break
    else:
        continue
p=random.randint(1, n)
while True:
    try:
        x=int(input("Guess: "))
        if x<=0:
            continue
        if x<p:
            print("Too small!")
            continue
        elif x==p:
            print("Just right!")
            break
        elif x>p:
            print("Too large!")
            continue
    except ValueError:
        pass


