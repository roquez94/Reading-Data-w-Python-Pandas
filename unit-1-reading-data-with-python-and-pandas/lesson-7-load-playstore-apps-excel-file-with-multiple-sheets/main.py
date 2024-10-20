import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore = pd.read_excel(data_url,
                          index_col='App')

contentID = pd.read_excel(data_url, sheet_name='Content_ID', index_col='Content_ID')

print(playstore)

print(contentID)

# Using the `playstore.xlsx` Excel file from the given `data_url` and:

# - Save in a `playstore_df` variable the `Google_playstore` sheet. Use the first column as index.
# - Save in a `content_id_df` variable the `Content_ID` sheet. Use `Content_ID` as index.