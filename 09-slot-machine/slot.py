"""
Overview of the Slot Machine Project: Concept: A text-based simulation of a slot machine where the user can deposit money, place bets on lines, 
and spin to win based on randomly generated symbols. How it works: Dynamic Configuration: You define the number of rows and columns (the grid size) 
and the types of symbols (e.g., A, B, C, D) along with their respective values and frequency. Probability Logic: The program uses the random module 
to pick symbols for each column based on their defined frequency. Win Calculation: After a spin, the code iterates through each row to check if all 
symbols are identical. If they are, the user wins based on the symbol's value multiplied by their bet. Banking System: The script maintains a running
balance, handling deposits and deductions in real-time. Key Coding Concepts Used: Nested Lists (Matrices): Managing the grid state. Random Module: 
Essential for simulating the "random" nature of slot machine spins. Functions: Organizing logic for depositing, betting, spinning, and checking 
winnings. Mathematical Operations: Calculating multipliers and updating the user's currency balance.
"""

import random

grid_rows = 3
grid_cols = 3

symbol_pool = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

payouts = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def spin_reels(rows, cols, pool):
    choices = []
    for sym, count in pool.items():
        choices.extend([sym] * count)
    
    reels = []
    for _ in range(cols):
        reel = [random.choice(choices) for _ in range(rows)]
        reels.append(reel)
    return reels

def get_rows(reels):
    return [[reels[col][row] for col in range(len(reels))] for row in range(len(reels[0]))]

def show_grid(board):
    print("\n--- SPIN RESULTS ---")
    for row in board:
        print(" | ".join(row))
    print("--------------------")

def calculate_win(board, lines, bet, multipliers):
    total_won = 0
    won_lines = []
    
    for i in range(lines):
        current_row = board[i]
        if len(set(current_row)) == 1:
            matching_symbol = current_row[0]
            total_won += multipliers[matching_symbol] * bet
            won_lines.append(i + 1)
            
    return total_won, won_lines

def get_deposit():
    while True:
        val = input("Enter amount to deposit ($): ")
        if val.isdigit() and int(val) > 0:
            return int(val)
        print("Please enter a valid number greater than 0.")

def get_lines_to_bet():
    while True:
        val = input(f"Enter number of lines to bet on (1-{grid_rows}): ")
        if val.isdigit() and 1 <= int(val) <= grid_rows:
            return int(val)
        print(f"Must be a valid number between 1 and {grid_rows}.")

def get_line_bet():
    while True:
        val = input("Enter bet per line ($): ")
        if val.isdigit() and int(val) > 0:
            return int(val)
        print("Please enter a valid bet amount.")

def play_hand(credits):
    lines = get_lines_to_bet()
    
    while True:
        bet = get_line_bet()
        cost = bet * lines
        if cost <= credits:
            break
        print(f"You don't have enough money! Current balance: ${credits}")

    print(f"Betting ${bet} on {lines} lines. Total cost: ${cost}")

    reels = spin_reels(grid_rows, grid_cols, symbol_pool)
    board = get_rows(reels)
    show_grid(board)
    
    won_amt, won_lines = calculate_win(board, lines, bet, payouts)
    winnings_this_turn = won_amt - cost
    
    if won_amt > 0:
        print(f"🎉 You won ${won_amt}!")
        print("Winning lines:", *won_lines)
    else:
        print("❌ No luck this time.")
        
    return winnings_this_turn

def main():
    print("Welcome to the Python Text Slot Machine!")
    wallet = get_deposit()
    
    while wallet > 0:
        print(f"\nCurrent Balance: ${wallet}")
        action = input("Press Enter to spin (or 'q' to cash out): ").lower()
        if action == 'q':
            break
        wallet += play_hand(wallet)
        
    print(f"\nGame over. You left with ${wallet}. Thanks for playing!")

if __name__ == "__main__":
    main()
