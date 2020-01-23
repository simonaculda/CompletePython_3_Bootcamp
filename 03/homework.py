# def palindrome(s):
#     s = ''.join(s.split())
#     if len(s)% 2 == 0:
#         return s[:len(s)//2][::-1] == s[(len(s)//2):]
#     else:
#         return s[:len(s)//2][::-1] == s[(len(s)//2)+1:]
#
#     # print(s[:len(s)//2][::-1])
#     # print(s[(len(s)//2):])
#
#
# print(palindrome('helaleh'))
# print(not True)

import string


def ispanagram(str1, alphabet=string.ascii_lowercase):
    frec = [0] * len(alphabet)
    for char in ''.join(str1.split()):
        if frec[alphabet.index(char.lower())] == 0 and char in alphabet:
            frec[alphabet.index(char.lower())] = 1
    return not (0 in frec)


print(ispanagram('The quick brown fox jumps over the lazy dog'))

