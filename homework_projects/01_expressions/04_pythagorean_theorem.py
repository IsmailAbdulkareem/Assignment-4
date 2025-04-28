import math  # This gives us the square root toy

def main():
    # Ask for the length of AB
    ab = float(input("Enter the length of AB: "))
    
    # Ask for the length of AC
    ac = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse (BC) using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)
    
    # Show the answer
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == "__main__":
    main()