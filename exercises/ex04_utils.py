"""EX04 - 'List' Utility Functions."""
__author__ = "730556073"

def all(num_list: list[int], num: int) -> bool:
    i: int = 0
    while i < len(num_list):
        if num_list[i] != num:
            return False
        else:
            i += 1
    return True


def max(input: list[int]) -> int:
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
    assert len(list_1) == len(list_2)
    k: int = 0
    while k < len(list_1):
        if list_1[k] == list_2[k]:
            k += 1
        else:
            return False
    return True