import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np

# Dataframe loading
url_title_ratings = "https://datasets.imdbws.com/title.ratings.tsv.gz"
df_title_ratings = fct.load_database(url_title_ratings, 0, 'tconst')

# ======================================================================================
# \\N replacement by NaN
value_to_replace = chr(92) + "N"
df_title_crew = fct.replace_n_to_nan(df_title_ratings, value_to_replace)

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
col_name = "directors"
NumberNaN = df_title_crew[col_name].isna().sum()
nb_total_val = df_title_crew[col_name].count()
Filled_field = nb_total_val - NumberNaN
data = [NumberNaN, Filled_field]
fig, ax = plt.subplots(figsize=(10,10))
explode = [0.02, 0.02]
labels = ['NaN', 'Field filled']
colors = sns.color_palette('bright')
Text_Title = "% du nombre de NaN dans la colonne " + col_name
plt.title(Text_Title)
plt.pie(data, labels=labels, colors=colors, autopct='%0.0f%%', explode=explode)
plt.show()

# Test to explode the lists, to transform them into lines
toto = df_title_crew.explode('directors')
print("fini")

