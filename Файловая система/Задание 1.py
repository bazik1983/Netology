import json

new_dict = {}
with open('purchase_log.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        dict = json.loads(line)
        key = dict['user_id']
        value = dict['category']
        if key != 'user_id':
            new_dict.setdefault(key, value)
    print(new_dict)