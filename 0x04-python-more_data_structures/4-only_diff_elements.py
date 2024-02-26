#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # function that returns a set of all elements present in only one set
    only_diff_set = set()
    for i in set_1:
        if i not in set_2:
            only_diff_set.add(i)
    for i in set_2:
        if i not in set_1:
            only_diff_set.add(i)
    return only_diff_set
