# -- Python Modules --
import module_1.test_module as test
from module_1.test_module import Student as MyStudent
from module_1.my_module import say_hello as hi

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# + Create a Module
# To create a module just save the code you want in a file with the file extension .py


# + Use a Module
# Now we can use the module we just created, by using the import statement:
# ::NOTE:: When using a function from a module, use the syntax: module_name.function_name.

# from module_1.my_module and say_hello
hi()

# + Variables in Module
# The module can contain functions,
# as already described, but also variables of all types (arrays, dictionaries, objects etc):

print(test.a_var)

obj = test.Student()
obj.add_student('More', 25)
obj.add_student('More Than', 28)

print(obj.get_students())

students = MyStudent()
students.add_student('More', 25)

# + Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# + Re-naming a Module
# You can create an alias when you import a module, by using the as keyword
# Create an alias for module_1.my_module called mx:
# import module_1.my_module as mx

# + Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
# Import and use the platform module:

import platform

x = platform.system()
print(x)

import os

os.system('date')
output = os.popen('date')
print(output.read())

# + Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
# ::NOTE:: The dir() function can be used on all modules, also the ones you create yourself.

x = dir(test)
print(x)

# + Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from module_1.test_module import Student

st = Student()
st.add_student("More", 25)

# ::NOTE:: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: var_name, not module_name.var_name

# https://www.w3schools.com/python/python_modules.asp
