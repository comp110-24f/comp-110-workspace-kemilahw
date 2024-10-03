"""Wordle game"""

__author__ = "730736603"


def input_guess(secret_word_len: int) -> str:
    """input guessed word of same length as secret word"""
    # This prompts the user to enter their guess"
    user_guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # input a guess
    while (
        len(user_guess) != secret_word_len
    ):  # evaluates the length of the "user_guess" not being equal to the length of "secret_word_len"; entering the body
        user_guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # this prompts the user_guess to try again b/c the length of their guessed word doesn't equal the correct length
    print(
        user_guess
    )  # if the user_guess is the same length as secret_word_len, this prints the user_guess
    return user_guess  # return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Testing each index of a word to see if it matches the single character"""
    assert len(char_guess) == 1  # ensures that char_guess is a single character
    index: int = 0
    while (
        len(secret_word) > index
    ):  # length of secret word is greater than index value; enter the body
        if (
            secret_word[index] == char_guess
        ):  # if the secret word at index (value to represent the position) is equal to the guessed character; enter body under it
            return True  # Return true if the "if" statement is true
        index += (
            1  # increase index by 1 to prevent infinite loop and to check each indices
        )
    return False  # return false if the "while loop" evaluates to false


def emojified(guess: str, secret: str) -> str:
    """Using emojis to represent the accuracy of a guess in relation to a secret word by comparing two strings of equal length"""
    assert len(guess) == len(
        secret
    )  # ensures that the length of guess is equal to the length of secret
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # ^ named constants; variables that will not change later in the program (also, these evaluate to emojis)
    index: int = 0
    emojis: str = (
        ""  # similar to count(), but instead given the name "emojis" (by choice) and the type is str because the emojis are going to be a concatenated string
    )
    # the empty string is used because the emojis are going to be put together into a string
    while (
        len(secret) > index
    ):  # if the length of secret is greater than the index value; enter the body
        if (
            guess[index] == secret[index]
        ):  # if the character at the index of the guess word matches (equal) the character at the same index of the secret word; enter body
            emojis = (
                emojis + GREEN_BOX
            )  # shows the emojis that represent the correctly matched character in the correct position
        else:
            if contains_char(
                secret, guess[index]
            ):  # utilizing the "contains_char" function to determine if the index of a character in the guess word is present in the secret word at the same position; therefore, it helps determine whether to use white or yellow
                # continuance -> this is found by searching through the "secret" and checking "guess[index]"  to see if a character matches at the current index
                emojis = (
                    emojis + YELLOW_BOX
                )  # if it contains a matched character at the wrong position, a yellow box must be printed at that specific position
            else:
                emojis = (
                    emojis + WHITE_BOX
                )  # else if there are not any instances of the character at the current index, print a white box
        index += 1  # prevents the infinite loop while increasing the index by 1 to iterate over each character
    return emojis  # return emojis to get the string concatenation of emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    num_turns: int = (
        1  # keeps track of the number of turns; starts at 1 instead of 0 so the display of turns shows "Turn 1"
    )
    while (
        num_turns <= 6
    ):  # if the number of turns is less than or equal to the set amount of turns (6); enter the body
        print(f"=== Turn {num_turns}/6 === ")  # print statement for the number of turns
        word_guessed: str = input_guess(
            len(secret)
        )  # variable for the prompting the user for a guess, using the input_guess function with length of secret to match the parameter (int); this uses the secret word as an input
        print(
            emojified(word_guessed, secret)
        )  # print statement for the string concatenation of emojis
        if (
            word_guessed == secret
        ):  # if the user_guess_2 (word guessed) is equal to the secret (secret word); enter body
            print(
                f"You won in {num_turns}/6 turns!"
            )  # if its equal, print the statement with the amount turns it took to guess the secret word correctly
            num_turns = 7  # changed the number of turns to 7, so the loop will exit after evaluating the while statement
        else:
            num_turns += 1  # else increase the number of turns by 1 if the "if statement" isn't true
            if (
                num_turns > 6
            ):  # if the number of turns are greater than the set amount (6) turns, then move into body
                print(
                    "X/6 - Sorry, try again tomorrow!"
                )  # print statement for not guessing the correct word in 6 guesses or less


if __name__ == "__main__":
    main(secret="codes")
