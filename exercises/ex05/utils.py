"""Implementing more list utility functions."""

__author__ = "730736603"


def only_evens(nums: list[int]) -> list[int]:
    """Returning only even elements in the list."""
    remainder: int = 0
    even_nums: list[int] = []
    # initialize a empty list so the even numbers can be added later
    for elems in nums:
        # "elems" iterates over each element in the "nums" ist
        if (elems % 2) == remainder:
            # to obtain only even numbers, then each "elem" has to be divided by 2 and return a remainder of 0 to be considered "even"
            even_nums.append(elems)
            # this adds the even "elem" (number in the list) to the empty list (even_nums)
    return even_nums


# even_nums should be return so all the even values are in a list


def sub(vals: list[int], start_id: int, end_id: int) -> list[int]:
    """Creates a subset of values from the inputed list."""
    sub_nums: list[int] = []
    if start_id < 0:
        start_id = 0  # assign the start index to 0; this is used to start at the beginning of the list
    if end_id > len(vals):
        end_id = len(
            vals
        )  # to get the element at the end of the list because of the end index being greater than the len(vals)
        # assign the end index to length of vals (total number of elements in the list) subtracted by 1; this gives access to what is at the end of the list
    while start_id < end_id:
        sub_nums.append(vals[start_id])
        # to create the subset of the "vals" list; adds the value from "vals" list using the start index; (e.g. vals=[1,2,3], sub_nums.append(vals[2]) -> sub_nums = [3] "3" is now in the new list "sub_nums")
        start_id += 1  # increases the start index by 1 until it reaches the end index (e.g. list1=[1,2,3,5,6] start_id = 1, end_id = 4; first loop until last loop (end index): new_list=[2, 3, 5])
    if len(vals) == 0:
        return sub_nums
    if start_id >= len(vals):
        return sub_nums
    if end_id <= 0:
        return sub_nums
    return sub_nums  # should return the new list (subset of the input list)


def add_at_index(list_num: list[int], elem: int, id: int) -> None:
    """Adds an element at a specific index"""
    if id < 0 or id > len(list_num):
        raise IndexError("Index is out of bounds for the input list")
    list_num.append(elem)  # adds the "elem" to the end of the list
    val: int = len(list_num) - 1
    # created variable to use when shifting elements to the right to create the space needed to add the "elem" in
    # by setting the "val" variable to the (length of list_num - 1) it can access the element at the end of the list; (e.g. if list_num = [1,2,3,4], then len(list_num) = 4 subtracted by 1 is 3,
    # so if i do list_num[3] then i would get the last element in the list)
    while id < val:
        list_num[val] = list_num[val - 1]
        # set the last element in the list to element in front of it, so the element in front of it can take its position; shifting to the right
        val -= 1
        # moves the elements to right in the list every time it loops until there is space for the inputed "id" (index) to insert the "elem" (e.g. elem = 9, id = 3 [6,7,8,10] -> [6, 7, 8, _ , 10] the 9 will go in front of the 10)
    list_num[id] = elem
    # After looping, there is space to insert the new "elem" at the correct "id" (index)
