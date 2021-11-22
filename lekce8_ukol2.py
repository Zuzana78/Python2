import requests
import pandas
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing


r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)

data = pandas.read_csv("MLTollsStackOverflow.csv")

decompose = seasonal_decompose(data["python"], model='multiplicative', period=12)
decompose.plot()
plt.show()

mod = ExponentialSmoothing(data["python"], seasonal_periods=12, trend="multiplicative", seasonal="multiplicative",
                              initialization_method="estimated")
res = mod.fit()
data["HM"] = res.fittedvalues
data_forecast = pandas.DataFrame(res.forecast(12), columns=["Forecast"])
data_with_forecast = pandas.concat([data, data_forecast])
data_with_forecast[["HM", "python", "Forecast"]].plot()
plt.show()
