import requests
import pandas
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

ryby = pandas.read_csv("Fish.csv")

prumery = ryby.groupby("Species")["Weight"].mean()
ryby["ryby_prumerna_vaha"] = ryby["Species"].map(prumery)

mod = smf.ols(formula="Weight ~ Length2 + Height + ryby_prumerna_vaha", data=ryby)
res = mod.fit()
print(res.summary())

#bez parametru vahy ryby byl koeficient determinace 0,84, po pridani parametru vahy se koeficient zvysil na 0,875. Model je tedy presnejsi
#po pridani druhy ryby se model zpresnil na 0.90

