import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import  numpy as np
import pickle
pd.options.mode.chained_assignment = None  # default='warn'

with open('df_title_principals.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_principals = pickle.load(file)

with open('df_name_basics.pkl', 'rb') as file:
    # Call load method to deserialze
    df_name_basics = pickle.load(file)


df_merge = df_title_principals.merge(df_name_basics, left_on="nconst",
                                     right_index=True, how="left")

df_merge = df_merge["primaryName"]
df_merge = df_merge.to_frame()

temp = df_merge.groupby(df_merge.index)["primaryName"].apply(list)

fct.plot_nan_prop(df_merge, "primaryName")

plt.show()
