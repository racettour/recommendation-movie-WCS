import title_basics as basics
import title_akas as akas
import title_ranking as rank
import title_crew as crew
import title_principals as principals
import  name_basics as name
import pickle
import function as fct
import matplotlib.pyplot as plt



# clean all the table independatly
#basics.table_cleaning()
#akas.table_cleaning()
#rank.table_cleaning()
#crew.table_cleaning()
#principals.table_cleaning()
#name.table_cleaning()

# load the tables
print("loading")
with open('df_title_basics.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_basics = pickle.load(file)

with open('df_akas.pkl', 'rb') as file:
    # Call load method to deserialze
    df_akas = pickle.load(file)

# Loading df_title_ratings
with open('df_title_ratings.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_ratings = pickle.load(file)

with open('df_title_crew.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_crew = pickle.load(file)

with open('df_title_principals.pkl', 'rb') as file:
    # Call load method to deserialze
    df_title_principals = pickle.load(file)

with open('df_name_basics.pkl', 'rb') as file:
    # Call load method to deserialze
    df_name_basics = pickle.load(file)


# merge df_title_basics, df_title_ratings and df_title_crew
print("merge database")
df_merge = df_title_basics.merge(df_title_ratings, left_index=True, right_index = True, how ="left")
df_merge = df_merge.merge(df_title_crew, left_index=True, right_index=True, how ="left")

# drop lines with nan values
df_merge = df_merge.merge(df_akas, left_index=True, right_index=True, how ="left")
df_merge = df_merge.dropna()

# merge df_title_principals and df_name_basics and keep only the primaryName columns
df_temp = df_title_principals.merge(df_name_basics, left_on="nconst",
                                    right_index=True, how="left")
df_temp = df_temp["primaryName"]
df_temp = df_temp.to_frame()
df_temp = df_temp.dropna()
# group by index (films) and apply list function to have the actors list
df_temp = df_temp.groupby(df_temp.index)["primaryName"].apply(list)



df_merge = df_merge.merge(df_temp, left_index=True, right_index=True, how ="left")


df_merge = df_merge.rename(columns={"title": "title_fr", "primaryName" : "Actors_name"})
df_merge = df_merge.drop('region', axis=1)
df_merge = df_merge.dropna()


columns_name = df_merge.columns.values

for i_col in columns_name:
    fct.plot_nan_prop(df_merge, i_col)

plt.show()



df_clean = df_merge.copy()

with open('df_clean.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(df_clean, file)
