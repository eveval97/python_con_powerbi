import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

dfspoty = pd.read_csv("D:/INFORMATICA-Proyectos/Bootcam_data_platform/demo_bootcamp/spotify_dataset.csv")  

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

plt.figure(figsize=(10, 6))
sns.scatterplot(x=dfspoty["pca1"], y=dfspoty["pca2"], hue=dfspoty["cluster"], palette="viridis", alpha=0.7)
plt.title("Clusters de Canciones (PCA)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.legend(title="Cluster")
plt.show()
