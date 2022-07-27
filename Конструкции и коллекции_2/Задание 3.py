results = {
'vk': {'revenue': 103, 'cost': 98},
'yandex': {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},
}

for key, value in sorted(results.items()):
    value['ROI'] = round(((value['revenue'] / value['cost']) - 1)*100 , 2)
    print(key, value)
