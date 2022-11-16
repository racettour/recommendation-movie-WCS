import pandas as pd
import function as fct
import pickle
pd.options.mode.chained_assignment = None  # default='warn'

def table_cleaning():
    """
    load the dataframe "title_cleaning",
    clean it and save the clean dataframe
    """
    # load the dataframe
    print('loading df')
    url_title_principals = "https://datasets.imdbws.com/title.principals.tsv.gz"
    df = pd.read_csv(url_title_principals, sep='\t', index_col='tconst',
                     low_memory=True, chunksize=300000)
    #df = fct.load_database(url_title_principals, 0, 'tconst')

    # variable loading
    with open('IndexSelect.pkl', 'rb') as file:
        # Call load method to deserialze
        Index = pickle.load(file)


    print('=' * 30)

    print('select lines')
    df_title_principals = pd.DataFrame()

    for i_df in df:
        toto = list(set(i_df.index).intersection(Index))
        if len(toto) != 0:
            df_temp = i_df.loc[toto]
            df_title_principals = pd.concat([df_title_principals, df_temp])

    del df

    #===========================================================================================
    # drop column "characters" and "ordering"
    print('loading df')
    df_title_principals = df_title_principals.drop(columns=["characters"])
    df_title_principals = df_title_principals.drop(columns=["ordering"])
    df_title_principals = df_title_principals.drop(columns=["job"])

    #===========================================================================================
    print('Nan transformation')
    # \N and/or \\N replacement by NaN
    value_to_replace = chr(92) + "N"
    df_title_principals = fct.replace_n_to_nan(df_title_principals, value_to_replace)

    value_to_replace2 = chr(92) + chr(92) + "N"
    df_title_principals = fct.replace_n_to_nan(df_title_principals, value_to_replace2)

    #===========================================================================================
    # Keep actors and actress in "category"
    print('select actors and actress')
    df_test = df_title_principals.loc[df_title_principals['category'] == 'actor']
    df_test1 = df_title_principals.loc[df_title_principals['category'] == 'actress']
    df_title_principals = pd.concat([df_test, df_test1])

    #===========================================================================================
    # Convert types of dataframe's columns
    columns_name = df_title_principals.columns.values
    type_conv = ["string", "string"]

    for pos in range(len(type_conv)):
        df_title_principals = fct.convert_col(df_title_principals, columns_name[pos], type_conv[pos])


    #===========================================================================================

    with open('df_title_principals.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_title_principals, file)
