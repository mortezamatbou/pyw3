# -- Mutability in python --

a_dict = {
    'Mori': 10,
    'Ali': 10,
    'Alish': 10
}

print("1] ", id(a_dict))

a_dict = {
    'Mori': 10,
    'Ali': 10,
    'Alish': 10
}

print("2]", id(a_dict))
a_dict.update(Mori2=10)

print("3]", a_dict)
print("4]", id(a_dict))

num = 10
print("5]", id(num))
num += 1
print("6]", id(num))
num = 20
print("7]", id(num))

a_list = ["Mori", "Ali", "Alish"]
print("8]", id(a_list))

a_list.append("Mori2")
print("9]", id(a_list))

"""
integers -> all functions return new int objects
floats
strings
tuples
"""
