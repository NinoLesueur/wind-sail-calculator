# Wind Sail Calculator

Wind Sail Calculator is a small Python terminal tool that helps prepare a sailing, windsurfing or catamaran session.

The program asks for the activity, level, wind speed, gusts, wind direction and weight, then gives a simple session status, a risk level and practical advice.

## Features

- Choose an activity: windsurf, catamaran or dinghy
- Choose a level: beginner, intermediate or advanced
- Enter wind speed and gusts
- Enter wind direction
- Enter rider weight
- Get a session status
- Get a risk level
- Get a recommended sail size for windsurfing
- Get safety advice depending on the conditions

## Technologies

- Python 3

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
Activity (windsurf/catamaran/dinghy): windsurf
Level (beginner/intermediate/advanced): intermediate
Wind speed in knots: 18
Gusts in knots: 25
Wind direction (onshore/offshore/sideshore): sideshore
Weight in kg: 63

Session status: Sporty but possible
Risk level: Medium
Recommended sail size: 5.5 - 6.5 m²
Advice:
- Good conditions for planing
- Use harness and footstraps if you are comfortable
- Be careful with gusts
```

## Future improvements

- Save sessions in a CSV file
- Add session history
- Add more precise sail size recommendations
- Add support for board volume
- Add weather API
- Add French language option

## Author

Nino Lesueur
