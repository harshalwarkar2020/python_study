"""The print() function
The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before being written to the screen.
"""
print("Welcome to Python and automation training")
print("Hello", "how are you?")


print("------------------------------------------------------------------------------------------------------")
"""Print two messages, and specify the separator:"""
print("Hello", "how are you?", "Good Morning", sep="---")


print("------------------------------------------------------------------------------------------------------")
"""Python end parameter in print()
By default python’s print() function ends with a newline.
Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character. We can end a print statement with any character/string using this parameter.
"""
print("Welcome to Python coaching session", end='')
print("We are here to learn Python in detail")
print("Welcome to Python coaching session", end='@')
print(" We are here to learn Python in detail")

my_list = ["red", "green", "blue"]
for i in my_list:
    print(i, end='')


print("------------------------------------------------------------------------------------------------------")
"""Python input() Function
In Python, we use the input() function to take input from the user. Whatever you enter as input, the input function converts it into a string. If we enter an integer value, the input() function converts it into a string.
"""
name = input("Enter your name:- ")
print("Hello", name)

# Taking input from the user as integer.
num = int(input("Enter a number:"))
add = num + 1
print(add)


print("------------------------------------------------------------------------------------------------------")
"""Python String format() Method
The format() method formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}.
The format() method returns the formatted string.
The Placeholders
The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
"""

car_name = "swift"
car_color = "Red"
car_price = 600000

# even empty placeholders {}
print("I have a {} car which is of {} color and its current price is {}".format(car_name, car_color, car_price))

# numbered indexes {0}
print("I have a {1} car which is of {0} color and its current price is {2}".format(car_name, car_color, car_price))

# named indexes {price}
print("I have a {car_name} car which is of {car_color} color and its current price is {car_price}".format(car_name ="swift", car_color ="Red", car_price = 600000))


"""f-strings in Python
To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format().
"""

car_name = "swift"
car_color = "Red"
car_price = 600000
print(f"I have a {car_name} car which is of {car_color} color and its current price is {car_price}")

car = "swift"
colour = "Red"
my_dict = {f"car_detail": "I have a " + car + " which is of " + colour}
print(my_dict)
print("------------------------------------------------------------------------------------------------------")
