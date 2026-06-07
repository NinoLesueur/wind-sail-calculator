from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def score_color(score):
    if score >= 80:
        return "green"
    if score >= 60:
        return "yellow"
    if score >= 40:
        return "orange1"
    return "red"

def risk_color(risk):
    if risk == "Low":
        return "green"
    if risk == "Medium":
        return "yellow"
    if risk == "High":
        return "orange1"
    return "red"

def print_title():
    console.print()
    console.print(
        Panel.fit(
            "[bold cyan]Wind Sail Calculator[/bold cyan]\n[dim]Sailing session advisor[/dim]",
            border_style="blue"
        )
    )

def print_session_table(data):
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column("Field", style="bold cyan", width=12)
    table.add_column("Value", style="white", width=18)

    if "spot" in data:
        table.add_row("Spot", data["spot"])

    if "weather_mode" in data:
        table.add_row("Mode", data["weather_mode"])

    table.add_row("Activity", data["activity"])
    table.add_row("Level", data["level"])
    table.add_row("Wind", str(data["wind"]) + " kt")
    table.add_row("Gusts", str(data["gusts"]) + " kt")
    table.add_row("Direction", data["direction"])

    if "wind_degrees" in data:
        table.add_row("Wind angle", str(data["wind_degrees"]) + "°")

    table.add_row("Weight", str(data["weight"]) + " kg")

    console.print(
        Panel.fit(
            table,
            title="Session Report",
            border_style="cyan"
        )
    )

def print_scores(status, risk, scores, sail_size):
    safety_color = score_color(scores["safety"])
    fun_color = score_color(scores["fun"])
    overall_color = score_color(scores["overall"])
    r_color = risk_color(risk)

    console.print("[bold]Session status:[/bold]", status)
    console.print("[bold]Risk level:[/bold]", "[" + r_color + "]" + risk + "[/" + r_color + "]")
    console.print("[bold]Safety score:[/bold]", "[" + safety_color + "]" + str(scores["safety"]) + "/100[/" + safety_color + "]")
    console.print("[bold]Fun score:[/bold]", "[" + fun_color + "]" + str(scores["fun"]) + "/100[/" + fun_color + "]")
    console.print("[bold]Overall score:[/bold]", "[" + overall_color + "]" + str(scores["overall"]) + "/100[/" + overall_color + "]")

    if sail_size is not None:
        console.print("[bold]Recommended sail size:[/bold]", sail_size)

def is_warning(item):
    warning_words = [
        "avoid",
        "dangerous",
        "not suitable",
        "do not",
        "be careful",
        "offshore",
        "shore break",
        "strong wind",
        "stay close",
        "smaller sail"
    ]

    text = item.lower()

    for word in warning_words:
        if word in text:
            return True

    return False

def print_advice(advice):
    console.print()
    console.print("[bold cyan]Advice[/bold cyan]")

    for item in advice:
        if is_warning(item):
            console.print("[yellow][!][/yellow]", item)
        else:
            console.print("[green][OK][/green]", item)

def print_report(data, status, risk, scores, sail_size, advice):
    print_title()
    print_session_table(data)
    print_scores(status, risk, scores, sail_size)
    print_advice(advice)
    console.print()
