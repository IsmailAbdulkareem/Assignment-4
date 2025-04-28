def main():
    # ask for the user age 
    age = int(input("how old are you? "))

    # check peturksbouipo (voting age 16)
    if age >= 16:
        print("you can vote in peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in peturksbouipo where the voting age 16. ")

    # Check Stanlau (voting age 25)
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")
    
    # Check Mayengua (voting age 48)
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")
    
if __name__ == '__main__':
    main()