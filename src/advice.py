def windsurf_advice(wind, gusts):
    advice = []

    if wind >= 14:
        advice.append("Good conditions for planing.")
        advice.append("Use harness and footstraps if you are comfortable.")
    else:
        advice.append("Light wind session, focus on balance and technique.")

    if gusts - wind >= 7:
        advice.append("Be careful with gusts.")

    return advice

def catamaran_advice(wind, level):
    advice = []

    if wind >= 16:
        advice.append("Prepare for a sporty catamaran session.")
        advice.append("Check the mainsheet and be ready to ease the sail.")
    else:
        advice.append("Good conditions to work on steering and sail trim.")

    if level == "beginner" and wind >= 14:
        advice.append("A beginner crew should sail with an instructor.")

    return advice

def dinghy_advice(wind):
    advice = []

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

def activity_advice(activity, wind, gusts, direction, level):
    if activity == "windsurf":
        advice = windsurf_advice(wind, gusts)
    elif activity == "catamaran":
        advice = catamaran_advice(wind, level)
    else:
        advice = dinghy_advice(wind)

    advice.append(direction_advice(direction))
    return advice
