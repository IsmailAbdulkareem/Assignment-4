import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generate and print N_NUMBERS random numbers between
    MIN_VALUE and MAX_VALUE (inclusive).
    """
    # Loop N_NUMBERS times to generate required amount of random numbers
    for i in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        # Print the random number
        print(random_number)

if __name__ == '__main__':
    main()
