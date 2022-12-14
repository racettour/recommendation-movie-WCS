import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer


def load_database(url_name : str, n_rows : int, index_name : str) -> pd.DataFrame:
    """
    load the database. if n_rows = 0 all the database is loaded. else, the indicated number of rows is loaded
    :param url_name : 
    :param n_rows: 
    :param index_name: 
    :return: dataframe
    """
    if n_rows == 0:
        df = pd.read_csv(url_name, sep='\t', index_col=index_name, low_memory=False)
    else:
        df = pd.read_csv(url_name, sep='\t', nrows=n_rows, index_col=index_name, low_memory=False)
    return df


def select_col(df: pd.DataFrame, list_col_name: list) -> pd.DataFrame:
    """
    select col_name column in df
    :param df: dataframe
    :param list_col_name: list
    :return: dataframe
    """
    df2 = df[list_col_name]
    return df2


def count_col_val(df: pd.DataFrame, col_cont: str) -> pd.DataFrame:
    """
    count the different values in col_cont column of the dataframe df
    :param df: dataframe
    :param col_cont:
    :return: dataframe
    """
    df2: pd.Series = df.groupby(col_cont)[col_cont].count().sort_index()
    df2 = df2.to_frame()
    return df2


def convert_col(table_name, columns_name, convert_type):
    '''
    Convert the type of columns_name of DataFrame
    :param table_name: Name_of_the_DataFrame
    :param columns_name: Name_of_column_to_convert
    :param convert_type: Type_of_conversion
    :return: The_converted_DataFrame
    '''
    try:
        if convert_type == 'list':
            table_name2 = table_name.astype({columns_name: 'string'})
            table_name2[columns_name] = table_name2[columns_name].str.split(',')
        elif convert_type == 'bool':
            table_name2 = table_name.astype({columns_name: 'int'})
            table_name2 = table_name2.astype({columns_name: convert_type})
        elif convert_type == 'datetime64[ns]':
            table_name2 = table_name.copy()
            table_name2[columns_name] = pd.to_datetime(table_name2[columns_name], format = '%Y')
        else:
            table_name2 = table_name.astype({columns_name: convert_type})

    except ValueError:
        if (convert_type == 'float') or (convert_type == 'int'):
            dec_value =  table_name[columns_name].str.isdecimal()

            table_name[dec_value == False] = np.nan
            table_name2 = table_name.astype({columns_name: convert_type})

        else:
            table_name2 = table_name

    else:
        print(columns_name, 'conversion ')

    return table_name2


def replace_n_to_nan(table_name, parameter_to_replace):
    """
   select the table to replace a parameter by Nan
    :param table_name: DataFrame
    :param parameter_to_replace: str, date, int, float, objet, bool,
    :return: DataFrame
    """
    table_name = table_name.replace(to_replace=parameter_to_replace, value=np.NaN)
    return table_name


def count_value(df, col_name):
    """
     identifies valuers, rendering them unique and counting their occurrences
    :param df: dataframe
    :param col_name: str
    :return: dataframe
    """

    df2 = df[col_name].value_counts(dropna=False)
    df2 = df2.to_frame()
    df2 = df2.sort_values(by=col_name, ascending=False)

    return df2


def count_index(df):
    """
     identifies valuers, rendering them unique and counting their occurrences
    :param df: dataframe
    :return: dataframe
    """

    df2 = df.index.value_counts()
    df2 = df2.to_frame()
    df2 = df2.sort_values(by=df2.columns[0], ascending=False)

    return df2


def drop_rep_val(df, list_col):
    """
    drop line if value is repeted and keep the last one
    :param df: dataframe
    :param list_col: list
    :return: dataframe
    """
    for i_col in list_col:
        df = df.drop_duplicates(subset=[i_col],keep='last')
    return df


def plot_boxplot(df, list_col, nb_line, nb_col):
    """
    plot boxplot of all  dataframe columns in subplot graphic
    :param df: dataframe
    :param nb_line: int
    :param nb_col: int
    :return: none
    """
    fig, ax = plt.subplots(nb_line, nb_col, figsize=(20, 15))

    i_line = 0
    i_col = 0
    for i_c in list_col:
        sns.boxplot(data=df,
                    x=i_c,
                    ax=ax[i_line, i_col])
        i_line += 1
        if i_line >= nb_line:
            i_line = 0
            i_col += 1

    return


def drop_outliers(df, col_name):
    """
    drop line with outliers of the selected columns list
    :param df: dataframe
    :param col_name: str
    :return: dataframe
    """

    for i_col in col_name:
        Q1 = df[i_col].quantile(0.25)
        Q3 = df[i_col].quantile(0.75)
        IQR = Q3 - Q1  # IQR is interquartile range.

        filter = (df[i_col] >= Q1 - 1.5 * IQR) & (df[i_col] <= Q3 + 1.5 * IQR)

        q_low = df[i_col].quantile(0.02)
        q_hi = df[i_col].quantile(0.98)

        df_filtered = df[filter]

    return df_filtered


def replace_values(df, col_name, init_value, replaced_value):
    """
    replace an init_value of a column of a dataframe by the replaced_value
    :param df: dataframe
    :param col_name: str
    :param init_value: int|str|list
    :param replaced_value: int|str|list
    :return: dataframe
    """
    df[col_name] = df[col_name].replace(init_value, replaced_value)
    return df


def replace_nan(df, col_name, replaced_value):
    """
    replace nan of a column of a dataframe by the replaced_value
    :param df: dataframe
    :param col_name: str
    :param replaced_value: int|str|list
    :return: dataframe
    """
    df[col_name] = df[col_name].fillna(replaced_value)
    return df


def delete_duplicate_index(df):
    """
    delete duplicated index
    :param df: dataframe
    :return: dataframe without duplicates
    """
    idx = np.unique(df.index.values, return_index=True)[1]
    df = df.iloc[idx]
    return df


def plot_nan_prop(df, col_name):
    """
    display a pie chart with Nan and field values in %
    :param df: dataframe
    :param col_name: str
    :return: nons
    """
    NumberNaN = df[col_name].isna().sum()
    Filled_field = df[col_name].count()
    data = [NumberNaN, Filled_field]
    fig, ax = plt.subplots(figsize=(10, 10))
    explode = [0.02, 0.02]
    labels = ['NaN', 'Field filled']
    colors = sns.color_palette('bright')
    Text_Title = "% du nombre de NaN dans la colonne " + col_name
    plt.title(Text_Title, fontdict = {'fontsize' : 25})
    plt.pie(data, labels=labels, colors=colors, autopct='%0.0f%%', explode=explode, textprops={'fontsize': 25})



def listTostr(list1):
    """
    convert list to str
    :param list1: list
    :return: str
    """
    str1 = " "
    return str1.join(list1)


def convert_Tfi(df, col):
    """
    apply TfidfVectorizer to a column of a dataframe
    :param df: dataframe
    :param col: str
    :return:
    """
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

def convert_Tfi_sparse(df,col):
    """
    apply TfidfVectorizer to a column of a dataframe. the function return the sparse marix
    :param df: dataframe
    :param col: str
    :return: sparse matrix
    """

    tfi = TfidfVectorizer()
    sparse = tfi.fit_transform(df[col])

    col_name = tfi.get_feature_names_out()
    ind_name = df.index.values

    return sparse, col_name, ind_name

