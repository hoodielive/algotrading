from base64 import b32encode
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data
data = {
    'Age': [24, 30, 45, 66],
    'Monthly Spending': [95, 92, 93, 99]
}

df = pd.DataFrame(data)
plt.scatter(df['Age'], df['Monthly Spending'])
plt.xlabel('Age')
plt.ylabel('Monthly Spending')
plt.show()

# Number of clusters
k = 3
kmeans = KMeans(n_clusters=k)
df['Cluster'] - kmeans.fit_predict(df[['Age'], 'Monthy Spending'])

# Getting the cluster centers
centers = kmeans.cluster_centers_

for i in range(k):
    subset = df[df['Cluster'] == i]
    plt.scatter(subset['Age'], subset['Monthly Spending'], label=f'Cluster {i}')

plt.scatter(
    centers[:, 0], 
    centers[:, 1], 
    s=200, 
    alpha=0.75, 
    color='black', 
    marker='X', 
    label='Centroids'
)

plt.xlabel('Age')
plt.ylabel('Monthly Spending')
plt.legend()
plt.show()
