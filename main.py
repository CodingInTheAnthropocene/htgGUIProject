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
from modules.customWidgets import *
from modules.flowLayout import FlowLayout
from modules.settingsWrapper import *
from modules.initiationDictionary import initiationDictionary
from modules.datasetObjects import *


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
        
        self.datasetSettingsList = []

        # instantiate catalogue data sets
        datasetList = sorted(
            [i for i in initiationDictionary["datasets"]["catalogueDatasets"]], key=lambda x: initiationDictionary["datasets"]["catalogueDatasets"][x]["name"]
        )

        flowLayoutCatalogue= FlowLayout(widgets.frameCatalogueDatasets)
       
        

        for i in datasetList:
            newDatasetObject= Dataset(i)

            # instantiate dataset setttings Widget
            newDatasetSettingsWidget = DatasetSettingsWidget(widgets.frameAllSettings, newDatasetObject)
            self.datasetSettingsList.append(newDatasetSettingsWidget)

            newDatasetFrame = datasetFrame(widgets.frameCatalogueDatasets, newDatasetObject, newDatasetObject.catalogueUpdateProcess, self, widgets, newDatasetSettingsWidget)

            flowLayoutCatalogue.addWidget(newDatasetFrame) 
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)
      

        
        # instantiate hybrid datasets
        datasetList = sorted(
            [i for i in initiationDictionary["datasets"]["hybridDatasets"]], key=lambda x: initiationDictionary["datasets"]["hybridDatasets"][x]["name"]
        )

        flowLayoutHybridDatasets= FlowLayout(widgets.frameOtherDatasets)
        widgets.frameCatalogueDatasets.setLayout(flowLayoutHybridDatasets)

        
        for i in datasetList:
            newDatasetObject= Dataset(i)

            # instantiate dataset settings widget
            newDatasetSettingsWidget = DatasetSettingsWidget(widgets.frameAllSettings, newDatasetObject)
            self.datasetSettingsList.append(newDatasetSettingsWidget)

            newDatasetFrame = datasetFrame(widgets.frameOtherDatasets, newDatasetObject, newDatasetObject.catalogueUpdateProcess, self, widgets, newDatasetSettingsWidget)




            flowLayoutHybridDatasets.addWidget(newDatasetFrame)
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)
            
            

        ############################################################################################
        # Log instantiation
        ############################################################################################
        try:
            self.flowLayoutLogs = FlowLayout(widgets.scrollAreaLogsButtons)

            for directoryName, _, files in walk(UniversalSettingsWrapper.logFolder):
                for file in files:
                    newMonthButton = logButton(
                        widgets.scrollAreaLogsButtons,
                        f"{directoryName}\\{file}",
                        widgets.textEditLogs,
                    )
                    self.flowLayoutLogs.addWidget(newMonthButton)
                    newMonthButton.updateTextEdit()
        except:
            print_exc
        
        ############################################################################################
        # Settings
        ############################################################################################

        self.universalSettingsInitiation()
        widgets.buttonApplySettings.clicked.connect(self.updateAllSettings)
        

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # //////////////////////////////////////////////////////////////

    def universalSettingsInitiation(self):
        widgets.lineEditEmail.setText(UniversalSettingsWrapper.email)        
        widgets.lineEditDownloadFolder.setText(UniversalSettingsWrapper.downloadFolder)
        widgets.lineEditArchiveFolder.setText(UniversalSettingsWrapper.archiveFolder)
        widgets.lineEditLogFolder.setText(UniversalSettingsWrapper.logFolder)
        widgets.lineEditHtgLands.setText(UniversalPathsWrapper.htgLandsPath)
        widgets.lineEditSoiAll.setText(UniversalPathsWrapper.soiPath)
        widgets.lineEditCore.setText(UniversalPathsWrapper.soiCorePath)
        widgets.lineEditMarine.setText(UniversalPathsWrapper.soiMarinePath)
        widgets.lineEditWha.setText(UniversalPathsWrapper.soiWhaPath)
        widgets.lineEditSwBc.setText(UniversalPathsWrapper.aoiSwBcPath)
    

    def updateAllSettings(self):
        universalSettingsDictionary={
        "email":widgets.lineEditEmail.text(),
        "downloadFolder":widgets.lineEditDownloadFolder.text(),
        "archiveFolder":widgets.lineEditArchiveFolder.text(),
        "logFolder":widgets.lineEditLogFolder.text(),
        
        }

        universalPathsDictionary={
        "htgLandsPath":widgets.lineEditHtgLands.text(),

        "soiPath": widgets.lineEditSoiAll.text(),
        "soiCorePath":widgets.lineEditCore.text(),
        "soiMarinePath":widgets.lineEditMarine.text(),
        "soiWhaPath":widgets.lineEditWha.text(),
        "aoiSwBcPath":widgets.lineEditSwBc.text()
        }

        UniversalPathsWrapper.settingsWriter(universalPathsDictionary)
        UniversalSettingsWrapper.settingsWriter(universalSettingsDictionary)
        for i  in self.datasetSettingsList:
            i.outputToSettings()
        


    
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
