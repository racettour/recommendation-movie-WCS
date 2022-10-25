import pandas as pd


def load_database(url_name, n_rows, index_name):
    if n_rows == 0:
        df = pd.read_csv(url_name, sep='\t', index_col=index_name)
    else:
        df = pd.read_csv(url_name, sep='\t', nrows=n_rows, index_col=index_name)
    return df


def select_col(df, list_col_name):
    df2 = df[list_col_name]
    return df2


def count_col_val(df: pd.DataFrame, col_cont: str) -> pd.DataFrame:
    df2: pd.Series = df.groupby(col_cont)[col_cont].count().sort_index()
    df2 = df2.to_frame()
    return df2
