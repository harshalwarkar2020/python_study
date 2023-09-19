"""For Loop In Python
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
Exit loop when x is "cherry", break comes after the print"""

fruits = ["apple", "banana", "cherry", "grapes"]
for x in fruits:
    print(x)
    if x == "cherry":
        break


# Exit the loop when x is "banana", break comes before print:
for x in fruits:
    if x == "banana":
        break
    print(x)


"""With the continue statement we can stop the current iteration of the loop, and continue with the next:
Consider the situation when you need to write a program which prints the number from 1 to 10 and not 6. It is specified that you have to do this using a loop and only one loop is allowed to use. Here comes the usage of the continue statement. What we can do here is we can run a loop from 1 to 10 and every time we have to compare the value of the iterator with 6. If it is equal to 6 we will use the continue statement to continue to the next iteration without printing anything otherwise we will print the value.
"""


for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")



