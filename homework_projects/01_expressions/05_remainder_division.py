def main():
    # Ask for the first number (to be divided)
    num1 = int(input("Please enter an integer to be divided: "))
    
    # Ask for the second number (to divide by)
    num2 = int(input("Please enter an integer to divide by: "))
    
    # Calculate the quotient (whole number result)
    quotient = num1 // num2
    
    # Calculate the remainder (what’s left)
    remainder = num1 % num2
    
    # Tell the answer
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()