def even_check(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False


lst = list(range(10))
# print(lst)
print(list(filter(even_check, lst)))
print(list(filter(lambda num: num % 2 == 0, lst)))
l = [(1, 2), (3, 4), (5,6)]


