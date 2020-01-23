l = ['a', 'b', 'c']
for count, item in enumerate(l):
    print(count, item)

for count, item in enumerate(l):
    if count >= 2:
        break
    else:
        print(item)