import pandas as pd
import matplotlib as plt
import function as fct
import seaborn as sns
import  numpy as np


url_title_principals = "https://datasets.imdbws.com/title.principals.tsv.gz"
df = fct.load_database(url_title_principals, 0, 'tconst')

df_title_principals = df.copy()
print('=' * 30)
#===========================================================================================
# \N and/or \\N replacement by NaN
value_to_replace = chr(92) + "N"
df_title_principals = fct.replace_n_to_nan(df_title_principals, value_to_replace)

value_to_replace2 = chr(92) + chr(92) + "N"
df_title_principals = fct.replace_n_to_nan(df_title_principals, value_to_replace2)

print('=' * 30)

#===========================================================================================
df_title_principals = fct.convert_col(df_title_principals, "characters", "string")

# replace a chosen value by the chosen value: here it is 0 replace by  the median

df_title_principals['characters'] = df_title_principals['characters'].replace('\]','', regex=True)
df_title_principals['characters'] = df_title_principals['characters'].replace('\[','', regex=True)
df_title_principals['characters'] = df_title_principals['characters'].replace('\"','', regex=True)
df_title_principals['characters'] = df_title_principals['characters'].replace('\'','', regex=True)

print('=' * 30)
#===========================================================================================
# Convert types of dataframe's columns
columns_name = df_title_principals.columns.values
type_conv = ["int64", "string", "string", "string", "string"]

for pos in range(len(type_conv)):
    df_title_principals = fct.convert_col(df_title_principals, columns_name[pos], type_conv[pos])

print(df_title_principals.dtypes)

print('=' * 30)

#===========================================================================================
# drop column "characters" and "ordering"
df_title_principals = df_title_principals.drop(columns=["characters"])
df_title_principals = df_title_principals.drop(columns=["ordering"])

print('=' * 30)

#===========================================================================================
fct.count_value(df_title_principals, "category")
fct.count_value(df_title_principals, "job")


