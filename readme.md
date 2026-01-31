# Analyseur de PIB des pays d'Asie de l'Est

Ce projet contient un script Python qui analyse et compare les Produits Intérieurs Bruts (PIB) des pays d'Asie de l'Est. Les données sont récupérées dynamiquement depuis l'API de la Banque Mondiale.

## Fonctionnalités

- Récupère les données du PIB (en dollars américains courants) pour les pays d'Asie de l'Est.
- Affiche un tableau avec les dernières données de PIB disponibles pour chaque pays.
- Génère un graphique linéaire montrant l'évolution du PIB pour chaque pays au cours des 20 dernières années.
- Sauvegarde le graphique sous forme de fichier image (`gdp_comparison.png`).

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

*Note : Les données pour certains pays (comme la Corée du Nord et Taïwan) peuvent ne pas être disponibles dans la base de données de la Banque Mondiale.*

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

Le script affichera le tableau des PIB dans la console et générera le fichier `gdp_comparison.png` dans le même répertoire.

## Exemple de sortie

Le script produira un tableau similaire à celui-ci dans la console :

```
Dernières données de PIB disponibles (en milliards de $ US) :
               PIB (milliards $)
Pays
Chine                  18,316.77
Japon                   4,262.46
Corée du Sud            1,799.36
Hong Kong                 358.68
Macao                      24.93
Mongolie                   17.15
Corée du Nord                NaN
```

De plus, une image nommée `gdp_comparison.png` sera créée, montrant l'évolution des PIB.
