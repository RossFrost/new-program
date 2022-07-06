
from properties import (
    variables,
    default
)
from menus.addEntryMain import entryAdd

from PySide6 import (
    QtCore,
    QtWidgets,
    QtGui
)

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QGridLayout,
    QVBoxLayout,
    QListWidget,
    QLayout
)



class mainMenu(QWidget): 


    def __init__(self):
        super().__init__()

        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        
    def focusFrame(self) -> None:

            label  = QLabel()
            search = QLineEdit()       
            button = QPushButton()
            layout = QGridLayout()         

            label.setText(variables.text.mainMenu.SEARCH_BAR["title"])
            button.setText(variables.text.mainMenu.SEARCH_BAR["search"])

            layout.addWidget(label,     variables.property.searchLabelCoordinates[0], 
                                        variables.property.searchLabelCoordinates[1])
            layout.addWidget(search, 
                                        variables.property.searchBarCoordinates[0], 
                                        variables.property.searchBarCoordinates[1])
            layout.addWidget(button, 
                                        variables.property.searchButtonCoordinates[0], 
                                        variables.property.searchButtonCoordinates[1])

            self.mainLayout.addLayout(layout, 
                                        variables.property.searchLayoutCoordinates[0],
                                        variables.property.searchLayoutCoordinates[1])

    def scrollFrame(self):
        scroll       = QListWidget()
        add          = QPushButton()
        layout       = QGridLayout()
        scrollLayout = QVBoxLayout()

        add.setText(variables.property.SCROLL["add"])                

        layout.addWidget(scroll, variables.property.scrollableContentCoordinates[0],
                                    variables.property.scrollableContentCoordinates[1])

        layout.addWidget(add, variables.property.scrollableAddCoordinates[0],
                                variables.property.scrollableAddCoordinates[1])

        scroll.setLayout(scrollLayout)

        self.mainLayout.addLayout(layout,
                                    variables.property.scrollableLayoutCoordinates[0],
                                    variables.property.scrollableLayoutCoordinates[1])
        
        self.entryAdd = entryAdd()
        add.clicked.connect(
                            lambda: [
                                     self.entryAdd.show(), 
                                     self.entryAdd.resize(300, 300)
                                    ]
                            )

    def options(self):
        pass
            

        

