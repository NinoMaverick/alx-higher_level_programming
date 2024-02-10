#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # a function that replaces all occurrences of an element by another in a new list.
    
    new_list = []
    # create a new list that would be printed when the replacements are done

    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
        
    search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)