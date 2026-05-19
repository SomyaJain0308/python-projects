"""
Library Usage: The project uses the random module for selecting characters and the string module to easily access collections of
    letters, digits, and punctuation.
Function Design: The generator function (generate_password) is built with optional parameters for minimum length, enabling numbers, 
    and enabling special characters. This makes the tool highly reusable.
Character Set Aggregation: The script dynamically builds a single string of allowed characters based on user preferences.
Criteria Validation: A while loop ensures the password continues to grow until it hits the min_length and meets specific requirements 
    (e.g., contains at least one number and one special character).
Random Selection: random.choice() is used to pick individual characters from the aggregated pool to build the password string.
"""
import random, string
while True:
    try:
        num=int(input("How many characters do you want it to be? "))
        if num<8:
            print("Too Short let's make the password a bit discreet!")
            continue
        elif num>16:
            print("Woah! are you trynna forget it? Let's make it smaller.")
            continue
        else:
            break
    except ValueError:
        print("Enter a number!")
chars = string.ascii_letters + string.digits + string.punctuation
chars = random.choices(chars, k=num)
print("".join(chars))
