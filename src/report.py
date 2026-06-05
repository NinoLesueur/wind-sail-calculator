def print_report(data, status, risk, sail_size, advice):
    print()
    print("==============================")
    print("        SESSION REPORT")
    print("==============================")
    print("Activity:", data["activity"])
    print("Level:", data["level"])
    print("Wind:", str(data["wind"]), "knots")
    print("Gusts:", str(data["gusts"]), "knots")
    print("Direction:", data["direction"])
    print()
    print("Session status:", status)
    print("Risk level:", risk)

    if sail_size is not None:
        print("Recommended sail size:", sail_size)

    print()
    print("Advice:")
    for item in advice:
        print("-", item)
