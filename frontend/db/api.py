import pathlib
import psycopg2
import pandas as pd

def get_wind_data(start, end):
    """
    Query PMR data iniitally between two ranges

    :params start: start row id
    :params end: end row id
    :returns: pandas dataframe object
    """

    start = 1592528600738
    #end = 1592529478045
    con = psycopg2.connect("host=34.232.62.35 dbname=postgres user=db_select password=<setpassword>")
    statement = f"SELECT pmr FROM price_metcalfe_ratio WHERE timestamp > '{start}' AND timestamp <= '{end}';"
    df = pd.read_sql_query(statement, con)
    return df
