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


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)

data = pandas.read_csv("kosatce.csv")

#print(data.shape)
print(data["target"].value_counts(normalize=True))

X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_train.shape)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(y_pred)

ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
    display_labels=clf.classes_,
    cmap=plt.cm.Reds,
)

plt.show()
print(confusion_matrix(y_true=y_test, y_pred=y_pred))

print(f1_score(y_test, y_pred))

#vysledna hodnota dosahla 86,49% Coz znamena ze na zaklade techto hodnot lze predpovedet typ kosatce.






