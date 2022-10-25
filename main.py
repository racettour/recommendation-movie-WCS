import pandas as pd
import matplotlib as plt
import function as fct
import seaborn as sns
import  numpy as np

# url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
# df_name_basics = fct.load_database(url_name_basics , 500)

toto = chr(92) + "N"


url_title_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
df_title_basics = fct.load_database(url_title_basics, 0, 'nconst')

year_df = fct.select_col(df_title_basics, ['startYear', 'titleType'])

year_df.replace(to_replace=toto,
                value= np.nan,  inplace=True
                )
nb_film_years = fct.count_col_val(year_df,'startYear')

df2 = nb_film_years.dropna(how='all')


tt = df_title_basics.groupby('startYear')['startYear'].count().sort_index()

tt = tt.to_frame()
tt['YEARS'] = tt.index.values

ind = tt.index.values
val = tt.values

sns.scatterplot(data=tt, x="YEARS", y="startYear")

plt.pyplot.show()


tttt