# Analyseur de Données des Pays d'Asie de l'Est

Ce projet contient un script Python qui analyse et compare des indicateurs économiques et démographiques clés pour les pays d'Asie de l'Est. Les données sont récupérées dynamiquement depuis l'API de la Banque Mondiale.

## Fonctionnalités

- **Analyse du PIB :**
    - Récupère les données du PIB (en dollars américains courants).
    - Affiche un tableau classant les pays par leur dernier PIB disponible.
    - Génère un graphique linéaire (`gdp_comparison.png`) montrant l'évolution du PIB pour chaque pays.

- **Analyse de la Population :**
    - Récupère les données démographiques totales.
    - Affiche un tableau classant les pays par leur nombre d'habitants le plus récent.

## Pays analysés

Le script analyse les pays suivants :
- Chine
- Japon
- Corée du Sud
- Corée du Nord
- Taïwan
- Mongolie
- Hong Kong
- Macao

*Note : Les données pour certains pays (comme la Corée du Nord et Taïwan) peuvent ne pas être disponibles dans la base de données de la Banque Mondiale, auquel cas ils n'apparaîtront pas dans les classements.*

## Comment utiliser

### Prérequis

Assurez-vous d'avoir Python 3 et `pip` installés sur votre système.

### Installation

1. Clonez ce dépôt ou téléchargez les fichiers.
2. Ouvrez un terminal dans le répertoire du projet.
3. Installez les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install wbdata pandas matplotlib
```

### Exécution

Pour lancer l'analyse, exécutez le script `main.py` depuis votre terminal :

```bash
python3 main.py
```

Le script affichera les tableaux de classement dans la console et générera le fichier `gdp_comparison.png`.

## Exemple de sortie

Le script produira des tableaux similaires à ceux-ci dans la console :

**Classement par PIB :**
```
Dernières données de PIB disponibles :
               PIB (milliards $)
Pays
Chine                  18,316.77
Japon                   4,262.46
Corée du Sud            1,799.36
Hong Kong                 358.68
Macao                      24.93
Mongolie                   17.15
```

**Classement par Population :**
```
Dernières données de Population disponibles :
              Population (millions)
Pays
Chine                         1,425
Japon                           125
Corée du Sud                     51
Corée du Nord                    26
Hong Kong                         7
Mongolie                          3
Macao                             1
```

De plus, une image nommée `gdp_comparison.png` sera créée, montrant l'évolution des PIB.