import pandas as pd
import numpy as np


column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews',	'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']

csv_url = 'movies.csv'
df = pd.read_csv(csv_url, 
                 sep ='|', names=column_names)

print(df)
df.head(10)

df.describe()

df['movie_title'].describe()