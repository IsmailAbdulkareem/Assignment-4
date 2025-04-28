def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    number = int(input("Enter a number: "))
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    result = in_range(number, lower, upper)
    print(f"Is {number} between {lower} and {upper}? {result}")

if __name__ == "__main__":
    main()
