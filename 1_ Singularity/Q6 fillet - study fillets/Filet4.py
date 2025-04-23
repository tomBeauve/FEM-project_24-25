# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:24:42 2025

@author: layal
"""
"""
#Zone 4 bas droite
import matplotlib.pyplot as plt

# Data
number_of_elements05 = [1058, 3818,13842,52967,81636,140997,203089,313203]
number_of_elements1  = [883,3454,13093,51772,80486,140703,202407,313419]
number_of_elements2  = [1039, 3767,13272,52864,81588,143067,204960,312990]
number_of_elements5  = [943,3615,13433,53120,82933,143576,205554,315127]


von_mises_rayon05 = [209.74,272.81,346.54,379.11,390.51,421.36,411.11,432.15]
von_mises_rayon1 = [201.77,278,24,306,23,309.97,326.84,328.67,327.43,328.59]
von_mises_rayon2 = [172.53,214.39,239.93,238.98,245.34,245.76,245.68,258.52]
von_mises_rayon5 = [147.54,157.90,162.74,165.96,166.06,165.09,164.97,190.93]

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

# ZONE 4 – bas droite

# Data
number_of_elements05 = [1058, 3818, 13842, 52967, 81636, 140997, 203089, 313203]
number_of_elements1  = [883, 3454, 13093, 51772, 80486, 140703, 202407, 313419]
number_of_elements2  = [1039, 3767, 13272, 52864, 81588, 143067, 204960, 312990]
number_of_elements5  = [943, 3615, 13433, 53120, 82933, 143576, 205554, 315127]

von_mises_rayon05 = [209.74, 272.81, 346.54, 379.11, 390.51, 421.36, 411.11, 432.15]
von_mises_rayon1  = [201.77, 278.24, 306.23, 309.97, 326.84, 328.67, 327.43, 328.59]
von_mises_rayon2  = [172.53, 214.39, 239.93, 238.98, 245.34, 245.76, 245.68, 258.52]
von_mises_rayon5  = [147.54, 157.90, 162.74, 165.96, 166.06, 165.09, 164.97, 190.93]

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
plt.title('Convergence of Von Mises Stress for Different Radii for Zone 4')
plt.grid(True)
plt.legend()  # Display the legend
plt.tight_layout()
plt.savefig("von_mises_convergenceZONE4.eps", format='eps')
plt.show()
