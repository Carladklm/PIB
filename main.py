import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# Pays d'Asie de l'Est
# Vous pouvez modifier ce dictionnaire pour inclure d'autres pays
COUNTRIES = {
    "CN": "Chine",
    "JP": "Japon",
    "KR": "Corée du Sud",
    "KP": "Corée du Nord",
    "TW": "Taïwan",
    "MN": "Mongolie",
    "HK": "Hong Kong",
    "MO": "Macao"
}

# Indicateur pour le PIB en dollars américains courants
GDP_INDICATOR = {"NY.GDP.MKTP.CD": "PIB"}

def fetch_gdp_data(countries, indicator, start_year, end_year):
    """
    Récupère les données du PIB pour les pays et la période spécifiés.
    """
    try:
        # wbdata.get_dataframe attend une liste de codes pays
        gdp_data = wbdata.get_dataframe(indicator, country=countries, date=(str(start_year), str(end_year)))
        return gdp_data
    except Exception as e:
        print(f"Une erreur est survenue lors de la récupération des données : {e}")
        return None

def plot_gdp_data(data, country_names_map):
    """
    Génère un graphique à partir des données du PIB.
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    for country_code in data.columns:
        # Utilise le mapping pour obtenir le nom français pour la légende
        label = country_names_map.get(country_code, country_code)
        ax.plot(data.index, data[country_code] / 1e12, label=label, marker='o', linestyle='-')

    ax.set_title("Comparaison du PIB des pays d'Asie de l'Est", fontsize=16)
    ax.set_xlabel("Année", fontsize=12)
    ax.set_ylabel("PIB (en billions de $ US)", fontsize=12)
    ax.legend(title="Pays", bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True)
    plt.tight_layout()
    
    # Sauvegarde du graphique
    plt.savefig("gdp_comparison.png")
    print("\nLe graphique de comparaison des PIB a été sauvegardé sous 'gdp_comparison.png'")

def main():
    """
    Fonction principale pour analyser et comparer les PIB.
    """
    print("Analyse et comparaison des PIB des pays d'Asie de l'Est")
    print("Source des données : Banque Mondiale")
    
    start_year = 2000
    end_year = 2022
    
    country_codes = list(COUNTRIES.keys())
    
    gdp_data = fetch_gdp_data(country_codes, GDP_INDICATOR, start_year, end_year)
    
    if gdp_data is None or gdp_data.empty:
        print("Échec de la récupération des données ou aucune donnée disponible.")
        return
    
    # Pivoter les données pour avoir les pays en colonnes
    gdp_pivot = gdp_data.unstack(level=0)['PIB']

    # Supprimer les lignes (années) et colonnes (pays) entièrement vides
    gdp_pivot_cleaned = gdp_pivot.dropna(how='all', axis=0).dropna(how='all', axis=1)

    if gdp_pivot_cleaned.empty:
        print("Aucune donnée de PIB disponible pour la période sélectionnée après nettoyage.")
        return

    # Afficher les données les plus récentes
    print("\nDernières données de PIB disponibles (en milliards de $ US) :")
    latest_gdp = gdp_pivot_cleaned.ffill().iloc[-1] / 1e9
    
    # Créer un DataFrame pour un affichage propre
    latest_gdp_df = pd.DataFrame(latest_gdp)
    latest_gdp_df.columns = ["PIB (milliards $)"]
    latest_gdp_df.index.name = "Pays"
    
    # Remplacer les codes pays par les noms complets pour l'affichage
    latest_gdp_df.index = latest_gdp_df.index.map(COUNTRIES)

    print(latest_gdp_df.sort_values(by="PIB (milliards $)", ascending=False).to_string(float_format="{:,.2f}".format))

    # Génération du graphique
    plot_gdp_data(gdp_pivot_cleaned, COUNTRIES)

if __name__ == "__main__":
    main()