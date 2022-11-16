import function as fct
import pickle


def table_cleaning():
    """
    load the dataframe "title_ranking",
    clean it and save the clean dataframe
    """
    # load the dataframe
    url_title = "https://datasets.imdbws.com/title.ratings.tsv.gz"
    df = fct.load_database(url_title, 0, 'tconst')

    df_title_ratings = df.copy()

    # save the dataframe
    with open('df_title_ratings.pkl', 'wb') as file:
        # A new file will be created
        pickle.dump(df_title_ratings, file)


    print("title ranking is cleaned")
