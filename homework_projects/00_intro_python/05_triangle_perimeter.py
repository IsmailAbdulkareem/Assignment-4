def main():
    #Ask for the lenght of side 1
    side1 = float(input("what is the lenght of side 1 ?"))

    #Ask for the lenght of side 2
    side2 = float(input("what is the lenght of side 2 ?"))

    #Ask for the lenght of side 3
    side3 = float(input("what is the lenght of side 3 ?"))

    perimeter = side1 + side2 + side3

    # Tell the answer 
    print("The perimeter of the triangle is", perimeter)

if __name__ == "__main__":
    main()