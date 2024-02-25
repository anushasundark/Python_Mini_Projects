def madlibs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    
    story = f"The {adjective} {noun} {verb} over the lazy dog."
    
    print("Madlibs Result:")
    print(story)
madlibs()
