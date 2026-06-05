from src.constants import LEVEL_FACTOR
from src.constants import ACTIVITY_FACTOR
from src.constants import IDEAL_WIND

def wind_penalty(wind, level):
    min_wind, max_wind = IDEAL_WIND[level]

    if wind < min_wind:
        return (min_wind - wind) * 2
    if wind > max_wind:
        return (wind - max_wind) * 4
    return 0

def gust_penalty(wind, gusts):
    gap = gusts - wind

    if gap <= 4:
        return 0
    if gap <= 8:
        return 10
    return 20

def direction_penalty(direction, level):
    if direction == "sideshore":
        return 0
    if direction == "onshore":
        return 5
    if level == "beginner":
        return 35
    return 25

def calculate_session_score(data):
    penalty = 0

    penalty += wind_penalty(data["wind"], data["level"])
    penalty += gust_penalty(data["wind"], data["gusts"])
    penalty += direction_penalty(data["direction"], data["level"])

    penalty *= LEVEL_FACTOR[data["level"]]
    penalty *= ACTIVITY_FACTOR[data["activity"]]

    score = 100 - penalty

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    return int(score)

def score_to_status(score):
    if score >= 80:
        return "Good session"
    if score >= 60:
        return "Sporty but manageable"
    if score >= 40:
        return "Risky session"
    return "Dangerous session"

def score_to_risk(score):
    if score >= 80:
        return "Low"
    if score >= 60:
        return "Medium"
    if score >= 40:
        return "High"
    return "Very high"
