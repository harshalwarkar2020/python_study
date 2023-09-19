""" Method Overloading:- This concept provides the ability for several methods having the same name within a class but differ in type or differ in number of arguments."""

# Class having two methods with same name

class School:

    def teacher_info(self):
        print("We have total 22 teachers in our school")

    def teacher_info(self):
        print("We have total 50 teachers in our school")


sc = School()
sc.teacher_info()

print("-------------------------------------------------------------------")
# Class having two methods with same name and different types of arguments

class Car:

    def car_info(self, color, name):
        print("Car Name:- {}".format(name))
        print("Car Color:- ".format(color))

    def car_info(self, number_of_wheels, car_number):
        print("Total number of wheels:- {}".format(number_of_wheels))
        print("Car Number:- {}".format(car_number))


cr = Car()
cr.car_info("Red", "BMW")

print("-------------------------------------------------------------------")
# Class having two methods with same name and different number of arguments

class AdditionOperation:

    def do_addition(self, a, b):
        total = a + b
        print(total)

    def do_addition(self, a, b, c):
        total = a + b + c
        print(total)


ad = AdditionOperation()
ad.do_addition(20, 30, 50)

print("-------------------------------------------------------------------")
"""Method Overriding:- If there is a method in super class and method having the same name and same number of arguments in child class then the child class method is said to be overriding the parent class method."""


class Teacher:
    name = "Ajay"
    age = 25

    def display(self):
        print("Parent class method")


class Student(Teacher):

    def display(self):
        print("child class method with parent class attributes:- {0} and {1}".format(self.name, self.age))


obj1 = Teacher()
obj1.display()

obj2 = Student()
obj2.display()
print("-------------------------------------------------------------------")

