# -- Boolean types in python --

# The following will return False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# The following will return True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


class Test:
    name = 'Name'

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __len__(self):
        # this made type of class False
        return 0


obj = Test("Ali")
print("Test class: ", bool(obj))

type_23 = 200
type_23_2 = 200.5
type_24 = "400"
type_25 = "400"

if isinstance(type_23, int):
    print("type_23 is int")

if isinstance(type_23_2, float):
    print("type_23_2 is float")

if isinstance(type_24, str):
    print("type_24 is str")

if isinstance(int(type_25), int):
    print("type_25 is int")

# https://www.w3schools.com/python/python_booleans.asp
