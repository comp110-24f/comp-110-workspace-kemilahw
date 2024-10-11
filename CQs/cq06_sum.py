"""Summing the elements of a list using different loops"""

__author__ = "730736603"


def w_sum(vals: list[float]) -> float:
    """summing the list of values"""
    index: int = 0  # initialize as 0
    sum: float = 0.0  # sum variable to add the values each time the "while loop" loops
    while index < len(vals):
        sum = (
            vals[index] + sum
        )  # updates the sum value as it continues to add up the values in the list
        index += 1  # iterates over each value in the list
    return sum  # return statement placed on the same index as the "while" to prevent it from running only once


def f_sum(vals: list[float]) -> float:
    """Summing all elements similar to first function (w_sum)"""
    sum: float = 0.0  # this will update as values are added to it
    for nums in vals:  # nums represent my values in the "vals" list
        sum = (
            nums + sum
        )  # this updates the sum variable as "nums" (each value in the list) is added to the sum value of "0.0"
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Summing all elements similar to the last two functions (w_sum & f_sum)"""
    sum: float = 0.0  # sum variable
    for numbers in range(
        0, len(vals)
    ):  # "numbers" represent the "index" of each value in the list when using the "for ... in.. range()" loop
        sum = (
            vals[numbers] + sum
        )  # have to put vals (the list of floats) with the "index" (numbers) because "numbers" is the index of each value in the list, then add it to the sum so it can add all the values together
    return sum
