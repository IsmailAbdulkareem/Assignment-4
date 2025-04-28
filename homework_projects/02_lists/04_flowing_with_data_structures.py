def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)
def main():
    message = input("Enter a message to copy: ")  # Asks for your message
    my_list = []  # Creates an empty list (toy box)
    print("List before:", my_list)  # Shows the empty list
    add_three_copies(my_list, message)  # Adds your message 3 times
    print("List after:", my_list)  # Shows the list with 3 messages

if __name__ == "__main__":
    main()  # Runs the program