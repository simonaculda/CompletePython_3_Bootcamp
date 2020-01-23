def add(n1, n2):
    print(n1 + n2)


# result = 0
# try:
#     # WANT TO ATTEMPT THIS CODE
#     # MAY HAVE ERROR
#     result = 10 + 10
# except:
#     print("Hey it's look like you are't adding correctly")
# else:
#     print("Add went well!")
#     print(result)

# print(add(10, 20))
# number1 = 10
# number2 = input("Please provide a number")
# print(add(number1, number2))
# print(result)


# try:
#     f = open('testfile', 'w')  # 'r' to induce an error
#     f.write("Write a test line ")
# except TypeError:
#     print("There was a type error!")
# except OSError:
#     print("Hey you have an OS Error")
# finally:
#     print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number"))
        except:
            print("Whoops that is nor a number ")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")


ask_for_int()



























