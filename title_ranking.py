import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle


url_title = "https://datasets.imdbws.com/title.ratings.tsv.gz"
df = fct.load_database(url_title, 0, 'tconst')

df_title_ratings = df.copy()

# variable loading

with open('df_title_ratings.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(df_title_ratings, file)

print('=' * 30)

















print("fini")