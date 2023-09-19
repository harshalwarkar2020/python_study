"""Default constructor"""


class School:

    def __init__(self):
        self.name = "Ajay"
        self.age = 20

    def student(self):
        print("name is {0} and age is {1}".format(self.name, self.age))


obj = School()
obj.student()


class School:
    def __init__(self):
        print("I am in init method")

    def student(self):
        print("Name of student is Ajay")


sc = School()
sc.student()

print("-----------------------------------------------")
"""Parameterized constructor"""


class School:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student(self):
        print("name is {0} and age is {1}".format(self.name, self.age))


obj = School("Vijay", 18)
obj.student()
