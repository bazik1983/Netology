import pandas as pd


ratings = pd.read_csv('ml-latest-small/ratings.csv')
life = ratings.groupby('userId').agg({'timestamp': ['min', 'max'], 'userId': 'count'})
life = life[life['userId']['count'] > 100]
life.loc[:, 'livetime'] = life['timestamp']['max'] - life['timestamp']['min']
print(life.reset_index())