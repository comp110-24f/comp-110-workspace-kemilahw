"""Mutating functions."""

__author__ = "730736603"


def manual_append(word: list[int], value: int) -> None:
    """Appending (attach) a value to a list."""
    word.append(value)  # this attaches an input value to the list


def double(num: list[int]) -> None:
    """Multiplying each item in the list by 2"""
    index: int = 0
    while index < len(
        num
    ):  # makes the statement true to enter the body of the while loop; length of the list is greater than the index
        num[index] = (
            num[index] * 2
        )  # At each index in the list, this allows the value in the list to each be multiplied by 2;
        index += 1  # prevents the infinite loop and increases the index by 1 to iterate over each item in the list


list_1: list[int] = [1, 2, 3]  # Global variable
list_2: list[int] = list_1  # Global variable; assigning list_2 the values of list_1
double(list_2)  # this uses the double function to multiply the
print(list_1)  # this will print "list_1" list of values
print(list_2)  # This will also print "list_1" values as list_2 is assgined those values
