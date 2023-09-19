"""Sets In Python
Sets are used to store multiple items in a single variable.
Sets are useful in mathematical operations like union, intersection, difference, symmetric difference.
Sets are unordered, meaning that the items in a set do not have a defined order. Set items can appear in a different order every time we use them, and cannot be referred to by index or key.
Set items are unchangeable, meaning that we cannot modify its elements after the set has been created.
Sets do not allow duplicates.
"""

# Create a set
set1 = {"apple", "banana", "cherry"}
print(set1)

# Duplicate values will be ignored:
set2 = {"apple", "banana", "cherry", "apple"}
print(set2)
