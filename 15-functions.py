# -- Python functions --


def function_name():
    print('Print from function_name')


function_name()


# + Arguments
# Arguments are often shortened to args in Python documentations.
def print_message(message):
    print(message)


print_message('Print from print_message')


# + Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# + Number of Arguments
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.


def print_name(name, family):
    print(name, family)


print_name("More", "Than")


# ::NOTE:: If you try to call the function with 1 or 3 arguments, you will get an error:

# print_name("More", "Than", 5)  # get an error

# + Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments,
# and can access the items accordingly:
# Arbitrary Arguments are often shortened to *args in Python documentations.

def a_func(*arg):
    for i in arg:
        print(i, end=', ')
    print('')


a_func(1, 2, 3)


# + Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments <<does not matter>>
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

def a_func_2(name, family, age):
    print(name, family, age)


a_func_2(family="Than", age=25, name="More")


# + Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def a_func_3(**kwargs):
    print(kwargs['name'], kwargs['family'])


a_func_3(name="More", family="Than")


# + Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def a_func_4(name="More", family="Than"):
    print(name, family)


# + Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_function(food):
    for x in food:
        print(x, end=', ')
    print("")


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# + Return Values
def x2(x):
    return x * 2


print(x2(5))


# + The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def a_func_6():
    pass

# https://www.w3schools.com/python/python_functions.asp
