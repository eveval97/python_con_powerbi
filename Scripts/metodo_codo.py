import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


dfspoty = pd.read_csv("ruta/spotify_dataset.csv")  

# Seleccionamos las características para el clustering
features = ["danceability", "energy", "valence", "tempo", "speechiness", "acousticness", "instrumentalness"]
df_selected = dfspoty[features]

# Acá hice escalamiento de datos ya que K-Means es sensible a las escalas
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_selected)

#primero realizar el análisis del codo para determinar cantidad de clusters
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
dfspoty["cluster"] = kmeans.fit_predict(df_scaled)

#Visualizar los clusters con PCA con reducción a 2D
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
dfspoty["pca1"] = df_pca[:, 0]
dfspoty["pca2"] = df_pca[:, 1]


inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker="o", linestyle="--")
plt.xlabel("Número de Clusters (K)")
plt.ylabel("Inercia")
plt.title("Método del Codo para Seleccionar K")
plt.show()
