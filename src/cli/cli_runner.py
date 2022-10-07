import click
from src.cli.commands.print_hello import display_hello
from src.cli.commands.print_message import display_message


@click.group()
def refactor_cli():
    pass


refactor_cli.add_command(display_hello)
refactor_cli.add_command(display_message)


if __name__ == "__main__":
    refactor_cli()
