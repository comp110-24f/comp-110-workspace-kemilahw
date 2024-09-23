"""A program to plan a tea party."""

__author__ = "730736603"


def main_planner(guests: int) -> None:
    """Brings all the functions together"""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# Called each function and pulled the strings together within each print statement
# For the cost statement, each argument is set to the function that goes with it. Tea_count is based on the number of tea bags needed as treat_count is based on the number of treats needed


def tea_bags(people: int) -> int:
    """Number of tea bags needed"""
    return people * 2


# Multiplication used to show that each person receive 2 tea bags
# I struggled at first with constructing the return statement; I used the powerpoints to help


def treats(people: int) -> int:
    """Number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


# I am confused on how to convert the calling of the tea_bag function
# Use int() to convert the function that is being called


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats combined"""
    return float((tea_count * 0.50) + (treat_count * 0.75))


# tea_count multiplied by its given value and treat_count is multiplied by its given value, then both are added together to get the sum

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
