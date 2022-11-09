import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle


# Dataframe loading
url_title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
df = fct.load_database(url_title_basics, 0, 'tconst')

df_title_basics = df.copy()

df_title_basics = df_title_basics[df_title_basics['isAdult'] == '0']
df_title_basics = df_title_basics[df_title_basics['titleType'] == 'movie']

#
# ======================================================================================================
# \N and/or \\N replacement by NaN
value_to_replace = chr(92) + "N"
df_title_basics = fct.replace_n_to_nan(df_title_basics, value_to_replace)

value_to_replace2 = chr(92) + chr(92) + "N"
df_title_basics = fct.replace_n_to_nan(df_title_basics, value_to_replace2)

# ======================================================================================================
# Convert types of dataframe's columns
columns_name = df_title_basics.columns.values
type_conv = ["string", "string", "string", "bool", "datetime64[ns]", "datetime64[ns]", "float", "list"]
tata0 = df_title_basics.head(10000)

for pos in range(len(type_conv)):
    df_title_basics = fct.convert_col(df_title_basics, columns_name[pos], type_conv[pos])

print(df_title_basics.dtypes)
print('=' * 30)

df_title_basics.drop(['endYear', 'isAdult', 'primaryTitle', 'titleType'], axis=1, inplace=True)
columns_name = df_title_basics.columns.values

mask = (df_title_basics['startYear'] > '1945-1-1') & (df_title_basics['startYear'] <= '2022-1-1')
df_title_basics = df_title_basics.loc[mask]

tata2 = df_title_basics.head(10000)

# ======================================================================================================
# drop line with the same value in a given column
list_col = ['originalTitle']
df_title_basics = fct.drop_rep_val(df_title_basics, list_col)

# ======================================================================================================
# compt and class INDEX repetition
df = fct.count_index(df_title_basics)
print(df.head(30))

# ======================================================================================================
# compt and class values repetition
for i_col in columns_name:
    df = fct.count_value(df_title_basics, i_col)
    print(df)
    print('=' * 30)

# ======================================================================================================
# replace nan value by the chosen value: here it is the median
df2 = df_title_basics['startYear'].value_counts(dropna=False)
year_values = df2.index


for i_year in year_values:
    df3 = df_title_basics[df_title_basics['startYear'].values == i_year]

    replaced_value = df3['runtimeMinutes'].median()
    #ind = df_title_basics.loc[df3.index]
    df_title_basics.loc[df3.index] = fct.replace_nan(df_title_basics.loc[df3.index], 'runtimeMinutes', replaced_value)



df_title_basics = df_title_basics[df_title_basics['runtimeMinutes'] >= 60]
df_title_basics = df_title_basics[df_title_basics['runtimeMinutes'] <= 240]

tata = df_title_basics.head(10000)


# =====================================================================================================
# plot boxplot of the columns dataframe
#  !!!!!!!  becarefull only float or int columns car be plot
col_select = ['runtimeMinutes','runtimeMinutes']
fct.plot_boxplot(df_title_basics, col_select, 2, 2)

# =====================================================================================================
# drop outlayers
col_select = ['runtimeMinutes']
#df_title_basics = fct.drop_outliers(df_title_basics, col_select)

# plot boxplot of the columns dataframe
#  !!!!!!!  be careful only float or int columns car be plot
col_select = ['runtimeMinutes', 'runtimeMinutes']
fct.plot_boxplot(df_title_basics, col_select, 4, 2)

# toto = df_title_basics.explode('genres')

# Plot the figure durée moyenne des oeuvres cinématographique par année
# fig, ax = plt.subplots(figsize=(12, 6))
# df_group_Year = df_title_basics.groupby(by="startYear").mean()
# sns.lineplot(data=df_group_Year, x=df_group_Year.index, y="runtimeMinutes")
# ax.set(xlim=[None, 2022])
# ax.set_title("Durée moyenne des films par année")

# nb de film par genre en fonction de l'année
# fig, ax = plt.subplots(figsize=(12, 6))
# df_genre = df_title_basics.groupby(by=["startYear", "genres"]).count()
# sns.histplot(data=df_genre, x=df_genre.index.get_level_values(0).to_numpy(), y='primaryTitle',
#             hue=df_genre.index.get_level_values(1).to_numpy())
# df_genre2=pd.pivot_table(df_title_basics,index="genres",aggfunc="count")

index_select = df_title_basics.index
with open('IndexSelect.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(index_select, file)


with open('df_title_basics.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(df_title_basics, file)

plt.show()
print("fini")
