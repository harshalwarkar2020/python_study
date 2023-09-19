"""Super class having constructor and sub class doesn’t have constructor"""

class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working")


class B(A):
    def feature_2(self):
        print("feature 2 is working")


obj = B()


print("-----------------------------------------------")
""" Both Super class and subclass have constructor."""
class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working")

class B(A):
    def __init__(self):
        print("This is the constructor of class B")

    def feature_2(self):
        print("feature 2 is working")

obj = B()


print("-----------------------------------------------")
"""Both Super class and subclass have constructor and with the object of
sub class we are able call the init method of both classes."""


class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working")


class B(A):
    def __init__(self):
        super().__init__()
        print("This is the constructor of class B")

    def feature_2(self):
        print("feature 2 is working")


obj = B()

print("-----------------------------------------------")
"""One class inherits two other classes and calling init of super classes then it will
prefer left first and then right.
"""

class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working")


class B:
    def __init__(self):
        print("This is the constructor of class B")

    def feature_2(self):
        print("feature 2 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("This is the constructor of C")


obj = C()


print("-----------------------------------------------")
""""With the super(), the child class is able to call the constructor of the multiple parent classes."""
class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working")


class B:
    def __init__(self):
        self.name = "Ajay"
        print("This is the constructor of class B")

    def feature_2(self):
        print("feature 2 is working")


class C(A, B):
    def __init__(self):
        super().__init__()
        super(A, self).__init__()
        print("This is the constructor of class C")


print("-----------------------------------------------")
"""Methods with MRO[Method Resolution Order]"""
class A:
    def __init__(self):
        print("This is the constructor of class A")

    def feature_1(self):
        print("feature 1 is working for class A")


class B:
    def __init__(self):
        print("This is the constructor of class B")

    def feature_1(self):
        print("feature 1 is working for class B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("This is the constructor of class C")


obj = C()
obj.feature_1()


print("-----------------------------------------------")
"""With the super(), the child class is able to call the method of the parent class."""
class A:
    def feature_1(self):
        print("feature 1 is working for Class A")


class B(A):
    def feat(self):
        super().feature_1()


obj = B()
obj.feat()

