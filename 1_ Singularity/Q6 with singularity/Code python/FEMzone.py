# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 15:33:49 2025

@author: layal
"""


import matplotlib.pyplot as plt
import numpy as np

# Données
size = [2]  # en mm pour le maillage (pas utilisé dans ce tracé directement)
nombre_elements = np.array([150, 896, 3496, 13283, 52045, 80944, 141484, 203150, 313289])
nombre_elements = nombre_elements/1000

von_mises_zone5 = [29, 78.20, 128.72, 201.49,
                   297.08, 340.13, 394.25, 443.55, 498.61]
von_mises_zone6 = [22, 56.64, 92.21, 144.92,
                   212.32, 242.80, 280.79, 314.54, 354.67]

zones = [von_mises_zone5, von_mises_zone6]

# Tracer chaque courbe dans une figure séparée
for i in range(2):
    plt.figure(figsize=(7, 6))  # Créer une nouvelle figure pour chaque graphe
    plt.plot(nombre_elements, zones[i], marker='o', linestyle='-')
    plt.xlabel('Number of elements x $10^3$ [-]', fontsize=20)
    plt.ylabel('Von Mises stress [MPa]', fontsize=20)
    plt.xticks(fontsize=17)
    plt.yticks(np.arange(0, 1001, 100), fontsize=17)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'von_mises_zone_{i+5}.eps', dpi=300, bbox_inches='tight', format='eps')
    plt.savefig(f'VM{i+5}.png', dpi=300, bbox_inches='tight', format='png')
    plt.show()



