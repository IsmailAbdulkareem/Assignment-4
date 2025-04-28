def main():
    # Create an empty dictionary to store number counts
    counts = {}
    
    # Keep asking for numbers until the user presses Enter
    while True:
        number = input("Enter a number: ")
        if number == "":  # Stop if the input is empty
            break
        # Convert the input to an integer and count it
        number = int(number)
        if number in counts:
            counts[number] += 1  # Increase count if number exists
        else:
            counts[number] = 1  # Start count at 1 if new number
    
    # Print the counts for each number
    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()