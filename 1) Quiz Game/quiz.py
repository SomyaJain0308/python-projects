"""
The Quiz Game is a beginner-friendly project designed to introduce fundamental programming concepts like input handling, string manipulation, 
and basic conditional logic.
User Interaction: The program prompts the user to play and collects their answers to a series of questions.
Logic & Flow: It checks if the user's input matches the correct answer, typically converting the input to lowercase using .lower() to ensure case-insensitive matching.
Score Tracking: It initializes a variable (e.g., score = 0) to keep track of correct answers, incrementing it every time the user provides a correct response.
Feedback: After completing the questions, the program calculates the final score and provides a summary (e.g., "You got 2 questions correct") 
"""
import sys
print("--------------------------------------------------------------------------------------------------------------")
print("Hi, Welcome to my quiz!")
print("Let's START!")
print("--------------------------------------------------------------------------------------------------------------")
score=0
while True:
    q1=input("Do you watch shows or movies? ").lower().strip()
    if q1=="yes":
        print("--------------------------------------------------------------------------------------------------------------")
        while True:
            q2=input("So... Which one do you prefer? Shows or Movies? ").lower().strip()
            if q2=="movies":
                print("--------------------------------------------------------------------------------------------------------------")
                while True:
                    q3=input("Let's actually start now!\nWhich is the better movie?\nA)Interstellar\nB)Inception\nC)Treasure vs Treasure Can't say!\nD)I am a dumbass and haven't watched them yet.\nYour Answer: ").strip().upper()
                    if q3=="A":
                        score+=2
                        print(f"I would choose the same!\nScore: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="B":
                        score+=1
                        print(f"Personally I would go with interstellar but can't hate Inception tho it's a gem of it's own!\n Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="C":
                        score+=1.5
                        print(f"Fuck Yeah both are awesome!\nScore {score}")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="D":
                        print("The fuck are you doing missing the goats go buy netflix sub!")
                        print(f"Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    else:
                        print("Type 'A' or 'B' or 'C' or 'D' dumbass!")
                        print("--------------------------------------------------------------------------------------------------------------")
                        continue
            elif q2=="shows":
                print("--------------------------------------------------------------------------------------------------------------")
                while True:
                    q3=input("Let's actually start now!\nWhich is the better show?\nA)Breaking Bad\nB)Money Heist\nC)Treasure vs Treasure Can't say!\nD)I am a dumbass and haven't watched them yet.\nYour Answer: ").strip().upper()
                    if q3=="A":
                        score+=2
                        print(f"I would choose the same!\n Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="B":
                        score+=1
                        print(f"Personally I would go with Breaking Bad but can't hate Money Heist tho it's a gem of it's own!\n Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="C":
                        score+=1.5
                        print(f"Fuck Yeah both are awesome!\n")
                        print(f"Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    elif q3=="D":
                        print("The fuck are you doing missing the goats go buy netflix sub!")
                        print(f"Score: {score}/2")
                        print("--------------------------------------------------------------------------------------------------------------")
                        sys.exit()
                    else:
                        print("Type 'A' or 'B' or 'C' or 'D' dumbass!")
                        print("--------------------------------------------------------------------------------------------------------------")
                        continue
            else:
                print("Type 'shows' or 'movies' dumbass!")
                print("--------------------------------------------------------------------------------------------------------------")
                continue
    elif q1=="no":
        score=-1 
        print(f"Why tf are you here?\nScore: {score}")
        sys.exit()
    else:
        print("Type 'yes' or 'no' dumbass!")
        print("--------------------------------------------------------------------------------------------------------------")
        continue
