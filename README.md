# DU_POC_Netflix
A Proof of concept for DU that uses a Kaggle dataset and to be visualized to be presented.


## Data Profiling

The data was imported from CP-1252 to UTF-8 and has corrupted some of the foreign characters in the movies that com from Netflix. We made the mistake of manually chaning this data to similar english character in excel.

Most of the data is text strings so no quantitfing way to show the amount of show titles.

about 50% of the show season_title will be blank. Becuase it is comparing top 10 Tv shows and Movies and movies don't have season_title.

```python
country_df = pd.read_csv('country_weekly.csv', encoding='unicode_escape')
country_df_clean = country_df.drop(["country_iso2", "cumulative_weeks_in_top_10"], axis=1)
print(country_df.describe())
```
|Calculations|weekly_rank | cumulative_weeks_in_top_10|
|:---|---:|---:|
|count | 60160.000000       |        60160.000000|
|mean  |    5.500000        |           3.000066|
|std   |    2.872305        |           3.599029|
|min   |    1.000000        |           1.000000|
|25%   |    3.000000        |           1.000000|
|50%   |    5.500000        |           2.000000|
|75%   |    8.000000        |           3.000000|
|max   |   10.000000        |          32.000000|

```python
print(country_df_clean.value_counts(country_df_clean["show_title"]))
```
|Show_Title|Count of each Show Title|
| :--- | ---: |
|Money Heist | 1574|
|The Good Doctor | 1498|
|Squid Game | 1187|
|You | 950|
|The Witcher | 879|
| | ...|
|Ip Man | 1|
|The 40-Year-Old Virgin | 1|
|Iron Man | 1|
|It | 1|
|Solomon Kane | 1|
Length 2156, dtype: int64

```python
print(country_df_clean.nunique(axis=0))
```
|Column|Count of Entries|
|:---|---:|
|country_name|94|
|week | 32|
|category | 2|
|weekly_rank | 10|
|show_title | 2156|
|season_title | 692|
dtype: int64


