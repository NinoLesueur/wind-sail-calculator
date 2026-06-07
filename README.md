# Wind Sail Calculator

Wind Sail Calculator is a Python terminal application that helps prepare a sailing session based on wind conditions, rider level and activity type.

The tool asks for basic session information such as activity, level, wind speed, gusts, wind direction and rider weight. It then calculates a session score, risk level, windsurf sail size recommendation and practical advice.

This project was created as a personal tool related to sailing and windsurfing, with a focus on simple rules, readable code and a clean terminal interface.

## Features

- Choose an activity: windsurf, catamaran or dinghy
- Choose a level: beginner, intermediate or advanced
- Enter wind speed and gusts in knots
- Enter wind direction: onshore, offshore or sideshore
- Enter rider weight
- Calculate a session status
- Calculate a risk level
- Display a session score out of 100
- Recommend a sail size for windsurfing
- Display practical advice depending on conditions
- Clean terminal interface using Rich

## Technologies

- Python 3
- Rich

## Project structure

```text
wind-sail-calculator/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── __init__.py
    ├── input_handler.py
    ├── score.py
    ├── sail_size.py
    ├── advice.py
    └── report.py
