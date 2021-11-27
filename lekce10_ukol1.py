import pandas
import requests
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv"
)
open("soybean-2-rot.csv", "wb").write(r.content)

data = pandas.read_csv("soybean-2-rot.csv")

X = data.drop(columns=["class"])
y = data["class"]


oh_encoder = OneHotEncoder()
X = oh_encoder.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)


clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))

print(clf.feature_importances_)
print(oh_encoder.get_feature_names_out())

#nejvetsi dulezitost ma promenna "plant-stand" - 0,494
#f1_score je 0,94 pri pouziti vsech promennych
#zaver je, ze jedna nejvetsi promenna neni dostatecna pro spravne vyhodnoceni modulu, jeji vyse je prilis nizka
#rozdil mezi temito dvema promennymi je 0,44



