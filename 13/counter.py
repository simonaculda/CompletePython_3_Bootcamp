# Counter
# quickly count the element of a list
# return a dictionary

from collections import Counter
l = [1, 1, 2, 1, 12, 3, 3, 4, 4, 2, 1]
# print(Counter(l))

s = "aaaaaasssssdffhfghffgd"
# print(Counter(s))

s1 = "How many times each word show up in this sentence word word shoe up up show"
words = s1.split()
c = Counter(words)
# print(c.most_common(3))
print(sum(c.values()))
