import pandas as pd

tables = pd.read_html('https://fortrader.org/quotes')
print('Найдено таблиц:', len(tables))
df1 = pd.DataFrame(tables[4])
print(df1.columns)
