# -> JSON (Java Script Object Notation)
'''syntax for storing and exchanging data'''

# -> the purpose of the load() and loads() methods in Python?
'''The load() method is used to load a JSON file, while the loads() method is used to load a JSON string.'''

import json

data = '{"name":"Sandeep","age":29,"designation":"Python backend developer"}'   # json data in string format
print(f"json data: {data}")

parsed_data = json.loads(data)
print(f"parsed data converted to dict: {parsed_data}")
print(parsed_data['name'])      # accessing value of a single variable from parsed data



# -> function of the dump() and dumps() methods in Python?
'''
    - dump() method is used to serialize data from a Python object into a JSON formatted string 

    - dumps() method is used to serialize data from a Python object into a JSON formatted string that is returned as a Python string.
'''

# how to check whether following json is valid or invalid. 
'''
Python provides The json.tool module to validate JSON objects from the command line. Run the following command.

Command: echo "JSON DATA" | python -m json.tool'''

# OR

import json

def validateJSON(jsonDATA):
    try:
        json.loads(jsonDATA)
    except ValueError as err:
        return False
    return True

Invalid_json_data = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}"""

isvalid = validateJSON(Invalid_json_data)
print("given json data is:", isvalid)


