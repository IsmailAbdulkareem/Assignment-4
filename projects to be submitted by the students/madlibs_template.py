# madlibs.py

# Ask user for inputs with hints
adjective = input("Enter an adjective (e.g., funny, scary, tall): ")
animal = input("Enter an animal (e.g., lion, monkey, elephant): ")
verb_past = input("Enter a past tense verb (e.g., ran, jumped, danced): ")
adverb = input("Enter an adverb (e.g., quickly, silently, happily): ")
adjective2 = input("Enter another adjective (e.g., shiny, large, stinky): ")
noun = input("Enter a noun (e.g., cave, house, spaceship): ")

# Create the story using f-string
story = f"Today I went to the zoo. I saw a(n) {adjective} {animal} jumping up and down in its tree. " \
        f"He {verb_past} {adverb} through the large tunnel that led to its {adjective2} {noun}."

# Print the completed story
print("\nYour Mad Libs story:")
print(story)
