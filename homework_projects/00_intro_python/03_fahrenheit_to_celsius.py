def main():
    
    #Ask for the temperature in fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    #Do the magic math to turn ot into Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    #show the answer 
    print(f"Temperature: {fahrenheit}F = {celsius}C 🌡🔥")

if __name__ == "__main__":
    main()
