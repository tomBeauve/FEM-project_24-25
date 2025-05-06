import pandas as pd
import matplotlib.pyplot as plt
import os

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
def plot_metric(x_key, y_key, ylabel, title, filename, reference_line=None):
    plt.figure(figsize=(10, 6))
    for folder in folders:
        df = data[folder]
        plt.plot(df[x_key], df[y_key], marker='o', label=folder)
    if reference_line is not None:
        plt.axhline(reference_line, color='gray',
                    linestyle='--', label='Référence')
    plt.xlabel(x_key)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join("plot_CSV", filename), dpi=300)
    plt.close()


# Tracés demandés
plot_metric('NElem', 'TPE', 'TPE', "TPE vs NElem", 'TPE_vs_NElem.png')
plot_metric('NDOF', 'TPE', 'TPE', "TPE vs NDOF", 'TPE_vs_NDOF.png')
plot_metric('NElem', 'Area', 'Area', "Area vs NElem",
            'Area_vs_NElem.png', reference_line=True_area)
plot_metric('NDOF', 'Area', 'Area', "Area vs NDOF",
            'Area_vs_NDOF.png', reference_line=True_area)
plot_metric('NElem', 'CPU', 'CPU (s)', "CPU vs NElem", 'CPU_vs_NElem.png')
plot_metric('NDOF', 'CPU', 'CPU (s)', "CPU vs NDOF", 'CPU_vs_NDOF.png')
# plot_metric('CPU', 'TPE', 'TPE', "TPE vs CPU", 'TPE_vs_CPU.png')

# Tracés Sigma_i vs NElem (i = 1 à 6)
for i in range(1, 7):
    sigma_col = f"Sigma_{i}"
    plot_metric('NElem', sigma_col, f'{sigma_col}',
                f"Stress in zone {i} vs NElem", f"Stress{i}_vs_NElem.png")
