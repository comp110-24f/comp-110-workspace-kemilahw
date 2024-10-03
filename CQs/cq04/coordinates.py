"""Coordinates function"""

__author__ = "730736603"


def get_coords(xs: str, ys: str) -> None:
    """Print the formatted pairs of each character in the two input strings"""
    index: int = (
        0  # Declaring the index variable with the count starting at 0; this allows the loop to iterate over every character (for the first while loop (xs))
    )
    while index < len(
        xs
    ):  # if the index is less than the length of the string (xs: str), then it moves into the body of the while loop
        index: int = (
            0  # declare index variable for the while loop that is nested into this to iterate over each character in the (ys)
        )
        index += 1  # to prevent an infinite loop, increase the variable by 1 to also be able to iterate over each character
        print(xs)  # print the character within xs for the "x" value of the coordinate
        while index < len(
            ys
        ):  # if the index is less than the length of the string (ys: str), then move into the body of the function
            index += 1  # increase the index variable by 1 to iterate over every character in (ys)
            print(
                xs, ys
            )  # finally, print the character in xs, then the character in ys
