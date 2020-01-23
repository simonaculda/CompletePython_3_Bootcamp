# two.py
import one
print("top level in two.py")

one.func()

if __name__ == '__main__':
    print("TWO.PY IS BEEN RUN DIRECTLY")
else:
    print("TWO.PY HAS BEEN IMPORTED")
