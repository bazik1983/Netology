ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

geo = ids.values()

new_geo = []
for i in geo:
    for f in i:
        new_geo.append(f)

print(set(new_geo))