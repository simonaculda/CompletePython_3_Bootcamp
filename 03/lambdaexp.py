def square(num):
    return num**2


my_mums = [1, 2, 3, 4, 5]
# for item in map(square, my_mums):
#     print(item)
print(list(map(square, my_mums)))
# lambda exp
print(list(map(lambda num: num ** 2, my_mums)))


def splicer(mystring):
    if len(mystring)%2 ==0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Simona', 'Dani', 'Ali', 'Sergiu', 'Aliona', 'Eve']
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))


# def square(num): return num ** 2
lambda num: num ** 2


print(square(5))

print(list(map(lambda name: name[::-1], names)))
