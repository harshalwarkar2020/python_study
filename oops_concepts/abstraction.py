"""abstraction means hiding the complexity and only showing the essential features of the object. So in a way, abstraction means hiding the real implementation and we as a user only know how to use it.
When a method has only a declaration and not definition then that method is an abstract method. A class which will have an abstract method is called an abstract class.
Abstraction in python is achieved by using abstract classes and interfaces.
abstract class contains one or more abstract methods.
abstract methods don't have implementation.
abstract methods need to be implemented in subclass.
We can not create the object of abstract class.
abstract class need to have at least one abstract method.
"""

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        n1 = 20
        n2 = 30
        total = n1 + n2
        print(total)

    def display(self):
        print("Python")


obj = Laptop()
obj.process()
obj.display()
