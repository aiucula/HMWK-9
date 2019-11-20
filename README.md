# Assignment 10 Package

HMWK-9 is a package containing code used to For analyzing the Iris dataset which has three “populations” or “classifications”.
The code separates the three classifications and models the dataset.

Process used for accomplishing the clustering task:

Step 1: Identify the classes by analyzing the data (iris.DESCR, Iris.data, iris.feature_names, iris.target_names, iris.target))

Step 2: Identify which clusters have the least overlap by comparing the maximum and minimum of each cluster to each other and selecting the ones with the greatest differences from one cluster’s max to another’s min.

Step 3: Once the most appropriate clusters have been selected for analysis (least overlap between max and min of clusters), calculate the average of each cluster (kmean).

Step 4: Calculate the distance of the new data points to each cluster’s respective kmean. This can be done using the Pythagorean equation": a²+b²=c².

Step 5: Use an “If” statement to classify the new data point based on the shortest distance between the kmeans and the data point.

Ex: If (distance between new data and kmean.VirginicaCluster) is > (distance between new data and kmean.SetosaCluster) is < (distance between new data and kmean.VersicolorCluster)
Then classify as Setosa.

If (distance between new data and kmean.VirginicaCluster) is > (distance between new data and kmean.VersicolorCluster) is < (distance between new data and kmean.SetosaCluster)
Then classify as Versicolor.

Else classify as Virginica


To account for outliers, use Random sample consensus (RANSAC) which will fit lines onto the data, therefore outliers will have no influence on the result.


Project Data

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  


from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
