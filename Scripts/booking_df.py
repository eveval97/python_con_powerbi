#Con montos redondeados
#No olviden comentar los print()

import requests
import time
import pandas as pd
from geopy.geocoders import Nominatim

url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"

# Cabeceras de la API con datos personales
headers = {
    "x-rapidapi-host": "booking-com15.p.rapidapi.com",
    "x-rapidapi-key": "tuapikey"
}

#podemos cambiar las fechas de llegada y salida como necesitemos
arrival_date = "2025-03-10"
departure_date = "2025-03-15"

cities = [
    "Asunción, Paraguay",
    "Washington, USA",
    "Dublin, Ireland"
]

# Inicializamos el geolocalizador
geolocator = Nominatim(user_agent="booking_search")

data_list = []

for city in cities:
    location = geolocator.geocode(city)
    if not location:
        print(f"No se encontró la ubicación para {city}")
        continue

    # Separamos ciudad y país
    loc_split = city.split(",")
    city_name = loc_split[0].strip()
    country = loc_split[-1].strip() if len(loc_split) > 1 else ""

    # Estos son los parámetros de la API
    params = {
        "arrival_date": arrival_date,
        "departure_date": departure_date,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "room_number": 1,
        "languagecode": "es"
    }

    # Se hace la solicitud GET a la API
    response = requests.get(url, headers=headers, params=params)
    result_data = response.json()

    print(f"\nResultados para {city}:")
    print(result_data)

    hoteles = result_data.get("data", {}).get("result", [])
    for hotel in hoteles:
        # Extraemos el ID y nombre del hotel
        hotel_id = hotel.get("hotel_id")
        hotel_name = hotel.get("hotel_name_trans")

        # Obtener gross_amount y asegurarse de que sea un entero redondeado
        composite_price_breakdown = hotel.get("composite_price_breakdown", {})
        gross_amount_value = composite_price_breakdown.get("gross_amount", {}).get("value")

        try:
            # Convertimos a float, redondear y hacer cast a entero
            gross_amount_value = int(round(float(str(gross_amount_value).replace(",", ""))))
        except (ValueError, TypeError):
            gross_amount_value = None  # Si falla, asigna None

        record = {
            "hotel_id": hotel_id,
            "hotel_name": hotel_name,
            "gross_amount": gross_amount_value,
            "location": city,
            "country": country,
            "city": city_name,
            "checkin_date": arrival_date,
            "checkout_date": departure_date,
            "language_code": params["languagecode"],
            "sort_by": "default",
            "property_rating": None,
            "meals": None,
            "api_status": result_data.get("status", False)
        }
        data_list.append(record)

    time.sleep(1)
fact_hotels = pd.DataFrame(data_list)
fact_hotels.set_index("hotel_name", inplace=True)

from pandasql import sqldf
import matplotlib.pyplot as plt
import seaborn as sns

pysqldf = lambda q: sqldf(q, globals())

# Consulta SQL para traer hoteles con ciudad y gross_amount convertido en enteros sin comas
q = """
SELECT city, hotel_name, CAST(gross_amount AS INTEGER) AS gross_amount
FROM fact_hotels
ORDER BY city, gross_amount ASC;
"""

hotels_prices = pysqldf(q)

hotels_prices["gross_amount"] = hotels_prices["gross_amount"].astype("Int64")

print(hotels_prices)
print("\nDataFrame resultante:")
print(fact_hotels)
