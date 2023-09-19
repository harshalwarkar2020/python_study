"""Switch Statement in Python:- From version 3.10 upwards, Python has implemented a switch case feature called “structural pattern matching”. You can implement this feature with the match and case keywords.
To write switch statements with the structural pattern matching feature, we can use the syntax below:


lang = input("Which programming language do you want to learn?:-  ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Automation Engineer or Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
"""