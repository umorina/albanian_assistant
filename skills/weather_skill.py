import requests
from config import LATITUDE, LONGITUDE, CITY

def get_weather():
    """
    Fetch current weather from Open-Meteo API and return a human-friendly string in Albanian.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true&timezone=Europe/Tirane"
    )
    try:
        response = requests.get(url)
        data = response.json()
        weather = data["current_weather"]
        temperature = weather["temperature"]
        windspeed = weather["windspeed"]
        weather_code = weather["weathercode"]

        # Simple mapping of weathercode to description (Albanian)
        weather_desc_map = {
            0: "qiell i pastër",
            1: "pak re",
            2: "mbi re",
            3: "shumë re",
            45: "mjegull",
            48: "mjegull me akull",
            51: "shiu i dobët",
            53: "shiu i moderuar",
            55: "shiu i fortë",
            56: "shi i ngrirë i dobët",
            57: "shi i ngrirë i fortë",
            61: "shiu i dobët",
            63: "shiu i moderuar",
            65: "shiu i fortë",
            66: "shi i ngrirë i dobët",
            67: "shi i ngrirë i fortë",
            71: "borë e dobët",
            73: "borë e moderuar",
            75: "borë e fortë",
            77: "granulat bore",
            80: "shira lokalë",
            81: "shira të shpërndara",
            82: "shira të forta",
            85: "borë lokalë",
            86: "borë e fortë",
            95: "tërmet dhe shira",
            96: "tërmet me shira të forta",
            99: "tërmet me borë"
        }

        description = weather_desc_map.get(weather_code, "mot i panjohur")
        return f"Moti në {CITY} është {description}, temperatura {temperature}°C dhe era {windspeed} km/h."
    except Exception as e:
        print("Error fetching weather:", e)
        return f"Më vjen keq, nuk mund të marr motin në {CITY} tani."
