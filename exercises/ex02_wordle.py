"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730736603"


def input_word() -> str:  # defining the function
    word_entered: str = input(
        "Enter a 5-character word: "
    )  # creating a local variable for the input word
    if len(word_entered) == 5:  # the length of input word must be 5 characters
        print(word_entered)
    else:
        if (
            len(word_entered) != 5
        ):  # if the input word does not equal 5 characters, then it prints a different message
            print("Error: Word must contain 5 characters.")
        exit()  # exit function is used if an input word does not meet the 5 characters, therefore the program will stop running after the error message.
    return word_entered


def input_letter() -> str:
    letter_entered: str = input(
        "Enter a single character: "
    )  # creating a local variable for the input character (letter)
    if (
        len(letter_entered) == 1
    ):  # if the input character is equal to a single length (one character), then that character will print
        print(letter_entered)
    else:
        if (
            len(letter_entered) != 1
        ):  # if the input character is not equal to an single length (single character), then it will print an error message
            print("Error: Character must be a single character.")
        exit()  # exit function is used if the input character is not a single character, therefore the program will exit after the error message
    return letter_entered


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)  # string concatenation
    count: int = 0
    if letter == word[0]:
        count = count + 1
        print(letter + " found at index 0")
    if letter == word[1]:
        count = count + 1
        print(letter + " found at index 1")
    if letter == word[2]:
        count = count + 1
        print(letter + " found at index 2")
    if letter == word[3]:
        count = count + 1
        print(letter + " found at index 3")
    if letter == word[4]:
        count = count + 1
        print(letter + " found at index 4")
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
