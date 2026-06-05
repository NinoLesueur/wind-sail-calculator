def beginner_risk(wind, gusts):
    if wind <= 8 and gusts <= 12:
        return "Low", "Easy session"
    if wind <= 14 and gusts <= 18:
        return "Medium", "Good but be careful"
    return "High", "Risky session"

def intermediate_risk(wind, gusts):
    if wind <= 10 and gusts <= 15:
        return "Low", "Light wind session"
    if wind <= 20 and gusts <= 26:
        return "Medium", "Sporty but possible"
    return "High", "Strong session"

def advanced_risk(wind, gusts):
    if wind <= 12 and gusts <= 18:
        return "Low", "Light wind session"
    if wind <= 28 and gusts <= 35:
        return "Medium", "Good strong wind session"
    return "High", "Dangerous session"

def get_base_risk(level, wind, gusts):
    if level == "beginner":
        return beginner_risk(wind, gusts)
    if level == "intermediate":
        return intermediate_risk(wind, gusts)
    return advanced_risk(wind, gusts)

def update_risk_with_direction(risk, direction):
    if direction != "offshore":
        return risk
    if risk == "Low":
        return "Medium"
    return "High"
