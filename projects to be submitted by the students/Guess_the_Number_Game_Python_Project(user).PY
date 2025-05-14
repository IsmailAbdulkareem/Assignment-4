import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
       if low != high:
           guess = random.randint(low, high)
       else:
           guess = low  # could also be high b/c low = high
           # Break the loop if low and high are equal to avoid ValueError
           break #The loop breaks when low == high to avoid the ValueError: empty range for randrange()
       feedback = input(f"Is {guess} to high (H), to low (L), or correct (C)").lower()
       if feedback == 'h':
           high = guess - 1
       elif feedback == 'l':
           low = guess + 1  # Corrected indentation and logic (should be low, not high)
           print(f'YaY! The computer guessed your number, {guess}, correctly!')  
       # If feedback is 'c', the loop will exit, and the program will end

computer_guess(10)