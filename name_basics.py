import pandas as pd
import matplotlib.pyplot as plt
import function as fct
import seaborn as sns
import numpy as np
import pickle

pd.options.mode.chained_assignment = None  # default='warn


def table_cleaning():
    """
    load the dataframe "name_basics",
    clean it and save the clean dataframe
    """

    # Dataframe loading
    print('loading df')
    url_name_basics = "https://datasets.imdbws.com/name.basics.tsv.gz"
    df_cleaning = fct.load_database(url_name_basics, 0, 'nconst')

    print('cleaning df')
    # deleted column "knownForTitles", "birthYear", "primaryProfession"
    df_cleaning = df_cleaning.drop(["knownForTitles",
                                    "birthYear",
                                    "primaryProfession"], axis=1)


    # replace values /N and //N by Nan
    value_to_replace = chr(92) + "N"
    df_cleaning = fct.replace_n_to_nan(df_cleaning, value_to_replace)

    value_to_replace2 = chr(92) + chr(92) + "N"
    df_cleaning = fct.replace_n_to_nan(df_cleaning, value_to_replace)

    # Convert types of dataframe's columns
    print('columns conversion... ')
    columns_name = df_cleaning.columns.values
    type_conv = ["string", "float"]

    for pos in range(len(type_conv)):
        df_cleaning = fct.convert_col(df_cleaning, columns_name[pos], type_conv[pos])

    print('=' * 30)

    # deleted duplicates in index
    idx = np.unique(df_cleaning.index.values, return_index=True)[1]
    df_cleaning = df_cleaning.iloc[idx]

    # select row with Nan in the columns "deathYear"
    df_test_with_nan = df_cleaning[(df_cleaning["deathYear"].isnull())]

    # CLEANING df_cleaning with a condition
    # delete row where deathYear before 1945
    died_too_soon = 1945
    df_test = df_cleaning[(df_cleaning["deathYear"] > died_too_soon)]

    print('=' * 30)

    # concatenation df_test and df_test_with_nan]
    df_cleaning = pd.concat([df_test, df_test_with_nan])


    # concatenation df_select
    df_cleaning = df_cleaning["primaryName"]
    df_cleaning = df_cleaning.to_frame()

    df_name_basics = df_cleaning.copy()

    with open('df_name_basics.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_name_basics, file)

    print("name_basics is cleaned")
