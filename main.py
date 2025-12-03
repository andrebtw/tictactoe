CLI_VERSION = False
from cli import cli
from game_gui import gui

if __name__ == "__main__":
    if CLI_VERSION:
        cli()
    else:
        gui()
