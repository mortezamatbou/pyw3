# -- Python Try Except --

# The <<try>> block lets you test a block of code for errors.
# The <<except>> block lets you handle the error.
# The <<finally>> block lets you execute code, regardless of the result of the try- and except blocks.

try:
    # This statement will raise an error, because x is not defined:
    print(x)
except:
    print("An exception occurred")

# + Many Exceptions
# You can define as many exception blocks as you want,
# e.g. if you want to execute a special block of code for a special kind of error:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# + Else
# You can use the else keyword to define a block
# of code to be executed if no errors were raised:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# + Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# ::NOTE:: This can be useful to close objects and clean up resources:
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Try to open and write to a file that is not writable:
try:
    f = open("./assets/sample.txt")
    f.write("Hi")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# + Raise an exception

x = -1
if x < 0:
    # raise Exception("Sorry, no numbers below zero")
    pass

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# Raise a TypeError if x is not an integer:
x = "Hello"
if not type(x) is int:
    # raise TypeError("Only integers are allowed")
    pass

# https://www.w3schools.com/python/python_try_except.asp
