# <<<<<<<<<<<<<< JSON >>>>>>>>>>>>>>>

import json
json_obj = '{"name":"Sandeep","age":29,"designation":"software engineer"}'

# print(data['name'])   # we cannot access the keys or values from the json directly

# json loads >> converts json into dictionary
print("*****************json loads*********************")

parsed = json.loads(json_obj)  
print(type(parsed))    
print(parsed)
print(parsed['designation'])

# json dumps >> converts dictionary into json
print("*****************json dumps*********************")

python_obj = {
  "car": "lancer",
  "company":"mitsubishi",
  "est": 1899 
}
jsn = json.dumps(python_obj)
print(type(jsn))
print(jsn)

print("************converting python objects into json strings**************")

python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

print(json.dumps(python_dict))
print(json.dumps(python_list))
print(json.dumps(python_str))
print(json.dumps(python_float))
print(json.dumps(python_T))
print(json.dumps(python_F))
print(json.dumps(python_N))

print("************converting python dict into json, obj membs & indent 4**************")

p_str = {'4': 5, '6': 7, '1': 3, '2': 4}

j_str = json.dumps(p_str,sort_keys=True,indent=4)
print(j_str)

print("************converting json to python **************")

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'

print(json.loads(jobj_dict))
print(json.loads(jobj_list))
print(json.loads(jobj_string))
print(json.loads(jobj_int))
print(json.loads(jobj_float))

print("************create new json file from existing json file **************")
'''
with open('states.json') as f:
    state_data = json.load(f)

with open('new_states.json','w') as f:
    json.dump(state_data,f,indent=2)
    print("stored in new file")
'''

print("************ Check whether an instance is complex or not **************")

def encode_complex(object):
    # checking using an instance
    if isinstance(object,complex):
        return object.real, object.imag
    # raise error if not complex
    raise TypeError(repr(object)+" is not JSON serialized")

complex_obj = json.dumps(2+3j, default=encode_complex)
print(complex_obj)

