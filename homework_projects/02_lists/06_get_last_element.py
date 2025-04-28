def get_last_element(lst):
    print(lst[-1]) # Print the first element of the list 

def main():
    #Ask how many elements the user wants to input
    num_elements = int(input("How many elements do you want to add to the list? "))

    # Create an empty list from the user
    my_list = [] 
    for i in range(num_elements):
        element = input("Enter element " + str(i + 1) + ": ")
        my_list.append(element) # Add the element to the list

    # CAll the function to print the first element
    get_last_element(my_list)

# This line is required to call main()
if __name__ == "__main__":
    main()