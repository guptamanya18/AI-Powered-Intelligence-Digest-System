from rich.console import Console
from datetime import datetime

console = Console()

def log_info(message: str):
    console.print(f"[green][INFO][/green] {message}")

def log_warn(message: str):
    console.print(f"[yellow][WARN][/yellow] {message}")

def log_error(message: str):
    console.print(f"[red][ERROR][/red] {message}")

def log_step(step: str):
    console.print(f"\n[bold cyan]▶ {step}[/bold cyan]")
