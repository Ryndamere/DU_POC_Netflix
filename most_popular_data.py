import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=******")
cur = conn.cursor()
""" connect to postgres and load the csv file into the database """ 
with open('du_poc/most_popular.csv', 'r') as f:
    next(f)
    cur.copy_from(f,'most_popular', sep=',')
conn.commit()
