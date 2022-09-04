import pandas as pd

movies_dt = pd.read_csv('movies.csv')
ratings_dt = pd.read_csv('ratings.csv')

x = ratings_dt.merge(movies_dt, how='left')

films_rating = x.groupby('title').mean().reset_index()[['title', 'rating']]
years = [str(i + 1950) for i in range(61)]


def production_year(row):
    for year in years:
        if year in row['title']:
            return year
    return '1900'


films_rating['year'] = films_rating.apply(production_year, axis=1)
print(films_rating.sort_values('rating', ascending=False).head(50))
