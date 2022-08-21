"""
main.py - Main module for application.Includes view and functionality for main window.
"""

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

from ui_main import *
from modules.customWidgets import *
from dependencies.flowLayout import FlowLayout
from modules.settingsWrapper import *
from configuration.initiationDictionary import initiationDictionary
from modules.datasetObjects import *

#Global variables
widgets = None
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

stylesheet="""
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """

class MainWindow(QMainWindow):
    """
    Main window for application.
    """
    def __init__(self):
        """
        Constructor method for main window.
        """        
        QMainWindow.__init__(self)
        
        # Set widgets as global 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # Set ui definitions  
        self.uiDefinitions()

        # show main window
        self.show()

        # Set home page and select menu/
        widgets.stackedWidget.setCurrentWidget(widgets.data)
        widgets.buttonData.setStyleSheet(
            self.selectMenu(widgets.buttonData.styleSheet())
        )

        # Signals and slots left menu
        widgets.buttonData.clicked.connect(self.buttonClick)
        widgets.buttonLogs.clicked.connect(self.buttonClick)
        widgets.buttonDataSettings.clicked.connect(self.buttonClick)
        widgets.buttonRefresh.clicked.connect(self.datasetReset)        

        # tooltips
        widgets.buttonData.setToolTip("   Datasets")
        widgets.buttonLogs.setToolTip("   Logs")
        widgets.buttonDataSettings.setToolTip("   Data Settings")
        widgets.buttonRefresh.setToolTip("   Refresh Datasets")

        # Instantiate custom layouts
        self.flowLayoutCatalogue = FlowLayout(widgets.frameCatalogueDatasets)
        self.flowLayoutHybridDatasets = FlowLayout(widgets.frameOtherDatasets)
        self.flowLayoutLogs = FlowLayout(widgets.scrollAreaLogsButtons)

        # instantiate universal settings wrapper
        self.universalSettingsWrapper = UniversalSettingsWrapper()

        # instantiate data sets and their corresponding custom widgets     
        self.datasetInstantiation()

        # instantiate logs
        try: 
            self.logInstantiation()
        except:
            print_exc()
        
        # instantiate universal settings
        self.universalSettingsInstantiation()

    def datasetInstantiation(self):
        """
        Instantiates datasets and their respective custom widgets
        """ 
        

        self.datasetList= []
        self.datasetFrameList = []
        self.datasetSettingsList = []

        # instantiate catalogue datasets from initiation dictionary
        self.catalogueDatasetList = sorted(
            [i for i in initiationDictionary["datasets"]["catalogueDatasets"]],
            key=lambda x: initiationDictionary["datasets"]["catalogueDatasets"][x][
                "name"
            ],
        )

        # for each catalogue dataset instantiate a DatasetSettingsWidget, and DatasetFrame, add them to respective layouts
        for i in self.catalogueDatasetList:
            newDatasetObject = Dataset(i)
            self.datasetList.append(newDatasetObject)

            newDatasetSettingsWidget = DatasetSettingsWidget(
                widgets.frameAllSettings, newDatasetObject, self
            )
            self.datasetSettingsList.append(newDatasetSettingsWidget)

            newDatasetFrame = DatasetFrame(
                widgets.frameCatalogueDatasets,
                newDatasetObject,
                self,
                widgets,
                newDatasetSettingsWidget,
            )

            self.datasetFrameList.append(newDatasetFrame)

            self.flowLayoutCatalogue.addWidget(newDatasetFrame)
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)

        # for each hybrid dataset, instantiate a DatasetSettingsWidget, and DatasetFrame, add them to respective layouts 
        self.hybridDatasetList = sorted(
            [i for i in initiationDictionary["datasets"]["hybridDatasets"]],
            key=lambda x: initiationDictionary["datasets"]["hybridDatasets"][x]["name"],
        )

        for i in self.hybridDatasetList:
            newDatasetObject = Dataset(i)
            self.datasetList.append(newDatasetObject)

            newDatasetSettingsWidget = DatasetSettingsWidget(
                widgets.frameAllSettings, newDatasetObject, self
            )
            self.datasetSettingsList.append(newDatasetSettingsWidget)


            newDatasetFrame = DatasetFrame(
                widgets.frameOtherDatasets,
                newDatasetObject,
                self,
                widgets,
                newDatasetSettingsWidget,
            )

            self.datasetFrameList.append(newDatasetFrame)

            self.flowLayoutHybridDatasets.addWidget(newDatasetFrame)
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)
    
    def datasetReset(self):
        """
        Resets all dataset related objects and widgets
        """        

        for i  in self.datasetSettingsList:
            i.deleteLater()

        for i  in self.datasetFrameList:
            try: 
                self.flowLayoutCatalogue.removeWidget(i)
            except:
                self.flowLayoutHybridDatasets.removeWidget(i)
            i.deleteLater()
            
        for i  in self.datasetList:
            del i
        
        for i in self.logWidgetList:
            self.flowLayoutLogs.removeWidget(i)
            del i
        
        self.datasetInstantiation()
        self.logInstantiation()

    def logInstantiation(self):
        """
        Generates buttons for log files, and displays Log for last button created
        """        
        
        # for all files in log folder, create a LogButton in order of the log created date
        buttonPathList = []
        self.logWidgetList=[]

        for directoryName, _, files in walk(self.universalSettingsWrapper.logFolder):
            for file in files:
                buttonPathList.append(f"{directoryName}\\{file}")
        
        for path in sorted(buttonPathList, key= lambda x: getFileCreatedDate(x)):

            newMonthButton = LogButton(
                widgets.scrollAreaLogsButtons,
                path,
                widgets.textEditLogs,
            )

            self.logWidgetList.append(newMonthButton)
            self.flowLayoutLogs.addWidget(newMonthButton)
            
            # display log from most recently created button  in textedit
            newMonthButton.updateTextEdit()
  
    def universalSettingsInstantiation(self):
        """
        Starting state for Universal settings. Instantiated as part of the main application. 
        """        

        widgets.lineEditEmail.setText(self.universalSettingsWrapper.email)
        widgets.lineEditDownloadFolder.setText(self.universalSettingsWrapper.downloadFolder)
        widgets.lineEditArchiveFolder.setText(self.universalSettingsWrapper.archiveFolder)
        widgets.lineEditLogFolder.setText(self.universalSettingsWrapper.logFolder)
        widgets.lineEditHtgLands.setText(self.universalSettingsWrapper.htgLandsPath)
        widgets.lineEditSoiAll.setText(self.universalSettingsWrapper.soiPath)
        widgets.lineEditCore.setText(self.universalSettingsWrapper.soiCorePath)
        widgets.lineEditMarine.setText(self.universalSettingsWrapper.soiMarinePath)
        widgets.lineEditWha.setText(self.universalSettingsWrapper.soiWhaPath)
        widgets.lineEditSwBc.setText(self.universalSettingsWrapper.aoiSwBcPath)

        # signals and slots for settings update button
        widgets.buttonApplySettings.clicked.connect(self.updateAllSettings)

        # display text from settings.json
        widgets.buttonCorePath.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditCore)
        )
        widgets.buttonMarinePath.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditMarine)
        )
        widgets.buttonMarinePath.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditMarine)
        )
        widgets.buttonSoiAll.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditSoiAll)
        )
        widgets.buttonHtgLands.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditHtgLands)
        )
        widgets.buttonSwBcPath.clicked.connect(
            lambda: self.fileDialogueFile(widgets.lineEditSwBc)
        )

        widgets.buttonDownloadPath.clicked.connect(
            lambda: self.fileDialogueFolder(widgets.lineEditDownloadFolder)
        )
        widgets.buttonArchiveFolderPath.clicked.connect(
            lambda: self.fileDialogueFolder(widgets.lineEditArchiveFolder)
        )
        widgets.buttonLogFolderPath.clicked.connect(
            lambda: self.fileDialogueFolder(widgets.lineEditLogFolder)
        )


    def updateAllSettings(self):
        """
        Write state of all settings to settings.json. Also does a dataset refresh so that new settings are available immediately.
        """        
        
        # get text from universal settings and store in  dictionary 
        universalSettingsDictionary = {
            "email": widgets.lineEditEmail.text(),
            "downloadFolder": widgets.lineEditDownloadFolder.text(),
            "archiveFolder": widgets.lineEditArchiveFolder.text(),
            "logFolder": widgets.lineEditLogFolder.text(),

            "htgLandsPath": widgets.lineEditHtgLands.text(),
            "soiPath": widgets.lineEditSoiAll.text(),
            "soiCorePath": widgets.lineEditCore.text(),
            "soiMarinePath": widgets.lineEditMarine.text(),
            "soiWhaPath": widgets.lineEditWha.text(),
            "aoiSwBcPath": widgets.lineEditSwBc.text()
        }

        # get text from universal path's and store in dictionary
        
        #write universal to settings.json
        self.universalSettingsWrapper.settingsWriter(universalSettingsDictionary)
        
        #write dataset settings to settings.json
        for i in self.datasetSettingsList:
            i.outputToSettings()

        # reset all datasets
        self.datasetReset()

    def fileDialogueFolder(self, lineEdit):
        """
        Open file dialogue for files
        """
        fileDialogueOutput = normpath(QFileDialog().getExistingDirectory())
        lineEdit.setText(fileDialogueOutput)

    def fileDialogueFile(self, lineEdit):
        """
        Open file dialogue for files
        """
        fileDialogueOutput = normpath(QFileDialog().getOpenFileName()[0])
        lineEdit.setText(fileDialogueOutput)

    def buttonClick(self):
        """
        Actions for left menu
        """
        # get button clicked
        btn = self.sender()
        btnName = btn.objectName()

        #  Show datasets
        if btnName == "buttonData":
            widgets.stackedWidget.setCurrentWidget(widgets.data)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # Show Logs
        if btnName == "buttonLogs":
            widgets.stackedWidget.setCurrentWidget(widgets.logs)
            self.resetStyle( btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # Show Data Settings
        if btnName == "buttonDataSettings":
            widgets.stackedWidget.setCurrentWidget(widgets.settings)
            self.resetStyle( btnName)  
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

    def resizeEvent(self, event):
        # Update Size Grips
        self.resize_grips()

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(self, getStyle):
        select = getStyle + stylesheet
        return select

    # DESELECT
    def deselectMenu(self,getStyle):
        deselect = getStyle.replace(stylesheet, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(self.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: self.maximize_restore())
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

 
        #STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.returStatus():
                self.maximize_restore()
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)


        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: self.maximize_restore())

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())


