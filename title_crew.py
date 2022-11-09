import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle

# Dataframe loading
url_title_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
df_title_crew = fct.load_database(url_title_crew, 0, 'tconst')

# ======================================================================================
# \\N replacement by NaN
value_to_replace = chr(92) + "N"
df_title_crew = fct.replace_n_to_nan(df_title_crew, value_to_replace)

# ======================================================================================
# Convert types of dataframe's columns
columns_name = df_title_crew.columns.values
type_conv = ["list", "list"]

for pos in range(len(type_conv)):
   df_title_crew = fct.convert_col(df_title_crew, columns_name[pos], type_conv[pos])

# ======================================================================================
# Count a number of <NA> in the column writers
df_title_crew["writers"].isna().sum()

# ======================================================================================
# Count a number of <NA> in the column directors
df_title_crew["directors"].isna().sum()

# ======================================================================================
# Count all values
df_title_crew.count()

# ======================================================================================
# Creating a pie chart for writers and directors
col_name = "writers"
col_name2 = "directors"
fct.plot_nan_prop(df_title_crew, col_name)
fct.plot_nan_prop(df_title_crew,col_name2)

plt.show()


df_title_crew = df_title_crew["directors"]
# Test to explode the lists, to transform them into lines
#toto = df_title_crew.explode('directors')

with open('df_title_crew.pkl', 'wb') as file:
   # A new file will be created
   pickle.dump(df_title_crew, file)

print("fini")
