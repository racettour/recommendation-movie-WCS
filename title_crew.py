import matplotlib.pyplot as plt
import function as fct
import pickle


def table_cleaning():
    """
    load the dataframe "title_crews",
    clean it and save the clean dataframe
    """
    print("title_crew cleaning...")
    print("=" * 30)
    # Dataframe loading
    url_title_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
    df_title_crew = fct.load_database(url_title_crew, 0, 'tconst')

    # ======================================================================================
    # \\N replacement by NaN
    value_to_replace = chr(92) + "N"
    df_title_crew = fct.replace_n_to_nan(df_title_crew, value_to_replace)

    # ======================================================================================
    # Convert types of dataframe's columns
    columns_name = df_title_crew.columns.values
    type_conv = ["list", "list"]

    for pos in range(len(type_conv)):
        df_title_crew = fct.convert_col(df_title_crew, columns_name[pos], type_conv[pos])


    df_title_crew = df_title_crew["directors"]


    with open('df_title_crew.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_title_crew, file)

    print("=" * 30)
    print("title_crew cleaned and saved...")
