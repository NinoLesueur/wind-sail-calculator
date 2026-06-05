from src.input_handler import get_session_data
from src.risk import get_base_risk
from src.risk import update_risk_with_direction
from src.sail_size import windsurf_sail_size
from src.advice import activity_advice
from src.report import print_report

def main():
    print("Wind Sail Calculator")
    print()

    data = get_session_data()

    risk, status = get_base_risk(
        data["level"],
        data["wind"],
        data["gusts"]
    )
    risk = update_risk_with_direction(risk, data["direction"])

    sail_size = None
    if data["activity"] == "windsurf":
        sail_size = windsurf_sail_size(data["wind"], data["weight"])

    advice = activity_advice(
        data["activity"],
        data["wind"],
        data["gusts"],
        data["direction"],
        data["level"]
    )

    print_report(data, status, risk, sail_size, advice)

if __name__ == "__main__":
    main()
