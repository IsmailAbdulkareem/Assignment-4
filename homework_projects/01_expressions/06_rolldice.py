import random  # This is our toy box for rolling dice

def main():
    # Roll the first die
    die1 = random.randint(1, 6)
    # Roll the second die
    die2 = random.randint(1, 6)
    
    # Show the results of each roll
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    
    # Add them up and show the total
    total = die1 + die2
    print(f"Total: {total}")

if __name__ == "__main__":
    main()