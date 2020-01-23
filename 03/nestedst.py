# x = 25
#
#
# def printer():
#     x = 50
#     return x
#
#
# print(x)
# print(printer())

name = 'This is a global string' #global


def greet():

    name = 'Sammy' # Enclosing function locals

    def hello():
        name = 'I AM a LOCAL'  #LOCAL
        print('Hello '+name)

    hello()


greet()

