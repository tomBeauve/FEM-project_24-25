# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:24:41 2025

@author: layal
"""
"""
#ZONE 3 bas gauche
import matplotlib.pyplot as plt

# Data
number_of_elements05 = [1058, 3818,13842,52967,81636,140997,203089,313203]
number_of_elements1  = [883,3454,13093,51772,80486,140703,202407,313419]
number_of_elements2  = [1039, 3767,13272,52864,81588,143067,204960,312990]
number_of_elements5  = [943,3615,13433,53120,82933,143576,205554,315127]

von_mises_rayon05 = [211.11,298.39,362.62,411.46,468.85,505.44,462.10,502.71]
von_mises_rayon1 = [216.63,306.75,360.33,365.49,381.85,384.18,385.72,383.80]
von_mises_rayon2 = [201.67,257.29,288.49,287.93,284.67,290.44,286.97,302.07]
von_mises_rayon5 = [174.40,175.99,194.88,196.86,196.39,194.89,194.73,223.26]

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

# ZONE 3 – bas gauche

# Data
number_of_elements05 = [1058, 3818, 13842, 52967, 81636, 140997, 203089, 313203]
number_of_elements1  = [883, 3454, 13093, 51772, 80486, 140703, 202407, 313419]
number_of_elements2  = [1039, 3767, 13272, 52864, 81588, 143067, 204960, 312990]
number_of_elements5  = [943, 3615, 13433, 53120, 82933, 143576, 205554, 315127]

von_mises_rayon05 = [211.11, 298.39, 362.62, 411.46, 468.85, 505.44, 462.10, 502.71]
von_mises_rayon1  = [216.63, 306.75, 360.33, 365.49, 381.85, 384.18, 385.72, 383.80]
von_mises_rayon2  = [201.67, 257.29, 288.49, 287.93, 284.67, 290.44, 286.97, 302.07]
von_mises_rayon5  = [174.40, 175.99, 194.88, 196.86, 196.39, 194.89, 194.73, 223.26]

# Grouped data
number_of_elements = [number_of_elements05, number_of_elements1, number_of_elements2, number_of_elements5]
von_mises = [von_mises_rayon05, von_mises_rayon1, von_mises_rayon2, von_mises_rayon5]
radius_labels = ['Radius 0.5 mm', 'Radius 1 mm', 'Radius 2 mm', 'Radius 5 mm']

# Create the figure
plt.figure(figsize=(10, 6))

# Plot all curves
for i in range(4):
    plt.plot(number_of_elements[i], von_mises[i], marker='o', linestyle='-', label=radius_labels[i])

# Graph settings
plt.xlabel('Number of Elements [-]')
plt.ylabel('Max Von Mises Stress [MPa]')
plt.title('Convergence of Von Mises Stress for Different Radii for Zone 3')
plt.grid(True)
plt.legend()  # Display the legend
plt.tight_layout()
plt.savefig("von_mises_convergenceZONE3.eps", format='eps')
plt.show()

