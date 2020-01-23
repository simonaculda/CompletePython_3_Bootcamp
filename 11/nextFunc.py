def simple_gen():
    for x in range(3):
        yield x


# for numb in simple_gen():
#     print(numb)
# g = simple_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

s = "Hello"
# for letter in s:
#     print(letter)
# next(s) # we can't do this
s_iter = iter(s)
print(next(s_iter))