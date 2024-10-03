"""Concatenation of strings"""

__author__ = "730736603"


def concat(one: str, two: str) -> str:
    """Concatenation of two strings"""
    return (
        one + two
    )  # this returns concatenation of two strings (e.g. "hey" + "person" -> "Hey person")


if (
    __name__ == "__main__"
):  # allows the called function to still occur while beig ran in a file
    word1: str = "happy"  # local variable (global variable)
    word2: str = "tuesday"  # local variable (global variable)
    print(
        concat("happy", "tuesday")
    )  # printing the results from calling the concat function
