import os
import psycopg2
import pandas as pd 
import numpy as np 
import psycopg2.extras as extras
from io import StringIO
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Waj62mWaj62m")
cur = conn.cursor()

country_df = pd.read_csv('du_poc/country_weekly.csv', encoding='unicode_escape')

def execute_values(conn, df, table):
    """
    Using psycopg2.extras.execute_values() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = [tuple(x) for x in df.to_numpy()]
    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL quert to execute
    query  = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("execute_values() done")
    cursor.close()

execute_values(conn, country_df, "country_weekly")
