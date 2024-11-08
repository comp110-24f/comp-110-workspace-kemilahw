"""File to define Fish class."""


class Fish:
    """Class represents the fish living in the river."""

    age: int

    def __init__(self):
        """Initial constructor."""
        self.age = 0
        return None

    def one_day(self):
        """One day of life in the river for fish."""
        self.age += 1
        return None
