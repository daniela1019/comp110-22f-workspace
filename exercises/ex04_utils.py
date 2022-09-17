"""EX04 - 'List' Utility Functions."""
__author__ = "730556073"


def all(num_list: list[int], num: int) -> bool:
    """Checks if every integer in a list is equal to the given integer."""
    if len(num_list) == 0:
        return False
    i: int = 0
    while i < len(num_list):
        if num_list[i] != num:
            return False
        else:
            i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    j: int = 1
    max_num: int = input[0]
    while j < len(input):
        if max_num <= input[j]:
            max_num = input[j]
        j += 1
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if every element at every index is equal in both lists."""
    k: int = 0
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    if (len(list_1) == 0 and len(list_2) != 0) or (len(list_1) != 0 and len(list_2) == 0) or len(list_1) != len(list_2):
        return False
    while k < len(list_1):
        if list_1[k] == list_2[k]:
            k += 1
        else:
            return False
    return True