import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=*******")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE country_weekly(
        country_name VARCHAR(50) NOT NULL,
        country_iso2 VARCHAR(20) NOT NULL,
        week DATE,
        category VARCHAR(20),
        weekly_rank INTEGER,
        show_title VARCHAR(200),
        season_title VARCHAR(200),
        cumulative_weeks_in_top_10 INTEGER
    )
""")
conn.commit()

