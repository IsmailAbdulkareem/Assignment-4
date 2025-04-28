def main():
    # Step 1: Ask user for a starting number
    curr_value = int(input("Enter a number: "))
    
    # Step 2: Keep doubling the number until it reaches 100 or more
    while curr_value < 100:
        # Step 3: Double the current value
        curr_value = curr_value * 2
        # Step 4: Print the new value
        print(curr_value)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main() 