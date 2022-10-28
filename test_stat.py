import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import  numpy as np

# Dataframe loading
url_title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
df_title_basics = fct.load_database(url_title_basics, 0, 'tconst')

df4 = df_title_basics.groupby(by="genres").counts()
df4
# \N and/or \\N replacement by NaN

value_to_replace = chr(92) + "N"
df_title_basics = fct.replaceN_to_Nan(df_title_basics, value_to_replace)

value_to_replace2 = chr(92) + chr(92) + "N"
df_title_basics = fct.replaceN_to_Nan(df_title_basics, value_to_replace)




# Convert types of dataframe's columns
columns_name = df_title_basics.columns.values
type_conv = ["string", "string", "string", "bool", "float", "datetime64[ns]", "float", "string"]

#for pos in range(len(type_conv)):
for pos in range(1,7):
    df_title_basics = fct.convert_col(df_title_basics, columns_name[pos], type_conv[pos])


print(df_title_basics.dtypes)


# Plot the figure durée moyenne des oeuvres cinématographique par année
fig, ax = plt.subplots(figsize=(12, 6))
df_Groupby_Year = df_title_basics.groupby(by="startYear").mean()
sns.lineplot(data =df_Groupby_Year, x=df_Groupby_Year.index, y="runtimeMinutes")
ax.set_title("Durée moyenne des films par année")
plt.show()

#nb de film par genre en fonction de l'année
#fig, ax = plt.subplots(figsize=(12, 6))
#df_genre=df_title_basics.groupby(by= ["startYear", "genres"]).count()
#sns.histplot(data=df_title_basics, x=)
#df_genre2=pd.pivot_table(df_title_basics,index=["startYear"],values=["genres"],aggfunc="count")

print("fini")

