import pandas
import requests
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_plan.csv")
open("sales_plan.csv", 'wb').write(r.content)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/sales_actual.csv")
open("sales_actual.csv", 'wb').write(r.content)

df_plan = pandas.read_csv("sales_plan.csv")

df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()

# print(df_plan)

df_actual = pandas.read_csv("sales_actual.csv")
df_actual["date"] = pandas.to_datetime(df_actual["date"])
df_actual["month"] = df_actual["date"].dt.month
df_actual["year"] = df_actual["date"].dt.year
df_actual_grouped = df_actual.groupby(["month", "year"]).sum()
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped["contract_value"].cumsum()
df_actual_grouped = df_actual_grouped.reset_index()

df_joined = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])
df_joined = df_joined.set_index("month")

#print(df_joined.tail())

#ax = df_joined.plot(color="red", y="sales_plan_cumsum", title="Skutence vs planovane trzby")
#df_joined.(kind="bar", y="sales_actual_cumusum", ax=ax)


df_joined.plot(kind="bar", y=["sales_plan_cumsum", "sales_actual_cumsum"], color=["grey", "orange"], title="Skutečné vs plánované tržby")
plt.legend(['Plán tržeb', "Skutečné tržby"])

#plt.show()

import numpy
df_actual_pivot = pandas.pivot_table(df_actual, index="country", columns="sales_manager" , values="contract_value", aggfunc=numpy.sum, margins=True)
#print(df_actual_pivot)

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/user_registration.json")
open("user_registration.json", 'wb').write(r.content)

df_registration = pandas.read_json("user_registration.json")
df_registration["month"] = df_registration["date_time"].dt.month
df_registration = df_registration.groupby("month").cumsum()

#pandas.set_option('display.max_columns', None)
print(df_registration.tail())






