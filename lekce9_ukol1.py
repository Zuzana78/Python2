import requests
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    ConfusionMatrixDisplay,
)
import seaborn as sns
import matplotlib.pyplot as plt


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

data = pandas.read_csv("water-potability.csv")

#print(data.isna().sum())
#print(data.shape)
data = data.dropna()
#print(data.shape)

#print(data["Potability"].value_counts(normalize=True))

X = data.drop(columns=["Potability"])
y = data["Potability"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#print(X_train.shape, y_train.shape)
#print(X_test.shape, y_train.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#print(X_train)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
#print(y_pred)

ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Blues,
)

plt.show()
print(confusion_matrix(y_true=y_test, y_pred=y_pred))

# 74 / (74 + 52)
print(precision_score(y_test, y_pred))
print(f1_score(y_test, y_pred))


ks = [1, 3, 5,  7, 9, 11,]
precision = []
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    precision.append(precision_score(y_test, y_pred))
    print(k,precision_score(y_test, y_pred))

plt.plot(ks, precision)
plt.show()

clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(precision_score(y_test, y_pred))

# nejvyssi hodnota je na 5 sousedovi, tedy 0.5853, pote klesa a stoupa az u 9 souseda k hodnote 0.6091
# odvozeny vypocet precision_score z matice je 74 / (74 + 52) = 0.5873 a odpovida 5 sousedovi z metody presicion


