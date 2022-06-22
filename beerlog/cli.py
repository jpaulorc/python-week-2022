import typer

main = typer.Typer(help="Beer Management Application")


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
    print(name, style)


@main.command("list")
def list_beers(style: str):
    """Lists beers in database

    Args:
        style (str): Beer Style
    """
    print(style)
