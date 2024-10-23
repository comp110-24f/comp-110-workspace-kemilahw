"""Defining unit tests for the utility functions."""

__author__ = "730736603"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_usecase1() -> None:
    """Testing to make sure the only_evens function returns only the even numbers in a list"""
    assert only_evens([55, 80, 24, 36, 24]) == [80, 24, 36, 24]


def test_only_evens_dont_mutate_usecase2() -> None:
    """Testing to make sure only_evens does not mutate its input"""
    input_list: list[int] = [20, 1, 5, 18, 24]
    new_list: list[int] = []
    new_list.append(20)
    new_list.append(18)
    new_list.append(24)
    assert only_evens(input_list) == new_list


def test_only_evens_edgecase() -> None:
    """Testing only_evens on a empty list; it should return empty brackets"""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_sub_usecase1() -> None:
    """Testing sub to make sure it returns the subset list of the input list"""
    my_list: list[int] = [40, 45, 47, 50, 99]
    start_id: int = 1
    end_id: int = 4
    assert sub(my_list, start_id, end_id) == [45, 47, 50]


def test_sub_dont_mutate_usecase2() -> None:
    """Testing to make sure sub is not mutating its input list"""
    my_list1: list[int] = [40, 45, 47, 50, 80, 99]
    start_id: int = 2
    end_id: int = 6
    subset_list: list[int] = []
    subset_list.append(my_list1[2])
    subset_list.append(my_list1[3])
    subset_list.append(my_list1[4])
    subset_list.append(my_list1[5])
    assert sub(my_list1, start_id, end_id) == subset_list


def test_sub_edgecase() -> None:
    """Testing sub on a empty list; should return empty brackets"""
    list2: list[int] = []
    start_id: int = 3
    end_id: int = 5
    assert sub(list2, start_id, end_id) == []


def test_add_at_index_usecase1() -> None:
    """Testing to make sure add_at_index returns none"""
    list1: list[int] = [20, 21, 23, 24]
    add_elem: int = 22
    index: int = 2
    assert add_at_index(list1, add_elem, index) == None


def test_add_at_index_usecase2() -> None:
    """Testing to make sure add_at_index mutates the input list."""
    list1: list[int] = [20, 21, 23, 24]
    add_elem: int = 22
    index: int = 2
    add_at_index(list1, add_elem, index)
    assert list1 == [20, 21, 22, 23, 24]


def test_add_at_index_raises_indexerror() -> None:
    """Testing to make sure add_at_index raises an IndexError for an invalid index"""
    list_nums: list[int] = [1, 2, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(list_nums, 3, 5)
