# Write lambdas to Square a number x2
square = lambda x: x ** 2
print(square(3))

# Inverse a number 1/x
inverse = lambda x: 1 / x
print(inverse(3))

# Negate a number
negate = lambda x: -x
result = negate(5)
print(result)

print("-------------------------------------------------------------")
"""Use reduce function and an appropriate lambda to find the maximum number in a list. """
from functools import reduce
lst = [22, 36, 47, 2, 13]
print("maximum number in a list:- {}".format(reduce(lambda x, y: x if (x > y) else y, lst)))

print("-------------------------------------------------------------")
"""Write a function map_multiple that takes a list of functions/lambdas as first argument and a sequence type 
as second argument. The function picks first lambda from list, applies it to first element, then applies the second function to the result of first one and …. Similarly it does for each element and generates a mapping of input to output . def map_multiple(functs, sequence):  # write definition here 
Ex: let list of lambdas be from question 1 and the list on numbers be [1,2,4] 
      So first function gives [1, 4, 16] 
      Second gives [1, 0.25, 0.0625] 
      Third gives [-1, -0.25, -0.0625]. Which is the final result. """

square = lambda x: x ** 2
inverse = lambda x: 1 / x
negate = lambda x: -x


def map_multiple(functs, lst1):
    lst2 = []

    for num in lst1:
        res = num
        for i in functs:
            res = i(res)
        lst2.append(res)
    print(lst2)

map_multiple([square, inverse, negate], [1, 2, 4])

print("-------------------------------------------------------------")
"""Use filter function to filter a list of numbers and strings such that the result contains only numbers. 
(Hint : Use isinstance method)  """

my_list = [1, 'apple', 2.5, 'banana', 3, 'cherry']
numbers_only = [x for x in my_list if isinstance(x, (int, float))]
print(numbers_only)

print("-------------------------------------------------------------")






