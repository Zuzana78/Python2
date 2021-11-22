import pandas
import requests
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

psenice = pandas.read_csv("psenice.csv")

#H0: Prumerna delka zrn psenice je stejna pro obe odrudy.
#H1: Prurerna delka zrn odrudy Rosa je mensi nez prumerna delka zrn odrudy Canadian.

x = psenice["Rosa"]
y = psenice["Canadian"]
print(mannwhitneyu(x, y, alternative="less"))

#Zaver je, ze p-hodnota je vetsi nez hladina vyznamnosti, tudiz nulovou hypotezu nezamitame.