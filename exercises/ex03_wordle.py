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
    set_turns: int = (
        6  # local variable to set the turns to 6 instead of typing 6 within the body
    )
    num_turns: int = (
        1  # keeps track of the number of turns (guesses); starts at 1 instead of 0 so the display of turns shows "Turn 1"
    )
    user_won: bool = False
    while (
        num_turns <= set_turns and not user_won
    ):  # instructions were to "make game loop while the user still has turns left and has not yet won" instead of making it numb_guesses<= set_turns; this also makes the statement true
        print(
            f"=== Turn {num_turns}/{set_turns} ==="
        )  # print the current turn number; not by typing 6 in (use set_turns that is set as 6)
        word_guessed = input_guess(
            len(secret)
        )  # prompting the users to enter their guess
        guess_results = emojified(
            word_guessed, secret
        )  # codify the emoji result of the user's guess
        print(guess_results)  # print the string concatenation of emojis
        if (
            word_guessed == secret
        ):  # ends game; do not have to change number of turns b/c the user has guessed correctly
            user_won = True  # this becomes true because the user has won the game
        else:
            num_turns += 1  # increase by 1 to prevent infinite loop; this is the "next turn" if the user does not guess correctly
    if user_won:
        print(
            f"You won in {num_turns}/{set_turns} !"
        )  # print statement for the user winning
    else:
        print(
            f"X/{set_turns} - Sorry, try again tomorrow!"
        )  # print statement if the user does not win


if __name__ == "__main__":
    main(secret="codes")
