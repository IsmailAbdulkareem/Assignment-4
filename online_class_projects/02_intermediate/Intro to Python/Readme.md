# Planetary Weight Calculator

This Python program calculates how much a person would weigh on different planets in our solar system. It's a fun way to learn about planetary gravity and practice Python programming!

## How It Works

The program uses the fact that each planet has different gravity compared to Earth. For example:
- On Mars, you weigh only 37.8% of your Earth weight
- On Jupiter, you weigh 236% of your Earth weight!

## Step-by-Step Guide to Create the Program

### Step 1: Set Up the Constants
First, we need to define the gravity constants for each planet (as a percentage of Earth's gravity):
```python
MERCURY_GRAVITY = 0.376  # 37.6%
VENUS_GRAVITY = 0.889    # 88.9%
MARS_GRAVITY = 0.378     # 37.8%
JUPITER_GRAVITY = 2.360  # 236.0%
SATURN_GRAVITY = 1.081   # 108.1%
URANUS_GRAVITY = 0.815   # 81.5%
NEPTUNE_GRAVITY = 1.140  # 114.0%
```

### Step 2: Get User Input
Next, we need to get two pieces of information from the user:
```python
# Get the user's Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Get the planet name
planet = input("Enter a planet: ")
```

### Step 3: Create the Planet Selection Logic
We use if/elif statements to select the correct gravity constant:
```python
if planet == "Mercury":
    gravity_constant = MERCURY_GRAVITY
elif planet == "Venus":
    gravity_constant = VENUS_GRAVITY
# ... and so on for each planet
```

### Step 4: Calculate the Weight
Finally, we calculate and display the weight:
```python
# Calculate weight on the selected planet
planetary_weight = earth_weight * gravity_constant
rounded_weight = round(planetary_weight, 2)

# Display the result
print("The equivalent weight on " + planet + ": " + str(rounded_weight))
```

## Sample Runs

```bash
Example 1:
Enter a weight on Earth: 120
Enter a planet: Mars
The equivalent weight on Mars: 45.36

Example 2:
Enter a weight on Earth: 150
Enter a planet: Jupiter
The equivalent weight on Jupiter: 354.0
```

## Important Notes

1. The program assumes the user will enter planet names with proper capitalization (first letter capital, rest lowercase)
2. Weights are automatically rounded to 2 decimal places when needed
3. The program uses Python's built-in `round()` function for decimal place formatting

