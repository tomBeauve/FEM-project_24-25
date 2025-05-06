# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:24:41 2025

@author: layal
"""
"""
#ZONE 2haut droit
import matplotlib.pyplot as plt

# Data
number_of_elements05 = [1058, 3818,13842,52967,81636,140997,203089,313203]
number_of_elements1  = [883,3454,13093,51772,80486,140703,202407,313419]
number_of_elements2  = [1039, 3767,13272,52864,81588,143067,204960,312990]
number_of_elements5  = [943,3615,13433,53120,82933,143576,205554,315127]

von_mises_rayon05 = [318.02,450.88,538.26,646.44,663.82,642.36,625.68,676.04]
von_mises_rayon1 = [313.70,381.58,503.75,490.21,517.73,532.19,529.09,531.92]
von_mises_rayon2 = [306.44,336.19,367.96,399.86,395.01,402.26,403.86,418.62]
von_mises_rayon5 = [247.61,268.94,279.26,281.96,285.05,283.64,284.01,329.52]

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

# ZONE 2 haut droit

# Data
number_of_elements05 = [1058, 3818, 13842, 52967, 81636, 140997, 203089, 313203]
number_of_elements1  = [883, 3454, 13093, 51772, 80486, 140703, 202407, 313419]
number_of_elements2  = [1039, 3767, 13272, 52864, 81588, 143067, 204960, 312990]
number_of_elements5  = [943, 3615, 13433, 53120, 82933, 143576, 205554, 315127]

von_mises_rayon05 = [318.02, 450.88, 538.26, 646.44, 663.82, 642.36, 625.68, 676.04]
von_mises_rayon1  = [313.70, 381.58, 503.75, 490.21, 517.73, 532.19, 529.09, 531.92]
von_mises_rayon2  = [306.44, 336.19, 367.96, 399.86, 395.01, 402.26, 403.86, 418.62]
von_mises_rayon5  = [247.61, 268.94, 279.26, 281.96, 285.05, 283.64, 284.01, 329.52]

# Grouped data for plotting
number_of_elements = [number_of_elements05, number_of_elements1, number_of_elements2, number_of_elements5]
von_mises = [von_mises_rayon05, von_mises_rayon1, von_mises_rayon2, von_mises_rayon5]
radius_labels = ['Radius 0.5 mm', 'Radius 1 mm', 'Radius 2 mm', 'Radius 5 mm']

# Create a single figure
plt.figure(figsize=(10, 6))

# Plot all curves
for i in range(4):
    plt.plot([x / 1000 for x in number_of_elements[i]], von_mises[i], marker='o', linestyle='-', label=radius_labels[i])

# Graph settings
plt.xlabel('Number of Elements x $10^3$ [-]', fontsize=16)  # Update the label
plt.ylabel('Max Von Mises Stress [MPa]', fontsize=16)
plt.xticks(fontsize=14)  # Change font size of x-axis ticks
plt.yticks(fontsize=14)  # Change font size of y-axis ticks
plt.grid(True)
plt.legend(fontsize=11)  # Display the legend
plt.tight_layout()
plt.savefig("von_mises_filletZONE2.eps", format='eps')
plt.show()
