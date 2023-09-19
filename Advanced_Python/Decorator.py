"""Python Decorator

In Python, a decorator is a design pattern which allows us to modify the functionality of a function by wrapping it in another function.
Basically, a decorator takes in a function, adds some functionality and returns it.

The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.
"""


def make_pretty(func):
    def inner():
        print("I got decorated")

        func()

    return inner


def ordinary():
    print("I am ordinary")


decorated_func = make_pretty(ordinary)

decorated_func()


# @ Symbol With Decorator:-
# Here, the ordinary() function is decorated with the make_pretty() decorator using the @make_pretty  syntax.


def make_pretty(func):
    def inner():
        print("I got decorated")

        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()
