# def name_function():
#     """
#     DOCSTRING: Information about the function
#     INPUT:
#     OUTPUT:
#     :return: NO
#     """
#     print("Hello")
#
#
# def say_hello(name='NAME'):
#     return 'hello ' + name
#
#
# result = say_hello('Simona')
# # print(result)
#
# def add(n1, n2):
#     return n1 + n2
#
#
# print(add(2, 3))


def dog_check(s):
    """
    Find out if the word 'dog' is in  a string
    :param s: str
    :return:
    """
    # if 'dog' in s.lower():
    #     return True
    # else:
    #     return False
    return 'dog' in s.lower()


# print(dog_check('My dog ran away '))
# print(dog_check('My cat ran away'))
# print(dog_check('Dog ran away'))


def pig_latin(word):

    firs_letter = word[0]

    # check if is vowel
    if firs_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:]+firs_letter +'ay'
    return pig_word


print(pig_latin('apple'))
print(pig_latin('word'))

