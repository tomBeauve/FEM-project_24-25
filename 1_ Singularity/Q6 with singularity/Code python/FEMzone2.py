# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:29:06 2025

@author: layal
"""

import matplotlib.pyplot as plt


size = [2]  # en mm pour le maillage
nombre_elements = [150, 896, 3496, 13283, 52045, 80944,
                   141484, 203150, 313289]  # même pour toutes les zones

von_mises_zone1 = [213.63, 338.85, 424.52, 526.97,
                   679.65, 744.59, 836.30, 891.57, 966.98]
von_mises_zone2 = [156.38, 255.42, 321.76,
                   401.59, 518.39, 568.8, 634.94, 684, 746.89]
von_mises_zone3 = [102.91, 164.87, 210.80, 283.65,
                   371.49, 405.31, 458.10, 497.37, 553.15]
von_mises_zone4 = [94.56, 134.33, 188.80, 245.02,
                   313.30, 343.84, 388.73, 426.44, 469.49]

# Initialiser la figure avec 4 sous-graphes (2 lignes, 2 colonnes)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

zones = [von_mises_zone1, von_mises_zone2, von_mises_zone3, von_mises_zone4]
titles = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4']

# Tracer chaque courbe dans son propre graphe
for i, ax in enumerate(axs.flatten()):
    ax.plot(nombre_elements, zones[i], marker='o', linestyle='-')
    ax.set_xlabel('Nombre d\'éléments')
    ax.set_ylabel('Contrainte de Von Mises [MPa]')
    ax.set_title(titles[i])
    ax.grid(True)

plt.tight_layout()
plt.show()
plt.savefig('VM 1,2,3,4.eps', dpi=300, bbox_inches='tight', format='eps')
