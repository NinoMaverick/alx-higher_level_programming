#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # function that replaces all occurrences of an element in a new list.
    new_list = []
    # create a new list that would be printed when the replacements are done

    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
