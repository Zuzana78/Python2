import pandas
import requests
import seaborn
import matplotlib.pyplot as plt
import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)

kryptomeny = pandas.read_csv("crypto_prices.csv")
kryptomeny["pct_zmena"] = kryptomeny.groupby(["Name"]).shift(-1)["Close"].pct_change()

kryptomeny_pivot = kryptomeny.pivot('Date','Name','pct_zmena').reset_index()

kryptomeny_pivot = kryptomeny_pivot.corr()

kryptomeny_pivot = kryptomeny_pivot.unstack().sort_values()

pandas.set_option('display.max_rows', None)
print(kryptomeny_pivot)

seaborn.jointplot("XRP", "Wrapped Bitcoin", kryptomeny_pivot, kind='scatter', color='red')
seaborn.jointplot("Aave", "Uniswap", kryptomeny_pivot, kind='scatter', color='blue')
plt.show()
