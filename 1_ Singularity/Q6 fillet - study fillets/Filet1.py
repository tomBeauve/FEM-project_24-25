# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:26:21 2025

@author: layal
"""
"""
#ZONE 1 haut gauche
import matplotlib.pyplot as plt
#2,1,05,025,02,015,0125,01
# Data
number_of_elements05 = [1058, 3818,13842,52967,81636,140997,203089,313203]
number_of_elements1  = [883,3454,13093,51772,80486,140703,202407,313419]
number_of_elements2  = [1039, 3767,13272,52864,81588,143067,204960,312990]
number_of_elements5  = [943,3615,13433,53120,82933,143576,205554,315127]

von_mises_rayon05 = [433.69,483.48,718.70,749.77,863.10,870.10,808.49,886.81]
von_mises_rayon1 = [446.42,507.70,605.39,631.52,666.63,670.59,680.92,681.73]
von_mises_rayon2 = [420.61,426.41,493.60,517.38,522.76,529.14,529.34,549.56]
von_mises_rayon5 = [329.83,336.60,371.70,382.47,380.92,382.27,383.47,443.53]

zones = [von_mises_rayon05, von_mises_rayon1, von_mises_rayon2, von_mises_rayon5]
zone_labels = ['0.5 ', '1', '2','5']  # Legend labels

# Create a single figure
plt.figure(figsize=(10, 6))

# Plot all curves on the same graph
for i in range(4):
    plt.plot(number_of_elements, zones[i], marker='o', linestyle='-', label=zone_labels[i])

# Graph settings
plt.xlabel('Number of Elements [-]')
plt.ylabel('Von Mises Stress [MPa]')
plt.title('Convergence of Von Mises Stress by radius [mm]')
plt.grid(True)
plt.legend()  # Display the legend
plt.tight_layout()
plt.show()
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data
number_of_elements05 = [1058, 3818, 13842, 52967, 81636, 140997, 203089, 313203]
number_of_elements1  = [883, 3454, 13093, 51772, 80486, 140703, 202407, 313419]
number_of_elements2  = [1039, 3767, 13272, 52864, 81588, 143067, 204960, 312990]
number_of_elements5  = [943, 3615, 13433, 53120, 82933, 143576, 205554, 315127]

von_mises_rayon05 = [433.69, 483.48, 718.70, 749.77, 863.10, 870.10, 808.49, 886.81]
von_mises_rayon1  = [446.42, 507.70, 605.39, 631.52, 666.63, 670.59, 681.73, 681.73]
von_mises_rayon2  = [420.61, 426.41, 493.60, 517.38, 522.76, 529.14, 529.34, 549.56]
von_mises_rayon5  = [329.83, 336.60, 371.70, 382.47, 380.92, 382.27, 383.47, 443.53]

# Group the X and Y data together
number_of_elements = [number_of_elements05, number_of_elements1, number_of_elements2, number_of_elements5]
von_mises = [von_mises_rayon05, von_mises_rayon1, von_mises_rayon2, von_mises_rayon5]
radius_labels = ['Radius 0.5 mm', 'Radius 1 mm', 'Radius 2 mm', 'Radius 5 mm']  # Legend labels

# Create a single figure
plt.figure(figsize=(10, 6))

# Plot all curves on the same graph
for i in range(4):
    plt.plot([x / 1000 for x in number_of_elements[i]], von_mises[i], marker='o', linestyle='-', label=radius_labels[i])

# Graph settings
plt.xlabel('Number of Elements x $10^3$ [-]', fontsize=16)  # Update the label
plt.ylabel('Max Von Mises Stress [MPa]', fontsize=16)
plt.xticks(fontsize=14)  # Change font size of x-axis ticks
plt.yticks(fontsize=14)  # Change font size of y-axis ticks
plt.grid(True)
plt.legend(fontsize=12)  # Display the legend
plt.tight_layout()
plt.savefig("von_mises_convergenceZONE1.eps", format='eps')
plt.show()
