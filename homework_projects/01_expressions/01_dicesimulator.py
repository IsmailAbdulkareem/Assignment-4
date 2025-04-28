import random  # This is our toy box with dice-rolling magic

def roll_dice():
    # Roll two dice inside this play area
    die1 = random.randint(1, 6)  # First die gets a number 1 to 6
    die2 = random.randint(1, 6)  # Second die gets a number 1 to 6
    print(f"Die 1 is {die1} and Die 2 is {die2}")  # Tell the numbers

def main():
    # Roll the dice three times
    print("Rolling the dice three times:")
    roll_dice()  # First roll
    roll_dice()  # Second roll
    roll_dice()  # Third roll

if __name__ == "__main__":
    main()