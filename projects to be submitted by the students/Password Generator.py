import random
import string

def generate_password(length, include_digits, include_letters):
    characters = ""
    if include_digits:
        characters += string.digits
    if include_letters:
        characters += string.ascii_letters
    
    if not characters:
        return "No character types selected."  # Handle invalid input gracefully
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        include_digits = input("Include digits (yes/no)? ").lower() == "yes"
        include_letters = input("Include letters (yes/no)? ").lower() == "yes"

        password = generate_password(length, include_digits, include_letters)
        print("Generated password:", password)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")