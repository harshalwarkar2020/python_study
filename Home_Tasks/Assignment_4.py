"""Write a for loop to print numbers from 1 to 10. All numbers should be in separate lines."""

for i in range(1, 11):
    print(i)

print("--------------------------------------------------")
"""Write a for loop to print numbers from 10 to 1. All numbers should be in separate lines. """

for i in range(10, 0, -1):
    print(i)

print("--------------------------------------------------")
"""Print Elements at Odd indexes from a list (Using for loop)"""

my_list = [10, 11, 20, 21, 30, 31, 40, 41]
for i in range(1, len(my_list)):
    if my_list[i] % 2 == 0:
        pass
    else:
        print(my_list[i])

print("--------------------------------------------------")
"""Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use a for loop."""

import random

rand_num_list = []

for i in range(5):
    random_number = random.randint(1, 100)
    rand_num_list.append(random_number)

print(rand_num_list)

total = 0
avg = 0
for j in range(len(rand_num_list)):
    total = total + rand_num_list[j]

print("Total of all elements from list is:- {}".format(total))
avg = total / len(rand_num_list)
print("Average of all elements from list is:- {}".format(avg))

print("--------------------------------------------------")
"""WAP to input a string and print individual characters in the string using a for loop.
"""

my_string = "Happy New Year"

for i in my_string:
    print(i)

print("--------------------------------------------------")
"""WAP to input a string and print the ASCII value of each character in the string.
"""

input_string = "Happy"

for char in input_string:
    ascii_value = ord(char)
    print(f"Character '{char}' has ASCII value: {ascii_value}")

print("--------------------------------------------------")
"""WAP to input a string and store ASCII values of all characters in a tuple."""

input_string = "Happy"
my_tuple = ()
for char in input_string:
    ascii_value = ord(char)
    my_tuple = my_tuple + (ascii_value,)
print("ASCII values of characters in given string:", my_tuple)

print("--------------------------------------------------")
"""Write a function that takes a list of numbers from user as argument and returns the sum of only"""


def sum_of_numbers(numbers_list):
    total = 0
    for i in numbers_list:
        total = total + i

    return total


user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(x) for x in user_input.split()]

print(numbers_list)
print(f"The sum of numbers in the list is: {sum_of_numbers(numbers_list)}")

print("--------------------------------------------------")
"""WAP to input a list of numbers and store in a tuple. Now input another number and print the index of this number in the tuple."""

user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(x) for x in user_input.split()]

numbers_tuple = tuple(numbers_list)

search_number = int(input("Enter a number to search for in the tuple: "))

if search_number in numbers_tuple:
    index = numbers_tuple.index(search_number)
    print(f"The number {search_number} is found at index {index} in the tuple.")
else:
    print(f"The number {search_number} is not in the tuple.")

print("--------------------------------------------------")
"""WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
"""
number_list = []

for i in range(10):
    try:
        number = float(input("Enter a number: "))

        number_list.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("List of numbers entered:", number_list)

print("--------------------------------------------------")
"""WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
"""
total = 0

for i in range(10):
    try:
        number = float(input("Enter a number: "))

        total = total + number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Total of Entered number:-", total)

print("--------------------------------------------------")
"""WAP to input a number and print all numbers from 1 till that number"""

input_number = int(input("Enter Number:- "))

for i in range(1, input_number + 1):
    print(i)

print("--------------------------------------------------")
""" WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number whose factorial is to be found. """


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"{num}! = {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

print("--------------------------------------------------")
