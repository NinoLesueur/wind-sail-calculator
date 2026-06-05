def round_sail_size(size):
    return round(size * 2) / 2

def min_max_size(size):
    min_size = size - 0.5
    max_size = size + 0.5

    if min_size < 2.0:
        min_size = 2.0

    return str(min_size) + " - " + str(max_size) + " m²"

def level_max_size(level):
    if level == "beginner":
        return 5.5
    if level == "intermediate":
        return 7.0
    return 8.0

def level_adjustment(level):
    if level == "beginner":
        return -1.0
    if level == "advanced":
        return 0.5
    return 0

def gust_adjustment(wind, gusts):
    if gusts - wind > 8:
        return -0.5
    if gusts - wind > 5:
        return -0.2
    return 0

def base_sail_size(wind, weight):
    if wind < 8:
        size = 6.0
    elif wind < 11:
        size = 6.5
    elif wind < 14:
        size = 6.2
    elif wind < 17:
        size = 6.0
    elif wind < 20:
        size = 5.5
    elif wind < 24:
        size = 4.7
    elif wind < 28:
        size = 4.2
    else:
        size = 3.7

    if weight < 60:
        size -= 0.3
    elif weight > 85:
        size += 0.7
    elif weight > 75:
        size += 0.5
    elif weight > 68:
        size += 0.3

    return size

def windsurf_sail_size(wind, weight, level, gusts):
    if wind <= 0:
        return "Unknown"

    size = base_sail_size(wind, weight)
    size += level_adjustment(level)
    size += gust_adjustment(wind, gusts)

    max_size = level_max_size(level)
    if size > max_size:
        size = max_size

    if size < 2.5:
        size = 2.5

    size = round_sail_size(size)

    return min_max_size(size)
