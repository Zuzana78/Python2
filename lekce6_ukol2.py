import requests
import pandas
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

air_polution = pandas.read_csv("air_polution_ukol.csv")
air_polution["date_converted"] = pandas.to_datetime(air_polution["date"])

#H0: Prumerne mnozstvi jemnych castic je stejna pro oba mesice.
#H1: Prurerne mnozstvi jemnych castic je ruzne pro oba mesice.

x = air_polution[air_polution["date_converted"].dt.strftime('%Y-%m') == '2019-01']["pm25"]
y = air_polution[air_polution["date_converted"].dt.strftime('%Y-%m') == '2020-01']["pm25"]

print(mannwhitneyu(x, y))

#Zaver je, ze p-hodnota je vetsi nez hladina vyznamnosti, tudiz nulovou hypotezu nezamitame.



