from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add_beer(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database

    Args:
        name (str): Beer Name
        style (str): Beer Style
    """
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database

    Args:
        style (str): Beer Style
    """
    beers = get_beers_from_database(style)
    table = Table(title="Brewlog :beer_mug:")
    headers = [
        "id",
        "name",
        "style",
        "flavor",
        "image",
        "cost",
        "rate",
        "date",
    ]

    for header in headers:
        table.add_column(header, style="magenta")

    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)

    console.print(table)
