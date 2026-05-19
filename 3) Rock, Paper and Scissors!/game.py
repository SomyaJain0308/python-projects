"""
The third project in the video is Rock, Paper, Scissors. This project builds on previous logic by introducing the random module to simulate a computer opponent 
and while loops for continuous gameplay.
The Basic Idea:
Computer Selection: The program uses random.randint to pick between 'rock', 'paper', and 'scissors'.
Conditional Logic: It utilizes multiple elif statements to compare the user's input against the computer's choice to determine the winner.
Score Tracking: It maintains variables (user_wins and computer_wins) to keep a running tally of the score throughout the session.
"""
import random, sys
def computer_choice():
    computer__choice= random.randint(1, 3)
    if computer__choice==1:
        print("Computer chose Rock 🪨!")
        return 1
    elif computer__choice==2:
        print("Computer chose Paper 📃!")
        return 2
    elif computer__choice==3:
        print("Computer chose Scissor ✂️!")
        return 3

def user_choice():
    while True:
        try:
            user__choice=input("What do you choose? ['1', '2', '3'] ").strip()
            user__choice=int(user__choice)
            if user__choice==1:
                print("You chose Rock 🪨!")
                return 1
            elif user__choice==2:
                print("You chose Paper 📃!")
                return 2
            elif user__choice==3:
                print("You chose Scissor ✂️!")
                return 3
            else:
                print("Type '1' or '2' or '3' dumbass")
                continue
        except ValueError:
            print("Type '1' or '2' or '3' dumbass")

def greet_user():
    print("-----------------------------------------------------------------------")
    print("Let's play Rock, Papers and Scissors")
    print("Instructions:")
    print("1) Rock 🪨 = '1'")
    print("2) Paper 📃 = '2'")
    print("3) Scissor ✂️ = '3'")
    print("4) Quit: To Quit Press '^C'.")
    print("-----------------------------------------------------------------------")

def calc_result(user_choice, computer_choice):
    score=0
    #User Wins
    if user_choice==1 and computer_choice==3:
        score+=1
        print("You Won!")
        print("Score:", score)
    elif user_choice==2 and computer_choice==1:
        score+=1
        print("You Won!")
        print("Score:", score)
    elif user_choice==3 and computer_choice==2:
        score+=1
        print("You Won!")
        print("Score:", score)
    #User Loses
    elif user_choice==1 and computer_choice==2:
        print("You Lost!")
        print("Score:", score)
    elif user_choice==2 and computer_choice==3:
        print("You Lost!")
        print("Score:", score)
    elif user_choice==3 and computer_choice==1:
        score=score
        print("You Lost!")
        print("Score:", score)
    #draw
    else:
        score=score
        print("It was a Draw!")   
        print("Score:", score)
    print("-----------------------------------------------------------------------")

 

def main():
    greet_user()
    score=0
    while True:

        calc_result(user_choice(), computer_choice())
    

if __name__=="__main__":
    main()
