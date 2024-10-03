"""Practicing with lists"""

# creating a list variable that's initally empty
my_numbers: list[float] = []
print(my_numbers)

# let's add ("append") a value to the end of the list
my_numbers.append(1.5)
print(my_numbers)

# Make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points[2])

# Changing the value of an item
game_points[1] = 72
print(game_points)
# print(len(game_points))
game_points.pop(1)
print(game_points)

# Can we cahnge individual chars in strings this way?
my_name: str = "Milah"
# my_name[1] = "y"  # didnt work. try converting it.
name_as_list: list[str] = list(my_name)
print(name_as_list)
name_as_list[1] = "y"
print(name_as_list)
name_as_list.append("h")
print(name_as_list)

name_as_list.insert(3, "l")
print(name_as_list)

grocery_list: list[str] = ["banana", "apple", "carrot"]
# print((len(grocery_list))) # lesson quiz, this accesses the last item of the list.
# grocery_list.append("beans")
# print(grocery_list)
# grocery_list.pop(1)
# print(grocery_list)
# grocery_list[10] # for lesson quiz, received an index error
# print(grocery_list)
# grocery_list.append("bananas")
# print(grocery_list)
