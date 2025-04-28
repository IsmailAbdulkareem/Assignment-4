def count_even(lst):
   """
       Returns number of even numbers in the list and prints it.
       >>> count_even([1, 2, 3, 4])
       2
       >>> count_even([1, 3, 5])
       0
   """
   count = 0
   for num in lst:
      if num % 2 == 0:
         count += 1
   print(count)

def get_list_of_ints():
   """
       Prompts the user for integers until Enter is pressed, and returns the list of integers.
   """
   lst = []
   user_input = input("Enter an integer or press enter to stop: ")
   while user_input != "":
      lst.append(int(user_input))
      user_input = input("Enter an integer or press enter to stop: ")
   return lst

def main():
   lst = get_list_of_ints()
   count_even(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()   