"""EX07 - Dictionary Functions."""
__author__ = "730556073"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and inverts its keys and values."""
    list_values: list[str] = []
    list_keys: list[str] = []
    reverse_dict_1: dict = {}
    for key in dict_1:
        list_values.append(dict_1[key])
    for key in dict_1:
        list_keys.append(key)
    for i in range(0, len(dict_1)):
        reverse_dict_1[list_values[i]] = list_keys[i]
    i: int = 0
    j: int = 1
    while i < len(list_values):
        while j < len(list_values):
            if list_values[i] == list_values[j]:
                raise KeyError()
            j += 1
        i += 1
        j = i + 1
    return reverse_dict_1


def favorite_color(dict_2: dict[str, str]) -> str:
    """Returns most frequently-appearing color value in the dictionary; in case of tie, return color that appeared first."""
    list_colors: list[str] = []
    color_count: dict[str, int] = {}
    for name in dict_2:
        list_colors.append(dict_2[name])
    for color in list_colors:
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1
    pop_color_value: int = None
    pop_color: str = None
    for color_key in color_count:
        if pop_color_value is None or pop_color_value < color_count[color_key]:
            pop_color_value = color_count[color_key]
            pop_color = color_key
    return pop_color
    

def count(list_1: list[str]) -> dict[str, int]:
    """Given a list, outputs a dictionary giving the frequency of each unique list value."""
    dict_freqs: dict[str, int] = {}
    for item in list_1:
        if item not in dict_freqs:
            dict_freqs[item] = 1
        else:
            dict_freqs[item] += 1
    return dict_freqs