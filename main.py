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

# Indicateurs de la Banque Mondiale
GDP_INDICATOR = {"NY.GDP.MKTP.CD": "PIB"}
POPULATION_INDICATOR = {"SP.POP.TOTL": "Population"}

def fetch_wb_data(countries, indicator, start_year, end_year):
    """
    Récupère les données de la Banque Mondiale pour les pays et la période spécifiés.
    """
    try:
        data = wbdata.get_dataframe(indicator, country=countries, date=(str(start_year), str(end_year)))
        return data
    except Exception as e:
        print(f"Une erreur est survenue lors de la récupération des données pour {list(indicator.values())[0]}: {e}")
        return None

def plot_gdp_data(data, country_names_map):
    """
    Génère un graphique à partir des données du PIB.
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    for country_code in data.columns:
        label = country_names_map.get(country_code, country_code)
        ax.plot(data.index, data[country_code] / 1e12, label=label, marker='o', linestyle='-')

    ax.set_title("Comparaison du PIB des pays d'Asie de l'Est", fontsize=16)
    ax.set_xlabel("Année", fontsize=12)
    ax.set_ylabel("PIB (en billions de $ US)", fontsize=12)
    ax.legend(title="Pays", bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True)
    plt.tight_layout()
    
    plt.savefig("gdp_comparison.png")
    print("\nLe graphique de comparaison des PIB a été sauvegardé sous 'gdp_comparison.png'")

def process_and_display_data(data, column_name, display_name, country_map, unit_divisor=1, unit_name="", sort_ascending=False, float_format="{:,.2f}"):
    """
    Traite les données et affiche un classement.
    """
    if data is None or data.empty:
        print(f"Aucune donnée disponible pour {display_name}.")
        return None
    
    pivot = data.unstack(level=0)[column_name]
    cleaned_data = pivot.dropna(how='all', axis=0).dropna(how='all', axis=1)

    if cleaned_data.empty:
        print(f"Aucune donnée de {display_name} disponible pour la période sélectionnée après nettoyage.")
        return None

    print(f"\nDernières données de {display_name} disponibles :")
    latest_data = cleaned_data.ffill().iloc[-1] / unit_divisor
    
    df = pd.DataFrame(latest_data)
    df.columns = [f"{display_name} ({unit_name})"]
    df.index.name = "Pays"
    df.index = df.index.map(country_map)

    print(df.sort_values(by=df.columns[0], ascending=sort_ascending).to_string(float_format=float_format))
    return cleaned_data

def main():
    """
    Fonction principale pour analyser et comparer les données des pays.
    """
    print("Analyse et comparaison des données des pays d'Asie de l'Est")
    print("Source des données : Banque Mondiale")
    
    start_year = 2000
    end_year = 2022
    
    country_codes = list(COUNTRIES.keys())
    
    # Traitement du PIB
    gdp_data = fetch_wb_data(country_codes, GDP_INDICATOR, start_year, end_year)
    gdp_pivot_cleaned = process_and_display_data(gdp_data, 'PIB', 'PIB', COUNTRIES, unit_divisor=1e9, unit_name="milliards $")

    if gdp_pivot_cleaned is not None:
        plot_gdp_data(gdp_pivot_cleaned, COUNTRIES)

    # Traitement de la population
    population_data = fetch_wb_data(country_codes, POPULATION_INDICATOR, start_year, end_year)
    process_and_display_data(population_data, 'Population', 'Population', COUNTRIES, unit_divisor=1e6, unit_name="millions", float_format="{:,.0f}")

if __name__ == "__main__":
    main()
