import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

platform_colors = {
    'netflix': '#E50914',  # Rojo para Netflix
    'amazon': '#00A8E1',   # Azul claro para Amazon Prime
    'disney': '#113CCF'    # Azul oscuro para Disney+
}


sns.set_style("whitegrid") 
sns.set_context("notebook")

# Figura sin fondo usando facecolor="none"
plt.figure(figsize=(10, 6), facecolor="none")


g = sns.catplot(
    x="platform", kind="count", data=dataset, col="type",
    height=7, palette=platform_colors, aspect=1
)

# Para quitar el fondo de cada subplot
for ax in g.axes.flat:
    ax.set_facecolor("none")  # Hace que el fondo del subplot sea transparente
    ax.patch.set_alpha(0)  
    ax.set_xlabel("")
    
    # Para cambiar el color y tamaño de los ejes
    ax.xaxis.label.set_color("white") 
    ax.xaxis.label.set_size(14)  
    ax.yaxis.label.set_color("white") 
    ax.yaxis.label.set_size(14)  
    
   
    ax.tick_params(axis="x", colors="white", labelsize=14)  
    ax.tick_params(axis="y", colors="white", labelsize=14)  

g.fig.patch.set_facecolor("none")

g.fig.suptitle("Cantidad de películas y shows por tipo y plataforma", y=1.03, color="white", fontsize=18)
g.set_titles("{col_name}s", color="white", fontsize=16)

if g._legend:
    plt.setp(g._legend.get_texts(), color="white", fontsize=12) 
    g._legend.get_title().set_color("white") 
    g._legend.get_title().set_fontsize(14)  

plt.show()
