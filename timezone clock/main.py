import sys
from menus.mainMenu import *
from build import *

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = mainMenu()
    buildMainMenu(main)

    main.resize(800, 600)
    main.show()
    sys.exit(app.exec())