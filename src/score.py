from src.constants import LEVEL_FACTOR
from src.constants import ACTIVITY_FACTOR
from src.constants import IDEAL_WIND

def clamp_score(score):
    if score < 0:
        return 0
    if score > 100:
        return 100
    return int(score)

def wind_safety_penalty(wind, level):
    min_wind, max_wind = IDEAL_WIND[level]

    if wind <= max_wind:
        return 0

    return (wind - max_wind) * 5

def wind_fun_penalty(wind, level):
    min_wind, max_wind = IDEAL_WIND[level]

    if wind < min_wind:
        return (min_wind - wind) * 6
    if wind > max_wind:
        return (wind - max_wind) * 3

    return 0

def gust_safety_penalty(wind, gusts):
    gap = gusts - wind

    if gap <= 4:
        return 0
    if gap <= 8:
        return 8
    if gap <= 12:
        return 18
    return 30

def gust_fun_penalty(wind, gusts):
    gap = gusts - wind

    if gap <= 4:
        return 0
    if gap <= 8:
        return 6
    if gap <= 12:
        return 12
    return 20

def direction_safety_penalty(direction, level):
    if direction == "sideshore":
        return 0

    if direction == "onshore":
        if level == "beginner":
            return 12
        return 6

    if level == "beginner":
        return 40
    if level == "intermediate":
        return 30
    return 20

def direction_fun_penalty(direction):
    if direction == "sideshore":
        return 0
    if direction == "onshore":
        return 8
    return 15

def calculate_safety_score(data):
    penalty = 0

    penalty += wind_safety_penalty(data["wind"], data["level"])
    penalty += gust_safety_penalty(data["wind"], data["gusts"])
    penalty += direction_safety_penalty(data["direction"], data["level"])

    penalty *= LEVEL_FACTOR[data["level"]]
    penalty *= ACTIVITY_FACTOR[data["activity"]]

    return clamp_score(100 - penalty)

def calculate_fun_score(data):
    penalty = 0

    penalty += wind_fun_penalty(data["wind"], data["level"])
    penalty += gust_fun_penalty(data["wind"], data["gusts"])
    penalty += direction_fun_penalty(data["direction"])

    if data["activity"] == "windsurf" and data["wind"] < 12:
        penalty += 15

    if data["activity"] == "catamaran" and data["wind"] < 8:
        penalty += 10

    if data["activity"] == "dinghy" and data["wind"] > 22:
        penalty += 10

    return clamp_score(100 - penalty)

def calculate_overall_score(safety_score, fun_score):
    score = safety_score * 0.65 + fun_score * 0.35
    return clamp_score(score)

def calculate_scores(data):
    safety_score = calculate_safety_score(data)
    fun_score = calculate_fun_score(data)
    overall_score = calculate_overall_score(safety_score, fun_score)

    return {
        "safety": safety_score,
        "fun": fun_score,
        "overall": overall_score
    }

def score_to_status(score):
    if score >= 85:
        return "Good session"
    if score >= 70:
        return "Manageable session"
    if score >= 50:
        return "Sporty or unstable session"
    if score >= 30:
        return "Risky session"
    return "Dangerous session"

def safety_to_risk(safety_score):
    if safety_score >= 75:
        return "Low"
    if safety_score >= 55:
        return "Medium"
    if safety_score >= 35:
        return "High"
    return "Very high"
