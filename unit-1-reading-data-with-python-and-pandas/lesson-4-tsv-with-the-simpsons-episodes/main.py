import numpy as np
import pandas as pd

column_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']

simpsons = pd.read_csv('unit-1-reading-data-with-python-and-pandas\lesson-4-tsv-with-the-simpsons-episodes\data\simpsons-episodes.tsv',
                       sep = '\t',
                       names = column_names,
                       skiprows= 4,
                       usecols= ['Title', 'Air date', 'Production code', 'IMDB rating'],
                       na_values='no_val',
                       index_col='Production code',
                       parse_dates=['Air date'])

simpsons.describe()
print(simpsons)


# Use correct separator as data is tabular separated.
# - Use the following `col_names` list as column names.
# - Load just `Title`, `Air date`, `Production code` and `IMDB rating`.
# - Don't load the first empty columns.
# - Set `Production code` as index.
# - Null values are encoded as `no_val` values, be careful with that when loading the data.
# - Parse the `Air date` columns as Date.