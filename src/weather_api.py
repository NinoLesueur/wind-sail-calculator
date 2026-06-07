import requests

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "wind_speed_10m,wind_direction_10m,wind_gusts_10m",
        "wind_speed_unit": "kn",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    weather = {
        "wind": current["wind_speed_10m"],
        "gusts": current["wind_gusts_10m"],
        "wind_degrees": current["wind_direction_10m"]
    }

    return weather

def degrees_to_direction(degrees):
    if degrees >= 315 or degrees < 45:
        return "north"
    if degrees >= 45 and degrees < 135:
        return "east"
    if degrees >= 135 and degrees < 225:
        return "south"
    return "west"
