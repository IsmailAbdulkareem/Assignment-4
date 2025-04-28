import random

# Constants
NUM_ROUNDS = 5  # Number of rounds to play

def get_valid_choice():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if choice in ['higher', 'lower']:
            return choice
        print("Please enter either higher or lower: ", end="")

def play_game():
    score = 0
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Play for NUM_ROUNDS rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        # Generate random numbers for player and computer
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)
        
        print(f"Your number is {player_num}")
        
        # Get player's guess
        player_choice = get_valid_choice()
        
        # Check if player won the round
        player_won = False
        if player_choice == 'higher' and player_num > computer_num:
            player_won = True
        elif player_choice == 'lower' and player_num < computer_num:
            player_won = True
            
        # Display round results
        if player_won:
            score += 1
            print(f"You were right! The computer's number was {computer_num}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        print(f"Your score is now {score}")
    
    # Display ending message based on performance
    print("\nThanks for playing!")
    if score == NUM_ROUNDS:
        print("\nWow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")

# Start the game
if __name__ == "__main__":
    play_game()
