# my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict)
# print(my_dict['key1'])
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k2'][2])
print(d['k3']['insideKey'])
d = {'key1': ['a', 'b', 'c']}
my_list = d['key1']
# print(my_list)
letter = my_list[2]
# print(letter)
letter.upper()
print(d['key1'][2].upper())
print(d.keys())
print(d.values())
print(d.items())