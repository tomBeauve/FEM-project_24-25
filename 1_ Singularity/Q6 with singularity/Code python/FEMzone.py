# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:33:49 2025

@author: layal
"""


import matplotlib.pyplot as plt

# Données
size = [2]  # en mm pour le maillage (pas utilisé dans ce tracé directement)
nombre_elements = [150, 896, 3496, 13283, 52045, 80944, 141484, 203150, 313289]

von_mises_zone5 = [29, 78.20, 128.72, 201.49, 297.08, 340.13, 394.25, 443.55, 498.61]
von_mises_zone6 = [22, 56.64, 92.21, 144.92, 212.32, 242.80, 280.79, 314.54, 354.67]

# Initialiser la figure avec 2 sous-graphes (1 ligne, 2 colonnes)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))  # <-- 1 ligne, 2 colonnes

zones = [von_mises_zone5, von_mises_zone6]
titles = ['Zone 5', 'Zone 6']

# Tracer chaque courbe dans son propre graphe
for i, ax in enumerate(axs.flatten()):
    ax.plot(nombre_elements, zones[i], marker='o', linestyle='-')
    ax.set_xlabel('Nombre d\'éléments')
    ax.set_ylabel('Contrainte de Von Mises [MPa]')
    ax.set_title(titles[i])
    ax.grid(True)

plt.tight_layout()
plt.show()

