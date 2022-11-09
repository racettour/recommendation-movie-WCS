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
#df_explode = df_explode.loc[df_explode['genres'].isin(['Drama','Comedy'])]

print(df_explode.dtypes)
##  graphique en fonction du temps

commits = df_explode.groupby(['startYear', 'genres']).sum()

sns.lineplot(data=commits.sort_values(by='startYear',
                                      ascending=True),
                                      x='startYear',
                                      y='val',
                                    hue='genres'
             ).set_title('Commits')

########################################################
#sns.lineplot(data=commits.sort_values(by='startYear',
#                                      ascending=True),
#                                      x='startYear',
#                                      y='val',
#                                    hue='genres'
#             ).set_title('Commits')

#fig = px.line(commits, x="startYear", y="val", color="genres", line_group="genres", hover_name="genres",
#        line_shape="spline", render_mode="svg")



plt.show()
#y_plot = 'runtimeMinutes'
#fig = px.line(df_explode, x="startYear", y=y_plot, title='Life expectancy in Canada')
#fig.show()
values = 'genres'
table = pd.pivot_table(df_explode, values='val' , index=['startYear'],
                    columns=[values], aggfunc=np.sum)

fig, ax = plt.subplots(figsize=(10, 10))

#y_val = ['Action', 'Adventure']
#sns.lineplot(data = table, x=table.index, y = 'Action')
sns.lineplot(data = df_explode, x='startYear', y ='val', hue = 'genres')





plt.show()
print("fini")