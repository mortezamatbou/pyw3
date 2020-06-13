# -- Python Inheritance --

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# <<Parent class>> is the class being inherited from, also called base class.
# <<Child class>> is the class that inherits from another class, also called derived class.

# + Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        # return self.name, self.age
        return self.name + " " + str(self.age)


obj = Person("More Than", 28)
print(obj.print_name())


# + Create a Child Class

class Student(Person):
    pass


obj = Student("More Than", 28)
obj.print_name()


# + Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# ::NOTE:: The __init__() function is called automatically every time the class is being used to create a new object.

class Student(Person):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


obj = Student("More Than", 25)
print(obj.print_name())


class Student(Person):

    def __init__(self, name, age):
        Person.__init__(self, name, age)

    def print_student(self):
        return self.print_name()


a = Student("More Than", 40)
print(a.print_student())


# + Use the super() Function
# Python also has a super() function that will make the child class
# inherit all the methods and properties from its parent:

class A:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_str(self):
        return self.title


class B(A):

    def __init__(self, title):
        super().__init__(title)
        # Add a property called year to the B class:
        self.year = 2020

    def get_str(self):
        return self.title + " " + str(self.year)


obj = B("Title of post 112524")
# print(obj.get_title())

# + Add Properties
# Add a property called year to the B class:
# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.
print(obj.get_str())
