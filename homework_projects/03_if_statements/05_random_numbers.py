import random

def main():
    # Print 10 random numbers between 1 and 100
    for i in range(10):
        number = random.randint(1, 100)  # Get a random number
        print(number, end=" ")  # Print with a space after
    print()  # Add a newline at the end

if __name__ == '__main__':
    main()