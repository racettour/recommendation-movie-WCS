import streamlit as st
import pandas as pd
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
import mpld3
import streamlit as st
import streamlit.components.v1 as components
import  datetime as dt
import numpy as np

# load dataframe
with open('df_clean.pkl', 'rb') as file:
    # Call load method to deserialze
    df = pickle.load(file)

date_min = dt.datetime.strptime('1945','%Y')
date_max = dt.datetime.strptime('2022','%Y')

# =============================================================================
# graphique part
# title
st.title('Analyse de  la base de données IMdb')

# add de sidebar the all the genres
with st.sidebar:
    # ============================graph part============================
    bt_Action = st.checkbox('Action', value=True)
    bt_Adult = st.checkbox('POUR_TOI_CLEMENT', value=False)
    bt_Adventure = st.checkbox('Adventure', value=False)
    bt_Animation = st.checkbox('Animation', value=False)
    bt_Biography = st.checkbox('Biography', value=False)
    bt_Comedy = st.checkbox('Comedy', value=False)
    bt_Crime = st.checkbox('Crime', value=False)
    bt_Documentary = st.checkbox('Documentary', value=False)
    bt_Drama = st.checkbox('Drama', value=False)
    bt_Family = st.checkbox('Family', value=False)
    bt_Fantasy = st.checkbox('Fantasy', value=False)
    bt_Film_Noir = st.checkbox('Film-Noir', value=False)
    bt_Game_Show = st.checkbox('Game-Show', value=False)
    bt_History = st.checkbox('History', value=False)
    bt_Horror = st.checkbox('Horror', value=False)
    bt_Music = st.checkbox('Music', value=False)
    bt_Musical = st.checkbox('Musical', value=False)
    bt_Mystery = st.checkbox('Mystery', value=False)
    bt_News = st.checkbox('News', value=False)
    bt_Reality_TV = st.checkbox('Reality-TV', value=False)
    bt_Romance = st.checkbox('Romance', value=False)
    bt_Sci_Fi = st.checkbox('Sci-Fi', value=False)
    bt_Sport = st.checkbox('Sport', value=False)
    bt_Talk_Show = st.checkbox('Talk-Show', value=False)
    bt_Thriller = st.checkbox('Thriller', value=False)
    bt_War = st.checkbox('War', value=False)
    bt_Western = st.checkbox('Western', value=False)

    # ============================ action part ============================
    # select the genre and add in a list
    genre_list = []
    if bt_Action:
        genre_list.append('Action')
    if bt_Adult:
        genre_list.append('Adult')
    if bt_Adventure:
        genre_list.append('Adventure')
    if bt_Animation:
        genre_list.append('Animation')
    if bt_Biography:
        genre_list.append('Biography')
    if bt_Comedy:
        genre_list.append('Comedy')
    if bt_Crime:
        genre_list.append('Crime')
    if bt_Documentary:
        genre_list.append('Documentary')
    if bt_Drama:
        genre_list.append('Drama')
    if bt_Family:
        genre_list.append('Family')
    if bt_Fantasy:
        genre_list.append('Fantasy')
    if bt_Film_Noir:
        genre_list.append('Film-Noir')
    if bt_Game_Show:
        genre_list.append('Game-Show')
    if bt_History:
        genre_list.append('History')
    if bt_Horror:
        genre_list.append('Horror')
    if bt_Music:
        genre_list.append('Music')
    if bt_Musical:
        genre_list.append('Musical')
    if bt_Mystery:
        genre_list.append('Mystery')
    if bt_News:
        genre_list.append('News')
    if bt_Reality_TV:
        genre_list.append('Reality-TV')
    if bt_Romance:
        genre_list.append('Romance')
    if bt_Sci_Fi:
        genre_list.append('Sci-Fi')
    if bt_Sport:
        genre_list.append('Sport')
    if bt_Talk_Show:
        genre_list.append('Talk-Show')
    if bt_Thriller:
        genre_list.append('Thriller')
    if bt_War:
        genre_list.append('War')
    if bt_Western:
        genre_list.append('Western')

# ============================graph part============================
# add 3 tabs with the 3 kind of graph
tab_temp, tab_rep, tab_corr = st.tabs(["Analyse en fonction du temps", "Répartition de la production", "Corrélation"])

with tab_temp:
    # ============================graph part============================

    tap_temp_value = st.radio(
        "",
        ('Notes', 'Duree', 'Nombre_de_film', "Nombre_de_vote"))
    x_range_temp = st.slider("x range", min_value= date_min,
                             max_value=date_max, value=[date_min, date_max])


    # ============================ action part ============================
    # recover the selected  value of the tap_rep_value and assign the col_value to plot it
    if tap_temp_value == 'Notes':
        col_value_temp = "averageRating"
    elif tap_temp_value == "Duree":
        col_value_temp = "runtimeMinutes"
    elif tap_temp_value == "Nombre_de_film":
        col_value_temp = "val"
    elif tap_temp_value == "Nombre_de_vote":
        col_value_temp = "numVotes"

    df_temp = df.explode('genres')
    df_temp['val'] = 1
    df_temp = df_temp.loc[df_temp['genres'].isin(genre_list)]

    df_temp_sum = df_temp.groupby(['startYear', 'genres']).sum()
    df_temp_mean = df_temp.groupby(['startYear', 'genres']).mean()

    fig_temp, ax_temp = plt.subplots()
    if tap_temp_value in ['Notes', "Duree"]:
        viz_temp = sns.lineplot(
            data=df_temp_mean.sort_values(by='startYear',
                                          ascending=True),
            x='startYear',
            y=col_value_temp,
            hue='genres'
        ).set_title(tap_temp_value)
    elif tap_temp_value in ['Nombre_de_film', "Nombre_de_vote"]:
        viz_temp = sns.lineplot(
            data=df_temp_sum.sort_values(by='startYear',
                                         ascending=True),
            x='startYear',
            y=col_value_temp,
            hue='genres'
        ).set_title(tap_temp_value)

    #st.pyplot(fig_temp)
    ax_temp.set_xlim(x_range_temp[0], x_range_temp[1])
    fig_html_temp = mpld3.fig_to_html(fig_temp)
    components.html(fig_html_temp, height=500)


with tab_rep:
    # ============================graph part============================

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>',
             unsafe_allow_html=True)

    tap_rep_value = st.radio(
        "",
        ('Duree', 'Notes', 'Nombre_de_votes'))




    # ============================ action part ============================
    # recover the selected  value of the tap_rep_value and assign the col_value to plot it
    if tap_rep_value == 'Duree':
        col_value_rep = "runtimeMinutes"
    elif tap_rep_value == "Notes":
        col_value_rep = "averageRating"
    elif tap_rep_value == "Nombre_de_votes":
        col_value_rep = "numVotes"

    # ============================ action part ============================
    select_columns = ['genres', col_value_rep]
    df_rep = df[select_columns]

    # explode columns col_name
    df_rep = df_rep.explode("genres")
    df_plot = df_rep.loc[df_rep["genres"].isin(genre_list)]


    min_cor=int(df_plot[col_value_rep].min())-10
    max_cor=int(df_plot[col_value_rep].max())+10
    x_range_cor = st.slider("x range", min_value=min_cor,
                            max_value=max_cor, value=[min_cor, max_cor])

    # Plot the boxplot
    fig_rep,ax_rep = plt.subplots()
    viz_boxplot = sns.boxplot(df_plot, x=col_value_rep, y="genres")
    #st.pyplot(fig_rep)
    ax_rep.set_xlim(x_range_cor[0], x_range_cor[1])
    fig_html_rep = mpld3.fig_to_html(fig_rep)
    components.html(fig_html_rep, height=500)

with tab_corr:
    # Compute the correlation matrix
    df_corr = df.copy()
    df_corr['startYear'] = df_corr['startYear'].dt.strftime('%Y').astype(int)

    corr = df_corr.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig_corr, ax_corr = plt.subplots()

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    viz_corr = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                           square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)


    st.pyplot(fig_corr)
    st.write('Matrice de corrélation')
    st.write(corr)
    st.write('dataframe')

    st.write(df_corr.head(1000))



    #fig_html_rep = mpld3.fig_to_html(viz_corr)
    #components.html(fig_html_rep, height=500)



