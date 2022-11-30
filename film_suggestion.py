import seaborn as sns
import pickle
import matplotlib.pyplot as plt
import mpld3
import streamlit as st
import streamlit.components.v1 as components
import datetime as dt
import numpy as np
import web_scapping_fct as ws
import pandas as pd
import function_sugestion as fct_sug
import pyautogui


font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 26px;
}
</style>
"""

st.write(font_css, unsafe_allow_html=True)


load_tab = True
text_vu = ""

with open('df_IA.pkl', 'rb') as file:
    # Call load method to deserialze
    df_IA = pickle.load(file)



with open('df_clean.pkl', 'rb') as file:
    # Call load method to deserialze
    df_clean = pickle.load(file)

df_clean['startYear'] = df_clean['startYear'].dt.strftime('%Y').astype(int)


try :
    with open('last_id.pkl', 'rb') as file:
        # Call load method to deserialze
        text_id = pickle.load(file)
except:
    text_id = ""

with open('IA_reco2.pkl', 'rb') as file:
    # Call load method to deserialze
    distanceKNN2 = pickle.load(file)

with open('df_IA_2.pkl', 'rb') as file:
    # Call load method to deserialze
    sparse = pickle.load(file)


#=================================================
st.title('Recommandation de films')


if len(text_vu) != 0:
    st.write(text_vu)

with st.sidebar:
    idd = st.text_input(
        "identidiant",
        text_id,
        key="idd",
    )

if idd:

    with open('last_id.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(idd, file)


    with st.sidebar:
        st.write("Vous êtes connecté(e) en tant que: ", idd)
        user_name = idd + ".pkl"
        try:
            with open(user_name, 'rb') as file:
                # Call load method to deserialze
                film_list = pickle.load(file)
            fct_sug.print_film_list(df_clean, film_list)

        except:
            film_list = []
else:
    film_list = []

tab_search, tab_suggestion, tab_film_list = st.tabs(["recherche...", "recommandation", "films vus"])

with tab_search:
    text_search = st.text_input(
        "Titre du film ",
        "",
        key="text_search"
    )

    if text_search:

        df_search = df_clean[df_clean["title_fr"].str.lower().str.contains(text_search)]

        if len(df_search) > 5:
            df_search = df_search.head(5)


        for line in range(len(df_search)):
            txt_bt = "bt_" + str(line)
            df_temp = df_search.iloc[line]

            film_list, load_tab = fct_sug.expander_func(df_temp,df_clean, txt_bt,film_list, user_name,load_tab)

with tab_suggestion:


    if len(film_list) != 0:

        if load_tab == True:

            film_suggestions = fct_sug.IA_2(film_list, distanceKNN2, df_clean, sparse)

            for line in range(len(film_suggestions)):
                txt_bt = "btS_" + str(line)
                df_temp = film_suggestions.iloc[line]

                film_list,load_tab = fct_sug.expander_func(df_temp, df_clean, txt_bt, film_list, user_name, load_tab)

with tab_film_list:

    st.write(df_clean.loc[film_list])

    with st.sidebar:

        toto = df_clean.loc[film_list]

        if len(toto) != 0:
            st.title('**Description**')

            st.write(toto["Actors_name"])
            st.write(toto["genres"])
            st.write(toto["startYear"])
            st.write(toto["averageRating"])
            st.write(toto["directors"])