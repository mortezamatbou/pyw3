# -- Python Iterators --

# An iterator is an object that contains a countable number of values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

a_tuple = ("apple", "banana", "cherry")
myitr = iter(a_tuple)

print(next(myitr), end=", ")
print(next(myitr), end=", ")
print(next(myitr))
# print(next(myitr), end="")  # will raise an error

# Even strings are iterable objects, and can return an iterator:

str_message = "Hello"

for ch in str_message:
    print(ch, end=",")

print()

myiter = iter(str_message)

print(next(myiter), end=',')
print(next(myiter), end=',')
print(next(myiter), end=',')
print(next(myiter), end=',')
print(next(myiter), end=',')
print()


# + Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class A:

    def __init__(self, name, age):
        pass

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        x = self.i
        x += 1
        return x


obj = A("More", 25)
myiter = iter(obj)

print(next(myiter))


class Student:

    def __init__(self):
        self.students = list()

    def add_student(self, name, age):
        self.students.append({"name": name, "age": age})

    def get_students(self):
        return self.students

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.students):
            x = self.students[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration


st = Student()
st.add_student("More", 28)
st.add_student("Less", 24)
st.add_student("Bess", 20)

print(st.get_students())

myiter = iter(st)
index_1 = next(myiter)
index_2 = next(myiter)
index_3 = next(myiter)
print(index_1['name'], index_1['age'])
print(index_2)
print(index_3['age'] if index_3 else "")

obj = Student()
obj.add_student("Morteza", 28)
obj.add_student("Reza", 23)
obj.add_student("Sahar", 22)
obj.add_student("Sajjad", 25)

my_students = iter(obj)

for student in obj:
    print(student['name'], student['age'])
