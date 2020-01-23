def func():
    return 1


def hello():

    return "Hello"


greet = hello
del hello
# print(hello())
print(greet())
# print(func())
