"""EX03 - Wordle - The real thing!"""
__author__ = "730556073"


def contains_char(word: str, char: str) -> bool:
    """Checks whether or not the character argument is found in the word"""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
            # The position of the given character does not matter;
            # If it is contained in the word, func will return True
        i = i + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Compares guess word and secret word indices, returning the right emoji box"""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    j: int = 0
    emoji: str = ""
    while j < len(secret):
        # Loop works so long as the index is less than the word length
        if not contains_char(secret, guess[j]):
            emoji = emoji + white_box
            # White box appended if the character is nowhere to be found in the word
        else:
            if secret[j] == guess[j]:
                emoji = emoji + green_box
                # Green box appended if contains_char is True and the indices of the given char match
            else:
                emoji = emoji + yellow_box
                # Yellow box appended if character exists in both words but at different indices
        j += 1
        # Incrementation keeps loop from being infinite and checks all characters in the guess word against the secret 
    return emoji

def input_guess(exp_len: int) -> str:
    """Prints out a guess of correct length, prompting until that length is given."""
    guess_word: str = input(f"Enter a {exp_len}-character word: ")
    while len(guess_word) != exp_len:
        guess_word = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess_word

def main() -> None:
    """The entry point of the program and main game loop."""
    real_secret: str = "codes"
    # real_secret is set in advance as the word to guess
    turn: int = 1
    win: bool = False
    while turn <= 6 and not win:
        # Game continues so long as all turns are not used up and the word isn't guessed
        print(f"=== Turn {turn}/6 ===")
        real_guess: str = input_guess(len(real_secret))
        # input_guess makes sure that user's guess matches in length to the secret word
        print(emojified(real_guess, real_secret))
        # Emojification of guess
        if real_guess == real_secret:
            win = True
        else:
            turn = turn + 1
            # If word is not guessed (win is False), user is given another turn
    if win:
        win_string: str = f"You won in {turn}/6 turns!"
        return print(win_string)
    else:
        loss_string: str = "X/6 - Sorry, try again tomorrow!"
        return print(loss_string)
    # Above if/else statement lets the user know either how quick they won,
    # Or the fact that they lost

if __name__ == "__main__":
    main()