import pathlib
import sqlite3
import psycopg2
import pandas as pd


DB_FILE = pathlib.Path(__file__).resolve().parent.joinpath("wind-data.db").resolve()


def get_wind_data(start, end):
    """
    Query wind data rows between two ranges

    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    """

    #con = sqlite3.connect(str(DB_FILE))
    #statement = f'SELECT Speed, SpeedError, Direction FROM Wind WHERE rowid > "{start}" AND rowid <= "{end}";'
    #df = pd.read_sql_query(statement, con)
    #return df
    #start = 1592528600738
    #end = 1592529478045
    con = psycopg2.connect("host=34.232.62.35 dbname=postgres user=db_select password=<setpassword>")
    statement = f"SELECT pmr FROM price_metcalfe_ratio WHERE timestamp > '{start}' AND timestamp <= '{end}';"
    df = pd.read_sql_query(statement, con)
    return df


def get_wind_data_by_id(id):
    """
    Query a row from the Wind Table

    :params id: a row id
    :returns: pandas dataframe object
    """

    con = sqlite3.connect(str(DB_FILE))
    statement = f'SELECT * FROM Wind WHERE rowid = "{id}";'
    df = pd.read_sql_query(statement, con)
    return df
