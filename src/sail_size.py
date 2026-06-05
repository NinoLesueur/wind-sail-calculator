def light_wind_size(weight):
    if weight < 70:
        return "7.0 - 8.0 m²"
    return "7.5 - 8.5 m²"

def medium_wind_size(weight):
    if weight < 70:
        return "6.0 - 7.0 m²"
    return "6.5 - 7.5 m²"

def strong_wind_size(weight):
    if weight < 70:
        return "5.0 - 6.0 m²"
    return "5.5 - 6.5 m²"

def very_strong_wind_size(weight):
    if weight < 70:
        return "4.0 - 5.0 m²"
    return "4.5 - 5.5 m²"

def windsurf_sail_size(wind, weight):
    if wind < 10:
        return light_wind_size(weight)
    if wind < 16:
        return medium_wind_size(weight)
    if wind < 22:
        return strong_wind_size(weight)
    if wind < 28:
        return very_strong_wind_size(weight)
    return "3.5 - 4.5 m²"
