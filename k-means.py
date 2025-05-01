import numpy as np
import matplotlib.pyplot as plt

# Euclidean distance
def euclidean(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# K-Means algorithm
def k_means(X, k, max_iters=100):
    # Step 1: Initialize centroids randomly from the data points
    indices = np.random.choice(len(X), k, replace=False)
    centroids = X[indices]
    
    for _ in range(max_iters):
        # Step 2: Assign clusters
        clusters = [[] for _ in range(k)]
        for x in X:
            distances = [euclidean(x, c) for c in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(x)
        
        # Step 3: Update centroids
        new_centroids = np.array([np.mean(cluster, axis=0) if cluster else centroids[i]
                                  for i, cluster in enumerate(clusters)])
        
        # Convergence check
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    # Final cluster assignment
    labels = np.zeros(len(X), dtype=int)
    for i, x in enumerate(X):
        distances = [euclidean(x, c) for c in centroids]
        labels[i] = np.argmin(distances)
    
    return centroids, labels

# Generate sample data
np.random.seed(42)
X1 = np.random.randn(50, 2) + [2, 2]
X2 = np.random.randn(50, 2) + [8, 3]
X3 = np.random.randn(50, 2) + [5, 8]
X = np.vstack((X1, X2, X3))

# Run K-Means
k = 3
centroids, labels = k_means(X, k)

# Plot results
colors = ['r', 'g', 'b']
for i in range(k):
    cluster_points = X[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='yellow', marker='X', label='Centroids')
plt.legend()
plt.title('K-Means Clustering')
plt.show()
