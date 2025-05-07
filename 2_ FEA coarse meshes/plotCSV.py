import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# Dossiers contenant les fichiers results.csv
folders = ['Q6', 'Q8', 'T3', 'T6']

# Dictionnaire pour stocker les données de chaque type
data = {}
True_area = 2953.3638


# Lecture des fichiers
for folder in folders:
    file_path = os.path.join(folder, 'results.csv')
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # Nettoyage des colonnes
    data[folder] = df


# Fonctions de tracé
def plot_metric(x_key, y_key,xlabel, ylabel, title, filename, reference_line=None):
    plt.figure(figsize=(10, 6))
    for folder in folders:
        df = data[folder]
        if x_key == 'NElem':
            # Create a temporary x_values for plotting, leaving the original data unchanged
            x_values = np.array(df[x_key]) / 1e5 if x_key == 'NElem' else df[x_key]
            plt.plot(x_values, df[y_key], marker='o', label=folder)
            xlabel = 'Number of elements x $10^5$ [-]'
        elif x_key == 'NDOF':
            # Create a temporary x_values for plotting, leaving the original data unchanged
            x_values = np.array(df[x_key]) / 1e6 if x_key == 'NDOF' else df[x_key]
            plt.plot(x_values, df[y_key], marker='o', label=folder)
            xlabel = 'Number of degrees of freedom x $10^6$ [-]'
        else:
            plt.plot(df[x_key], df[y_key], marker='o', label=folder)
        
    if reference_line is not None:
        plt.axhline(reference_line, color='gray',
                    linestyle='--', label='Reference')
    
        
    plt.xlabel(xlabel, fontsize=25) 
    plt.ylabel(ylabel, fontsize=25)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    #plt.title(title)
    plt.legend(fontsize=25)
    plt.grid(True, alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join("plot_CSV", filename), dpi=300)
    plt.show()


# Tracés demandés
plot_metric('NElem', 'TPE','Number of elements [-]', 'TPE [J]', "TPE vs NElem", 'TPE_vs_NElem.png')
plot_metric('NDOF','TPE','Number of degrees of freedom [-]', 'TPE [J]', "TPE vs NDOF", 'TPE_vs_NDOF.png')
plot_metric('NElem', 'Area','Number of elements [-]', 'Area [mm$^2$]', "Area vs NElem",
            'Area_vs_NElem.png', reference_line=True_area)
plot_metric('NDOF', 'Area','Number of degrees of freedom [-]', 'Area [mm$^2$]', "Area vs NDOF",
            'Area_vs_NDOF.png', reference_line=True_area)
plot_metric('NElem', 'CPU','Number of elements [-]', 'CPU time [s]', "CPU vs NElem", 'CPU_vs_NElem.png')
plot_metric('NDOF', 'CPU','Number of degrees of freedom [-]', 'CPU time [s]', "CPU vs NDOF", 'CPU_vs_NDOF.png')
plot_metric('TPE', 'CPU','TPE [J]', 'CPU time [s]', "TPE vs CPU", 'TPE_vs_CPU.png')
plot_metric('NElem', 'epsilon_max','Number of elements [-]', 'Displacement [mm]','','Displacement_vs_NElem.png')

# Tracés Sigma_i vs NElem (i = 1 à 6)
for i in range(1, 7):
    sigma_col = f"Sigma_{i}"
    plot_metric('NElem', sigma_col,'Number of elements [-]', f'$\sigma_{i}$ [MPa]',
                f"Stress in zone {i} vs NElem", f"Stress{i}_vs_NElem.png")
