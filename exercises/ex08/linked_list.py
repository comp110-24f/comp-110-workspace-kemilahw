"""Exploring linked list utils in class."""

from __future__ import annotations

__author__ = "730736603"


class Node:
    """Class for Creating Node(s)."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Inital constructor."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method."""
        rest: str
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value in the a non-emp."""
    if head.next is None:  # Base case
        return head.value
    else:  # Recursive case
        return last(head.next)


def recursive_range(start: int, end: int) -> Node | None:
    """Creates a linked list of Nodes with values that increment from a start value up to an end value."""
    if start > end:
        raise Exception("Start shouldn't be bigger than end")
    # Base case
    if start == end:
        return None
    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
    return Node(first, rest)


# lots_of_nodes: Node | None = recursive_range(1, 100)


# two: Node = Node(2, None)
# one: Node = Node(1, two)
# print(one)
# print(last(one))


def value_at(head: Node | None, index: int) -> int:
    """Returns the data of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # Base case
        return head.value
    else:  # Recursive case
        val_at_index = value_at(head.next, index - 1)
        # decrease the index by 1, since it goes "backwards" (like memory diagram)
        return val_at_index


def max(head: Node | None) -> int:
    """Returns the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:  # Base case; account for if head.next is none
        return head.value  # if its none, then return the value
    else:
        max_val = max(head.next)  # Recursive case
        if max_val > head.value:  # get the highest value
            return max_val
        else:
            return head.value


def linkify(items: list[int]) -> Node | None:
    """Returns a Linked List of Nodes with the same values in the same order as the input list."""
    if len(items) == 0:  # if the list is empty return None
        return None
    my_node: Node = Node(items[0], linkify(items[1:]))
    # help in office hours; have to change the original elements into a Node
    # call the Node class with the input of the first value in the items list "items[0]" (for ".value")
    # input the recursive case "linkify" as the (.next) by calling linkify using the slice notation to create a new list
    # with the first value "items[0]", then the rest of the values from items "items[1:]"
    return my_node  # return the list of nodes


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list of Nodes by multiplying each value by the factor number."""
    if head is None:
        return None
    newlist_node: Node = Node(head.value * factor, scale(head.next, factor))
    # the comma used when calling "scale" still works because it is adding that value "head.value" to itself by the number of "factor" times. (e.g.
    return newlist_node
