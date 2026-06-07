from src.spots import show_spots
from src.spots import get_spot
from src.spots import get_local_direction
from src.weather_api import get_weather

def ask_choice(text, choices):
    value = input(text).strip().lower()

    while value not in choices:
        print("Invalid choice.")
        value = input(text).strip().lower()

    return value

def ask_number(text):
    value = input(text).strip()

    while not value.replace(".", "", 1).isdigit():
        print("Please enter a number.")
        value = input(text).strip()

    return float(value)

def get_manual_weather_data(data):
    data["wind"] = ask_number("Wind speed in knots: ")
    data["gusts"] = ask_number("Gusts in knots: ")

    data["direction"] = ask_choice(
        "Wind direction (onshore/offshore/sideshore): ",
        ["onshore", "offshore", "sideshore"]
    )

    return data

def get_api_weather_data(data):
    show_spots()
    spot_name = input("Spot name: ")
    spot = get_spot(spot_name)

    while spot is None:
        print("Unknown spot.")
        show_spots()
        spot_name = input("Spot name: ")
        spot = get_spot(spot_name)

    weather = get_weather(spot["latitude"], spot["longitude"])

    data["spot"] = spot["name"]
    data["wind"] = weather["wind"]
    data["gusts"] = weather["gusts"]
    data["wind_degrees"] = weather["wind_degrees"]
    data["direction"] = get_local_direction(spot, data["wind_degrees"])

    print()
    print("Weather loaded for", spot["name"])
    print("Wind:", str(data["wind"]), "kt")
    print("Gusts:", str(data["gusts"]), "kt")
    print("Direction:", str(data["wind_degrees"]), "degrees")
    print("Local direction:", data["direction"])

    override = ask_choice(
        "Override local direction? (yes/no): ",
        ["yes", "no"]
    )

    if override == "yes":
        data["direction"] = ask_choice(
            "Local wind direction (onshore/offshore/sideshore): ",
            ["onshore", "offshore", "sideshore"]
        )

    return data

def get_session_data():
    data = {}

    data["activity"] = ask_choice(
        "Activity (windsurf/catamaran/dinghy): ",
        ["windsurf", "catamaran", "dinghy"]
    )

    data["level"] = ask_choice(
        "Level (beginner/intermediate/advanced): ",
        ["beginner", "intermediate", "advanced"]
    )

    mode = ask_choice(
        "Weather mode (manual/api): ",
        ["manual", "api"]
    )

    data["weather_mode"] = mode

    if mode == "api":
        data = get_api_weather_data(data)
    else:
        data = get_manual_weather_data(data)

    data["weight"] = ask_number("Weight in kg: ")

    return data
