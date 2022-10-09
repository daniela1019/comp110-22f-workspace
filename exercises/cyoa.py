"""EX06 - Choose Your Own Adventure: The Genie Guesser."""
__author__ = "730556073"
from random import randint

points: int = 0
# points is number of guesses taken
player: str = ""
# player is player name
GAME_EMOJIS: str = "\U00000000"
# GAME_EMOJIS clarifies that all unicode strings used in the program are emojis


def greet() -> None:
    """Begins the game by asking the user their name and if they wish to play."""
    global player
    player = input("Welcome to the Genie Guesser. What is your name? ")
    decision: str = input(f"Greetings, {player}. I am the all-knowing Guessia\U0001F9DE. Do you dare read my mind?? Type yes/no: ")
    if decision == "no":
        print("I see you've made your decision\U0001F58B  Goodbye.")
        quit()


def correct_guess_message(end_guess_count: int) -> str:
    """Chooses what end message to give based on no. of guesses taken to get the right number."""
    print(f"You got the guess in {end_guess_count} tries!")
    if end_guess_count == 1:
        return "Are you sure you're not a genie? We're hiring btw\U0001F60F"
    if end_guess_count > 1 and end_guess_count <= 6:
        return "Impressive\U0001F44D  You're pretty good for a human."
    if end_guess_count > 6:
        return "There's always room for improvement\U0001F62C"


def wrong_guess_message() -> str:
    """Chooses a random message to output to the player when they get a wrong guess."""
    wrong_messages: list[str] = ["Is this all you got\U0001F928", "Wow... didn't think humans could be this slow. Try again.", "Wake me up when you guess correctly\U0001F634", "Nope\U0001F611"]
    return wrong_messages[randint(0, 3)]


def main() -> None:
    """The entry point of the program and main game loop."""
    greet()
    chosen_upper_bound: int = int(input(f"{player}, please give an upper bound for the range of numbers for me to choose from (max of 20): "))
    while chosen_upper_bound > 20:
        chosen_upper_bound = int(input("Can't you follow directions? Choose an upper bound again (max of 20): "))
    print("Wonderful. I will think of a number from 0 to your upper bound, inclusive, and you must guess it. Beware: I don't give hints\U0000274C")
    correct: bool = False
    genies_number: int = randint(0, chosen_upper_bound)
    global points
    while not correct:
        print(f"Guess #{points + 1}")
        player_guess: int = int(input("What number am I thinking of? "))
        while player_guess > chosen_upper_bound:
            print("Please give a guess within the range\U0000203C")
            player_guess = int(input("What number am I thinking of? "))
        if player_guess != genies_number:
            print(wrong_guess_message())
            player_decision: str = input("Do you wish to guess again? Type yes/no: ")
            if player_decision == "no":
                print("I guess I'm just too powerful. Goodbye.")
                quit()
            else:
                print(f"That's the spirit! On to guess #{points + 2}")
        else:
            correct = True
        points += 1
    if player_guess == genies_number:
        print(correct_guess_message(points))


if __name__ == "__main__":
    main()