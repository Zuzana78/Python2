import requests
import pandas
import numpy


with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
    open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)

swing_states = pandas.read_csv("1976-2020-president.csv")

swing_states["rank"] = swing_states.groupby(["year", "state"])["candidatevotes"].rank(ascending=False)
swing_states = swing_states.loc[(swing_states["rank"] == 1)]
swing_sorted = swing_states.sort_values(["state", "year"])
swing_sorted["previous_simplified"] = swing_sorted["party_simplified"].shift(-1)
swing_sorted["comparison"] = numpy.where(swing_sorted["party_simplified"] == swing_sorted["previous_simplified"],0,1)
swing_sorted = swing_sorted.groupby("state")["comparison"].sum().sort_values(ascending=False)

print(swing_sorted)

