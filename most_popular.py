import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Waj62mWaj62m")
cur = conn.cursor()
""" connect to postgres and create most_popular table """ 
cur.execute("""
    CREATE TABLE most_popular(
        category VARCHAR(25),
        rank INTEGER,
        show_title VARCHAR(200),
        season_title VARCHAR(200),
        hours_viewed INTEGER
    )
""")
conn.commit()

