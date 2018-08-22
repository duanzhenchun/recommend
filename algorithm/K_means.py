from sklearn.cluster import KMeans, MiniBatchKMeans, Birch
from sklearn import metrics
import numpy as np
import pandas as pd


# feature
X = np.array([[3.3, 6.5],
              [5.8, 2.6],
              [3.6, 6.3],
              [3.4, 5.8],
              [5.2, 3.1]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print(kmeans.labels_)
print(kmeans.predict([[0, 0],
                      [4, 4]]))

print(kmeans.cluster_centers_)



df_train = pd.read_csv("./ml-100k/u1.base", sep="\t", names=["user id", "item id", "rate", "timestamp"])
df_test = pd.read_csv("./ml-100k/u1.test", sep="\t", names=["user id", "item id", "rate", "timestamp"])
x_train = df_train.values
x_test = df_test.values
y_train = df_train.iloc[:, -2].values
y_test = df_test.iloc[:, -2].values

"""
kmeans = KMeans(n_clusters=5, random_state=1).fit(x_train)
y_pred = kmeans.predict(x_test)
print(metrics.adjusted_rand_score(y_pred, y_test))
print(y_test)
print(y_pred)
"""


"""
mini_batch_kmeans = MiniBatchKMeans(n_clusters=5, batch_size=20000, random_state=0).fit(x_train)
y_pred_ = mini_batch_kmeans.predict(x_test)
print(metrics.adjusted_rand_score(y_pred_, y_test))
print(y_test)
print(y_pred_)
"""


"""
birch = Birch(n_clusters=5).fit(x_train)
y_pred = birch.predict(x_test)
print(metrics.adjusted_rand_score(y_pred, y_test))
print(y_test)
print(y_pred)
"""
