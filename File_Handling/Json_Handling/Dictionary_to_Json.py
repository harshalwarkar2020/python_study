"""Dictionary to JSON:-
 We can convert a dictionary to JSON string using json.dumps() method.

Writing JSON to a file:-
To write JSON to a file in Python, we can use the json.dump() method.
"""

import json
data = {'name': 'ajay', 'age': 12, 'children': 2, "city": "Pune"}

with open('person_data.json', 'w') as json_file:
    json.dump(data, json_file)
