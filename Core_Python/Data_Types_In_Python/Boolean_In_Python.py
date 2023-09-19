"""Booleans represent one of two values: True or False.
In programming, we often need to know if an expression is True or False.
We can evaluate any expression in Python, and get one of two answers, True or False.
When we compare two values, the expression is evaluated and Python returns the Boolean.
"""

a = True
print(type(a))

b = False
print(type(b))

print("--------------------------------------------------------------")
x = 5
y = 10
print(bool(x == y))

print("--------------------------------------------------------------")
a = "Python"
b = "Java"
print(bool(a == b))

print("--------------------------------------------------------------")
p = ["a", "b", "c", "d"]
q = ["a", "b", "c", "d"]

print(p == q)

print("--------------------------------------------------------------")
p = 10
q = 20
print(p != q)
print(p > q)
print(p < q)

print("--------------------------------------------------------------")
print(int(True))
print(int(False))
print("--------------------------------------------------------------")

