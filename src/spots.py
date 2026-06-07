SPOTS = {
    "penvins": {
        "name": "Penvins",
        "latitude": 47.506,
        "longitude": -2.732
    },
    "quiberon": {
        "name": "Quiberon",
        "latitude": 47.484,
        "longitude": -3.119
    },
    "la baule": {
        "name": "La Baule",
        "latitude": 47.286,
        "longitude": -2.392
    },
    "carnac": {
        "name": "Carnac",
        "latitude": 47.584,
        "longitude": -3.079
    }
}

def show_spots():
    print("Available spots:")
    for spot in SPOTS:
        print("-", SPOTS[spot]["name"])

def get_spot(name):
    key = name.strip().lower()
    if key in SPOTS:
        return SPOTS[key]
    return None
