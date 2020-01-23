# for num in range(0, 11, 2):
#     print(num)

#
# word = 'abcde'
#
# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')
#
# my_list1 = [1, 2, 3]
# my_list2 = ['a', 'b', 'c']
# for item in zip(my_list1, my_list2):
#     print(item)
# print(list(zip(my_list1, my_list2)))

# my_list = [10, 20, 30, 50,100]
# print(min(my_list))
# print(max(my_list))
# from random import shuffle
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(my_list)
# print(my_list)


my_list = [num ** 2 for num in range(10)]
print(my_list)
my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

