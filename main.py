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
from modules.functionLib import *
from modules.dataSettings import *
import sys
import platform
from traceback import print_exc
from datetime import datetime, timedelta

from PySide6 import QtWidgets
from widgets.custom_grips.custom_grips import Widgets

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *



# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None,

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

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

                # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        #widgets.extraCloseColuQ2mnBtn.clicked.connect(openCloseLeftBox)

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

            # SET HACKS2
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.data)
        widgets.buttonData.setStyleSheet(UIFunctions.selectMenu(widgets.buttonData.styleSheet()))

        #Main left menu
        widgets.buttonData.clicked.connect(self.buttonClick)
        widgets.buttonLogs.clicked.connect(self.buttonClick)
        widgets.buttonDataSettings.clicked.connect(self.buttonClick)

        # tooltips
        widgets.buttonData.setToolTip("    Datasets")
        widgets.buttonLogs.setToolTip("    Logs")
        widgets.buttonDataSettings.setToolTip("    Data Settings")


        ############################################################################################
        #Dataset Controls
        #############################################################################################
        
        

        #Crown Tenures#
        #starting state
        try:
            widgets.qTreeCrownTenures.setHeaderLabel(f"Crown Tenures: {getFileCreatedDate(crownTenuresSettings.currentPath)}")
            widgets.qTreeCrownTenures.topLevelItem(0).child(1).setText(0, f"Size: {getsize(crownTenuresSettings.currentPath)/1000000:.2f} mb")  
        except:
            print_exc()
            
        widgets.qTreeCrownTenures.topLevelItem(0).child(0).setText(0, f"Hosted File Date: {(dataCurrency.crownTenures).date()} ")      
        widgets.qTreeCrownTenures.topLevelItem(0).child(2).setText(0, f"File Path: {crownTenuresSettings.currentPath}") 
        widgets.qTreeCrownTenures.topLevelItem(0).child(3).setText(0, f"Archive Folder: {crownTenuresSettings.archiveFolder}")               
        if getFileCreatedDate(crownTenuresSettings.currentPath) < (dataCurrency.crownTenures).date():
            widgets.qTreeCrownTenures.setStyleSheet("QHeaderView::section {border-radius: 5px; background: rgb(189, 147, 249);}")

        #qtreeCrownTenures functionality
        widgets.qTreeCrownTenures.expanded.connect(self.datasetResizeUp)
        widgets.qTreeCrownTenures.collapsed.connect(self.datasetResizeDown)
        widgets.buttonUpdateCrownTenures.clicked.connect(crownTenuresProcess)

        #Forest Tenures#
        #Starting state
        try:
            widgets.qTreeForestTenure.setHeaderLabel(f"Crown Tenures: {forestTenureSettings.createdDate}")
            widgets.qTreeForestTenure.topLevelItem(0).child(0).setText(0, "Hosted File Date: ")
            widgets.qTreeForestTenure.topLevelItem(0).child(1).setText(0, f"Size: {forestTenureSettings.size/1000000:.2f} mb")        
            widgets.qTreeForestTenure.topLevelItem(0).child(2).setText(0, f"File Path: {forestTenureSettings.currentPath}") 
            widgets.qTreeForestTenure.topLevelItem(0).child(3).setText(0, f"Archive Folder: {forestTenureSettings.archiveFolder}")
        except:
            print_exc()
            

    # Crown Tenuers methods
    def datasetResizeUp (self):
        widgets.frameCrownTenures.setSizePolicy(QSizePolicy.Ignored)

    def datasetResizeDown(self):
        widgets.frameCrownTenures.resize(300,111)
    
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    
    
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
            widgets.stackedWidget.setCurrentWidget(widgets.settings) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
