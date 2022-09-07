"""EX02 - One Shot Wordle - Loops!"""
__author__ = "730556073"

right_word: str = "python"
right_len: int = len(right_word)
guess_word = input(f"What is your {right_len}-letter guess? ")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i = 0
emoji = ""

while len(guess_word) != right_len:
    guess_word = input(f"That was not {right_len} letters! Try again: ")
# Allows program to proceed only if the length of the guess matches the length of the secret

if len(guess_word) == right_len:
    while i < len(right_word):
        if guess_word[i] == right_word[i]:
            emoji = emoji + green_box
            # If letter and index match, a green box is printed
        else:
            chr_exists: bool = False
            alt_i: int = 0
            while (chr_exists == False) and alt_i < len(right_word):
                if right_word[alt_i] == guess_word[i]:
                    chr_exists = True
                    # This won't be true the first time the while loop is read
                    # (if it were, this would be condition for a green box)
                    # The index will have to be changed in the else block, which makes sense when looking for a yellow box
                else:
                    alt_i = alt_i + 1
            if chr_exists == True:
                emoji = emoji + yellow_box
            else:
                emoji = emoji + white_box
                # This block will be read if no both words use completely different letters
                # Only way to get here would be for alt_i to violate the len statement
        i = i + 1
    print(emoji)
    if guess_word == right_word:
        print("Woo! You got it!")
    else:
        # Anything other than a perfect match
        print("Not quite. Play again soon!")

