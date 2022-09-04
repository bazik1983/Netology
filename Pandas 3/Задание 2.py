import pandas as pd


url = pd.read_csv('URLs.txt')
print(url[url.url.str.contains('/[0-9]{8}-', regex=True)].head())

