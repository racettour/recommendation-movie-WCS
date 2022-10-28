import pandas as pd
import matplotlib as plt
import function as fct
import seaborn as sns
import  numpy as np

# url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
# df_name_basics = fct.load_database(url_name_basics , 500)

toto = chr(92) + "N"


url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
df_name_basics = fct.load_database(url_name_basics, 0, 'nconst')

typecol = df_name_basics.primaryName.dtype
primaryName = str(df_name_basics["primaryName"])

# Convert "primaryName" from int to string
df_name_basics = df_name_basics.astype({'primaryName':'string'})

df_name_basics = fct.convert_col(df_name_basics, "primaryName", "string")

#remplacement valeur \N et/ou \\N par des NaN
value_to_replace = chr(92) + "N"
df_name_basics = fct.replaceN_to_Nan(df_name_basics, value_to_replace)
print("fini")
value_to_replace2 = chr(92) + chr(92) + "N"
df_name_basics = fct.replaceN_to_Nan(df_name_basics, value_to_replace)