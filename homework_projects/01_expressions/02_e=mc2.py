def main():
    # The speed of light (a constant number we always use)
    C = 299792458  # meters per second

    # keep asking for mass forever (contioually)
    while True:
        #Ask for mass in kilograms
        mass = float(input("Enter kilos of mass: "))

        # Calculate energy : E = m * c^2
        energy = mass * (C ** 2)

        #Show the formula and results
        print("e = m * C^2...")
        print(f"m = {mass} kg")
        print(f"m = {C} m/s")
        print(f"{energy} joules of energy!")

if __name__ == "__main__":
        main()
       