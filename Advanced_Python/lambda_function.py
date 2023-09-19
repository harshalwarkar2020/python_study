"""Lambda Function in Python
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Lambda functions have a compact syntax that allows you to define small, one-line functions without explicitly naming them. This can make the code more readable and reduce the overall number of lines.
Lambda functions are easy to define and use. They eliminate the need for writing a complete function definition using the def keyword, making the code more straightforward and less cluttered.
"""
# declare a lambda function
greet = lambda: print('Hello World')

# call the lambda
greet()


# Python lambda Function with an Argument
greet_user = lambda name: print('City Name,', name)
greet_user('Pune')


# The expression is executed and the result is returned:
fun_one = lambda a: a + 10
print(fun_one(5))


# Multiply argument a with argument b and return the result:
fun_two = lambda a, b: a * b
print(fun_two(5, 6))


# Summarise argument a, b, and c and return the result:
fun_three = lambda a, b, c: a + b + c
print(fun_three(5, 6, 2))
