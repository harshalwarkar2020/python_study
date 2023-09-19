# Arithmetic Operators
addition = 10 + 20
print(addition)


# Subtraction:-
subtraction = 400 - 100
print(subtraction)


# Multiplication:-
multiplication = 40 * 20
print(multiplication)


# Division:-
division = 100 / 20
print(division)


# Modulus:- remainder of the division of left operand by the right
Modulus = 7 % 2
print(Modulus)


# Floor division:- division that results in the whole number adjusted to the left in the number line. Basically, it removes the fractional part from the result of a normal division.
floor_division = 7 // 2
print("------------------------------------------------------------------------------------")


# Logical Operators
a = 150
b = 20

# AND Operator:- Returns True if both statements are true
if a < 100 and b < 50:
    pass

# OR Operator:- Returns True if one of statements is true.
if a < 100 or b > 50:
     pass

# not Operator:- return False if the result is true.
if not(a < 100 and b > 50):
    pass
print("------------------------------------------------------------------------------------")


# is Operator:- Returns True if both variables are the same.
if a is b:
    pass

# is not Operator:- True if both variables are not  same
if a is not b:
    pass
print("------------------------------------------------------------------------------------")

# Comparison Operators
# Equal Operator:-
if a == b:
    pass

# Not Equal Operator:-
if a != b:
    pass

# Greater than Operator:-
if a > b:
    pass

# Less than Operator:-
if a < b:
    pass

# Greater than or equal Operator:-
if a >= b:
    pass

# Less than or equal Operator:-
if a <= b:
    pass
print("------------------------------------------------------------------------------------")


# Membership Operators
a = 20
b = [20, 100, 40, 10, 50]

# in Operator:- True if value present in sequence.
if a in b:
    pass

# not in Operator:- True if value not present in sequence.
if a not in b:
    pass
print("------------------------------------------------------------------------------------")


"""Bitwise operations in Python:- are operations that work on the individual bits of integers. 
Python supports several bitwise operators that allow you to manipulate the bits of integers. 
These operators include:"""

# Bitwise AND:-
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a & b
print(result)  # Output: 1 (binary: 0001)

# Bitwise OR:-
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a | b
print(result)  # Output: 7 (binary: 0111)

# Bitwise XOR:-
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a ^ b
print(result)  # Output: 6 (binary: 0110)

# Left Shift:- These operators shift the bits of an integer left by a specified number of positions.
a = 5  # binary: 0101
result = a << 2
print(result)  # Output: 20 (binary: 10100)

# Right Shift:- These operators shift the bits of an integer right by a specified number of positions.
a = 20  # binary: 10100
result = a >> 2
print(result)  # Output: 5 (binary: 0101)

# Bitwise NOT:-
a = 5  # binary: 0101
result = ~a
print(result)  # Output: -6 (binary: 1010)
print("------------------------------------------------------------------------------------")






