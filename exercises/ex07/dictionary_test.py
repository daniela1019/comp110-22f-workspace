"""Test for dictionary functions."""
__author__ = "730556073"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_1() -> None:
    """Tests function on a str:str dictionary."""
    dict_1: dict[str, str] = {"Cleveland": "Ohio", "Omaha": "Nebraska", "Chicago": "Illinois", "Boston": "Massachusetts"}
    assert invert(dict_1) == {"Ohio": "Cleveland", "Nebraska": "Omaha", "Illinois": "Chicago", "Massachusetts": "Boston"}


def test_invert_2() -> None:
    """Tests function on another str:str dictionary."""
    dict_2: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(dict_2) == {"b": "a", "d": "c", "f": "e"}


def test_invert_repeating_values() -> None:
    """Tests function with repeating values (Key Error)."""
    with pytest.raises(KeyError):
        dict_repeat: dict[str, str] = {"Miami": "Florida", "Phoenix": "Arizona", "Austin": "Texas", "Dallas": "Texas"}
        invert(dict_repeat)


def test_favorite_color_tie() -> None:
    """Tests function with a tie for mode color."""
    colors_tie: dict[str, str] = {"Dani": "red", "Leia": "green", "Mica": "green", "Alyssa": "yellow", "Molly": "red"}
    assert favorite_color(colors_tie) == "red"


def test_favorite_color_1() -> None:
    """Tests function on a str:str dictionary with one mode."""
    colors_1: dict[str, str] = {"Dani": "red", "Leia": "green", "Mica": "green", "Alyssa": "yellow", "Molly": "purple"}
    assert favorite_color(colors_1) == "green"


def test_favorite_color_2() -> None:
    """Tests function on another str:str dictionary with one mode."""
    colors_2: dict[str, str] = {"Mom": "orange", "Dad": "blue", "Me": "orange", "Brother": "yellow"}
    assert favorite_color(colors_2) == "orange"


def test_count_empty_list() -> None:
    """Tests function on empty list."""
    list_empty: list[str] = []
    assert count(list_empty) == {}


def test_count_one_each() -> None:
    """Tests function on list with no repeating values."""
    list_unique: list[str] = ["apple", "banana", "pomegranate", "mandarin"]
    assert count(list_unique) == {"apple": 1, "banana": 1, "pomegranate": 1, "mandarin": 1}


def test_count_multiples() -> None:
    """Tests function on list with repeating values."""
    list_repeats: list[str] = ["potato", "radish", "potato", "potato", "carrot", "radish", "tomato"]
    assert count(list_repeats) == {"potato": 3, "radish": 2, "carrot": 1, "tomato": 1}