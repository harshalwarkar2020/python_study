# Predict Output
S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2))

print("---------------------------------------------------------")

# WAP to input a string and print its length.
test_string = input("Enter Test String:- ")
print("Length Of Given String:- {}".format(len(test_string)))
print("---------------------------------------------------------")

#  WAP to input 2 numbers and print their sum and difference.
num1 = int(input("Enter First Number:- "))
num2 = int(input("Enter Second Number:- "))
print("Sum of given numbers:- {}".format(num1 + num2))
print("Difference of given numbers:- {}".format(num1 - num2))
print("---------------------------------------------------------")

# Predict Output
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print("Addition of given Strings:- {}".format(s3))
print("---------------------------------------------------------")

# Predict Output,
s1 = 'ab' *4
print(s1)

print("---------------------------------------------------------")
"""WAP to input a string s and a number n. Print the string n times on the screen, each should appear in a separate line (do not use any kind of loops, use the multiplication operator)."""

test_string = input("Enter Test String:- ")
count = int(input("Enter Number:- "))
print(*count*(test_string,), sep='\n')

print("---------------------------------------------------------")
#  Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))

print("---------------------------------------------------------")
"""Find the name of the function to find the square root. (see all the options
   available in dir() of builtins)"""

import math
num = float(input('Enter a number:- '))
print("The square root of {} is:- {}".format(num, math.sqrt(num)))

num = float(input('Enter a number:- '))
num_sqrt = num ** 0.5
print("The square root of {} is:- {}".format(num, num_sqrt))


# WAP to input a number and print its square root ().
num = float(input('Enter a number:- '))
num_sqrt = num ** 0.5
print("The square root of {} is:- {}".format(num, num_sqrt))


print("---------------------------------------------------------")
"""WAP to input 4 numbers from user and print their average"""
num1 = float(input('Enter first number:- '))
num2 = float(input('Enter second number:- '))
num3 = float(input('Enter third number:- '))
num4 = float(input('Enter fourth number:- '))
average = (num1 + num2 + num3 + num4) / 4
print("Average of given numbers:- {}".format(average))
print("---------------------------------------------------------")

"""Use the help function to check what the abs function in python does."""
help(abs)


print("---------------------------------------------------------")
"""What is the output of this code when run from a python interpreter."""
print(__name__)
print("---------------------------------------------------------")









