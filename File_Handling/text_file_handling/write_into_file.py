"""Write into file with python:-


Write to an Existing File:-
To write to an existing file, you must add a parameter to the open() function:

"w" - Write - will overwrite any existing content.
"""
f = open("writeData.txt", "w")
f.write("Happy New Year 2022! Wish you a new year full of success, happiness, and blessings.")
f.close()


f = open("writeData.txt", "r")
print(f.read())


f = open("data_one.txt", "w")
f.writelines(["line1", "\nline2"])
