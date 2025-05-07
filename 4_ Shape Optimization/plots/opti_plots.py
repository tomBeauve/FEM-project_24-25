# -*- coding: utf-8 -*-
"""
Created on Wed May  7 21:37:38 2025

@author: layal
"""

import numpy as np
import matplotlib.pyplot as plt

# Données 1
nelem1 = np.array([877, 3488, 13062, 51184, 139704, 308277]) / 1e5
tpe1 = [1.97217832E-01, 2.03080991E-01, 2.05233973E-01, 2.06258785E-01, 2.06635843E-01, 2.06822578E-01]
defo1 = [0.486, 0.505, 0.513, 0.518, 0.520, 0.520]
stress1 = [89.03, 117.88, 194.43, 303.56, 414.39, 525.95]

# Données 2 (exemple fictif, à adapter)
nelem2 = np.array([846,3277,12158,47858,129340,285588]) / 1e5
tpe2 = [2.290806E-01,2.246645E-01,2.273984E-01, 2.284832E-01,2.288871E-01,2.290806E-01]
defo2 = [0.501,0.522,0.531,0.535,0.537,0.528]
stress2 = [89.80,118.21,194.86,302.78,414.28,525.88]

# Graphique 1 – TPE
plt.figure()
plt.plot(nelem1, tpe1, marker='o', label='Without hole')
plt.plot(nelem2, tpe2, marker='s', label='With hole')
plt.xlabel('Number of elements [-]', fontsize=20)
plt.ylabel('TPE [J]', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True)
plt.legend(fontsize=18)
plt.savefig('TPE_opt.png', dpi=300, bbox_inches='tight')
plt.show()

# Graphique 2 – Déplacement
plt.figure()
plt.plot(nelem1, defo1, marker='o', label='Without hole')
plt.plot(nelem2, defo2, marker='s', label='With hole')
plt.xlabel('Number of elements [-]', fontsize=20)
plt.ylabel('Displacement [mm]', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True)
plt.legend(fontsize=18)
plt.savefig('displacement_opt.png', dpi=300, bbox_inches='tight')
plt.show()

# Graphique 3 – Contrainte
plt.figure()
plt.plot(nelem1, stress1, marker='o', label='Without hole')
plt.plot(nelem2, stress2, marker='s', label='With hole')
plt.xlabel('Number of elements [-]', fontsize=20)
plt.ylabel('Stress [MPa]', fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True)
plt.legend(fontsize=18)
plt.savefig('Stress_opt.png', dpi=300, bbox_inches='tight')
plt.show()
