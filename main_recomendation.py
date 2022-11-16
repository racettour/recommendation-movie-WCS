import pickle
import function as fct
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

def listTostr(list1):
    str1 = " "
    return str1.join(list1)

def convert_Tfi(df, col):

    tfi = TfidfVectorizer()
    word_vector = tfi.fit_transform(df[col])

    # place tf-idf values in a pandas data frame
    df_temp2 = pd.DataFrame(word_vector.todense(),
                            columns=tfi.get_feature_names(),
                            index= df.index.values)

    # merge df_temp2 with df
    df = df.merge(df_temp2, left_index=True, right_index=True, how ="left")

    # drop the columns
    df = df.drop(col, axis = 1)

    return df

def convert_ord(df, col):
    val_cal = df[col].unique()

    orderencod = OrdinalEncoder(sparse=False, categories=[val_cal], drop = np.zeros(1,len(val_cal)))
    df[col] = orderencod.fit_transform(df[[col]])

    return df




with open('df_clean.pkl', 'rb') as file:
    # Call load method to deserialze
    df = pickle.load(file)

# convert startYear type  to int
df['startYear'] = df['startYear'].dt.strftime('%Y').astype(int)


df["genres"] = df["genres"].apply(lambda x: listTostr(x))
df = convert_Tfi(df, "genres")
df=df.drop(["fi", "film"], axis=1)
df=df.rename(columns={"sci": "sci_fi", "noir": "film noir"})

#df["Actors_name"] = df["Actors_name"].apply(lambda x: listTostr(x))

col = "directors"
df["directors"] = df["directors"].apply(lambda x: listTostr(x))

df = convert_ord(df, col)

col = "Actors_name"
df[col] = df[col].apply(lambda x: listTostr(x))
df = convert_ord(df, col)



df = df[~df.index.duplicated(keep='first')]





# ===================================================================================
# select data for trainning
X = df.select_dtypes("number")
scaler = StandardScaler()
scaler.fit(X)
X_stand = scaler.transform(X)
X_stand= pd.DataFrame(X_stand, index=X.index, columns=scaler.get_feature_names_out())
# initialize the model
distanceKNN = NearestNeighbors(n_neighbors=3).fit(X_stand)

# find film index
name_film = "Déconnecté"
df_entre = df.iloc[np.where(df["title_fr"].str.contains(name_film))]

# find film index
df_select = df_entre.iloc[0]

# remise de df_select en dataframe
df_select = df_select.to_frame()
df_select = df_select.T

X2 = df_select. drop(["originalTitle", "title_fr"], axis=1)
X2_stand = scaler.transform(X2)


X2_stand= pd.DataFrame(X2_stand, index=X2.index, columns=scaler.get_feature_names_out())


dist, film_list= distanceKNN.kneighbors(X2_stand)
film_list = film_list.tolist()
A= film_list[0]
film_propose = df.iloc[A]

supp_index=df_select.index
film_propose2 = film_propose.drop(supp_index)
print("fini")



