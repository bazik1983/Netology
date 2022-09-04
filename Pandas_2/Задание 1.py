import pandas as pd


data=pd.read_csv('ratings.csv', delimiter=',')
data.head()


def raiting_class(row):
    if row.rating >= 4.5:
        return 'высокий рейтинг'
    elif 2 < row.rating < 4.5:
        return 'средний рейтинг'
    elif row.rating <= 2:
        return 'низкий рейтинг'


data['class2'] = data.apply(raiting_class, axis=1)
print (data)