import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

df_titanic = pandas.read_csv("titanic.csv")
df_titanic_pivot = pandas.pivot_table(df_titanic, values="Survived", index="Pclass", columns="Sex", aggfunc=numpy.sum, margins=True)
#pandas.set_option('display.max_columns', None)
print(df_titanic_pivot)

