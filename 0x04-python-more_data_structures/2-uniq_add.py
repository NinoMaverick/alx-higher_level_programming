#!/usr/bin/python3
def uniq_add(my_list=[]):
    # func that adds all unique integers
    t = 0
    g = set(my_list)
    for i in g:
        t += i
    return t

j = [1, 2, 3, 1, 3, 4]
print(uniq_add(j))