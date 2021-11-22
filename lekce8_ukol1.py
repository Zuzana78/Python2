import yfinance as yf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
import matplotlib.pyplot as plt
import pandas

data = yf.Ticker("CSCO")
data_cisco = data.history(period="5y")

print(data_cisco["Close"].autocorr(lag=1))
plot_acf(data_cisco["Close"])
plt.show()


model = AutoReg(data_cisco["Close"], lags=5, trend="t", seasonal=False)
res = model.fit()

predictions = res.predict(start=data_cisco.shape[0], end=data_cisco.shape[0] + 5)
data_forecast = pandas.DataFrame(predictions, columns=["Close_prediction"])
data_with_prediction = pandas.concat([data_cisco, data_forecast])
data_with_prediction[["Close", "Close_prediction"]].tail(50).plot()

print(data_with_prediction["Close"])
plt.show()

