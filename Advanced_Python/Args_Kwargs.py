"""*args (Non Keyword Arguments)
When we are not sure about the number of arguments that can be passed to a function. Python has *args which allow us to pass the number of non keyword arguments to function.
args allows us to create more flexible functions that can handle a varying number of arguments.
"""


def my_function(*kids):
    for i in kids:
        print(i)


my_function("Yash", "Jay", "Vijay")

"""**kwargs (Keyword Arguments)
allows us to pass the number of keyword arguments to function.
kwargs is a special syntax that allows you to pass a variable-length list of keyword arguments to a function. It stands for "keyword arguments" 
"""


def test_method(**data):
    print("Data type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


test_method(Firstname="Ajay", Lastname="Sharma", Age=22)
