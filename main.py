from src.input_handler import get_session_data
from src.score import calculate_session_score
from src.score import score_to_status
from src.score import score_to_risk
from src.sail_size import windsurf_sail_size
from src.advice import activity_advice
from src.report import print_report

def main():
    data = get_session_data()

    score = calculate_session_score(data)
    status = score_to_status(score)
    risk = score_to_risk(score)

    sail_size = None
    if data["activity"] == "windsurf":
        sail_size = windsurf_sail_size(
            data["wind"],
            data["weight"],
            data["level"],
            data["gusts"]
        )

    advice = activity_advice(
        data["activity"],
        data["wind"],
        data["gusts"],
        data["direction"],
        data["level"]
    )

    print_report(data, status, risk, score, sail_size, advice)

if __name__ == "__main__":
    main()
