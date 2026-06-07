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
            "[bold cyan]Wind Sail Calculator[/bold cyan]",
            border_style="blue"
        )
    )

def print_session_table(data):
    table = Table(show_header=False, box=None)
    table.add_column("Field", style="bold cyan", width=14)
    table.add_column("Value", style="white")

    table.add_row("Activity", data["activity"])
    table.add_row("Level", data["level"])
    table.add_row("Wind", str(data["wind"]) + " kt")
    table.add_row("Gusts", str(data["gusts"]) + " kt")
    table.add_row("Direction", data["direction"])
    table.add_row("Weight", str(data["weight"]) + " kg")

    console.print(Panel(table, title="Session Report", border_style="cyan"))

def print_scores(status, risk, score, sail_size):
    s_color = score_color(score)
    r_color = risk_color(risk)

    console.print("[bold]Session status:[/bold]", status)
    console.print("[bold]Risk level:[/bold]", "[" + r_color + "]" + risk + "[/" + r_color + "]")
    console.print("[bold]Session score:[/bold]", "[" + s_color + "]" + str(score) + "/100[/" + s_color + "]")

    if sail_size is not None:
        console.print("[bold]Recommended sail size:[/bold]", sail_size)

def print_advice(advice):
    console.print()
    console.print("[bold cyan]Advice[/bold cyan]")

    for item in advice:
        if "Offshore" in item or "shore break" in item or "gusts" in item:
            console.print("[yellow]⚠[/yellow]", item)
        else:
            console.print("[green]✓[/green]", item)

def print_report(data, status, risk, score, sail_size, advice):
    print_title()
    print_session_table(data)
    print_scores(status, risk, score, sail_size)
    print_advice(advice)
    console.print()
