"""
Objective: The goal is to be the first player to reach a total score of 50.
The Turn: During a player's turn, they roll a die (1-6). If they roll anything other than a 1, the value is added to their turn total. 
    They can choose to roll again or stop.
The Catch: If a player rolls a 1, their turn ends immediately, and they lose all points accumulated during that specific turn.
Scoring: When a player decides to stop their turn, their accumulated turn points are added to their total score.
"""
import random
from time import sleep

def greet():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the pig game!")
    print("Objective: The goal is to be the first player to reach a total score of 50.")
    print("The Turn: During a player's turn, they roll a die (1-6). If they roll anything other than a 1, the value is added to their turn total.")
    print("Catch: If a player rolls a 1, their turn ends immediately, and they lose all points accumulated during that specific turn.")
    print("It's highly recommended to set bets on this game against your opponent!")
    print("Enjoy!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sleep(5)

def roll_dice(hi):
    score=hi
    round_score = 0
    rolling = True
    while rolling:
        random_num = random.randint(1, 6)
        print(f"Dice Rolled: {random_num}")
        sleep(2)
        if random_num != 1:
            round_score += random_num
            print(f"Round Score: {round_score}")
            while True:
                do_you = input("Do you want to roll another time? (Enter 'y' or 'n') ").strip().lower()
                if do_you == "y":
                    break
                elif do_you == "n":
                    rolling = False 
                    break            
                else:
                    print("Enter 'y' or 'n' dumbass!")
                    continue
        else:
            round_score = 0
            rolling = False 
    score+=round_score
    return score
    
def main():
    greet()
    game_loop()

def game_loop():
    player_1_score=0
    player_2_score=0
    while True:
        print("Player_1's Turn!")
        print(f"Player_1's Score: {player_1_score}")
        player_1_score=roll_dice(player_1_score)
        print(f"Player_1's Score: {player_1_score}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        sleep(4)
        print("Player_2's Turn!")
        print(f"Player_2's Score: {player_2_score}")
        player_2_score=roll_dice(player_2_score)
        print(f"Player_2's Score: {player_2_score}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if player_1_score>=50 and player_2_score<50:
            print("Player_1 Won!")
            break
        elif player_2_score>=50 and player_1_score<50:
            print("Player_2 Won!")
            break
        elif player_1_score>=50 and player_2_score<=50:
            if player_1_score>player_2_score:
                print("Player_1 Won!")
            elif player_2_score>player_1_score:
                print("Player_2 Won!")
            elif player_1_score==player_2_score:
                print("It was a tie alas!")
            break
        else:
            continue
    
if __name__=="__main__":
    main()