"""List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list.
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_list = []

for x in fruits:
    if "a" in x:
        my_list.append(x)

print(my_list)


# With list comprehension we can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_compr_list = [x for x in fruits if "a" in x]
print(my_compr_list)


# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_compr_list1 = [x for x in fruits if x != "apple"]
print(my_compr_list1)


# With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
my_compr_list2 = [x for x in fruits]
print(my_compr_list2)



