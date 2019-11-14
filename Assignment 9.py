.travis.yml file
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  


from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)

print(dir(iris))
print(iris.DESCR)
print(iris.data)
print(iris.feature_names)
print(iris.target_names)
print(iris.target)


print(iris.data[:,2])

np.where(iris.target == 0)
iris.data[np.where(iris.target == 0), 2]

# Based on petal length
petal_length_setosa = iris.data[np.where(iris.target == 0), 2]
print(petal_length_setosa.mean(),petal_length_setosa.max(),petal_length_setosa.min())

petal_length_versicolor = iris.data[np.where(iris.target == 1), 2]
print(petal_length_versicolor.mean(),petal_length_versicolor.max(),petal_length_versicolor.min())

petal_length_virginica = iris.data[np.where(iris.target == 2), 2]
print(petal_length_virginica.mean(),petal_length_virginica.max(),petal_length_virginica.min())

# Based on petal width
petal_width_setosa = iris.data[np.where(iris.target == 0), 3]
print(petal_width_setosa.mean(),petal_width_setosa.max(),petal_width_setosa.min())

petal_length_versicolor = iris.data[np.where(iris.target == 1), 3]
print(petal_width_versicolor.mean(),petal_width_versicolor.max(),petal_width_versicolor.min())

petal_length_virginica = iris.data[np.where(iris.target == 2), 3]
print(petal_width_virginica.mean(),petal_width_virginica.max(),petal_width_virginica.min())

#
#
# for flower_location, flower in enumerate(iris.data):
#    if iris.target[flower_location] == 0:
#        print(flower[2])

# flower_feature_location = 2
# flower_type = 0
# iris.data[np.where(iris.target == flower_type), flower_feature_location]
#

### Comparing new flower to the means of each class using 1 dimension

new_petal_length = 100.001

if abs(petal_length_virginica.mean() - new_petal_length) > abs(petal_length_versicolor.mean() - new_petal_length) > abs(petal_length_setosa.mean() - new_petal_length):
    print("Setosa")
elif abs(petal_length_virginica.mean() - new_petal_length) > abs(petal_length_versicolor.mean() - new_petal_length) < abs(petal_length_setosa.mean() - new_petal_length):
    print("Versicolor")
else: 
    print("Virginica")

new_petal_width = 50.001

if abs(petal_width_virginica.mean() - new_petal_width) > abs(petal_width_versicolor.mean() - new_petal_width) > abs(petal_width_setosa.mean() - new_petal_width):
    print("Setosa")
elif abs(petal_width_virginica.mean() - new_petal_width > abs(petal_width_versicolor.mean() - new_petal_width) < abs(petal_width_setosa.mean() - new_petal_width):
    print("Versicolor")
else: 
    print("Virginica")

### comparing new flower to the centroids of the clusters
np.random.seed(200)
k = 3
centroids = {
    i+1: [iris.data[:,2], iris.data[:,3]]
    for i in range(k)
}
fig = plt.figure(figsize=(10, 10))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()


def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(iris_df, centroids)
print(df.head())

fig = plt.figure(figsize=(10, 10))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
