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

from PySide6.QtWidgets import QGraphicsDropShadowEffect, QPushButton
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import QTimer, QEvent, Qt
import sys
from ui_main import *

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

from modules.customWidgets import *
from dependencies.flowLayout import FlowLayout
from modules.settingsWrapper import *
from settings.initiationDictionary import initiationDictionary
from modules.datasetObjects import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True
stylesheet="""
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # SET UI DEFINITIONS
        # //////////////////////////////////////////////////////////////
        self.uiDefinitions()
        self.show()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.data)
        widgets.buttonData.setStyleSheet(
            self.selectMenu(widgets.buttonData.styleSheet())
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
            [i for i in initiationDictionary["datasets"]["catalogueDatasets"]],
            key=lambda x: initiationDictionary["datasets"]["catalogueDatasets"][x][
                "name"
            ],
        )

        flowLayoutCatalogue = FlowLayout(widgets.frameCatalogueDatasets)

        for i in datasetList:
            newDatasetObject = Dataset(i)

            # instantiate dataset setttings Widget
            newDatasetSettingsWidget = DatasetSettingsWidget(
                widgets.frameAllSettings, newDatasetObject
            )
            self.datasetSettingsList.append(newDatasetSettingsWidget)

            newDatasetFrame = datasetFrame(
                widgets.frameCatalogueDatasets,
                newDatasetObject,
                self,
                widgets,
                newDatasetSettingsWidget,
            )

            flowLayoutCatalogue.addWidget(newDatasetFrame)
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)

        # instantiate hybrid datasets
        datasetList = sorted(
            [i for i in initiationDictionary["datasets"]["hybridDatasets"]],
            key=lambda x: initiationDictionary["datasets"]["hybridDatasets"][x]["name"],
        )

        flowLayoutHybridDatasets = FlowLayout(widgets.frameOtherDatasets)
        widgets.frameCatalogueDatasets.setLayout(flowLayoutHybridDatasets)

        for i in datasetList:
            newDatasetObject = Dataset(i)

            newDatasetSettingsWidget = DatasetSettingsWidget(
                widgets.frameAllSettings, newDatasetObject
            )
            self.datasetSettingsList.append(newDatasetSettingsWidget)


            newDatasetFrame = datasetFrame(
                widgets.frameOtherDatasets,
                newDatasetObject,
                self,
                widgets,
                newDatasetSettingsWidget,
            )

            flowLayoutHybridDatasets.addWidget(newDatasetFrame)
            widgets.verticalLayout.addWidget(newDatasetSettingsWidget)

        ############################################################################################
        # Log instantiation
        ############################################################################################
        try:
            self.flowLayoutLogs = FlowLayout(widgets.scrollAreaLogsButtons)
            
            pathList = []
            for directoryName, _, files in walk(UniversalSettingsWrapper.logFolder):
                for file in files:
                    pathList.append(f"{directoryName}\\{file}")
            
            for path in sorted(pathList, key= lambda x: getFileCreatedDate(x)):

                newMonthButton = logButton(
                    widgets.scrollAreaLogsButtons,
                    path,
                    widgets.textEditLogs,
                )
                self.flowLayoutLogs.addWidget(newMonthButton)
                newMonthButton.updateTextEdit()
        except:
            print_exc()

        ############################################################################################
        # Settings
        ############################################################################################

        self.universalSettingsInitiation()
        widgets.buttonApplySettings.clicked.connect(self.updateAllSettings)

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
            lambda: self.fileDialogueFile(widgets.buttonHtgLands)
        )
        widgets.buttonSwBcPath.clicked.connect(
            lambda: self.fileDialogueFile(widgets.buttonSwBcPath)
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
        universalSettingsDictionary = {
            "email": widgets.lineEditEmail.text(),
            "downloadFolder": widgets.lineEditDownloadFolder.text(),
            "archiveFolder": widgets.lineEditArchiveFolder.text(),
            "logFolder": widgets.lineEditLogFolder.text(),
        }

        universalPathsDictionary = {
            "htgLandsPath": widgets.lineEditHtgLands.text(),
            "soiPath": widgets.lineEditSoiAll.text(),
            "soiCorePath": widgets.lineEditCore.text(),
            "soiMarinePath": widgets.lineEditMarine.text(),
            "soiWhaPath": widgets.lineEditWha.text(),
            "aoiSwBcPath": widgets.lineEditSwBc.text(),
        }

        UniversalPathsWrapper.settingsWriter(universalPathsDictionary)
        UniversalSettingsWrapper.settingsWriter(universalSettingsDictionary)
        for i in self.datasetSettingsList:
            i.outputToSettings()

    def fileDialogueFolder(self, lineEdit):
        fileDialogueOutput = QFileDialog().getExistingDirectory()
        lineEdit.setText(fileDialogueOutput)

    def fileDialogueFile(self, lineEdit):
        fileDialogueOutput = QFileDialog().getOpenFileName()[0]
        lineEdit.setText(fileDialogueOutput)

    def buttonClick(self):
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
    
    sys.exit(app.exec_())


