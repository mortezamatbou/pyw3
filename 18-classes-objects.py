# -- Python Classes and objects --

# + Python Classes/Objects
# Python is an object oriented programming language.
# Everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# + Create a Class
# To create a class, use the keyword <<class>>
# Create a class named MyClass, with a property named x:
class MyClass:
    a = 25


# + Create Object
obj = MyClass
print(obj.a)


# + The __init__() Function
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:

class Person:

    # ::NOTE:: The __init__() function is called automatically every time
    # the class is being used to create a new object.
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    # ::NOTE:: The self parameter is a reference to the current instance of the class,
    # and is used to access variables that belong to the class.
    def get_person(self):
        print(self.name, self.family, self.age)


obj = Person("More", "Than", 28)
print(obj.name, obj.family, obj.age)
obj.get_person()


# + The self Parameter
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:


class Person:

    def __init__(a, name):
        a.name = name

    def get_name(a):
        return a.name


obj = Person("More")
print(obj.get_name())


# + Modify Object Properties

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


obj = Person("More Than", 25)
print(obj.age)
obj.age = 30
print(obj.age)
print(obj.name)
del obj.name
# print(obj.name)  # will raise an error

# + Delete Objects
# You can delete objects by using the del keyword:

del obj
print(obj.name)  # will raise an error


# + The pass Statement
class Person:
    pass

# https://www.w3schools.com/python/python_classes.asp
