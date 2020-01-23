class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self):
        print('I am a dog!')

    def bark(self):
        print('WOOF!')

    def eat(self):
        print('I am a dog and eating')


my_dog = Dog()
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_dog)

my_animal = Animal()
print(my_animal)
print(my_animal.eat())
print(my_animal.who_am_i())
