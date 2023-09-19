"""Define a variable for an object"""


class Computer:
    def __init__(self):
        self.name = "Ajay"
        self.age = 18


c1 = Computer()
c2 = Computer()

print(c1.name)
print(c2.name)

print("-----------------------------------------------")
"""We are also able to assign our own value. We are able to change the values from one object to different objects."""


class Computer:
    def __init__(self):
        self.name = "Ajay"
        self.age = 18


c1 = Computer()
c2 = Computer()

c1.name = "Vijay"

print(c1.name)
print(c2.name)

print("-----------------------------------------------")
"""Concept of Self"""


class Computer:
    def __init__(self):
        self.name = "Ajay"
        self.age = 18

    def update(self):
        self.age = 25
        print("Age change by update method:- {}".format(self.age))


c1 = Computer()
c2 = Computer()

c1.name = "Vijay"
print(c1.name)
print(c2.name)
c1.update()

print("-----------------------------------------------")
"""Comparing Two Objects"""


class Computer:
    def __init__(self):
        self.name = "Ajay"
        self.age = 18

    def compare(self, other):
        print("Age of c1:- ", self.age)
        print("Age of c2:- ", other.age)
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.age = 25

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")

print("-----------------------------------------------")

print("-----------------------------------------------")

print("-----------------------------------------------")

print("-----------------------------------------------")

