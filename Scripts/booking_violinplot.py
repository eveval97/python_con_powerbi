import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset = dataset.dropna(subset=['city', 'gross_amount'])


sns.set_style("whitegrid")
sns.set_context("notebook")


fig, ax = plt.subplots(figsize=(12, 6))


fig.patch.set_alpha(0)  
ax.patch.set_alpha(0)   
plt.gca().set_facecolor("none")  


sns.violinplot(x='city', y='gross_amount', data=dataset, palette="Set2", inner="quartile", ax=ax)


ax.set_title('Distribución de Precios de Hoteles por Ciudad', fontsize=18, color="white", fontweight="bold")
ax.set_xlabel('Ciudad', fontsize=16, color="white", fontweight="bold")
ax.set_ylabel('Precio Bruto (US$)', fontsize=16, color="white", fontweight="bold")


ax.tick_params(axis="x", colors="white", labelsize=14, rotation=0)
ax.tick_params(axis="y", colors="white", labelsize=14)

plt.show()
