import os
import sys

def clear_screen()->None:
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        print("Clear command not found...", file=sys.stderr)
        exit(1)
