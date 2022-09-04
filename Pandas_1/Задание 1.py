import pandas as pd
import requests
import zipfile
from io import BytesIO


def get_zip_files():
    response = requests.get('https://files.grouplens.org/datasets/movielens/ml-latest-small.zip')
    return zipfile.ZipFile(BytesIO(response.content))


def get_ratings_data_frame(zip_arch):
    return pd.read_csv(zip_arch.open(name='ml-latest-small/ratings.csv'))


def get_movies_data_frame(zip_arch):
    return pd.read_csv(zip_arch.open(name='ml-latest-small/movies.csv'))


movies_zip = get_zip_files()
ratings = get_ratings_data_frame(movies_zip)
movies_info = get_movies_data_frame(movies_zip).set_index(keys='movieId', drop=False)

top_films = ratings.query('rating == {}'.format(5))

best_film_id = top_films['movieId'].value_counts().idxmax()

print(f'Фильм: {movies_info.loc[best_film_id, "title"]}')

