"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730556073"

rightword: str = input("Enter a 5-character word: ")

if len(rightword) != 5:
    print("Error: Word must contain 5 characters")
else:
    charguess: str = input("Enter a single character: ")
    if len(charguess) != 1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for " + charguess + " in " + rightword)
        instance = 0

        if rightword[0] == charguess:
            print(charguess + " found at index 0")
            instance = instance + 1

        if rightword[1] == charguess:
            print(charguess + " found at index 1")
            instance = instance + 1

        if rightword[2] == charguess:
            print(charguess + " found at index 2")
            instance = instance + 1

        if rightword[3] == charguess:
            print(charguess + " found at index 3")
            instance = instance + 1

        if rightword[4] == charguess:
            print(charguess + " found at index 4")
            instance = instance + 1

        if instance == 0:
            print("No instances of " + charguess + " found in " + rightword)
        else:
            if instance == 1:
                print("1 instance of " + charguess + " found in " + rightword)
            else:
                print(str(instance) + " instances of " + charguess + " found in " + rightword)