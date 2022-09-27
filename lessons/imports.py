"""Examples of importing in Python."""
# Part of LS15 Notes

from lessons import helpers
# Below- alias (used if module name is too long to write out-
from lessons import helpers as hp
# Below - import a function directly (if you don't want to do whole module)-
# aka accessing global vars in other modules directly
from lessons.helpers import powerful, THE_ANSWER
# ^ comma separates individual names you are importing

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2,4))
    # You can do the above format when you import the func directly
    # ^ no need to say helpers.powerful
    print(THE_ANSWER)

if __name__ == "__main__":
    main()