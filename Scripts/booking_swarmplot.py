import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset = dataset.dropna(subset=['city', 'gross_amount'])


sns.set_style("whitegrid")
sns.set_context("notebook")


fig, ax = plt.subplots(figsize=(12, 6))

# PAra poner fondo transparente
fig.patch.set_alpha(0)  
ax.patch.set_alpha(0)   
plt.gca().set_facecolor("none")  

# Esta es una paleta predefinida para colores 
#Pueden usar otras como:
#"Set1" → Rojo, azul, verde
#"Set2" → Verde, naranja, azul
#"Paired" → Combinación de colores vibrantes
#"tab10" → Paleta con colores distintos


sns.swarmplot(x='city', y='gross_amount', data=dataset, size=6, palette="Paired", ax=ax)


ax.set_title('Distribución de Precios de Hoteles por Ciudad', fontsize=16, color="white")
ax.set_xlabel('Ciudad', fontsize=14, color="white")
ax.set_ylabel('Precio Bruto (US$)', fontsize=14, color="white")

ax.tick_params(axis="x", colors="white", labelsize=12, rotation=0)
ax.tick_params(axis="y", colors="white", labelsize=12)

plt.show()
