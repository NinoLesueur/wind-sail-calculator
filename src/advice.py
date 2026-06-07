def windsurf_advice(wind, gusts, level, risk):
    advice = []

    if risk == "Very high" or risk == "High":
        advice.append("Do not sail alone in these conditions.")
        advice.append("Use a smaller sail and stay close to the shore.")
        if level == "beginner":
            advice.append("These conditions are not suitable for a beginner.")
        return advice

    if wind < 10:
        advice.append("Light wind session, focus on balance and technique.")
    elif wind < 16:
        advice.append("Good conditions to work on progression and control.")
    elif wind < 22:
        advice.append("Good conditions for planing.")
        advice.append("Use harness and footstraps if you are comfortable.")
    else:
        advice.append("Strong wind session, keep control and reduce sail size.")

    if gusts - wind >= 6:
        advice.append("Be careful with gusts.")

    return advice

def catamaran_advice(wind, level, risk):
    advice = []

    if risk == "Very high" or risk == "High":
        advice.append("Avoid sailing without instructor or safety boat.")
        if level == "beginner":
            advice.append("These conditions are not suitable for a beginner crew.")
        return advice

    if wind >= 16:
        advice.append("Prepare for a sporty catamaran session.")
        advice.append("Check the mainsheet and be ready to ease the sail.")
    else:
        advice.append("Good conditions to work on steering and sail trim.")

    return advice

def dinghy_advice(wind, level, risk):
    advice = []

    if risk == "Very high" or risk == "High":
        advice.append("Avoid going out without safety support.")
        if level == "beginner":
            advice.append("These conditions are not suitable for a beginner.")
        return advice

    if wind >= 15:
        advice.append("Use hiking position and control the heel.")
    else:
        advice.append("Good conditions to practice tacks and gybes.")

    return advice

def direction_advice(direction):
    if direction == "offshore":
        return "Offshore wind: avoid going far from the shore."
    if direction == "onshore":
        return "Onshore wind: check waves and shore break."
    return "Sideshore wind: usually easier to manage."

def activity_advice(activity, wind, gusts, direction, level, risk):
    if activity == "windsurf":
        advice = windsurf_advice(wind, gusts, level, risk)
    elif activity == "catamaran":
        advice = catamaran_advice(wind, level, risk)
    else:
        advice = dinghy_advice(wind, level, risk)

    advice.append(direction_advice(direction))
    return advice
