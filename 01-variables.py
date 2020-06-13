# -- Variables in python --

v1, v2, v3 = 10, 11, 12
none_var = None


def calculate():
    global v1, v2
    v1 = 0
    v2 = 0


calculate()
print(v1 + v2 + v3)

if none_var == None:
    print("None Value")
else:
    print("Value by other type")

# https://www.w3schools.com/python/python_variables.asp
