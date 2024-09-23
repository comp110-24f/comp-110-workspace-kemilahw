"""Iterate over a string"""

__author__: str = "730736603"


def num_instances(
    phrase: str, search_char: str
) -> (
    int
):  # defining the num_instances function with the input of phrase and search_char to count the number of times the single charcter appears in the phrase.
    """Count of occurrences"""
    count: int = (
        0  # the count starts at 0 initally, also it counts the number of times the character is shown in the phrase
    )
    index: int = (
        0  # the index is used to find the character in each phrase by using a number to label each letter (starting at 0), for example: if hello[1] is used, then the index ([1]) will return the letter "e". It also starts at 0.
    )
    while index < len(
        phrase
    ):  # the while loop, if the length of the phrase is greater than the index then we enter the repeat block. This repeats the statements below and checks to see if it is still true.
        if (
            phrase[index] == search_char
        ):  # the if statement, if the character that is pulled by the index (example: [0], should pull "h" from "hello") equals the searched character (Example: "h") then move to the next step below it (count is next)
            count = (
                count + 1
            )  # if the "if statement" is true, then we add the count (= number of times the letter appeared) to the count while increasing it after every loop.
            index = index + 1  # if its true, add to the index and increase by 1
        else:
            index = (
                index + 1
            )  # if the "if statement" is false, then we skip the count and come here. It will add to the index, increasing it by 1
    return count  # return the count to have the number of occurrences
