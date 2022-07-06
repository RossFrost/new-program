from menuFunctions import * 

class defaults:
    defaultLanguage = "english"
    defaultWinSize  = [300, 300]



class widgetProperties:
    class mainMenu:
        searchLabelCoordinates              = [0, 0]
        searchBarCoordinates                = [0, 1]
        searchButtonCoordinates             = [0, 2]

        scrollableContentCoordinates        = [0, 0]
        scrollableAddCoordinates            = [1, 0]

        searchLayoutCoordinates             = [0, 2]
        scrollableLayoutCoordinates         = [1, 2]

class variables:
    language = defaults.defaultLanguage
    property = widgetProperties.mainMenu
    text = readYAMLContents(language)
    