def my_func(*args):
    return sum(args) * 0.05


# print(my_func(40, 60))


def my_func1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'. format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


# my_func1(fruit='apple', veggie='lettuce')


def my_func2(*args, **kwargs):
    print('I would like {} {}'. format(args[0], kwargs['food']))


my_func2(10, 20, 30, fruit='Orange', food='eggs', animal='dog')

# print(('mama'.upper()))


