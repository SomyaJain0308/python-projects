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
        num = int(input("How many characters do you want it to be? "))
        if num < 8:
            print("Too Short let's make the password a bit discreet!")
            continue
        elif num > 16:
            print("Woah! are you trynna forget it? Let's make it smaller.")
            continue
        else:
            break
    except ValueError:
        print("Enter a number!")
pool = string.ascii_letters + string.digits + string.punctuation
while True:
    password_list = random.choices(pool, k=num)    
    has_letter = any(c in string.ascii_letters for c in password_list)
    has_digit = any(c in string.digits for c in password_list)
    has_symbol = any(c in string.punctuation for c in password_list)
    if has_letter and has_digit and has_symbol:
        break
print("".join(password_list))
