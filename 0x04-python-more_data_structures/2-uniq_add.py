#!/usr/bin/python3
def uniq_add(my_list=[]):
    # func that adds all unique integers
    t = 0
    g = set(my_list)
    for i in g:
        t += i
    return t
    
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))