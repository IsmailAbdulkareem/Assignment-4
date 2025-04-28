def main():
    # The start of our sentence (it stays the same)
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my "
    
    # Ask for an adjective
    adjective = input("Please type an adjective and press enter. ")
    
    # Ask for a noun
    noun = input("Please type a noun and press enter. ")
    
    # Ask for a verb
    verb = input("Please type a verb and press enter. ")
    
    # Put it all together and show the sentence
    full_sentence = SENTENCE_START + adjective + " " + noun + " " + verb + "!"
    print(full_sentence)

if __name__ == "__main__":
    main()