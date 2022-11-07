import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import  numpy as np

# Dataframe loading
url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
df_name_basics = fct.load_database(url_name_basics, 200, 'nconst')
# create a copy of dataframe "df_name_basic"
df_cleaning = df_name_basics.copy()

#replace values /N and //N by Nan
value_to_replace = chr(92) + "N"
df_cleaning = fct.replace_n_to_nan(df_cleaning, value_to_replace)

value_to_replace2 = chr(92) + chr(92) + "N"
df_cleaning = fct.replace_n_to_nan(df_cleaning, value_to_replace)

#how many null in the columns "primaryProfession"
nb_val_null = df_cleaning["primaryProfession"].isnull().sum()

# Convert types of dataframe's columns
columns_name = df_cleaning.columns.values
type_conv = ["string", "float", "float", "list", "list"]

for pos in range(len(type_conv)):
    df_cleaning = fct.convert_col(df_cleaning, columns_name[pos], type_conv[pos])

print('=' * 30)

#deleted column "knownForTitles"
df_cleaning = df_cleaning.drop(["knownForTitles"],axis=1)

#deleted duplicates in index
idx = np.unique( df_cleaning.index.values, return_index = True )[1]
df_cleaning = df_cleaning.iloc[idx]


# CLEANING df_cleaning with a condition
# delete row where deathYear before 1945
died_too_soon = 1945
df_test = df_cleaning[(df_cleaning["deathYear"] > died_too_soon)]

# select row with Nan in the columns "deathYear"
df_test_with_nan = df_cleaning[(df_cleaning["deathYear"].isnull())]

#df_test_with_nan["primaryProfession"]=df_test_with_nan["primaryProfession"].replace(to_replace=np.NaN, value=[["unknown"]])

# concatenation df_test and df_test_with_nan]
df_cleaning = pd.concat([df_test,df_test_with_nan])

df_cleaning2_after_explode = df_cleaning.explode("primaryProfession")

df_count_Profession=fct.count_value(df_cleaning2_after_explode, "primaryProfession")

#pie matplotlib primaryProfession
fig, axs = plt.subplots(figsize = (20,10))
df2=df_count_Profession["primaryProfession"].index

axs.pie(x =df_cleaning2_after_explode['primaryProfession'].value_counts()[0:20],
       labels=df_cleaning2_after_explode['primaryProfession'].value_counts().index[0:20],autopct = lambda x: str(round(x, 2)) + '%')
plt.title("Répartition des 20 professions les plus présentes")

#delete primaryProfessionwhich are not in out selection(list_profession)
#list_profession = ["actor", "actress", "director", "producer", "writer"]
df_select1 = df_cleaning2_after_explode[(df_cleaning2_after_explode["primaryProfession"]=="actor")]
df_select2 = df_cleaning2_after_explode[(df_cleaning2_after_explode["primaryProfession"]=="actress")]
df_select3 = df_cleaning2_after_explode[(df_cleaning2_after_explode["primaryProfession"]=="director")]
df_select4 = df_cleaning2_after_explode[(df_cleaning2_after_explode["primaryProfession"]=="producer")]
df_select5 = df_cleaning2_after_explode[(df_cleaning2_after_explode["primaryProfession"]=="writer")]
#concatenation df_select
df_very_clean= pd.concat([df_select1,df_select2,df_select3,df_select4,df_select5])
fct.plot_nan_prop(df_very_clean,"birthYear")
print('finito')
#list_profession = ["actor", "actress", "directos", "producer", "writer"]
#df[col_name].value_counts(dropna=True)