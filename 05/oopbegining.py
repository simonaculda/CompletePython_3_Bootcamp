class Dog():
    # constructor for a class
    # is going to be called automatically when you create an instance of a  class
    # self represent the instance of the object itself
    # CLASS OBJECTS ATTRIBUTES
    # SAME FOR ANY INSTANCE OF A CLASS

    species = 'mammal'

    def __init__(self, breed, name):

        # Attributes
        # We take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # expect a boolean True/ False

    # Operation/ actions ---> Methods
    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))


# my_dog = Dog(breed='Lab', name='Sammy', spots=False)
# my_dog = Dog('Lab', 'Frankie')
# print(my_dog.name)
#
# print(my_dog.species)
# print(my_dog.breed)
# print(my_dog.bark(12))


class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi  # Circle.pi to make clear that is a class object attribute

    # Methods
    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.pi)
print(my_circle.get_circumference())
print(my_circle.area)
