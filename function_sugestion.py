import pickle
import streamlit as st
import web_scapping_fct as ws
import pandas as pd
import pyautogui


def weight(df):
    """
    impose weight for the IA on some columns
    :param df: dataframe
    :return: dataframe
    """
    weight1 = 2
    weight2 = 4
    weight0 = 0.25
    weight00 = 0.1
    df["startYear"] = df["startYear"] * weight1
    df.loc[:, "action":"western"] = df.loc[:, "action":"western"] * weight2
    df["averageRating"] = df["averageRating"] * weight0
    df["numVotes"] = df["numVotes"] * weight0
    df["runtimeMinutes"] = df["runtimeMinutes"] * weight00
    df["language number"] = df["language number"] * weight00
    return df


def IA_2(list_film, distanceKNN, df_clean, sparse_tot):
    """
    with the AI already trained, this function will find, according to the selected movies, the nearest neighbors, classified them and proposed them to the users
    :param list_film: list
    :param distanceKNN: KNN model
    :param df_clean: dataframe
    :param sparse_tot: sparse matrix
    :return: list
    """
    if len(list_film) == 1:

        index_pos = df_clean.index.get_loc(list_film[0])
        # find film index
        df_select = df_clean.iloc[index_pos]

        film_select = sparse_tot[index_pos, :]

        dist, film_list = distanceKNN.kneighbors(film_select)

        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        # Deletion of the lines of the films already viewed if they appear in the final dataframe
        supp_index = df_select.name
        film_propose2 = film_propose.drop(supp_index, errors='ignore')

    else:

        index_pos = df_clean.index.get_loc(list_film[0])

        # find film index
        df_select = df_clean.iloc[index_pos]

        film_select = sparse_tot[index_pos, :]

        dist, film_list = distanceKNN.kneighbors(film_select)

        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        # Deletion of the lines of the films already viewed if they appear in the final dataframe
        index_pos = df_clean.index.get_indexer(list_film)
        # find film index
        df_select = df_clean.iloc[index_pos]
        supp_index = df_select.index
        film_propose_lastfilm = film_propose.drop(supp_index, errors='ignore').head(2)

        ###################################

        # select other film
        index_pos = df_clean.index.get_indexer(list_film)
        # find film index
        df_select = df_clean.iloc[index_pos]

        film_select = sparse_tot[index_pos, :]

        film_select = film_select.mean(axis=0)

        dist, film_list = distanceKNN.kneighbors(film_select)

        # selection of the list in the list
        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        # Deletion of the lines of the films already viewed if they appear in the final dataframe
        supp_index = df_select.index
        supp_index_temp = film_propose_lastfilm.index
        supp_index = supp_index.union(supp_index_temp, sort=None)
        film_propose2 = film_propose.drop(supp_index, errors='ignore')

        film_propose2 = pd.concat([film_propose_lastfilm, film_propose2.head(3)])

    return film_propose2


"""
def IA(list_film, scaler, distanceKNN, df_clean, df_IA):
    if len(list_film) == 1:

        index_pos = df_clean.index.get_loc(list_film[0])
        # find film index
        df_select = df_IA.iloc[index_pos]

        # switch to dataframe
        df_select = df_select.to_frame()
        df_select = df_select.T

        X2 = df_select.drop(["originalTitle", "title_fr"], axis=1)
        X2_stand = scaler.transform(X2)

        X2_stand = pd.DataFrame(X2_stand, index=X2.index, columns=scaler.get_feature_names_out())
        X2_stand = weight(X2_stand)

        dist, film_list = distanceKNN.kneighbors(X2_stand)
        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        supp_index = df_select.index
        film_propose2 = film_propose.drop(supp_index)

    else:
        # select in function the last film view
        index_pos = df_clean.index.get_loc(list_film[0])
        # find film index
        df_select = df_IA.iloc[index_pos]

        # switch to dataframe
        df_select = df_select.to_frame()
        df_select = df_select.T

        X2 = df_select.drop(["originalTitle", "title_fr"], axis=1)
        X2_stand = scaler.transform(X2)

        X2_stand = pd.DataFrame(X2_stand, index=X2.index, columns=scaler.get_feature_names_out())
        X2_stand = weight(X2_stand)

        dist, film_list = distanceKNN.kneighbors(X2_stand)
        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        supp_index = df_select.index
        film_propose_lastfilm = film_propose.drop(supp_index).head(2)

        # select other film
        index_pos = df_clean.index.get_indexer(list_film)
        # find film index
        df_select = df_IA.iloc[index_pos]

        X2 = df_select.drop(["originalTitle", "title_fr"], axis=1)

        # standardization of film characteristics and switch to dataframe
        X2_stand = scaler.transform(X2)
        X2_stand = pd.DataFrame(X2_stand, index=X2.index, columns=scaler.get_feature_names_out())
        X2_stand = weight(X2_stand)

        # average of the characteristics of the films already viewed
        X2_stand = X2_stand.mean(axis=0)

        # switch to dataframe
        X2_stand = X2_stand.to_frame()
        X2_stand = X2_stand.T

        dist, film_list = distanceKNN.kneighbors(X2_stand)

        # selection of the list in the list
        film_list = film_list.tolist()
        A = film_list[0]
        film_propose = df_clean.iloc[A]

        # Deletion of the lines of the films already viewed if they appear in the final dataframe
        supp_index = df_select.index
        supp_index_temp = film_propose_lastfilm.index
        supp_index = supp_index.union(supp_index_temp, sort=None)
        film_propose2 = film_propose.drop(supp_index, errors='ignore')

        film_propose2 = pd.concat([film_propose_lastfilm, film_propose2.head(3)])

    return film_propose2
"""


def print_film_list(df, film_list):
    """
    plot list of selected film in the sidebar
    :param df: dataframe
    :param film_list: list
    """
    with st.sidebar:
        st.title("**Dernier(s) film(s) vu(s) :**")
        num = 1
        for i_film in film_list:
            title_fr = df.loc[i_film, "title_fr"]
            st.write(str(num), ".  ", title_fr)
            num += 1


def savelist(df, text, film_list, user, load_tab):
    """
    save list of selected film
    :param df: dataframe
    :param text: str
    :param film_list: list
    :param user: str
    :param load_tab: bool
    :return: list, bool
    """
    film_list.insert(0, text)

    if len(film_list) > 9:
        film_list = film_list[:10]

    with open(user, 'wb') as file:
        # A new file will be created
        pickle.dump(film_list, file)

    load_tab = False

    return film_list, load_tab


def expander_func(df_temp, df_clean, key: str, film_list, user, load_tab):
    """
    plot the expander with the all the film informations
    :param df_temp:  dataframe
    :param df_clean: dataframe
    :param key:  str
    :param film_list: list
    :param user:  str
    :param load_tab:  bool
    :return: list,bool
    """
    global text_search
    text_vu = ""
    with st.expander(df_temp["title_fr"]):
        # 3 columns creation
        col1, col_b, col2 = st.columns([2, 1, 2])

        with col1:

            # scrap the url film to obtain film picture and resume text
            try:
                url_film, text_resume = ws.find_picture(df_temp.name)
                st.image(url_film)

            except:
                text_resume = ""

        with col2:
            # plot important information of the film contain in the dataframe
            st.write("**Année :**", df_temp["startYear"])
            st.write("**Genre :**", ', '.join(df_temp["genres"]))
            st.write("**Note :**", df_temp["averageRating"])
            st.write("**Durée :**", df_temp["runtimeMinutes"])
            st.write("**Nombre de vue :**", df_temp["numVotes"])
            st.write("**réalisateur(s) :**", ', '.join(df_temp["directors"]))
            st.write("**Liste des acteurs :**", ', '.join(df_temp["Actors_name"]))

            # button to add the film in the selection
            if st.button('voir', key=key):
                st.write(df_temp.name)
                text_vu = df_temp.name
                film_list, load_tab = savelist(df_clean, text_vu, film_list, user, load_tab)
                pyautogui.hotkey("ctrl", "F5")

        st.write("**resumé :**", text_resume)

    return film_list, load_tab
