"""EX05 - List Utility Functions."""
__author__ = "730556073"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the even values of a given list."""
    evens: list[int] = []
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
    return evens


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Given 2 lists, returns the list concatenating the givens."""
    concated: list[int] = xs
    for y in ys:
        concated.append(y)
    return concated


def sub(ints: list[int], start: int, end: int) -> list[int]:
    """Given a list and start/end points, returns a subset of the given list between the start (inclusive) and end (exclusive) points."""
    sub_list: list[int] = []
    if len(ints) == 0 or start > len(ints) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(ints):
        end = len(ints)
    i: int = 0
    while i < len(ints):
        if i >= start and i < end:
            sub_list.append(ints[i])
        i += 1
    return sub_list