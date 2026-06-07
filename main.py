from src.input_handler import get_session_data
from src.score import calculate_scores
from src.score import score_to_status
from src.score import safety_to_risk
from src.sail_size import windsurf_sail_size
from src.advice import activity_advice
from src.report import print_report

def main():
    data = get_session_data()

    scores = calculate_scores(data)
    status = score_to_status(scores["overall"])
    risk = safety_to_risk(scores["safety"])

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
        data["level"],
        risk
    )

    print_report(data, status, risk, scores, sail_size, advice)

if __name__ == "__main__":
    main()
