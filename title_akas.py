import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle
pd.options.mode.chained_assignment = None  # default='warn'

with open('IndexSelect.pkl', 'rb') as file:
    # Call load method to deserialze
    IndexSelect = pickle.load(file)


# Dataframe loading
url_title_basics = "https://datasets.imdbws.com/title.akas.tsv.gz"
#df = fct.load_database(url_title_basics, 1000, 'titleId')

df_title = pd.DataFrame()

df = pd.read_csv(url_title_basics, sep='\t', index_col='titleId', low_memory=False, chunksize=100000, nrows=200000)
for i_df in df:
    toto = list(set(i_df.index).intersection(IndexSelect))
    if len(toto) != 0:
        df_temp = i_df.loc[toto]
        df_title = pd.concat([df_title, df_temp])

del df

#df_title = df.copy()

columns_name = df_title.columns.values

# =====================================================================================================
# df study
df_title.info()
print('=' * 30)

# compt and class values repetition
for i_col in columns_name:
    df = fct.count_value(df_title, i_col)
    print(df)
    print('=' * 30)

# =====================================================================================================
# there are not enouth information in "language", "types" and "attridutes". the columns are directly dropped
df_title.drop(['types', 'attributes', 'language'], axis=1, inplace=True)
columns_name = df_title.columns.values

tata = df_title.head(1000)

# ======================================================================================================
# \N and/or \\N replacement by NaN
value_to_replace = chr(92) + "N"
df_title = fct.replace_n_to_nan(df_title, value_to_replace)

value_to_replace2 = chr(92) + chr(92) + "N"
df_title = fct.replace_n_to_nan(df_title, value_to_replace2)

# ======================================================================================================
# Convert types of dataframe's columns
columns_name = df_title.columns.values
type_conv = ["int", "string", "string", "bool"]

for pos in range(len(type_conv)):
    df_title = fct.convert_col(df_title, columns_name[pos], type_conv[pos])

print(df_title.dtypes)
print('=' * 30)

# ======================================================================================================
list_ind = df_title.index.unique()
i_ind = list_ind[0]
for i_ind in list_ind:

    # select rows with index equal to i_ind
    df_temp = df_title.loc[i_ind]
    if type(df_temp) == pd.Series:
        tt = df_title.index.values == i_ind

        df_title.loc[tt, 'isOriginalTitle'] = True
        continue

    # in the previous selection, select the line which is original and keep only the first if there are several
    df_original_title = df_temp[df_temp['isOriginalTitle'] == True]

    # if there is no original title a line is add with 'No country origin' in region and isOriginalTitle = true
    if len(df_original_title) == 0:
        df_newline = df_temp.head(1)
        df_newline.loc[:, 'isOriginalTitle'] = True
        df_newline['region'] = 'No country origin'
        df_title = pd.concat([df_newline, df_title])
        continue

    # select his title
    original_title = df_original_title['title'][0]

    # in the previous selection, select the line which is not original
    df_temp2 = df_temp[df_temp['isOriginalTitle'] == False]

    # find in this list the same name and keep the last one
    df_same_name = df_temp2[df_temp2['title'] == original_title]
    df_same_name = df_same_name.tail(1)

    # select its region
    if len(df_same_name) == 0:
        prod_country = 'No country origin'
    else:
        prod_country = df_same_name['region'][0]

    # stcock the prod_country in the line of the original country and the column regione
    tt = (df_title['isOriginalTitle'] == True) & (df_title.index.values == i_ind)

    df_title.loc[tt, 'region'] = prod_country


# creation of 2 df : the first one contains the number of language available by movie index
df2 = df_title.groupby([df_title.index])['region'].nunique()
df2 = df2.to_frame()
df2 = df2.rename(columns={'region': 'language number'})  # old method

# the second one contains the origin country
df3 = df_title[df_title['isOriginalTitle'] == True]['region']
df3 = df3.to_frame()


# they are merge in df_title_clean
df_title_clean = df2.merge(df3, left_on=df2.index.values, right_on=df2.index.values, left_index=True)

print("fini")
