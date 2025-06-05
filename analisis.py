import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
df = pd.read_csv("peliculas_ejemplo.csv")
print(df.head())

plt.figure(figsize=(8, 4))
sns.histplot(df['duration_minutes'], bins=20, kde=True, color='skyblue')
plt.title('Distribución de la duración de las películas')
plt.xlabel('Duración (minutos)')
plt.ylabel('Cantidad de películas')
plt.tight_layout()
plt.savefig('duracion_histograma.png')
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['rating'], bins=20, kde=True, color='salmon')
plt.title('Distribución de ratings de películas')
plt.xlabel('Rating')
plt.ylabel('Cantidad de películas')
plt.tight_layout()
plt.savefig('rating_histograma.png')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='duration_minutes', y='rating', hue='genre', alpha=0.7)
plt.title('Relación entre duración y rating')
plt.xlabel('Duración (minutos)')
plt.ylabel('Rating')
plt.legend(title='Género', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('duracion_vs_rating.png')
plt.show()

df['duracion_categoria'] = pd.cut(df['duration_minutes'],
                                  bins=[60, 90, 120, 150, 220],
                                  labels=['Corta', 'Media', 'Larga', 'Muy larga'])

promedios = df.groupby('duracion_categoria')['rating'].mean().reset_index()

plt.figure(figsize=(6, 4))
sns.barplot(data=promedios, x='duracion_categoria', y='rating', palette='viridis')
plt.title('Rating promedio según categoría de duración')
plt.xlabel('Categoría de duración')
plt.ylabel('Rating promedio')
plt.tight_layout()
plt.savefig('rating_por_duracion_categoria.png')
plt.show()
