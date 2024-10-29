"""Practice with dictionary functions!"""

__author__ = "730736603"


def invert(input_list: dict[str, str]) -> dict[str, str]:
    """The input list's keys and values should swap in the output list"""
    output_list: dict[str, str] = {}
    for elem1 in input_list:  # accesses the string to be compared
        count: int = 0
        # variable needs to be inside the for loop but outside of the inner for loop; allows the count to restart versus continuing
        for elem2 in input_list:
            if input_list[elem1] == input_list[elem2]:
                # if at the index string (value) is the same as at the index of the other (value) string, then add to count
                count += 1
                # this means that there has been a duplicate key found, so once the count reaches 1, then it will raise an error
            if count > 1:
                # more than one of the same key has been found, so raise KeyError
                raise KeyError("The Keys are the same!")
    for keys in input_list:
        value = keys
        # the input keys becomes the values
        keys_to = input_list[value]
        # the input values become the keys
        output_list[keys_to] = value
        # assign elements to the empty dict; inverts the keys and values.
    return output_list


def favorite_color(ppl_color_list: dict[str, str]) -> str:
    """returns the most favorited color"""
    new_dict: dict[str, int] = {}
    # initialize an empty dict to create a new dict with the colors and values (from the number of times that color appears)
    current_color: str = ""  # track the current color
    highest_num: int = 0  # track the highest number of (most popular color)
    for (
        names
    ) in (
        ppl_color_list
    ):  # "names" represents the keys in the input list (ppl_color_list)
        if ppl_color_list[names] in new_dict:
            # checking to see if the color is already established as a key in the new_dict
            # if the person (ppl_color_list[names] - Key) favorite color (value) is in the new dictionary; then increase by one (number of times the color appears)
            new_dict[ppl_color_list[names]] += 1
        else:
            new_dict[ppl_color_list[names]] = (
                1  # else, we need to add the color to the new dictionary assigning it with the value of 1
            )
    for colors in new_dict:  # to obtain the most popular color; create another for loop
        if new_dict[colors] > highest_num:
            # if the value (number of times the color appeared) at the key (color) is greater than the highest number (starts at 0 since we do not have the highest value yet; have not compared it to anything yet)
            current_color = (
                colors  # update the current color with the color that we are on
            )
            highest_num = new_dict[colors]
            # update the highest_num with the value that is greater than the current highest number (0), which is the value at the key (new_dict[colors])
    return current_color  # return the current color that is most popular


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times that a value appears in the input list"""
    new_dict: dict[str, int] = (
        {}
    )  # initialize an empty dict for the items and the count of each item in the list
    for value in range(
        0, len(input_list)
    ):  # loop through each item in the list (input_list)
        if input_list[value] in new_dict:
            # checking to see if that item has already been established as a key in the new dictionary
            new_dict[
                input_list[value]
            ] += 1  # if it is, then increase the value associated with the key by 1
        else:
            new_dict[input_list[value]] = (
                1  # if not, then assign that value associated with key to 1
            )
    return new_dict  # return the new dictionary; should have each item from the input list (str) with the count of each item (int)


def alphabetizer(list_words: list[str]) -> dict[str, list[str]]:
    """Creates a dictionary of the letters and the list of words that belong to that letter"""
    result_dict: dict[str, list[str]] = {}  # initialize an empty dict
    for (
        elems
    ) in list_words:  # elems represent the words from the input list (list_words)
        if elems[0].lower() in result_dict:
            # "elems[0]" is the beginning letter of the input "word" (e.g. "happy" -> elems[0] -> "h")
            # checking to see if the letter is in the new dictionary (result_dict) as a key
            # .lower() returns the lower cased string of a given string; in case of a capitalized word is given then it can still be added to the list
            result_dict[elems[0].lower()].append(
                elems
            )  # if so, append the list of words associated with that letter to that key (the letter)
        else:
            result_dict[elems[0].lower()] = [
                elems
            ]  # if not, only assign the "word" not words that is associated only with that letter to that key (the letter)
    return result_dict  # return the new dictionary


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updating attendance log by mutating the existing dict."""
    if day in attendance_log:  # check to see if the given day is in the attendance log
        if not (student in attendance_log[day]):
            # check to see if the student is in attendance at that day, if the student is "not" "in" attendance on that day, then do nothing
            attendance_log[day].append(
                student
            )  # if so, then add their name to that day
    else:
        attendance_log[day] = [student]
        # else if the day is not listed in the attendance log, then add it to the log with the name of the "student" who attended on that day
