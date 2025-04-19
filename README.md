# 🚀 **FEM-project_24-25**

Repo du projet de MECA0036-2 Finite Element Method.

# 📁 Structure du projet

## 🗂️ Dossiers

### `0_ Orientation forces`
Préliminaire: sans fillet, déterminer le sens des pressions à appliquer dans NX

### `1_ Singularity`
Observation (sans fillet), puis étude & suppression des singularités (avec fillet) 
N'utiliser qu'un seul type de Mesh

### `2_ FEA coarse meshes`
Etude des différents types d'éléments (FEA), pièce sans singularités ( = avec fillet ), mesh grossiers tout faits par NX

### `3_ Advanced meshes`
Maillage avancé et raffiné, avec des mesh control,... pour améliorer la convergence des résultats. <br>
Servira peut-être également à déterminer le q_max

### `4_ Shape Optimization`
Optimisation de la forme de la transition entre l'ellipse et le cercle

--

## 📝 **Rapport**

Le Rapport se trouve dans le fichier 
```bash
FEM-project_24-25/Report
```
Il s'agit d'un document LaTeX fait sur Overleaf. Pour le mettre à jour il faut lier son compte Overleaf à GitHub pour pouvoir ensuite push les modifications sur le repo ci-présent.

## 📦 **Installation**

Pour cloner le Rapport sur Overleaf afin de pouvoir le modifier confortablement il faut :

```bash
1. Lier son compte Overleaf à GitHub :
  Account -> Project Synchronisation -> GitHub Sync

2. Créer un nouveau projet:
  New Project -> Import from GitHub -> tomBeauve/FEM-project_24-25

3. Changer le compilateur en XeLaTeX ou LuaLaTeX :
  Menu -> Settings -> Compiler
```
## 🛠️ **Utilisation**

Pour sauvegarder des modifications, tout se fait sur Overleaf :

```bash
Dans le projet,

Menu -> Sync -> GitHub -> Push Overleaf changes to GitHub
```

## ⚠️ **Attention**
N'oubliez pas de pull à chaque fois que vous allez travailler sur le rapport. Cela évite de refaire ce qu'un autre a peut-être déjà fait et cela évite les collisions. La marche à suivre pour faire un pull est la même que pour push, il suffit de choisir pull sur la fenêtre de synchronisation.
