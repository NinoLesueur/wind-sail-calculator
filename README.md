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
```

## Installation

Clone the repository:

```bash
git clone https://github.com/NinoLesueur/wind-sail-calculator.git
cd wind-sail-calculator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python3 main.py
```

## Usage

The program asks for the session information directly in the terminal.

Example input:

```text
Activity (windsurf/catamaran/dinghy): windsurf
Level (beginner/intermediate/advanced): intermediate
Wind speed in knots: 18
Gusts in knots: 25
Wind direction (onshore/offshore/sideshore): sideshore
Weight in kg: 63
```

Example output:

```text
Wind Sail Calculator
Sailing session advisor

Session Report
Activity      windsurf
Level         intermediate
Wind          18.0 kt
Gusts         25.0 kt
Direction     sideshore
Weight        63.0 kg

Session status: Sporty but manageable
Risk level: Medium
Session score: 90/100
Recommended sail size: 5.5 - 6.5 m²

Advice
[OK] Good conditions for planing.
[OK] Use harness and footstraps if you are comfortable.
[!] Be careful with gusts.
```

## Calculation model

The session score is based on several simple sailing rules:

- Wind speed compared to the rider level
- Difference between wind speed and gusts
- Wind direction
- Activity type
- Rider level

The windsurf sail size recommendation is based on:

- Wind speed
- Rider weight
- Rider level
- Gust strength

The goal is not to replace a real weather forecast or instructor judgment, but to provide a quick and useful estimation before a session.

## Safety note

This tool gives basic advice based on simple sailing experience rules.

It does not replace:

- Official weather forecasts
- Local safety rules
- Instructor advice
- Personal judgment
- Real sea condition analysis

Always check the spot, weather forecast and safety conditions before going on the water.

## Future improvements

- Add real weather data from an API
- Search sailing conditions by spot name
- Add wind direction analysis depending on the spot
- Split safety score and fun score
- Add a dedicated safety warning system
- Add board volume advice for windsurfing
- Add session history
- Add CSV export
- Add a terminal preview screenshot
- Add a French language option

## Author

Nino Lesueur
