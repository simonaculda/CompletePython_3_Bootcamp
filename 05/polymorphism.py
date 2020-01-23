class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Says Woof'


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' Says meow'


niko = Dog('Niko')
felix = Cat('Felix')
#
# print(niko.speak())
# print(felix.speak())
#
# for pet in [niko,felix]:
#     print(type(pet))
#     print((pet.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)

