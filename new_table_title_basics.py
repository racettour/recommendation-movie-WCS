import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle

# Loading df_title_basics

with open('df_title_basics.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_basics = pickle.load(file)

# Loading df_title_ratings
with open('df_title_ratings.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_ratings = pickle.load(file)

with open('df_title_crew.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_crew = pickle.load(file)

#Merge Datafram
#df_merge = df_title_basics.merge(df_title_ratings, left_on= df_title_basics.index  , right_on=df_title_ratings.index, how ="left").set_index(df_title_basics.index)
df_merge = df_title_basics.merge(df_title_ratings, left_index=True, right_index = True, how ="left")

# Count a number of <NA> in the column averageRating
df_merge["averageRating"].isna().sum()

# Count a number of <NA> in the column numVotes
df_merge["numVotes"].isna().sum()

# Count all values
df_merge.count()

# Delete all the NaN value

df_merge = df_merge.merge(df_title_crew, left_index=True, right_index=True, how ="left")


# Creating a pie chart for averageRating and numVotes
col_name = "averageRating"
col_name2 = "numVotes"
col_name3 = "directors"
fct.plot_nan_prop(df_merge, col_name)
fct.plot_nan_prop(df_merge, col_name2)
fct.plot_nan_prop(df_merge, col_name3)


plt.show()

df_merge = df_merge.dropna()

df_clean = df_merge.copy()

with open('df_clean.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(df_clean, file)


print(("fini"))