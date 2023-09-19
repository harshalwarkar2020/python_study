"""Encapsulation Python
Encapsulation is one of the key concepts of object-oriented languages like Python, Java, etc. Encapsulation is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.
"""

""""Public access modifier:-
- All the variables and methods  in python are by default public.
- If any class variable or method is declared without followed by any underscore it means
  that variable is public by default.
"""


class Student:
    def __init__(self, age):
        self.age = age


class Subject(Student):
    pass


obj = Student(21)
print("Calling Attribute with Parent class Object", obj.age)

obj1 = Subject(22)
print("Calling Attribute with Parent class Object", obj1.age)

print("--------------------------------------------------------------------")
"""Protected Access Modifier:-
- Protected members of a class are restricted to be used only by class members of the same class.
- It can be accessed or inherited by its derived class (child class).
- We can modify the values of protected variables of a class.
- If any class variable or method is declared followed by a single underscore it means that the variable is
  a protected variable.	
"""


class Student:
    def __init__(self):
        self._name = "Ajay"

    def _notes(self):
        print("This Is Protected Method")


class Subject(Student):
    pass

    def greet(self):
        self._notes()


obj = Student()
obj._notes()

obj1 = Subject()
obj1._notes()
obj1.greet()
print(obj1._name)

print("--------------------------------------------------------------------")
""""Private Access Modifier:- 
1. Private members of a class (variables or methods) are those members which are only
   accessible inside the class. We cannot use private members outside of class.
2. It is also not possible to inherit the private members of any class (parent class) to derived
    class (child class). 
"""


# 1. Class Methods are able to access private methods and variables.
class Student:
    def __init__(self, name):
        self.__name = name

    def __notes(self):
        print("This Is The Private Method")

    def feature_1(self):
        print("feature_1 is able to call private methods and attributes")
        self.__notes()
        print(self.__name)


obj = Student("Ajay")
obj.feature_1()


# 2. Class object is unable to call their own Private methods and variables.

class Student:
    def __init__(self, name):
        self.__name = name

    def __notes(self):
        print("This Is The Private Method")


obj = Student("Ajay")
print(obj.__name)
print(obj1._Student__name)
obj1._Student__notes()
obj.__notes()

print("--------------------------------------------------------------------")
