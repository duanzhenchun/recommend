from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

"""
# feature
X = np.array([[1, 2],
              [1, 4],
              [1, 0],
              [4, 2],
              [4, 4],
              [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print(kmeans.labels_)
print(kmeans.predict([[0, 0],
                      [4, 4]]))

print(kmeans.cluster_centers_)

"""

df = pd.read_csv("./ml-100k/u1.base", sep="\t", names=["user id", "item id", "rate", "timestamp"])
x = df.values
y = df.iloc[:, -2].values
print(y)
kmeans = KMeans(n_clusters=5, random_state=0).fit(x)
print(kmeans.predict([[1, 1, 5, 874965758]]))
print(kmeans.cluster_centers_)