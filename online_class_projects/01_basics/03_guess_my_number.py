import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    # Initial prompt
    print("I am thinking of a number between 0 and 99...")
    
    # Get the first guess from user
    guess = int(input("Enter a guess: "))
    
    # Keep asking for new guesses until correct
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        # Get next guess
        guess = int(input("\nEnter a new number: "))
    
    # Congratulate the user when they guess correctly
    print(f"Congrats! The number was: {secret_number}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
