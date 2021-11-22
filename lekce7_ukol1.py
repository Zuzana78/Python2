import requests
import pandas
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

cement = pandas.read_csv("Concrete_Data_Yeh.csv")

mod = smf.ols(formula="csMPa ~ cement + slag + flyash + water + superplasticizer "
                      "+ coarseaggregate + fineaggregate + age", data=cement)
res = mod.fit()
print(res.summary())

#print(cement.isna().sum())

seaborn.heatmap(cement.corr(), annot=True, cmap="Blues")
plt.show()

data = pandas.DataFrame({"cement": [446], "slag": [189], "flyash": [141], "water": [162], "superplasticizer": [8],
                         "coarseaggregate": [1047], "fineaggregate": [613], "age": [28],})

print(res.predict(data))

#koeficient determinace je 0,616, coz nam udava, ze bychom mohli urcit s vice nez 61% presnosti kompresni silu betonu
#negativne silu betonu ovlivnuje voda, ma zaporny regresni koeficient
# dle predikce mi vysla sila betonu na 74,69
#take v koleracni matici vysla voda negativne.