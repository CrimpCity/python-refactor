"""Install the script to run refactoring project."""
from setuptools import setup


setup(
    name="project-refactor",
    version="0.1.0",
    packages=["src"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "refactor = src.cli.cli_runner:refactor_cli",
        ],
    },
)
