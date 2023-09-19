
# To open a file for reading it is enough to specify the name of the file:
f11 = open("data.txt", "rt")


# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
f22 = open("data.txt")


# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("data.txt", "r")
print(f.read())


# Open a file by specifying location
f1 = open("data.txt", "r")
print(f.read())


# Read Only Parts of the File By default the read() method returns the whole text, but you can also specify how many characters we want to return:
f2 = open("data.txt", "r")
print(f2.read(5))


# Read Line:- We can return one line
f3 = open("data.txt", "r")
print(f3.readline())


# Read Lines:- We can return all lines in one list
f4 = open("data.txt", "r")
print(f4.readlines())


# Iterating lines with for loop.
f5 = open("data.txt", "r")
for i in f5.readlines():
    print(i)







