from menus.mainMenu import mainMenu
from menus.mainMenu import entryAdd

def buildMainMenu(menu: mainMenu):
    mainMenu.focusFrame(menu)
    mainMenu.scrollFrame(menu)
    mainMenu.options(menu)

def buildAddEntryMain(menu: entryAdd):
    pass