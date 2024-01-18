#!/usr/bin/python3
for num in range(0, 10):
    for numbs in range(num+1,10):
        if num == 8 and numbs == 9:
            print("{}{}".format(num, numbs))
        else:
            print("{}{}".format(num, numbs), end=", ")
