# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 13:26:52 2019

@author: n173437
"""

# import libraries as needed
import pandas as pd
import numpy as np
import string

from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib.pyplot as plt

import time
import gc

start = time.time()

# import the data and assign to the variable "questions"
questions = pd.read_csv("U:\Book1.csv", encoding='iso-8859-1')
    
vectorizer = TfidfVectorizer(stop_words = "english")
predictions = vectorizer.fit_transform(questions["Question"])

Sum_of_squared_distances = []
K = range(1,1500)
for k in K:
    km = MiniBatchKMeans(n_clusters = k, random_state = 322, batch_size = 100, init_size = 3001)
    km = km.fit(predictions)
    Sum_of_squared_distances.append(km.inertia_)
    gc.collect()

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum of squared distances')
plt.title('Elbow Method For Optimal k')
plt.show()

end = time.time()
print("Total runtime in seconds: ", end - start)


"""
n_range = range(1000,1300)


for num_clusters in n_range:
    clusterer = MiniBatchKMeans(n_clusters = num_clusters, random_state = 322, batch_size = 100)
    preds = clusterer.fit_predict(predictions)
    centers = clusterer.cluster_centers_
    score = silhouette_score(predictions, preds, metric = "euclidean", sample_size = 100)
    print("For n_clusters =", num_clusters,
          "Silhouette score =", score)
"""