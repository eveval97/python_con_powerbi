import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


dataset = dataset.drop_duplicates()

#Estos son los datos a tener en cuenta para el clustering
features = ["danceability", "energy", "valence", "tempo", "speechiness", "acousticness", "instrumentalness"]
df_selected = dataset[features]


scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_selected)

# Beneficio! Podemos seleccionar la cantidad de clusters: ej. 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
dataset["cluster"] = kmeans.fit_predict(df_scaled)

# Reducimos la dimensionalidad con PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
dataset["pca1"] = df_pca[:, 0]
dataset["pca2"] = df_pca[:, 1]


fig, ax = plt.subplots(figsize=(10, 6))

fig.patch.set_alpha(0)  
ax.patch.set_alpha(0)   
plt.gca().set_facecolor("none")  


sns.scatterplot(x=dataset["pca1"], y=dataset["pca2"], hue=dataset["cluster"], palette="Set1", alpha=0.7, ax=ax)


ax.set_title("Clusters de Canciones (PCA)", fontsize=18, color="white", fontweight="bold")
ax.set_xlabel("Componente Principal 1", fontsize=16, color="white", fontweight="bold")
ax.set_ylabel("Componente Principal 2", fontsize=16, color="white", fontweight="bold")

ax.tick_params(axis="x", colors="white", labelsize=14)
ax.tick_params(axis="y", colors="white", labelsize=14)

legend = ax.legend(title="Cluster", frameon=False)  
plt.setp(legend.get_texts(), color="white")
legend.get_title().set_color("white")


plt.show()
