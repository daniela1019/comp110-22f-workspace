"""Test for the utils functions."""
__author__ = "730556073"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_mixed_nums_1() -> None:
    xs: list[int] = [1,2,3,4,5,6,7,8]
    assert only_evens(xs) == [2,4,6,8]


def test_only_evens_mixed_nums_2() -> None:
    xs: list[int] = [2,5,6,9,4,3,2,6,0,1]
    assert only_evens(xs) == [2,6,4,2,6,0]


def test_only_evens_no_evens() -> None:
    xs: list[int] = [1,5,5,9,7,3]
    assert only_evens(xs) == []


def test_concat_same_len() -> None:
    xs: list[int] = [1,3,5,7,9]
    ys: list[int] = [2,4,6,8,0]
    assert concat(xs,ys) == [1,3,5,7,9,2,4,6,8,0]


def test_concat_diff_lens() -> None:
    xs: list[int] = [-1,3,6,0]
    ys: list[int] = [4,5,9]
    assert concat(xs,ys) == [-1,3,6,0,4,5,9]


def test_concat_empty_lists() -> None:
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs,ys) == []


def test_sub_norm_indices_1() -> None:
    xs: list[int] = [2,3,4,5,6,7,6,5,4,3]
    a: int = 2
    b: int = 6
    assert sub(xs,a,b) == [4,5,6,7]


def test_sub_norm_indices_2() -> None:
    xs: list[int] = [1,1,1,2,2,2,3,3,3,4,4,4]
    a: int = 5
    b: int = 6
    assert sub(xs,a,b) == [2]


def test_sub_large_start() -> None:
    xs: list[int] = [0,1,2,3,4,9]
    a: int = 7
    b: int = 4
    assert sub(xs,a,b) == []