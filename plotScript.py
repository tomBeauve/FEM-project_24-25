import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------
# User-editable section
# -------------------------------

csv_path = "1_ Singularity/Q6 with singularity/!Stress data/bottomLeft.csv"
output_path = "1_ Singularity/Q6 with singularity/images for singularity/stress_vs_elements_bottom_left"

x_label = 'Number of elements ×10³ [-]'
y_label = 'Max Von Mises Stress [MPa]'

plot_color = 'tab:blue'
marker_style = 'o'

# -------------------------------
# Data import and plot
# -------------------------------

df = pd.read_csv(csv_path, sep=',', header=None)

# Convert columns to numeric types (in case they were read as strings)
x = pd.to_numeric(df.iloc[:, 0], errors='coerce').values
y = pd.to_numeric(df.iloc[:, 1], errors='coerce').values

plt.figure(figsize=(8, 6))
plt.plot(x / 1000, y, marker=marker_style, linestyle='-', color=plot_color)

plt.xlabel(x_label, fontsize=12)
plt.ylabel(y_label, fontsize=12)
plt.grid(True)
plt.tight_layout()

plt.savefig(output_path + ".eps", dpi=300, bbox_inches='tight', format='eps')
plt.savefig(output_path + ".png", dpi=300, bbox_inches='tight', format='png')

plt.show()
