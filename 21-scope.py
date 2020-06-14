# -- Python Scope --
# A variable is only available from inside the region it is created. This is called scope.

# + Local Scope
# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.

x_1 = 100


def my_func():
    x_1 = 200
    print("Print from my_func:", x_1)


my_func()
print("Global x_1 value:", x_1)

x_2 = 200


def func_2():
    global x_2
    x_2 = 100


func_2()
print(x_2)

x_3 = 10.2


def func_3():
    # x_3 = 10.5
    print(x_3)


func_3()

test_var_name = 10.6


def check_variable_in_global(var_name):
    if var_name in globals():
        return True
    return False


print("Check variable in global <script>", check_variable_in_global('test_var_name'))
print("Check variable in global <script>", check_variable_in_global('test_var_name_2'))

var_2 = 22.23


class A:

    def check_var_in_global(self, var_name):
        var_1 = 10.3
        if var_name in globals():
            return True
        return False

    def check_var_in_local(self, var_name):
        var_1 = 10.5
        if var_name in locals():
            return True
        return False


obj = A()
print("Check Global in class:", obj.check_var_in_global('var_1'))
print("Check Global in class:", obj.check_var_in_global('var_2'))
print("Check Local in class:", obj.check_var_in_local('var_1'))


def def_1():
    x = 33.22

    def def_2():
        print(x)

    def_2()


def_1()

# https://www.w3schools.com/python/python_scope.asp
