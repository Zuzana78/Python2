import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

df_london = pandas.read_csv("london_merged.csv")
df_london["timestamp"] = pandas.to_datetime(df_london["timestamp"])
df_london["year"] = df_london["timestamp"].dt.year

df_london_pivot = pandas.pivot_table(df_london, values="cnt", index="weather_code", columns="year", aggfunc=numpy.sum, margins=True)

print(df_london_pivot)
