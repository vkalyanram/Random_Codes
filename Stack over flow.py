def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key] == value]
----------------------------------------------------------------------------------------------------------  
  my_dict = [
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5},
    {"name": "Pam", "age": 7}
]

next(filter(lambda obj: obj.get('name') == 'Pam', my_dict), None)
