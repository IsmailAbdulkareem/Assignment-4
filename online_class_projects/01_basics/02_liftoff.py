import time

def main():
    # Count down from 10 to 1 with a 1-second delay
    for i in range(10):
        # Print 10 minus the number of completed iterations
        print(10 - i)
        # Wait for 1 second
        time.sleep(.3)
    
    # After countdown finishes, print Liftoff!
    print("Liftoff!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
