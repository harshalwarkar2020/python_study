"""Dictionary In Python
Dictionaries are used to store data values in key:value pairs.Dictionaries are written with curly brackets.
Dictionaries are ordered, meaning that the items have a defined order, and that order will not change.
Dictionaries are changeable, meaning that we can modify the items after the dictionary has been created.
Dictionaries do not allow duplicates, meaning it cannot have two items with the same key.
"""

print("---------------------------------------------------------------------")
# Nested Dictionaries
my_fav_cars = {
    "car1": {"name": "swift", "year": [2004, 2010]},
    "car2": {"name": "Altroz", "year": 2007},
    "car3": {"name": "KUV", "year": 2011}}
print(my_fav_cars["car1"]["year"][1])

print("---------------------------------------------------------------------")
# Dictionary Length:-
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(len(my_dict))

print("---------------------------------------------------------------------")
# Accessing Items:-
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
access_item = my_dict["model"]

print("---------------------------------------------------------------------")
# get() Method:-
a = my_dict.get("model")

print("---------------------------------------------------------------------")
# values():-values of the dictionary, as a list.
p = my_dict.values()

print("---------------------------------------------------------------------")
# Change Values:-
my_dict1 = {"brand": "Ford", "model": "Mustang", "year": 2018}
my_dict1["year"] = 2018

print("---------------------------------------------------------------------")
# Adding Items:-
my_dict["brand"] = "Maruti"

print("---------------------------------------------------------------------")
# update():- The update() method inserts the specified items to the dictionary.
my_dict.update({"color": "White"})

print("---------------------------------------------------------------------")
# Removing Items:-
my_dict.pop("model")

print("---------------------------------------------------------------------")
# Loop Through a Dictionary - keys
for i in my_dict:
    print(i)

print("---------------------------------------------------------------------")
# Loop Through a Dictionary - values
for i in my_dict:
    print(my_dict[i])

print("---------------------------------------------------------------------")
# items():- Returns a list containing a tuple for each key value pair
for x, y in my_dict.items():
    print(x, y)

print("---------------------------------------------------------------------")
# enumerate()
for sr_no, key in enumerate(my_dict):
    print(sr_no, my_dict[key])

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
