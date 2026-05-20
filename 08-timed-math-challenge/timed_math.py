"""
Problem Generation Engine: The program uses a list of operators (like +, -, *) and the random module to pick two numbers and an operator. 
It creates a string representation of the equation (e.g., "5 + 3") and simultaneously calculates the result using the eval() function or basic 
conditional logic.
The Timing Mechanism: Before starting the loop of questions, the program captures the current time using time.time(). This sets the "start point."
The While Loop: The program enters a loop that runs for a set number of questions. Inside this loop:
It generates a new problem.
It enters a nested while loop that forces the user to input an answer.
Input Validation: The nested loop checks if the user's input matches the calculated result. If the user is wrong, 
it prints an error and repeats the prompt. It only breaks out of this inner loop when the correct answer is provided.
Performance Calculation: Once the outer loop finishes (all questions answered), it captures the time again. 
By subtracting the "start point" from the "end point," it derives the total elapsed seconds.
"""
import random
from time import sleep, time

def greet():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Hey, welcome!")
    print("Let's check your problem solving skills.")
    print("And see how much time you take to solve these questions!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(3)
    
def gen_rand_num():
    return random.randint(0, 10)

def gen_rand_op():
    return random.choice(['*', '-', '+'])

def check_start_time():
    return time()

def get_answer(x, y, op):
    while True:
        try:
            return int(input(f"{x} {op} {y} = "))

        except ValueError:
            print("Enter a number dumbass!")
            continue

def calc_answer(x, y, op):
    if op=="+":
        return x + y
    elif op=="-":
        return x - y
    else:
        return x * y

def check_answer(user_answer, correct_answer):
    print(f"Correct Answer: {correct_answer}")
    print(f"Your Answer: {user_answer}")
    if user_answer==correct_answer:
        print("Correct Answer! 🙌💯")
    else:
        print("Wrong Answer! 🤷‍♂️🤦‍♂️")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def check_end_time():
    return time()

def calc_time_elapsed(st_time, end_time):
    print(round(end_time - st_time))
    
def main():
    greet()
    st_time=check_start_time()
    for _ in range(10):
        x=gen_rand_num()
        y=gen_rand_num()
        op=gen_rand_op()
        user_answer=get_answer(x, y, op)
        correct_answer=calc_answer(x, y, op)
        check_ans=check_answer(user_answer, correct_answer)
    end_time=check_end_time()
    calculate_time_elapsed=calc_time_elapsed(st_time, end_time)

if __name__=="__main__":
    main()