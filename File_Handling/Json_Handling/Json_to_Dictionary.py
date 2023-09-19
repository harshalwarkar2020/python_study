"""JSON to Dictionary:-
We can parse a JSON string using the json.loads() method. This method returns a dictionary. json.load() method is used to read a file containing a JSON object.
"""

import json


def get_all_test_data():
    with open("test_data.json") as json_data:
        extracted_data = json.load(json_data)

    print(extracted_data)
    print(type(extracted_data))
    print(extracted_data['staging']['password'])
    return extracted_data


get_all_test_data()
