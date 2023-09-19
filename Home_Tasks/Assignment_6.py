"""1. WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
BMI.
Write code that calls this function after taking height and weight as inputs and then prints
underweight, normal, overweight or obese depending on the value of BMI.
Refer this link for the ranges:
https://en.wikipedia.org/wiki/Body_mass_index
"""


def bmi(weight_kg, height_cm):
    height_m = height_cm / 100

    bmi_value = weight_kg / (height_m ** 2)

    return bmi_value


weight = float(input("Enter weight in kilograms (kg): "))
height = float(input("Enter height in centimeters (cm): "))

result = bmi(weight, height)

if result < 18.5:
    print(f"Your BMI is {result:.2f}, which is categorized as 'Underweight'.")
elif 18.5 <= result < 24.9:
    print(f"Your BMI is {result:.2f}, which is categorized as 'Normal'.")
elif 24.9 <= result < 29.9:
    print(f"Your BMI is {result:.2f}, which is categorized as 'Overweight'.")
else:
    print(f"Your BMI is {result:.2f}, which is categorized as 'Obese'.")

print("------------------------------------------------------------------")
"""Take input of the age of 3 people by user and determine oldest and youngest among them."""

age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
age3 = int(input("Enter the age of the third person: "))

# Determine the oldest and youngest
oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

# Print the results
print(f"The oldest person is {oldest} years old.")
print(f"The youngest person is {youngest} years old.")

print("------------------------------------------------------------------")
"""WAP to input a number and check if number is divisible by both 5 and 7."""
# Input a number from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by both 5 and 7
if number % 5 == 0 and number % 7 == 0:
    print(f"{number} is divisible by both 5 and 7.")
else:
    print(f"{number} is not divisible by both 5 and 7.")

print("------------------------------------------------------------------")
""" is_alphabet() that takes a string argument and returns True or False. True if all characters
in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
functions)"""


def is_alphabet(input_string):
    for char in input_string:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            return False
    return True


input_string = input("Enter a string: ")

result = is_alphabet(input_string)
print(f"All characters in the string are alphabets: {result}")

print("------------------------------------------------------------------")
"""WAF: is_leap_year() that takes a year as input and returns True if year is leap year, otherwise False."""


def is_leap_year(year):
    # Check if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))

result = is_leap_year(year)
if result:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

print("------------------------------------------------------------------")
""" WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
as arguments and returns the number of days in the month.
Use the function is_leap_year() to check the special case of 29 days in leap year for month of
FEB. [Use a dictionary to store the mapping of month and days.]"""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month_name, year):
    # Dictionary mapping month abbreviations to the number of days
    month_days = {
        'Jan': 31,
        'Feb': 29 if is_leap_year(year) else 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Oct': 31,
        'Nov': 30,
        'Dec': 31
    }

    month_name = month_name.capitalize()

    if month_name in month_days:
        return month_days[month_name]
    else:
        return "Invalid month abbreviation"


month_name = input("Enter the month abbreviation (e.g., Jan, Feb, Mar): ")
year = int(input("Enter the year (YYYY): "))

result = days_in_month(month_name, year)
if isinstance(result, int):
    print(f"The number of days in {month_name} {year} is {result}.")
else:
    print(result)

print("------------------------------------------------------------------")
"""Update the above program to work with both 3 character month and complete name of month."""


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month_name, year):
    month_days = {
        'Jan': 31, 'January': 31,
        'Feb': 29 if is_leap_year(year) else 28, 'February': 29 if is_leap_year(year) else 28,
        'Mar': 31, 'March': 31,
        'Apr': 30, 'April': 30,
        'May': 31,
        'Jun': 30, 'June': 30,
        'Jul': 31, 'July': 31,
        'Aug': 31, 'August': 31,
        'Sep': 30, 'September': 30,
        'Oct': 31, 'October': 31,
        'Nov': 30, 'November': 30,
        'Dec': 31, 'December': 31
    }

    # Convert the month name to title case
    month_name = month_name.title()

    if month_name in month_days:
        return month_days[month_name]
    else:
        return "Invalid month name/abbreviation"


month_name = input("Enter the month (e.g., Jan, January, Feb, February, etc.): ")
year = int(input("Enter the year (YYYY): "))

result = days_in_month(month_name, year)
if isinstance(result, int):
    print(f"The number of days in {month_name} {year} is {result}.")
else:
    print(result)

print("------------------------------------------------------------------")
""" WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
common words in both the sentences. [Hint: store all the in a set. Read the documentation for set.]"""


def uncommon_words(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    # Create sets of unique words from each sentence
    set1 = set(words1)
    set2 = set(words2)

    # Find the common words by taking the intersection of the sets
    common_words = set1.intersection(set2)

    return common_words


sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

result = uncommon_words(sentence1, sentence2)

if result:
    print("Common words in both sentences:", ', '.join(result))
else:
    print("There are no common words in both sentences.")

print("------------------------------------------------------------------")
