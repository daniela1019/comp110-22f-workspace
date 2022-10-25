def odd_and_even(ints: list[int]) -> list[int]:
    """Returns odd elements with even indices in a given list."""
    i: int = 0
    list_return: list[int] = []
    while i < len(ints):
        if ints[i] % 2 == 1:
            list_return.append(ints[i])
        i += 2
    return list_return


def vowels_and_threes(string_1: str) -> str:
    """Returns characters in a string that are either vowels or have an index divisible by 3."""
    i: int = 0
    return_string: str = ""
    while i < len(string_1):
        if (string_1[i] == "a" or "e" or "i" or "o" or "u") or i % 3 == 0:
            return_string += string_1[i]
        i += 1
    return return_string


def zoo_visits(visits: dict[str, list[int]]) -> list[str]:
    """Returns a list of the most popular zoo animal each day of the weekend."""
    i: int = 0
    max_visits: list[str] = []
    while i < 3:
        max: int = 0
        animal: str = ""
        for exhibit in visits:
            if visits[exhibit][i] > max:
                max = visits[exhibit][i]
                animal = exhibit
    max_visits.append(animal)
    i += 1

    return max_visits


def average_grades(dict_1: dict[str, list[int]]) -> dict[str, float]:
    """Gives the average grade of each student."""
    avg_grades: dict[str, float] = {}
    avg_grade: float = None
    for name in dict_1:
        i: int = 0
        total_pts: int = 0
        while i < len(dict_1[name]):
            total_pts += dict_1[name][i]
            i += 1
        avg_grade = (total_pts)/len(dict_1[name])
        avg_grades[name] = avg_grade
    return avg_grades
