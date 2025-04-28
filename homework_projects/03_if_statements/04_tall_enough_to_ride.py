def main():
    # ask for the user for his height 
    height = int(input("How tall are you? "))

    # check the user heights
    if height >= 5.5:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
if __name__ == '__main__':
    main()