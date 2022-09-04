import pandas as pd

df_key = pd.read_csv('keywords.csv')
geo_data = {'Центр': ['москва', 'тула', 'ярославль'],
            'Северо-Запад': ['петербург', 'псков', 'мурманск'],
            'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']}


def find_region(row):
    for i in geo_data.items():
        for a in i[1]:
            if a in row['keyword']:
                return i[0]

    return 'undefined'

df_key['region'] = df_key.apply(find_region, axis=1)
print(df_key.head())
print(df_key[df_key['region'] == 'Центр'].head())