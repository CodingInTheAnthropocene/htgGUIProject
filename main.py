# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////


from os.path import getsize
import sys
from ui_main import *

from PySide6 import QtWidgets
from widgets.custom_grips.custom_grips import Widgets

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from modules.functionLib import *
from modules.customWidgets import *
from modules.flowLayout import FlowLayout
from modules.geoprocessingFunctions import *


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Dataset Updater"
        description = "HTG Dataset Updater"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # SET UI DEFINITIONS
        # //////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColuQ2mnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////

        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # widgets.gridLayout_3.addWidget(QPushButton("hellO!!"))

        ###

        # SET HOME PAGE AND SELECT MENUbe
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.data)
        widgets.buttonData.setStyleSheet(
            UIFunctions.selectMenu(widgets.buttonData.styleSheet())
        )

        # Main left menu
        widgets.buttonData.clicked.connect(self.buttonClick)
        widgets.buttonLogs.clicked.connect(self.buttonClick)
        widgets.buttonDataSettings.clicked.connect(self.buttonClick)

        # tooltips
        widgets.buttonData.setToolTip("    Datasets")
        widgets.buttonLogs.setToolTip("    Logs")
        widgets.buttonDataSettings.setToolTip("    Data Settings")

        ############################################################################################
        # Dataset Instantiation
        #############################################################################################

        initiationFunctionDictionary = {
            crownTenuresSettings: crownTenuresGeoprocessing,
            forestHarvestingAuthoritySettings: forestHarvestingAuthorityProcess,
            forestManagedLicenceSettings: forestManagedLicenceProcess,
            harvestedAreasSettings: harvestedAreasProcess,
            parksRecreationDatasetsSettings: parksRecreationDatasetsProcess,
            parcelMapBCSettings: parcelMapBCProcess,
            digitalRoadAtlasSettings: digitalRoadAtlasProcess,
            alcAlrPolygonsSettings: alcAlrPolygonsProcess,
            environmentalRemediationSitesSettings: environmentalRemediationSitesProcess,
        }

        datasetList = sorted(
            [i for i in initiationFunctionDictionary], key=lambda x: x.name
        )

        self.flowLayoutDatasets = FlowLayout(widgets.frameDatasets)

        for i in datasetList:
            newDataSetFrame = datasetFrame(
                widgets.frameDatasets, i, initiationFunctionDictionary[i]
            )
            self.flowLayoutDatasets.addWidget(newDataSetFrame)

        ############################################################################################
        # Log instantiation
        ############################################################################################
        self.flowLayoutLogs = FlowLayout(widgets.scrollAreaLogsButtons)

        for directoryName, _, files in walk(universalSettings.logFolder):
            for file in files:
                newMonthButton = logButton(
                    widgets.scrollAreaLogsButtons,
                    f"{directoryName}\\{file}",
                    widgets.textEditLogs,
                )
                self.flowLayoutLogs.addWidget(newMonthButton)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # //////////////////////////////////////////////////////////////

    def buttonClick(self):
        # get button clicked
        btn = self.sender()
        btnName = btn.objectName()

        #  Show datasets
        if btnName == "buttonData":
            widgets.stackedWidget.setCurrentWidget(widgets.data)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Show Logs
        if btnName == "buttonLogs":
            widgets.stackedWidget.setCurrentWidget(widgets.logs)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Show Data Settings
        if btnName == "buttonDataSettings":
            widgets.stackedWidget.setCurrentWidget(widgets.settings)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    ############################################################################################
    # Dataset Instantiation
    #############################################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
