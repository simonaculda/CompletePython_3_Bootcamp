def fahrenheit(T):
    return (9.0/5)*T + 32


# print(fahrenheit(0))
# temp = [0, 22.5, 40, 100]
# print(list(map(fahrenheit, temp)))
# print(list(map(lambda T: 9.0/5 *T + 32, temp)))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(list(map(lambda x, y, z: x+y+z, a, b, c)))
print(list(map(lambda num: num * -1, a)))
