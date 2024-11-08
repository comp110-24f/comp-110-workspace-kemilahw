"""File to define River class."""

__author__ = "730736603"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creating a River ecosystem with fish and bears."""

    day: int  # attribute
    fish: list[Fish]  # attribute
    bears: list[Bear]  # attribute

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):  # method
        """Checking the fish and bears ages."""
        newlist_fish: list[Fish] = []  # initialize empty list
        newlist_bears: list[Bear] = []  # initialize empty list
        for fish in self.fish:  # accesses each fish in the list
            if fish.age <= 3:
                # if the fish's age is under 3, then they are the "surviving fish"
                newlist_fish.append(
                    fish
                )  # so append the fish to the new list (newlist_fish)
        self.fish = newlist_fish  # update the existing list with the new list after appending the fish
        for bear in self.bears:  # accesess each bear in the list
            if bear.age <= 5:
                # if the bear's age is under 5, then they are the "surviving bears"
                newlist_bears.append(
                    bear
                )  # so append them to the new list (newlist_bears)
        self.bears = newlist_bears  # update the existing list with the new list after appending the bears
        return None

    def remove_fish(self, amount: int):
        """Remove input amount of fish from the river."""
        i: int = 0
        while i < amount:
            self.fish.pop(i)
            # pops the frontmost fish (1st fish); keeps going until it reaches the amount.
            i += 1

    def bears_eating(self):
        """Bears eating fish."""
        for bear in self.bears:  # to access each bear
            if len(self.fish) >= 5:
                # len(self.fish) gives the number of fish in the list
                self.remove_fish(3)
                # call method to remove 3 fish from the river
                bear.eat(3)
                # "bear" represents the "Bear" class; call "eat" method for the bear to eat 3 fish
        return None

    def check_hunger(self):
        """Checking the bear's hunger."""
        new_bear: list[Bear] = []  # initialize empty list for the surviving bears
        for bears in self.bears:  # access each bear to check
            if bears.hunger_score >= 0:
                # if the bears have a hunger score greater than 0, then they are the "surving bears"
                new_bear.append(bears)  # so append them to the new list
        self.bears = new_bear  # update the self.bears list
        return None

    def repopulate_fish(self):
        """Repopulating fish in the river."""
        new_fish: int = (len(self.fish) // 2) * 4
        for _ in range(0, new_fish):  # "_" is an int
            self.fish.append(
                Fish()
            )  # Fish() creates the actual new fish, so append it to the list
        return None

    def repopulate_bears(self):
        """Repopulating bears living by the River."""
        new_bear: int = len(self.bears) // 2
        for _ in range(0, new_bear):
            self.bears.append(Bear())
            # this appends the new bear (bear()) to the list (self.bear)
        return None

    def view_river(self):
        """Prints the River status."""
        print(f"~~~ Day {self.day}: ~~~")  # prints the day
        print(f"Fish population: {len(self.fish)}")
        # prints the number of fish in the list
        print(f"Bear population: {len(self.bears)}")
        # prints the number of bears in the list
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):  # method
        """Simulate one week of life in the river."""
        i: int = 0
        while i < 7:  # calls the one_river_day 7 times
            self.one_river_day()  # calling the method
            i += 1  # increase by 1, therefore it will stop at 7 ( which calls the method 7 times); prevents infinite loop
