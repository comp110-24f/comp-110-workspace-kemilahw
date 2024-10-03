"""Visualize practice"""

__author__ = "730736603"


from CQs.cq04.concatenation import concat

x: str = "123"  # global variable
y: str = "abc"  # global variable
print(
    concat("123", "abc")
)  # printing the results of calling the concat function with the global variables as the arguments

from CQs.cq04.coordinates import get_coords

get_coords("123", "abc")
# calling the get_coords function with the x and y global variables as the argument
