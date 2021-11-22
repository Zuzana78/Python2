import pandas
import requests
import statistics

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

kryptomeny = pandas.read_csv("crypto_prices.csv")
kryptomeny = kryptomeny.loc[kryptomeny["Name"] == "Bitcoin"]
kryptomeny = kryptomeny["Close"].pct_change()+1
kryptomeny_list = kryptomeny.tolist()[1:]

print(statistics.geometric_mean(kryptomeny_list))


