def main():
    # Create an empty list to store values
    my_list =[]

    #keep asking for input until the user presses Enter without typing
    while True:
        value = input("Enter a value: ")
        if value == "":
            print("Here's the list: ", my_list)
            break
        my_list.append(value)

# This line runs the main function
if __name__ == '__main__':
    main()