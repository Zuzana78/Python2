import pandas
import requests
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    ConfusionMatrixDisplay,
)
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC


r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

data = pandas.read_csv("auto.csv", na_values=["?"])

X = data.drop(columns=["origin"])
y = data["origin"]
print(data.shape)
print(y.value_counts())

data = data.groupby("year").count().reset_index()

data.plot.bar( x="year", y="name", title="spotreba_aut")
plt.show()

encoder = OneHotEncoder()
X = encoder.fit_transform(X)
pandas.DataFrame(X.toarray(), columns=encoder.get_feature_names_out())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(confusion_matrix(y_test, y_pred))


model = DecisionTreeClassifier(random_state=0)
clf = GridSearchCV(model, param_grid={'max_depth': [3, 5, 7, 12], 'min_samples_leaf': [2, 6, 10, 16]})
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


print(round(f1_score(y_test, y_pred, average='weighted'),2))
print(clf.best_params_)
print(round(clf.best_score_, 2))







