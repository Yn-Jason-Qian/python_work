import json

def save(data, file_name):
    try:
        with open(file_name, 'w') as file_object:
            json.dump(data, file_object)
    except FileNotFoundError:
        print('Can not find File ' + file_name)
    

def get(file_name):
    try:
        with open(file_name) as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        print('Can not find file ' + file_name)
