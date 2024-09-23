"""A simple number guessing game!"""

__author__: str = "730733603"


def guess_a_number() -> None:
    secret: int = 7  # Local variable -> name: type = value
    x: int = int(
        input("Guess a number:")
    )  # The "x" represents the guessed number that is an integer
    print(
        "Your guess was " + str(x)
    )  # "str(x)" has to be added into the following string in order for it to print the guessed number
    if (
        secret == x
    ):  # secret is the number 7 and if its equal to the guessed number ("x"), then it is correct
        print("You got it!")
    elif (
        secret > x
    ):  # if the secret value (7) is greater than the guessed value, then the guess value is too low
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        if (
            secret < x
        ):  # if the guessed value ("x") is greater than the secret value (7), then the guessed value is too high
            print(
                "Your guess was too high! The secret number is " + str(secret)
            )  # the "str(secret)" is added to the following string in order to print the correct value of the "secret"
    return None


if __name__ == "__main__":
    guess_a_number()
