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
    data["wind"] = ask_number("Wind speed in knots: ")
    data["gusts"] = ask_number("Gusts in knots: ")
    data["direction"] = ask_choice(
        "Wind direction (onshore/offshore/sideshore): ",
        ["onshore", "offshore", "sideshore"]
    )
    data["weight"] = ask_number("Weight in kg: ")

    return data
