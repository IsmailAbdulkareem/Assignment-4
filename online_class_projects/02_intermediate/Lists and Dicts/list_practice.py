def list_practice():
    # Create a list called `fruit_list` that contains the fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    """Access an element at the specified index."""
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range!"

def modify_element(lst, index, new_value):
    """Modify an element at the specified index."""
    try:
        lst[index] = new_value
        return "Element modified successfully!"
    except IndexError:
        return "Error: Index out of range!"

def slice_list(lst, start, end):
    """Return a slice of the list from start to end."""
    try:
        return lst[start:end]
    except IndexError:
        return "Error: Invalid slice range!"

def play_index_game():
    # Initialize the list with mixed elements
    game_list = [42, "hello", 3.14, "python", True]
    
    while True:
        print("\n=== Index Game ===")
        print("Current list:", game_list)
        print("\nOperations:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit game")
        
        choice = input("\nSelect an operation (1-4): ")
        
        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(game_list, index)
            print("Result:", result)
            
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            # Try to convert to int or float if possible
            try:
                new_value = int(new_value)
            except ValueError:
                try:
                    new_value = float(new_value)
                except ValueError:
                    pass
            result = modify_element(game_list, index, new_value)
            print(result)
            print("Updated list:", game_list)
            
        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(game_list, start, end)
            print("Sliced list:", result)
            
        elif choice == '4':
            print("Thanks for playing!")
            break
            
        else:
            print("Invalid choice! Please select 1-4.")

def main():
    print("=== List Practice ===")
    list_practice()
    
    print("\n=== Starting Index Game ===")
    play_index_game()

if __name__ == "__main__":
    main() 