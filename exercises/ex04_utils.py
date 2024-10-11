"""Implementing algorithms to practice computational thinking"""

__author__ = "730736603"


def all(nums: list[int], value: int) -> bool:
    """Indicates if all ints in the list are the same as the given int"""
    index: int = 0
    if len(nums) == 0:
        return False  # if the list is empty (0), then it can automatically return False
    while index < len(nums):
        if (
            value != nums[index]
        ):  # if the value is not equal to the index in nums, then it should return False
            return False
        index += 1  # prevents infinite loop and increase the variable by one to iterate over each value
    return (
        True  # should return true if each "nums" in the list are equal to the "value"
    )


def max(input: list[int]) -> int:
    """Returns the largest element in the list"""
    larg_num: int = input[0]
    index: int = 0
    if (
        len(input) == 0
    ):  # if the "input" list is empty, return the statement in the body
        raise ValueError("max() arg is an empty List")
    while index < len(input):
        if (
            larg_num < input[index]
        ):  # if the index of the value in the "input" is greater than "larg_num", enter the body
            larg_num = input[
                index
            ]  # updates the larg_num variable with the largest value in the list
        index += 1  # prevents the infinite loop; increases the index to iterate over each value
    return larg_num


def is_equal(set_1: list[int], set_2: list[int]) -> bool:
    """Tells if every element at every index is equal in both lists"""
    index: int = 0
    if len(set_1) != len(
        set_2
    ):  # if the length of each list is not equal then we know that the values are not equal, so return False
        return False
    while index < len(set_1):
        if (
            set_1[index] != set_2[index]
        ):  # if every element in each list is not equal at every index of the element in each list, then return false
            return False
        index += (
            1  # prevent infinite loop; increases the index to iterate over each element
        )
    return True


def extend(values_1: list[int], values_2: list[int]) -> None:
    """Mutates the first list of int values by appending the second list's value to it"""
    for nums in values_2:  # "nums" represents the values in "values_2" list
        values_1.append(
            nums
        )  # the "nums" in list 2 (values_2) are added to the end of list 1 values (values_1)


# does not return anything, so it can be left blank
