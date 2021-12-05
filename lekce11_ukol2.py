from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

digits = load_digits()
X = digits.data
print(X)

scaler = StandardScaler()
X = scaler.fit_transform(X)
X.shape

tsne = TSNE(
    init="pca",
    n_components=2,
    perplexity=10,
    learning_rate="auto",
    random_state=0,
)
X = tsne.fit_transform(X)

print(X.shape)
plt.scatter(X[:, 0], X[:, 1], s=50)


model = KMeans(n_clusters=8, random_state=0)
labels = model.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap="Set1")
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c="black", s=200, alpha=0.5)
plt.show()


print(silhouette_score(X, labels))