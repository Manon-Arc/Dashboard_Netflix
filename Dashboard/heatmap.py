"""
heatmap.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.basemap import Basemap

CSV_PATH = "netflix_coord.csv"
df = pd.read_csv(CSV_PATH)

country_counts = df["country"].value_counts()
total_films = df["title"].count()

plt.figure(figsize=(10, 5))
m = Basemap(
    projection="mill", llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180
)

m.drawcoastlines()
m.drawcountries()

# Convertir les noms de pays en coordonnées de la carte
for country, count in country_counts.items():
    try:
        country_lat = df[df["country"] == country]["latitude"].iloc[0]
        country_lon = df[df["country"] == country]["longitude"].iloc[0]

        x, y = m(country_lon, country_lat)

        # Ajuster la taille des marqueurs pour
        # qu'elle soit proportionnelle au nombre de films
        marker_size = count * 1  # Ajustez ce coefficient selon vos préférences

        # Définir les couleurs en fonction du nombre de titres Netflix
        # Ici, nous utilisons une colormap de type 'Reds' avec une inversion
        # pour obtenir des couleurs plus claires pour les valeurs plus élevées
        color = count / country_counts.max()
        # Division par le maximum pour normaliser entre 0 et 1

        m.scatter(
            x, y, s=marker_size, color=color, alpha=0.7, edgecolors="k", zorder=10
        )
    except IndexError:
        pass

# Créer une barre de couleur légende
norm = mcolors.Normalize(vmin=0, vmax=total_films)
sm = plt.cm.ScalarMappable(cmap="Reds", norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=plt.gca(), orientation="vertical", label="Nombre de titres Netflix")

# Titre et affichage
plt.title("Heatmap du monde basée sur le nombre de titres Netflix par pays")
plt.show()
