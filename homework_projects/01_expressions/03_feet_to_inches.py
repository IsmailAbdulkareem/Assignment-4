def main():
     # Ask the user for the number of feet
    feet = float(input("enter a feet in numbers: "))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * 12 
    
    # show the answer 
    print(f"{feet} feet is {inches} inches!")


if __name__ == '__main__':
    main()