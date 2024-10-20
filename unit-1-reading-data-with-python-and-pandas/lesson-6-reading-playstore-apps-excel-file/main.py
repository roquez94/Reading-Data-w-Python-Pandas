import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore = pd.read_excel(data_url,
                          usecols = ['App', 'Rating', 'Installs', 'Genres', 'Last_Updated'],
                          parse_dates= ['Last_Updated']
                          )

print(playstore)

print(playstore.nlargest(25,'Rating'))
# playstore_df = playstore_df.sort_values('Rating', ascending=False).head(25)



# Read the `playstore.xlsx` Excel file from the given `data_url` and store it in a `playstore_df` DataFrame.

# - When reading in the file, only use the columns `'App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'`.
# - Make sure `Last_Updated` is in datetime format, try do this while reading the file into the DataFrame.

# After reading the data, filter the records and keep only the top 25 with highest `Rating` (being 5 the highest possible rating value).