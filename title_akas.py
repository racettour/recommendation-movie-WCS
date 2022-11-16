import pandas as pd
import function as fct
import pickle
import numpy as np


def table_cleaning():
    """
    load the dataframe "title_akas",
    clean it and save the clean dataframe
    """
    pd.options.mode.chained_assignment = None  # default='warn'

    # index loading
    with open('IndexSelect.pkl', 'rb') as file:
        # Call load method to deserialze
        IndexSelect = pickle.load(file)


    # Dataframe loading
    url_title_basics = "https://datasets.imdbws.com/title.akas.tsv.gz"
    #df = fct.load_database(url_title_basics, 1000, 'titleId')

    df_title = pd.DataFrame()

    print('loading df')
    df = pd.read_csv(url_title_basics, sep='\t', index_col='titleId', low_memory=False, chunksize=100000)

    print('select lines')
    for i_df in df:
        toto = list(set(i_df.index).intersection(IndexSelect))
        if len(toto) != 0:
            df_temp = i_df.loc[toto]
            df_title = pd.concat([df_title, df_temp])

    del df

    #df_title = df.copy()

    # =====================================================================================================
    # there are not enouth information in "language", "types" and "attridutes". the columns are directly dropped
    df_title.drop(['types', 'attributes', 'language'], axis=1, inplace=True)
    columns_name = df_title.columns.values

    # =====================================================================================================
    # df study
    df_title.info()
    print('=' * 30)

    # compt and class values repetition
    for i_col in columns_name:
        df = fct.count_value(df_title, i_col)
        print(df)
        print('=' * 30)

    # ======================================================================================================
    # \N and/or \\N replacement by NaN
    print('Nan transformation')


    value_to_replace = chr(92) + "N"
    df_title = fct.replace_n_to_nan(df_title, value_to_replace)

    value_to_replace2 = chr(92) + chr(92) + "N"
    df_title = fct.replace_n_to_nan(df_title, value_to_replace2)

    # ======================================================================================================
    # Convert types of dataframe's columns
    columns_name = df_title.columns.values
    type_conv = ["int", "string", "string", "bool"]

    for pos in range(len(type_conv)):
        df_title = fct.convert_col(df_title, columns_name[pos], type_conv[pos])

    print(df_title.dtypes)
    print('=' * 30)

    # ======================================================================================================
    df_FR = df_title[df_title['region'] == "FR"]
    index_fr = df_FR.index
    df_title2 = df_title.loc[index_fr]


    # select original titles in a new df
    print("finding original region")
    """
    df_org =df_title[df_title['isOriginalTitle'] == True]
    # select no original titles in a new df
    df_no_org =df_title[df_title['isOriginalTitle'] == False]

    # find the intercection film nama in the 2 df and their positions
    titles, org_ind, no_org_ind = np.intersect1d(df_org['title'], df_no_org['title'], return_indices=True)

    # get the region of the films thanks df_no_org
    org_country = df_no_org.iloc[no_org_ind]['region']

    # past the region in df_org
    df_org.drop("region", axis = 1, inplace=True)
    df_org =df_org.merge(org_country, how='left',  left_index=True, right_index=True, sort=True)
    """

    # ======================================================================================================
    # select no original titles in a new df

    df_FR.drop(['ordering','isOriginalTitle'], axis=1, inplace=True)


    print("finding number of language")
    # creation of 2 df : the first one contains the number of language available by movie index
    df2 = df_title2.groupby([df_title2.index])['region'].count()
    df2 = df2.to_frame()
    df2 = df2.rename(columns={'region': 'language number'})  # old method

    df_FR =df_FR.merge(df2, how='left',  left_index=True, right_index=True, sort=True)

    df_FR['region'] = df_FR['region'].replace(np.nan, "no def")
    df_FR['language number'] = df_FR['language number'].replace(np.nan, 1)
    df_FR['language number'] = df_FR['language number'].replace(0, 1)



    with open('df_akas.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_FR, file)
    # they are merge in df_title_clean
    print("title akas is cleaned")

