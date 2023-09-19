"""If Statement in Python
An else statement can be combined with an if statement. An else statement contains the block of
code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.
The else statement is an optional statement and there could be at most only one else statement following if.
If Statement:-"""

a = 100
b = 50

if b > a:
    print("b is greater than a")

# Else:-
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# Nested If:-
num = 100
if num > 10:
    print("given number is greater than 10")
    if num > 20:
        print("given number is greater than 20")
    else:
        print("but given number is less than 20")


"""Elif:-  The elif keyword is Python's way of saying "if the previous conditions were not true, then
 try this condition”."""
num1 = 100
num2 = 50

if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is less than num2")
elif num1 == num2:
    print("num1 and num2 are equal")
