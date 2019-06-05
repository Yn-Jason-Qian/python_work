import json_util as util

user_info = {'name':'xiaoli', 'age': 28}

util.save(user_info, 'user_info.json')
info = util.get('user_info.json')
print(info['name'])
print(info['age'])


