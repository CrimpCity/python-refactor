import click
from click import Command


def hello(message: str) -> None:
    print("Hello!")
    print("\t\t", message)


@click.command()
@click.argument("message")
def display_message(message: str) -> None:
    """Test CLI command that prints user message.

    Args:
        message: string, user input

    Returns: None.
    """
    hello(message)


# make PyCharm happy about Click Commands
display_message: Command
