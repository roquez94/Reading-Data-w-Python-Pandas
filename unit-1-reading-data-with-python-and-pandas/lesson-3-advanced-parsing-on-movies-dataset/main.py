import numpy as np
import pandas as pd

column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

# - Use the appropriate separator.
movies = pd.read_csv("unit-1-reading-data-with-python-and-pandas\lesson-3-advanced-parsing-on-movies-dataset\data\movies.csv" ,
                     sep = '|',
                     na_values='?',
                     names= column_names,
                     thousands=',',
                     index_col='movie_title', 
                     dtype={'budget' : float})

movies.describe()

print(movies.dtypes)
print(movies.index)
print(movies)
# - The given data doesn't have a defined header. Use the column names given in the `column_names` variable.


# - Missing values are encoded as `?` characters. Parse those values as `NaN` objects.
# - The `budget` column has commas separating the thousands, make sure the column is of float data type.
# - The index of the DataFrame should be represented by the `movie_title` column.