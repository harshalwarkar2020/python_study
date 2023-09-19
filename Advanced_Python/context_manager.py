"""Whenever we have situation when we need to do open and close like in case of file
we open the file then we perform certain actions then we will close it. similarly for database
we first connect to database then we perform some queries and closing it. In these cases
we are writing repeated code for closing and opening so here context manager useful in such a situations"""

f = open("sample.txt", 'w')
f.write("Good Morning")
f.close()

print("------------------------------------------------------------------")
"""Here open is a context manager"""
with open("sample1.txt", 'w') as f:
    f.write("Learn Python")

print("------------------------------------------------------------------")
from contextlib import contextmanager


@contextmanager
def my_open(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with my_open("sample2.txt", 'w') as f:
    f.write("Hello this is my own context manager")

print("------------------------------------------------------------------")


class MyClassOpen(object):
    def __init__(self, filename, mode):
        self.file_name = filename
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.file.close()


with MyClassOpen("sample3.txt", 'w') as f:
    f.write("This is my own class context manager")
