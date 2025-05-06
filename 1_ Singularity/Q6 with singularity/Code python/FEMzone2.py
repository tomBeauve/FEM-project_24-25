# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:29:06 2025

@author: layal
"""

import matplotlib.pyplot as plt
import numpy as np

size = [2]  # en mm pour le maillage
nombre_elements = np.array([150, 896, 3496, 13283, 52045, 80944,
                   141484, 203150, 313289])  # même pour toutes les zones
nombre_elements = nombre_elements / 1000

von_mises_zone1 = [213.63, 338.85, 424.52, 526.97,
                   679.65, 744.59, 836.30, 891.57, 966.98]
von_mises_zone2 = [156.38, 255.42, 321.76,
                   401.59, 518.39, 568.8, 634.94, 684, 746.89]
von_mises_zone3 = [102.91, 164.87, 210.80, 283.65,
                   371.49, 405.31, 458.10, 497.37, 553.15]
von_mises_zone4 = [94.56, 134.33, 188.80, 245.02,
                   313.30, 343.84, 388.73, 426.44, 469.49]

zones = [von_mises_zone1, von_mises_zone2, von_mises_zone3, von_mises_zone4]
titles = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4']

# Tracer chaque courbe dans une figure séparée
for i in range(4):
    plt.figure(figsize=(7, 6))  # Créer une nouvelle figure pour chaque graphe
    plt.plot(nombre_elements, zones[i], marker='o', linestyle='-')
    plt.xlabel('Number of elements x $10^3$ [-]', fontsize=20)
    plt.ylabel('Von Mises stress [MPa]', fontsize=20)
    plt.xticks(fontsize=17)  # Revert x-ticks to default behavior
    plt.yticks(np.arange(0, 1001, 100), fontsize=17)  # Imposer les ticks de 0 à 1000 avec un pas de 100
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'von_mises_zone_{i+1}.eps', dpi=300, bbox_inches='tight', format='eps')
    plt.savefig(f'VM{i+1}.png', dpi=300, bbox_inches='tight', format='png')
    plt.show()


