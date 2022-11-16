import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle
import plotly.express as px

with open('df_clean.pkl', 'rb') as file:
    # Call load method to deserialze
    df = pickle.load(file)


df_explode = df.explode('genres')
df_explode.columns
df_explode['val']= 1
df_explode = df_explode.loc[df_explode['genres'].isin(['Drama','Comedy'])]

values = 'genres'
table_sum = pd.pivot_table(df_explode, values='val' , index=['startYear'],
                    columns=[values], aggfunc=np.sum)
##  graphique en fonction du temps

df_group_by_sum = df_explode.groupby(['startYear', 'genres']).sum()



df_cc = df.loc[:,['startYear', 'runtimeMinutes','genres', 'averageRating']]


df_group_by_mean = df_explode.groupby(['startYear', 'genres']).mean()
df_group_by_mean = df_group_by_mean.loc[:,['runtimeMinutes','averageRating']]



values_col = 'genres'
values_cell = 'averageRating'
table_moy = pd.pivot_table(df_explode, values= values_cell, index=['startYear'],
                    columns=[values_col], aggfunc=np.mean)

########################################################
# sum
y_val = 'numVotes'
sns.lineplot(data=df_group_by_sum.sort_values(by='startYear',
                                      ascending=True),
                                      x='startYear',
                                      y= y_val,
                                    hue='genres'
             ).set_title('Commits')

plt.show()

# mean
y_val = 'averageRating'
sns.lineplot(data=df_group_by_mean.sort_values(by='startYear',
                                      ascending=True),
                                      x='startYear',
                                      y= y_val,
                                    hue='genres'
             ).set_title('Commits')
plt.show()

#sns.lineplot(data=commits.sort_values(by='startYear',
#                                      ascending=True),
#                                      x='startYear',
#                                      y='val',
#                                    hue='genres'
#             ).set_title('Commits')




plt.show()






plt.show()
print("fini")