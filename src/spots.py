SPOTS = {
    "penvins": {
        "name": "Penvins",
        "latitude": 47.506,
        "longitude": -2.732,
        "onshore": [(160, 290)],
        "offshore": [(330, 360), (0, 80)]
    },
    "quiberon": {
        "name": "Quiberon",
        "latitude": 47.484,
        "longitude": -3.119,
        "onshore": [(180, 300)],
        "offshore": [(0, 90)]
    },
    "la baule": {
        "name": "La Baule",
        "latitude": 47.286,
        "longitude": -2.392,
        "onshore": [(170, 260)],
        "offshore": [(330, 360), (0, 80)]
    },
    "carnac": {
        "name": "Carnac",
        "latitude": 47.584,
        "longitude": -3.079,
        "onshore": [(160, 260)],
        "offshore": [(330, 360), (0, 80)]
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

def angle_in_range(angle, start, end):
    if start <= end:
        return angle >= start and angle <= end
    return angle >= start or angle <= end

def angle_in_ranges(angle, ranges):
    for start, end in ranges:
        if angle_in_range(angle, start, end):
            return True
    return False

def get_local_direction(spot, degrees):
    if angle_in_ranges(degrees, spot["onshore"]):
        return "onshore"
    if angle_in_ranges(degrees, spot["offshore"]):
        return "offshore"
    return "sideshore"
