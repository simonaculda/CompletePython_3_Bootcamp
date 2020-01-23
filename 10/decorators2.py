# how to pass in func into another function


def hello():
    return "Hi Simona!"


def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

# hello - when you just pass it in
# hello() - when you executed it


other(hello)



