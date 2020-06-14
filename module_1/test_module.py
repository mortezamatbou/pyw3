a_var = ['a', 'b', 'c']


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
