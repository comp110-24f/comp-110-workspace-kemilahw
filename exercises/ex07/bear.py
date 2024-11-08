"""File to define Bear class."""


class Bear:
    """Class to represent the Bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initial constructor."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day of life by the river for bears."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Amount of fish eaten by the bear."""
        self.hunger_score += num_fish
