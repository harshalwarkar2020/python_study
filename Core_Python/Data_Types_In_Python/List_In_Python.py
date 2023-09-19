"""List In Python
List can be defined as a collection of items of different types. The items in the list are separated with the comma "," and enclosed with the square brackets []. Lists are used to store multiple items in a single variable.It allows us to work with multiple elements at once.
Lists are ordered, meaning that the items have a defined order, and that order will not change.
Lists are changeable types; it means we can modify its element after it is created.
Lists are allowed to have duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc..
"""
lst = [200, 450, 800, 350, 999, 5000]


print("---------------------------------------------------------------------")
# Nested list:-
nested_list = ["mouse", [8, 4, 6], ['a', ["Ajay", 800]]]
print(nested_list[2][1][1])

print("---------------------------------------------------------------------")
# List of Dictionaries in Python:-
myList = [{'foo': 12, 'bar': 14}, {'moo': 52, 'car': 641}, {'doo': 6, 'tar': 84}]
print(myList[1]["car"])

print("---------------------------------------------------------------------")
# List Index:-
myList = ["apple", "banana", "cherry"]
print(myList .index('banana'))

print("---------------------------------------------------------------------")
# len():- It calculates the length of the list.
print(len(myList))

print("---------------------------------------------------------------------")
# Change Item Value:-
myList = ["apple", "banana", "cherry"]
myList[1] = "blackcurrant"

print("---------------------------------------------------------------------")
# Plus operator:-
print(myList + [21, 22, 23])

print("---------------------------------------------------------------------")
# Adding items in List:-
myList.append(100)

print("---------------------------------------------------------------------")
# extend() method:-
myList .extend([30, 40, 50])

print("---------------------------------------------------------------------")
# Insert:-
myList .insert(2, 100)

print("---------------------------------------------------------------------")
# Iterating Through a List:-
for fruit in ['apple', 'banana', 'mango']:
    print("I like", fruit)

print("---------------------------------------------------------------------")
# enumerate()
words = ["cup", "star", "falcon", "cloud", "wood", "door"]
for idx, word in enumerate(words, 1):
    print(idx, word)

print("---------------------------------------------------------------------")
# Sort():-
# Ascending
myList.sort()
# Descending
myList.sort(reverse=True)

print("---------------------------------------------------------------------")
# Remove elements
myList.pop(2)
myList.remove("banana")
print("---------------------------------------------------------------------")



