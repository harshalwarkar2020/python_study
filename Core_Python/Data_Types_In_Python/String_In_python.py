"""String In Python
Strings in python are surrounded by either single quotation marks, or double quotation marks. Even triple quotes can be generally used to represent multiline strings. strings in Python are arrays of bytes.
"""

print("---------------------------------------------------------------------")
d = "HELLO PYTHON"
e = d[0]
f1 = d[10]

print("---------------------------------------------------------------------")
# String index():- finds the first occurrence of the specified value.
my_str = "Hello, welcome to my world."
x = my_str.index("welcome")

print("---------------------------------------------------------------------")
# String Length
d = len(my_str)

print("---------------------------------------------------------------------")
# The split():-
w = "Hello, World!"
print(w.split(","))

print("---------------------------------------------------------------------")
# The replace():-
v = "Hello, World!"
print(v.replace("H", "J"))

print("---------------------------------------------------------------------")
# The strip()
q = " Good Morning "
print(q.lstrip()), print(q.rstrip()), print(q.strip())

print("---------------------------------------------------------------------")
# Iterating over string
k = "Hello, World!"
for i in k:
    print(i)

print("---------------------------------------------------------------------")
"""enumerate():- 
The enumerate function allows us to loop over list elements with their indexes.
"""
my_str = "Hello, welcome to my world."
for char, position in enumerate(my_str, 1):
    print(char, position)

print("---------------------------------------------------------------------")