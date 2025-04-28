# What it does: This is like setting up your notebook and asking people to tell you their names and phone numbers.
def read_phone_numbers():

    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

# What it does: This is like opening your notebook and reading out loud everyone’s name and number.
def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

#What it does: This is like someone asking, “What’s Alice’s phone number?” and you checking your notebook.
def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

#What it does: This is like the boss of the program, telling the other functions what to do and when.

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# Boilerplate
if __name__ == '__main__':
    main()