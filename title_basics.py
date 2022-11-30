import matplotlib.pyplot as plt
import function as fct
import pickle
import pandas as pd


def table_cleaning():
    """
    load the dataframe "title_basics",
    clean it and save the clean dataframe
    """

    # Dataframe loading
    print("df loading...")
    url_title_basics = "https://datasets.imdbws.com/title.basics.tsv.gz"
    df = fct.load_database(url_title_basics, 0, 'tconst')
    df_title_basics = df.copy()

    # apply a first filter
    print("filter applying...")
    df_title_basics = df_title_basics[df_title_basics['isAdult'] == '0']
    df_title_basics = df_title_basics[df_title_basics['titleType'] == 'movie']
    supp_adult = df_title_basics[df_title_basics['genres'].str.contains("Adult")].index
    df_title_basics.drop(index =supp_adult,  inplace=True )
    # ======================================================================================================
    # \N and/or \\N replacement by NaN
    value_to_replace = chr(92) + "N"
    df_title_basics = fct.replace_n_to_nan(df_title_basics, value_to_replace)

    value_to_replace2 = chr(92) + chr(92) + "N"
    df_title_basics = fct.replace_n_to_nan(df_title_basics, value_to_replace2)

    # ======================================================================================================
    # Convert types of dataframe's columns
    print('columns conversion... ')
    columns_name = df_title_basics.columns.values
    type_conv = ["string", "string", "string", "bool", "datetime64[ns]", "datetime64[ns]", "float", "list"]

    for pos in range(len(type_conv)):
        df_title_basics = fct.convert_col(df_title_basics, columns_name[pos], type_conv[pos])

    # ======================================================================================================
    # drop columns that not interest us anymore
    df_title_basics.drop(['endYear', 'isAdult', 'primaryTitle', 'titleType'], axis=1, inplace=True)
    columns_name = df_title_basics.columns.values

    # apply a second filter on the realise year
    mask = (df_title_basics['startYear'] > '1945-1-1') & (df_title_basics['startYear'] <= '2022-1-1')
    df_title_basics = df_title_basics.loc[mask]

    # ======================================================================================================
    # drop duplicate lines
    #df_title_basics.drop_duplicates(keep=False, inplace=True)



    # ======================================================================================================
    # replace nan value by the chosen value: here it is the median
    df2 = df_title_basics['startYear'].value_counts(dropna=False)
    year_values = df2.index

    for i_year in year_values:
        # select i_year line
        df3 = df_title_basics[df_title_basics['startYear'].values == i_year]
        # calculate the runtime median of i_year
        replaced_value = df3['runtimeMinutes'].median()
        # replace nan by replaced_value
        df_title_basics.loc[df3.index] = fct.replace_nan(df_title_basics.loc[df3.index],
                                                         'runtimeMinutes',
                                                         replaced_value)

    # ======================================================================================================
    # runtime filter
    df_title_basics = df_title_basics[df_title_basics['runtimeMinutes'] >= 60]
    df_title_basics = df_title_basics[df_title_basics['runtimeMinutes'] <= 240]

    # select and save index_value to filter the other table
    print("save values...")
    index_select = df_title_basics.index
    with open('IndexSelect.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(index_select, file)

    # select and save df_title_basics
    with open('df_title_basics.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_title_basics, file)

    print("title basics is cleaned")


table_cleaning()