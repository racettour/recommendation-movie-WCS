import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np


url_title_principals = "https://datasets.imdbws.com/title.ratings.tsv.gz"
df = fct.load_database(url_title_principals, 0, 'tconst')

df_title = df.copy()

# variable loading
with open('listEp.pkl', 'rb') as file:
    # Call load method to deserialze
    last_listEp = pickle.load(file)

# =====================================================================================================
# df study
df_title.info()
print('=' * 30)

















print("fini")