# Wind Sail Calculator

Wind Sail Calculator is a small Python terminal tool that helps prepare a sailing, windsurfing, catamaran or dinghy session.

The program asks for the activity, level, wind speed, gusts, wind direction and weight. Then it gives a session status, a risk level, a recommended sail size for windsurfing and practical safety advice.

## Features

- Choose an activity: windsurf, catamaran or dinghy
- Choose a level: beginner, intermediate or advanced
- Enter wind speed and gusts
- Enter wind direction
- Enter rider weight
- Get a session status
- Get a risk level
- Get a recommended sail size for windsurfing
- Get advice depending on the activity and conditions

## Technologies

- Python 3

## Project structure

```text
wind-sail-calculator/
├── main.py
├── README.md
├── .gitignore
└── src/
    ├── __init__.py
    ├── input_handler.py
    ├── risk.py
    ├── sail_size.py
    ├── advice.py
    └── report.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/wind-sail-calculator.git
cd wind-sail-calculator
```

Run the program:

```bash
python3 main.py
```

## Example

```text
Wind Sail Calculator

Activity (windsurf/catamaran/dinghy): windsurf
Level (beginner/intermediate/advanced): intermediate
Wind speed in knots: 18
Gusts in knots: 25
Wind direction (onshore/offshore/sideshore): sideshore
Weight in kg: 63

==============================
        SESSION REPORT
==============================
Activity: windsurf
Level: intermediate
Wind: 18.0 knots
Gusts: 25.0 knots
Direction: sideshore

Session status: Sporty but possible
Risk level: Medium
Recommended sail size: 5.0 - 6.0 m²

Advice:
- Good conditions for planing.
- Use harness and footstraps if you are comfortable.
- Be careful with gusts.
- Sideshore wind: usually easier to manage.
```

## Safety note

This project gives simple advice based on basic sailing experience rules. It does not replace real weather analysis, instructor advice, local safety rules or official weather warnings.

## Future improvements

- Save sessions in a CSV file
- Add session history
- Add board volume advice
- Add more precise sail size recommendations
- Add weather API
- Add French language option

## Author

Nino Lesueur
