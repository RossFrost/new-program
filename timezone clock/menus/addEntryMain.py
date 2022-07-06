from cmath import e
from nturl2path import url2pathname
from menus.mainMenu import *
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit
)

class entryAdd(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

    def formFrame(self):
        layout      = QFormLayout()
        url         = QLabel()
        lineEdit    = QLineEdit()



