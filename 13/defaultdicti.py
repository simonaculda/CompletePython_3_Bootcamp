from collections import defaultdict

# d = {'k1': 1}
# print(d['k1'])
# print(d['k2'])

# d = defaultdict(object)
# d['one']
# for item in d:
#     print(item)

d = defaultdict(lambda: 0)
d['one']
print(d['one'])
d['two'] = 2
print(d)

