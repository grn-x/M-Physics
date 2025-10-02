import json
import os

import numpy as np
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SoSy_KEY")
API_URL = os.getenv("SoSy_URL") + "rest/bodies/"

def fetch_data_from_api():
    """
    fetch data from the api; return False in tuple if request fails
    Returns:
        tuple: (success (bool), data (list))
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    fields = [
        "englishName", "isPlanet", "semimajorAxis", "density"
    ]
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()["bodies"]

        # relevant fields; remove non-planets; discard isPlanet field from selected data
        filtered_data = [
            {field: body.get(field) for field in fields if field != "isPlanet"}
            for body in data if body.get("isPlanet")
        ]
        return True, filtered_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return False, []

def data_supplier():
    """
    supply data for the plot; fallback to hardcoded values if api request fails
    returns:
        list: data to be used for plotting; structure comparable to fallback response
    """
    success, api_data = fetch_data_from_api()
    if success:
        # confirm api data
        print("Fetched data from API:")
        print("[\n\t" + ",\n\t".join(json.dumps(obj, separators=(',', ':')) for obj in api_data) + "\n]")
        return api_data
    else: #static fallback data
        return [
            {"englishName":"Uranus","semimajorAxis":2870658186,"density":1.27},
            {"englishName":"Neptune","semimajorAxis":4498396441,"density":1.638},
            {"englishName":"Jupiter","semimajorAxis":778340821,"density":1.3262},
            {"englishName":"Mars","semimajorAxis":227939200,"density":3.9341},
            {"englishName":"Mercury","semimajorAxis":57909050,"density":5.4291},
            {"englishName":"Saturn","semimajorAxis":1426666422,"density":0.6871},
            {"englishName":"Earth","semimajorAxis":149598023,"density":5.5136},
            {"englishName":"Venus","semimajorAxis":108208475,"density":5.243}
        ]

def plot_solar_system_data(data, equidistant_ticks=True):
    """
    plots solar system relations
    Args:
        data (list): list of dictionaries containing planet data; see data_supplier() for structure
    """
    planet_names = [item["englishName"] for item in data]
    distances_km = [item["semimajorAxis"] for item in data]
    densities = [item["density"] for item in data]

    plt.figure(figsize=(10, 6))
    plt.scatter(distances_km, densities, color='blue', edgecolor='black', s=100)

    for i, name in enumerate(planet_names):
        plt.text(distances_km[i], densities[i], name, fontsize=9, ha='right', va='bottom')

    # logarithmic scale
    plt.xscale('log')

    if equidistant_ticks:
        # equidistant ticks in log space
        log_min = int(np.floor(np.log10(min(distances_km))))
        log_max = int(np.ceil(np.log10(max(distances_km))))
        ticks = [10 ** i for i in range(log_min, log_max + 1)]
        plt.xticks(ticks, [f"{tick:.0e}" for tick in ticks])

    plt.xlabel('Distance from Sun (km, log scale)', fontsize=12)
    plt.ylabel('Density (g/cm³)', fontsize=12)
    plt.title('Planet Density vs Distance from Sun', fontsize=14)

    plt.grid(which='both', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = data_supplier()
    plot_solar_system_data(data)