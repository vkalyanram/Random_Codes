def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key] == value]
----------------------------------------------------------------------------------------------------------  
  my_dict = [
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5},
    {"name": "Pam", "age": 7}
]

next(filter(lambda obj: obj.get('name') == 'Pam', my_dict), None)
---------------------------------------------------------------------------------------------------------------
def call_print():
	print(json.dumps(List, indent=4))
---------------------------------------------------------------------------------------------------------
all

all will return True only when all the elements are Truthy.

Truth table

+-----------------------------------------+---------+---------+
|                                         |   any   |   all   |
+-----------------------------------------+---------+---------+
| All Truthy values                       |  True   |  True   |
+-----------------------------------------+---------+---------+
| All Falsy values                        |  False  |  False  |
+-----------------------------------------+---------+---------+
| One Truthy value (all others are Falsy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| One Falsy value (all others are Truthy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| Empty Iterable                          |  False  |  True   |
+-----------------------------------------+---------+---------+

# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
--------------------------------------------------------------
from dateutil import parser
def convert(date_time):
		datetime_str = parser.parse(date_time)
		return datetime_str	
--------------------------------------------------------------	
In short, {foreign_key_name}_id if you want to assign the id directly.
Django error. Cannot assign must be an instance
