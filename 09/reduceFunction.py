from functools import reduce
lst = [34, 23, 24, 24, 100, 2333, 2, 11]
max_find = lambda a, b: a if (a > b) else b

print(reduce(max_find, lst))