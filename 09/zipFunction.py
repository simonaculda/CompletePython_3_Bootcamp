# x = [1, 2, 3]
# y = [4, 5, 6]
# print(list(zip(x, y)))
#
# a = [1, 2, 3, 4, 5]
# b = [2, 2, 10, 1, 1]
# print(list(map(lambda pair: max(pair), zip(a, b))))

# for pair in zip(a,b):
#     print(max(pair))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}


def switcharoo(d1, d2):

    dout = {}
    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val
    return dout


# print(d1)
# print(d2)
print(switcharoo(d1, d2))