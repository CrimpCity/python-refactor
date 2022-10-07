import click
from click import Command


def hello() -> None:
    print("Hello!")


@click.command()
def display_hello() -> None:
    """Test CLI command that prints hello.

    Args: None.

    Returns: None.
    """
    hello()


# make PyCharm happy about Click Commands
display_hello: Command
