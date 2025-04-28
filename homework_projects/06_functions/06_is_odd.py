def main():
    print("=== ODD/EVEN CHECKER ===")
    for i in range(10):
        if is_odd(i):
            print(f"{i} is 🔴 ODD")
        else:
            print(f"{i} is 🟢 EVEN")
    print("=====================")
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()