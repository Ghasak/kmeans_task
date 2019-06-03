# =======================================================
#       Classifier Information
# =======================================================
# Simple K-means algorithm without machine learning
# Run with MacBook Pro - Mojave, Using Python 3.7
import os
import time
import datetime
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
# First we define the working directory
ResourceDir = os.getcwd()

# =======================================================
#       Input the dataset (features)
# =======================================================
# Lets start with these data as an assumption, then later we expend our algorithm.
X = np.array([[1.1,2.5],
              [3.4,1.9],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])

# Plot your current dataset
#plt.scatter(X[:,0],X[:,1], s=150)
#plt.show()

# =======================================================
#       K-means Classifier
# =======================================================
colors = 10*["g","r","c","b","k"]



class Simple_KMeans():

    def __init__(self, k= 2, tol = 0.001, max_iter = 300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i]= data[i]


        # We here start the optimization
        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                # We are using here the Euclidean's distance
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for  centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                # If you uncomment this, you will get the initial locations of centorids
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)


            Optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centorid = self.centroids[c]
                if np.sum((current_centorid - original_centroid)/ original_centroid * 100) > self.tol:
                    Optimized = False

            if Optimized:
                break

    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for  centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


clf = Simple_KMeans()
clf.fit(X)

# This function to give us the featureset (X) Coordinations and to which group the featureset belong.

def Task_Requirements():
    for classificiation in clf.classifications:
        color =colors[classificiation]

        for featureset in clf.classifications[classificiation]:
            plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5)
            print(f"the featureset of {featureset[0]},{featureset[1]} belong to Group{classificiation}")


    # Now we will get the centroids of each class coordinates:
    for item,centroid in enumerate(clf.centroids):
        print(5*"="+f"Centroid of group{item}="+f"{clf.centroids[centroid][0]}"+","+f"{clf.centroids[centroid][1]}")
        plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                    marker="o", color="k", s=150, linewidths=5)

    plt.show()


# Testing the classifier K-means with assumed featureset
Task_Requirements()



# Now lets test our algorithm with Sample size = 100,
# Note: generating the dataset here for testing the n_features should be same size with k in the class
# Test-1- Run the classifier with two groups
X1,y = make_blobs(n_samples=100, centers=2, n_features=2)

#

clf = Simple_KMeans()
clf.fit(X1)
Task_Requirements()


# Test with three groups
# Test-2- Run the classifier with three groups
X2,y = make_blobs(n_samples=100, centers=2, n_features=3)
clf = Simple_KMeans()
clf.k = 3
clf.fit(X2)
Task_Requirements()
