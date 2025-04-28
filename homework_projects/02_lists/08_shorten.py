MAX_LENGTH = 3

def shorten(lst):
    # Keep removing elements from the end until the list is MAX_LENGTH or shorter
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last element and store it
        print(removed_item)  # Print the removed element

def main():
    # This is already written, but for clarity, it might look like this:
    my_list = input("Enter elements separated by spaces: ").split()
    shorten(my_list)

if __name__ == '__main__':
    main()