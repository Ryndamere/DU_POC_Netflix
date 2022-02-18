import psycopg2
import pandas as pd 
import csv 
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Waj62mWaj62m")
cur = conn.cursor()

country_df = pd.read_csv('du_poc/country_weekly.csv', encoding='unicode_escape')
 
country_df['show_title'] = country_df['show_title'].str.replace(',','')
country_df['season_title'] = country_df['season_title'].str.replace(',','')

country_df.to_csv('C:/Users/MLJ1029/DU_POC/country_df.csv')