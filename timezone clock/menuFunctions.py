from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)
import typing
from language import readYAMLContents

class addScrollItem:
    def inputProperties(input, widget, properties: typing.Dict):
        pass

    def buildScrollItem(default: typing.List, layout: QGridLayout) -> None:
        iterate = 0
        for entry in default:
            layout.addWidget(entry, 0, iterate)
            iterate += 1
                
    def addScrollItem(layout: QVBoxLayout, item: QGridLayout) -> None:
        container = QWidget()
        container.setLayout(item)
        layout.addWidget(container)



def getScrollItemTemplate():
    class scrollItemTemplate:
        layout      = QGridLayout()      

        title       = QLabel("test")
        price       = QLabel("test")
        timeEnding  = QLabel("test")
        timeLeft    = QLabel("test")
        edit        = QPushButton()

        items = [title, price, timeEnding, timeLeft, edit]
    return scrollItemTemplate
