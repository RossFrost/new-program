from typing import (
    ClassVar,
    Type
)

from io import open

from yaml import (
    safe_load,
)

def readYAMLContents(language: str, raw: bool = False):
    FILE = safe_load(open("bin/languages/" + language + ".yml"))
    PROGRAM = FILE["PROGRAM"]

    class textBindings:
        class mainMenu:
            MAIN_MENU = PROGRAM["MAIN MENU"]
            SEARCH_BAR = MAIN_MENU["SEARCH BAR"]
            SCROLL = MAIN_MENU["SCROLL"]
            OPTIONS = MAIN_MENU["OPTIONS"]


    return textBindings