from collections import namedtuple
# t = (1, 2, 3)

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
print(sam.age)
print(sam.name)
# is just like a tuple but basically create a new object type and allows names for various field

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy', claws=False, name='Kitty')
print(c.name)
print(c[2])
