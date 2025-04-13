# uBlock Filters Cleaner

[🇬🇧 English version](#-english-version) | [🇫🇷 Version française](#-version-française)

---

## 🇬🇧 English Version

### 📌 Features

- Sorts custom uBlock filters by site (based on lines starting with `!` and a URL)
- Removes duplicate filters
- Alphabetically sorts filters per site
- Skips empty lines
- Outputs a clean and structured `.txt` file

### 📂 Files

- `uBlock_filters.txt`: raw/unsorted filter rules  
- `sorted_uBlock_filters.txt`: cleaned and sorted output

### ▶️ How to Use

1. Put your `uBlock_filters.txt` file in the same folder as the script.
2. Run the script with Python:
    ```bash
   python uBlock_filter_sorter.py
    ```
3. The result will be saved in `sorted_uBlock_filters.txt`.

### 📋 Example

**Input file:**

```
! 2024-05-18 https://www.youtube.com
youtube.com##.ad-banner
youtube.com###player-ads

! 29/08/2019 https://www.wordreference.com
wordreference.com##.ads
wordreference.com##.ads

! 29 mars 2019 http://duckduckgo.com
duckduckgo.com##.ad
duckduckgo.com##.tracker
```

**Output file:**

```
! http://www.duckduckgo.com
duckduckgo.com##.ad
duckduckgo.com##.tracker

! https://www.wordreference.com
wordreference.com##.ads

! https://www.youtube.com
youtube.com###player-ads
youtube.com##.ad-banner
```

### ✅ Requirements

- Python 3.6+
- No external dependencies

### 🛠️ Possible Improvements

- Command-line arguments (CLI)
- Merge multiple filter files
- Export as JSON or CSV

---

## 🇫🇷 Version Française

### 📌 Fonctionnalitées

- Trie les filtres personnalisés de uBlock par site (à partir des lignes commençant par `!` suivies d'une URL)
- Supprime les doublons de filtres
- Trie les filtres de chaque site par ordre alphabétique
- Ignore les lignes vides
- Produit un fichier `.txt` propre et structuré

### 📂 Fichiers

- `uBlock_filters.txt` : fichier brut, non trié  
- `sorted_uBlock_filters.txt` : fichier de sortie nettoyé et trié

### ▶️ Utilisation

1. Place ton fichier `uBlock_filters.txt` dans le même dossier que le script.
2. Exécute le script avec Python :
    ```bash
   python uBlock_filter_sorter.py
    ```
3. Le résultat sera enregistré dans `sorted_uBlock_filters.txt`.

### 📋 Exemple

**Fichier d'entrée :**

```
! 2024-05-18 https://www.youtube.com
youtube.com##.ad-banner
youtube.com###player-ads

! 29/08/2019 https://www.wordreference.com
wordreference.com##.ads
wordreference.com##.ads

! 29 mars 2019 http://duckduckgo.com
duckduckgo.com##.ad
duckduckgo.com##.tracker
```

**Fichier de sortie :**

```
! https://www.duckduckgo.com
duckduckgo.com##.ad
duckduckgo.com##.tracker

! https://www.wordreference.com
wordreference.com##.ads

! https://www.youtube.com
youtube.com###player-ads
youtube.com##.ad-banner
```

### ✅ Pré-requis

- Python 3.6+
- Aucune dépendance externe

### 🛠️ Pistes d'amélioration

- Ajout d'une interface en ligne de commande (CLI)
- Fusion de plusieurs fichiers
- Export JSON ou CSV
