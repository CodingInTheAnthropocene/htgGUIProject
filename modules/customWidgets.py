from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from datetime import timedelta, date
from genericpath import getsize
from os.path import split, splitext
from json import load
from re import sub
from traceback import print_exc

from modules.settingsWrapper import *
from modules.universalFunctions import getFileCreatedDate, getCurrency


class DatasetFrame(QFrame):
    """ 
    A datasetFrame is the primary interface for updating datasets in the updater. It consists of a QTree for presenting dataset information, an QPushbutton which starts the update process for that dataset, as well as QPushbutton which brings the user to the settings for that particular dataset. A custom QFrame.
    """

    def __init__(
        self, parent, dataset, mainWindow, mainWidgets, settingsWidget
    ):
        """
        Constructor method.

        :param parent: Parent widget
        :type parent: QWidet
        :param dataset: Dataset object
        :type dataset: Dataset
        :param mainWindow: Main window into which the Dataset Frame will be instantiated
        :type mainWindow: MainWindow
        :param mainWidgets: Widgets displayed in main window
        :type mainWidgets: Ui_MainWindow
        :param settingsWidget: DatasetSettingsWidget associated with dataset
        :type settingsWidget: DatasetSettingsWidget
        """    
        super(DatasetFrame, self).__init__(parent)

        # Attributes
        self.alias = dataset.alias
        self.name = dataset.name
        self.downloadFolder = dataset.downloadFolder
        self.archiveFolder = dataset.archiveFolder
        self.currentPath = dataset.currentPath
        self.updateFrequency = dataset.updateFrequency
        self.dataCatalogueIdList = dataset.dataCatalogueIdList
        self.xCollapsed = 250
        self.xExpanded = 500
        self.yCollapsed = 115
        self.yExpanded = 200
        self.mainWidgets = mainWidgets
        self.settingsWidget = settingsWidget
        self.mainWindow = mainWindow
        self.updateFunction = dataset.catalogueUpdateProcess

        # get data currency from data catalogue API if Data has a data catalogue ID
        if self.dataCatalogueIdList != "N/A":
            try:
                self.hostedFileDate = getCurrency(self.dataCatalogueIdList)
            except:
                self.hostedFileDate = "Not Found"

        else:
            self.hostedFileDate = "N/A"
            

        # get information about local current file, display "Not Found" if not found
        try:
            if arcpy.Describe(self.currentPath).dataType== "ShapeFile":
                self.fileSize = f"{getsize(self.currentPath)/1000000} mb"
                self.date = getFileCreatedDate(self.currentPath)
            
            else:
                self.date = getFileCreatedDate(arcpy.Describe(self.currentPath).path)
                self.fileSize = "gdb (can't calculate)"               
            
        except:
            self.fileSize = "Not Found"
            self.date = "Not Found"

        # functions on init
        self.initFrame()
        
        try:
            self.turnPurple()
            self.turnRed()
        except:
            print("Notification error")
            print_exc()

        # Signals and slots
        self.buttonUpdate.clicked.connect(self.updateFunction)
        self.buttonSettings.clicked.connect(self.navigateToSettings)
        self.buttonUpdate.clicked.connect(self.turnPurple)
        self.qtree.expanded.connect(self.qtreeExpand)
        self.qtree.collapsed.connect(self.qtreeCollapse)

    def initFrame(self):
        """
        Widget starting state
        """        
        self.setGeometry(QRect(0, 0, self.xCollapsed, self.yCollapsed))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.setSizePolicy(sizePolicy)

        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4 = QVBoxLayout(self)
        self.verticalLayout_4.setObjectName(f"verticalLayout_{self.alias}")

        self.qtree = QTreeWidget(self)
        font = QFont()
        font.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font)
        self.qtree.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.qtree)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.qtree.setObjectName(f"qTree_{self.alias}")
        self.qtree.header().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.qtree)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(f"layoutButtons_{self.alias}")

        self.buttonUpdate = QPushButton(self)
        self.buttonUpdate.setObjectName(f"buttonUpdate_{self.alias}")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.buttonUpdate.sizePolicy().hasHeightForWidth()
        )
        self.buttonUpdate.setSizePolicy(sizePolicy1)
        self.buttonUpdate.setMinimumSize(QSize(0, 0))
        self.buttonUpdate.setMaximumSize(QSize(16772155, 16777215))


        self.layoutButtons.addWidget(self.buttonUpdate)

        self.buttonSettings = QPushButton(self)
        self.buttonSettings.setObjectName(f"buttonSettings_{self.alias}")
        self.buttonSettings.setMaximumSize(QSize(16777215, 16777215))

        self.layoutButtons.addWidget(self.buttonSettings)
        self.verticalLayout_4.addLayout(self.layoutButtons)

        self.retranslateUi()

    def retranslateUi(self):
        qtreewidgetitem = self.qtree.headerItem()
        qtreewidgetitem.setText(
            0, QCoreApplication.translate("Form", f"{self.name}", None)
        )

        __sortingEnabled = self.qtree.isSortingEnabled()
        self.qtree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.qtree.topLevelItem(0)
        ___qtreewidgetitem1.setText(
            0, QCoreApplication.translate("Form", "Info:", None)
        )
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(
            0,
            QCoreApplication.translate(
                "Form", f"Hosted File Date: {self.hostedFileDate}", None
            ),
        )
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(
            0, QCoreApplication.translate("Form", f"Date: {self.date}", None)
        )
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)

        ___qtreewidgetitem4.setText(
            0, QCoreApplication.translate("Form", f"Size: {self.fileSize}", None)
        )

        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(
            0,
            QCoreApplication.translate("Form", f"File Path: {self.currentPath}", None),
        )
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(
            0,
            QCoreApplication.translate(
                "Form", f"Archive Folder: {self.archiveFolder}", None
            ),
        )
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(
            0,
            QCoreApplication.translate(
                "Form", f"Download Folder: {self.downloadFolder}", None
            ),
        )
        self.qtree.setSortingEnabled(__sortingEnabled)

        self.buttonUpdate.setText(QCoreApplication.translate("Form", "Update", None))
        self.buttonSettings.setText(
            QCoreApplication.translate("Form", "Settings", None)
        )


    def qtreeExpand(self):
        """
        Expands widget when info QTree is expanded
        """        
        self.animation = QPropertyAnimation(self, b"minimumSize")
        self.animation.setDuration(400)
        self.animation.setStartValue(QSize(self.xCollapsed, self.yCollapsed))
        self.animation.setEndValue(QSize(self.xExpanded, self.yExpanded))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def qtreeCollapse(self):
        """
        Collapses widget when info QTree is collapsed
        """       
        self.animationCollapse = QPropertyAnimation(self, b"minimumSize")
        self.animationCollapse.setDuration(400)
        self.animationCollapse.setStartValue(QSize(self.xExpanded, self.yExpanded))
        self.animationCollapse.setEndValue(QSize(self.xCollapsed, self.yCollapsed))
        self.animationCollapse.setEasingCurve(QEasingCurve.InOutQuart)

        self.animationCollapse.start()

    def turnPurple(self):
        """
        Turns QTree header purple when dataset is out of date based on update frequency  in Settings.
        """
        if (
            isinstance(self.date, date) == True
            and isinstance(self.hostedFileDate, date) == True
        ):
            if self.date < self.hostedFileDate - timedelta(days=self.updateFrequency):
                self.qtree.setStyleSheet(
                    "QHeaderView::section {border-radius: 5px; background: rgb(189, 147, 249); color: black}"
                )
                self.qtree.header().setVisible(True)

    def turnRed(self):
        """
        Turns QTree header red if there is a problem accessing the local file or info from BC data catalogue
        """
        if "Not Found" in (self.date, self.hostedFileDate):
            self.qtree.setStyleSheet(
                "QHeaderView::section {border-radius: 5px; background: rgb(255,153,153); color:black}"
            )
            self.qtree.header().setVisible(True)

    def navigateToSettings(self):
        """
        Navigates to corresponding DatasetSettingsWidget
        """        
        self.mainWidgets.stackedWidget.setCurrentWidget(self.mainWidgets.settings)
        self.mainWidgets.scrollAreaSettings.ensureWidgetVisible(self.settingsWidget)
        btn = self.mainWidgets.buttonDataSettings
        btnName = btn.objectName()
        self.mainWindow.resetStyle(btnName)
        btn.setStyleSheet(self.mainWindow.selectMenu(btn.styleSheet()))


class LogButton(QPushButton):
    """
    Buttons for switching the view of log information. A custom QPushbutton.
    """
    def __init__(self, parent, logFile, textEdit):
        """
        Constructor method

        :param parent: Parent Widget
        :type parent: QWidget
        :param logFile: JSON log file pat
        :type logFile: str
        :param textEdit: Log QTextEdit
        :type textEdit: QTextEdit
        """        

        super(LogButton, self).__init__(parent)
        self.logFile = logFile
        self.textEdit = textEdit

        # functions on init
        self.initButton()

        # signals and slots
        self.clicked.connect(self.updateTextEdit)

    def initButton(self):
        """ 
        Widget starting state.
        """
        fileName = splitext(split(self.logFile)[1])[0]
        self.setObjectName(f"button{fileName}")
        self.setGeometry(QRect(130, 120, 150, 30))
        self.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.setFont(font)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("background-color: rgb(52, 59, 72);")
        self.setText(fileName.replace("-", " "))
        icon = QIcon()
        icon.addFile(
            ":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.setIcon(icon)

    def updateTextEdit(self):
        """
        Updates target QTextedit widget with information from log and displays it in a fancy colour coordinated way.
        """
        try:
            # Read JSON Log into Python dictionary
            with open(self.logFile, "r") as log:
                logDictionary = load(log)["dates"]
            # clear textedit widget
            self.textEdit.clear()

            # display and colour date information  in TextEdit widget
            for dateEntry in logDictionary:
                self.textEdit.setTextColor(QColor.fromRgb(207, 249, 147))
                font = QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(12)
                font.setBold(True)
                self.textEdit.setCurrentFont(font)

                self.textEdit.append(f"{dateEntry}")
                dateEntry = logDictionary[dateEntry]["times"]

                # display and colour time information
                for timeEntry in dateEntry:
                    self.textEdit.setTextColor(QColor.fromRgb(189, 147, 249))
                    font = QFont()
                    font.setFamily("Segoe UI")
                    font.setPointSize(10)
                    font.setBold(True)
                    self.textEdit.setCurrentFont(font)

                    self.textEdit.append(f" {timeEntry}")
                    timeEntry = dateEntry[timeEntry]

                    # display and colour dataset attributes
                    for datasetAttribute in timeEntry:
                        self.textEdit.setTextColor(QColor.fromRgb(221, 221, 221))
                        font = QFont()
                        font.setFamily("Segoe UI")
                        font.setPointSize(9)
                        font.setBold(True)
                        self.textEdit.setCurrentFont(font)

                        # display Dataset attribute key/value pair Splitting camel case on capital letters
                        formattedDatasetAttribute = sub(
                            r"(\w)([A-Z])", r"\1 \2", datasetAttribute
                        ).title()
                        self.textEdit.append(
                            f"   {formattedDatasetAttribute}: {timeEntry[datasetAttribute]}"
                        )

                    # Space between update events
                    self.textEdit.append("\n")
        except:
            print("Log display error")

class DatasetSettingsWidget(QFrame):
    """
    Widget for controlling Dataset settings.
    """    
    def __init__(self, parent, dataset):
        """
        Constructor method

        :param parent: Parent widget
        :type parent: QWidget
        :param dataset: Associated Dataset
        :type dataset: Dataset
        """        
        super(DatasetSettingsWidget, self).__init__(parent)

        # attributes
        self.widgetParent = parent
        self.datasetSettings = dataset.settingsWrapper
        self.datasetName = dataset.settingsWrapper.name

        # show widget
        self.initSettingsWidget()

        # set text for lineEdits
        self.lineEditSettingsWidgetCurrentPath.setText(dataset.currentPath)
        self.lineEditSettingsWidgetArchiveFolder.setText(dataset.archiveFolder)
        self.lineEditSettingsWidgetUpdateFrequency.setText(str(dataset.updateFrequency))
        self.lineEditSettingsWidgetDownloadFolder.setText(dataset.downloadFolder)
        self.lineEditSettingsWidgetWorkspaceFolder.setText(
            dataset.arcgisWorkspaceFolder
        )
        self.lineEditSettingsWidgetFileName.setText(dataset.fileName)

        # Set lineEdit radio buttons
        if (
            dataset.settingsWrapper.downloadFolder
            == UniversalSettingsWrapper.downloadFolder
        ):
            self.radioSettingsWidgetDownloadFolder.setChecked(True)
            self.lineEditSettingsWidgetDownloadFolder.setReadOnly(True)

        if (
            dataset.settingsWrapper.archiveFolder
            == UniversalSettingsWrapper.archiveFolder
        ):
            self.radioSettingsWidgetArchiveFolder.setChecked(True)
            self.lineEditSettingsWidgetArchiveFolder.setReadOnly(True)

        if (
            dataset.settingsWrapper.arcgisWorkspaceFolder
            == UniversalSettingsWrapper.downloadFolder
        ):
            self.radioSettingsWidgetWorkspaceFolder.setChecked(True)
            self.lineEditSettingsWidgetWorkspaceFolder.setReadOnly(True)

        # set AOI radio buttons
        if dataset.settingsWrapper.aoi == "marine":
            self.radioSettingsWidgetMarine.setChecked(True)
        elif dataset.settingsWrapper.aoi == "core":
            self.radioSettingsWidgetCore.setChecked(True)
        elif dataset.settingsWrapper.aoi == "wha":
            self.radioSettingsWidgetWha.setChecked(True)
        elif dataset.settingsWrapper.aoi == "swbc":
            self.radioSettingsWidgetSwBc.setChecked(True)

        # signals and slots
        # radio button/lineEdit functionality
        self.radioSettingsWidgetDownloadFolder.toggled.connect(
            lambda: self.radioButtonToggle(
                self.radioSettingsWidgetDownloadFolder,
                self.lineEditSettingsWidgetDownloadFolder,
                dataset.settingsWrapper.downloadFolder,
            )
        )

        self.radioSettingsWidgetArchiveFolder.toggled.connect(
            lambda: self.radioButtonToggle(
                self.radioSettingsWidgetArchiveFolder,
                self.lineEditSettingsWidgetArchiveFolder,
                dataset.settingsWrapper.archiveFolder,
            )
        )

        self.radioSettingsWidgetWorkspaceFolder.toggled.connect(
            lambda: self.radioButtonToggle(
                self.radioSettingsWidgetWorkspaceFolder,
                self.lineEditSettingsWidgetWorkspaceFolder,
                dataset.settingsWrapper.arcgisWorkspaceFolder,
            )
        )

        # file dialogue buttons
        self.buttonSettingWidgetCurrentPath.clicked.connect(
            lambda: self.fileDialogueFile(self.lineEditSettingsWidgetCurrentPath)
        )
        
        self.buttonSettingsWidgetArchiveFolder.clicked.connect(
            lambda: self.fileDialogueFolder(self.lineEditSettingsWidgetArchiveFolder)
        )

        self.buttonSettingsWidgetDownloadFolder.clicked.connect(
            lambda: self.fileDialogueFolder(self.lineEditSettingsWidgetDownloadFolder)
        )

        self.buttonSettingsWidgetWorkspaceFolder.clicked.connect(
            lambda: self.fileDialogueFolder(self.lineEditSettingsWidgetWorkspaceFolder)
        )        


    def outputToSettings(self):
        """
        Output widget state to settings.json. This method is called from a button on the main page.
        """        
        if self.radioSettingsWidgetMarine.isChecked():
            soiValue = "marine"
        elif self.radioSettingsWidgetCore.isChecked():
            soiValue = "core"
        elif self.radioSettingsWidgetWha.isChecked():
            soiValue = "wha"
        elif self.radioSettingsWidgetSwBc.isChecked():
            soiValue = "swbc"

        archiveFolderValue = (
            "universal"
            if self.radioSettingsWidgetArchiveFolder.isChecked()
            else self.lineEditSettingsWidgetArchiveFolder.text()
        )

        downloadFolderValue = (
            "universal"
            if self.radioSettingsWidgetDownloadFolder.isChecked()
            else self.lineEditSettingsWidgetDownloadFolder.text()
        )

        arcgisWorkspaceFolderValue = (
            "download"
            if self.radioSettingsWidgetWorkspaceFolder.isChecked()
            else self.lineEditSettingsWidgetWorkspaceFolder.text()
        )

        dictionaryToSettings = {
            "fileName": self.lineEditSettingsWidgetFileName.text(),
            "currentPath": self.lineEditSettingsWidgetCurrentPath.text(),
            "archiveFolder": archiveFolderValue,
            "downloadFolder": downloadFolderValue,
            "arcgisWorkspaceFolder": arcgisWorkspaceFolderValue,
            "aoi": soiValue,
            "updateFrequency": int(self.lineEditSettingsWidgetUpdateFrequency.text()),
        }

        self.datasetSettings.settingsWriter(dictionaryToSettings)

    def radioButtonToggle(self, radioButton, lineEdit, fromSettings):
        """
        Changes corresponding lineEdit properties

        :param radioButton: Radio button
        :type radioButton: QRadioButton
        :param lineEdit: Line Edit
        :type lineEdit: QLineEdit
        :param fromSettings: Information in settings.json
        :type fromSettings: str
        """        
        # set lineEdit to read only if radio button checked
        if radioButton.isChecked():
            lineEdit.setText(fromSettings)
            lineEdit.setReadOnly(True)

        else:
            lineEdit.setReadOnly(False)

    def fileDialogueFile(self, lineEdit):
        """
        Open file dialogue for files
        """        
        fileDialogueOutput= QFileDialog().getOpenFileName()[0]
        lineEdit.setText(fileDialogueOutput)

    def fileDialogueFolder(self, lineEdit):
        """
        Open file dialogue for folders
        """        
        fileDialogueOutput= QFileDialog().getExistingDirectory()
        lineEdit.setText(fileDialogueOutput)
    
    def initSettingsWidget(self):
        """
        Widget starting state
        """ 
        self.setObjectName("frameSettingsWidget")
        self.setGeometry(QRect(110, 70, 630, 395))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frameSettingsWidget = QFrame(self)
        self.frameSettingsWidget.setObjectName("frameSettingsWidget")
        self.frameSettingsWidget.setFrameShape(QFrame.StyledPanel)
        self.frameSettingsWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frameSettingsWidget)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.labelSettingsWidget = QPushButton(self.frameSettingsWidget)
        self.labelSettingsWidget.setObjectName("labelSettingsWidget")

        # self.labelSettingsWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.labelSettingsWidget.setStyleSheet(
            'font: 700 15pt "Segoe UI Semibold"; color: rgb(147, 249, 240); border:none;'
        )

        self.horizontalLayout_43.addWidget(self.labelSettingsWidget, 0, Qt.AlignLeft)

        self.verticalLayout_23.addWidget(self.labelSettingsWidget, 0, Qt.AlignLeft)

        self.frameFileName = QFrame(self)
        self.frameFileName.setObjectName("frameFileName")
        self.frameFileName.setFrameShape(QFrame.StyledPanel)
        self.frameFileName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frameFileName)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.labelFileName = QLabel(self.frameFileName)
        self.labelFileName.setObjectName("labelFileName")
        self.labelFileName.setMaximumSize(QSize(110, 16777215))
        self.labelFileName.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_20.addWidget(self.labelFileName)

        self.lineEditSettingsWidgetFileName = QLineEdit(self.frameFileName)
        self.lineEditSettingsWidgetFileName.setObjectName(
            "lineEditSettingsWidgetFileName"
        )
        self.lineEditSettingsWidgetFileName.setMinimumSize(QSize(200, 25))
        self.lineEditSettingsWidgetFileName.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_20.addWidget(
            self.lineEditSettingsWidgetFileName, 0, Qt.AlignLeft
        )
        self.verticalLayout_23.addWidget(self.frameFileName, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEditSettingsWidgetCurrentPath = QLineEdit(self.frame_3)
        self.lineEditSettingsWidgetCurrentPath.setObjectName(
            "lineEditSettingsWidgetCurrentPath"
        )
        self.lineEditSettingsWidgetCurrentPath.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetCurrentPath.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEditSettingsWidgetCurrentPath)

        self.buttonSettingWidgetCurrentPath = QPushButton(self.frame_3)
        self.buttonSettingWidgetCurrentPath.setObjectName(
            "buttonSettingWidgetCurrentPath"
        )
        self.buttonSettingWidgetCurrentPath.setMinimumSize(QSize(120, 25))
        self.buttonSettingWidgetCurrentPath.setMaximumSize(QSize(120, 16777215))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.buttonSettingWidgetCurrentPath.setFont(font)
        self.buttonSettingWidgetCurrentPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingWidgetCurrentPath.setStyleSheet(
            "background-color: rgb(52, 59, 72);"
        )
        icon = QIcon()
        icon.addFile(
            ":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonSettingWidgetCurrentPath.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.buttonSettingWidgetCurrentPath)

        self.verticalLayout_23.addWidget(self.frame_3)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_5.addWidget(self.label)

        self.radioSettingsWidgetDownloadFolder = QRadioButton(self.frame_2)
        self.radioSettingsWidgetDownloadFolder.setObjectName(
            "radioSettingsWidgetDownloadFolder"
        )

        self.horizontalLayout_5.addWidget(self.radioSettingsWidgetDownloadFolder)

        self.lineEditSettingsWidgetDownloadFolder = QLineEdit(self.frame_2)
        self.lineEditSettingsWidgetDownloadFolder.setObjectName(
            "lineEditSettingsWidgetDownloadFolder"
        )
        self.lineEditSettingsWidgetDownloadFolder.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetDownloadFolder.setMaximumSize(
            QSize(16777215, 16777215)
        )

        self.horizontalLayout_5.addWidget(self.lineEditSettingsWidgetDownloadFolder)

        self.buttonSettingsWidgetDownloadFolder = QPushButton(self.frame_2)
        self.buttonSettingsWidgetDownloadFolder.setObjectName(
            "buttonSettingsWidgetDownloadFolder"
        )
        self.buttonSettingsWidgetDownloadFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetDownloadFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetDownloadFolder.setFont(font)
        self.buttonSettingsWidgetDownloadFolder.setCursor(
            QCursor(Qt.PointingHandCursor)
        )
        self.buttonSettingsWidgetDownloadFolder.setStyleSheet(
            "background-color: rgb(52, 59, 72);"
        )
        self.buttonSettingsWidgetDownloadFolder.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.buttonSettingsWidgetDownloadFolder)

        self.verticalLayout_23.addWidget(self.frame_2)

        self.frame_4 = QFrame(self)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_7.addWidget(self.label_4)

        self.radioSettingsWidgetArchiveFolder = QRadioButton(self.frame_4)
        self.radioSettingsWidgetArchiveFolder.setObjectName(
            "radioSettingsWidgetArchiveFolder"
        )

        self.horizontalLayout_7.addWidget(self.radioSettingsWidgetArchiveFolder)

        self.lineEditSettingsWidgetArchiveFolder = QLineEdit(self.frame_4)
        self.lineEditSettingsWidgetArchiveFolder.setObjectName(
            "lineEditSettingsWidgetArchiveFolder"
        )
        self.lineEditSettingsWidgetArchiveFolder.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetArchiveFolder.setMaximumSize(
            QSize(16777215, 16777215)
        )

        self.horizontalLayout_7.addWidget(self.lineEditSettingsWidgetArchiveFolder)

        self.buttonSettingsWidgetArchiveFolder = QPushButton(self.frame_4)
        self.buttonSettingsWidgetArchiveFolder.setObjectName(
            "buttonSettingsWidgetArchiveFolder"
        )
        self.buttonSettingsWidgetArchiveFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetArchiveFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetArchiveFolder.setFont(font)
        self.buttonSettingsWidgetArchiveFolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingsWidgetArchiveFolder.setStyleSheet(
            "background-color: rgb(52, 59, 72);"
        )
        self.buttonSettingsWidgetArchiveFolder.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.buttonSettingsWidgetArchiveFolder)

        self.verticalLayout_23.addWidget(self.frame_4)

        self.frame_14 = QFrame(self)
        self.frame_14.setObjectName("frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_17.addWidget(self.label_14)

        self.radioSettingsWidgetWorkspaceFolder = QRadioButton(self.frame_14)
        self.radioSettingsWidgetWorkspaceFolder.setObjectName(
            "radioSettingsWidgetWorkspaceFolder"
        )

        self.horizontalLayout_17.addWidget(self.radioSettingsWidgetWorkspaceFolder)

        self.lineEditSettingsWidgetWorkspaceFolder = QLineEdit(self.frame_14)
        self.lineEditSettingsWidgetWorkspaceFolder.setObjectName(
            "lineEditSettingsWidgetWorkspaceFolder"
        )
        self.lineEditSettingsWidgetWorkspaceFolder.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetWorkspaceFolder.setMaximumSize(
            QSize(16777215, 16777215)
        )

        self.horizontalLayout_17.addWidget(self.lineEditSettingsWidgetWorkspaceFolder)

        self.buttonSettingsWidgetWorkspaceFolder = QPushButton(self.frame_14)
        self.buttonSettingsWidgetWorkspaceFolder.setObjectName(
            "buttonSettingsWidgetWorkspaceFolder"
        )
        self.buttonSettingsWidgetWorkspaceFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetWorkspaceFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetWorkspaceFolder.setFont(font)
        self.buttonSettingsWidgetWorkspaceFolder.setCursor(
            QCursor(Qt.PointingHandCursor)
        )
        self.buttonSettingsWidgetWorkspaceFolder.setStyleSheet(
            "background-color: rgb(52, 59, 72);"
        )
        self.buttonSettingsWidgetWorkspaceFolder.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.buttonSettingsWidgetWorkspaceFolder)

        self.verticalLayout_23.addWidget(self.frame_14)

        self.frame_5 = QFrame(self)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(110, 16777215))
        self.label_5.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_8.addWidget(self.label_5)

        self.radioSettingsWidgetCore = QRadioButton(self.frame_5)
        self.radioSettingsWidgetCore.setObjectName("radioSettingsWidgetCore")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetCore)

        self.radioSettingsWidgetMarine = QRadioButton(self.frame_5)
        self.radioSettingsWidgetMarine.setObjectName("radioSettingsWidgetMarine")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetMarine)

        self.radioSettingsWidgetWha = QRadioButton(self.frame_5)
        self.radioSettingsWidgetWha.setObjectName("radioSettingsWidgetWha")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetWha)

        self.radioSettingsWidgetSwBc = QRadioButton(self.frame_5)
        self.radioSettingsWidgetSwBc.setObjectName("radioSettingsWidgetSwBc")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetSwBc)

        self.verticalLayout_23.addWidget(self.frame_5)

        self.frame_15 = QFrame(self)
        self.frame_15.setObjectName("frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName("label_15")
        self.label_15.setMaximumSize(QSize(110, 16777215))
        self.label_15.setStyleSheet('font: 700 10pt "Segoe UI Semibold"')

        self.horizontalLayout_18.addWidget(self.label_15)

        self.lineEditSettingsWidgetUpdateFrequency = QLineEdit(self.frame_15)
        self.lineEditSettingsWidgetUpdateFrequency.setObjectName(
            "lineEditSettingsWidgetUpdateFrequency"
        )
        self.lineEditSettingsWidgetUpdateFrequency.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetUpdateFrequency.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEditSettingsWidgetUpdateFrequency)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName("label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.verticalLayout_23.addWidget(self.frame_15)

        self.frame_16 = QFrame(self)
        self.frame_16.setObjectName("frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")

        self.verticalLayout_23.addWidget(self.frame_16)

        self.retranslateUi()

    def retranslateUi(self):

        self.labelSettingsWidget.setToolTip(
            QCoreApplication.translate("Form", "Click to hide", None)
        )
        self.labelSettingsWidget.setText(
            QCoreApplication.translate("Form", f"{self.datasetName}", None)
        )
        self.labelFileName.setText(
            QCoreApplication.translate("Form", "File Name:  ", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("Form", "Current Path:  ", None)
        )
        self.buttonSettingWidgetCurrentPath.setText(
            QCoreApplication.translate("Form", "Select Path", None)
        )
        self.label.setText(
            QCoreApplication.translate("Form", "Download Folder: ", None)
        )
        self.radioSettingsWidgetDownloadFolder.setText(
            QCoreApplication.translate("Form", "Universal", None)
        )
        self.buttonSettingsWidgetDownloadFolder.setText(
            QCoreApplication.translate("Form", "Select Path", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Form", "Archive Folder: ", None)
        )
        self.radioSettingsWidgetArchiveFolder.setText(
            QCoreApplication.translate("Form", "Universal", None)
        )
        self.buttonSettingsWidgetArchiveFolder.setText(
            QCoreApplication.translate("Form", "Select Path", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("Form", "Workspace Folder:", None)
        )
        self.radioSettingsWidgetWorkspaceFolder.setText(
            QCoreApplication.translate("Form", "Download", None)
        )
        self.buttonSettingsWidgetWorkspaceFolder.setText(
            QCoreApplication.translate("Form", "Select Path", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("Form", "Area of Interest:", None)
        )
        self.radioSettingsWidgetCore.setText(
            QCoreApplication.translate("Form", "Core", None)
        )
        self.radioSettingsWidgetMarine.setText(
            QCoreApplication.translate("Form", "Marine", None)
        )
        self.radioSettingsWidgetWha.setText(
            QCoreApplication.translate("Form", "WHA", None)
        )
        self.radioSettingsWidgetSwBc.setText(
            QCoreApplication.translate("Form", "SW BC", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("Form", "Update Frequency:", None)
        )
        self.lineEditSettingsWidgetUpdateFrequency.setText("")
        self.label_16.setText(
            QCoreApplication.translate("Form", "Days after last posted update", None)
        )

class CustomGrip(QWidget):
    """
    Custom grips for window. Template class.
    """    
    def __init__(self, parent, position, disable_color = False):

        # SETUP UI
        QWidget.__init__(self)
        self.parent = parent
        self.setParent(parent)
        self.wi = Widgets()

        # SHOW TOP GRIP
        if position == Qt.TopEdge:
            self.wi.top(self)
            self.setGeometry(0, 0, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # GRIPS
            top_left = QSizeGrip(self.wi.top_left)
            top_right = QSizeGrip(self.wi.top_right)

            # RESIZE TOP
            def resize_top(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
                geo = self.parent.geometry()
                geo.setTop(geo.bottom() - height)
                self.parent.setGeometry(geo)
                event.accept()
            self.wi.top.mouseMoveEvent = resize_top

            # ENABLE COLOR
            if disable_color:
                self.wi.top_left.setStyleSheet("background: transparent")
                self.wi.top_right.setStyleSheet("background: transparent")
                self.wi.top.setStyleSheet("background: transparent")

        # SHOW BOTTOM GRIP
        elif position == Qt.BottomEdge:
            self.wi.bottom(self)
            self.setGeometry(0, self.parent.height() - 10, self.parent.width(), 10)
            self.setMaximumHeight(10)

            # GRIPS
            self.bottom_left = QSizeGrip(self.wi.bottom_left)
            self.bottom_right = QSizeGrip(self.wi.bottom_right)

            # RESIZE BOTTOM
            def resize_bottom(event):
                delta = event.pos()
                height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
                self.parent.resize(self.parent.width(), height)
                event.accept()
            self.wi.bottom.mouseMoveEvent = resize_bottom

            # ENABLE COLOR
            if disable_color:
                self.wi.bottom_left.setStyleSheet("background: transparent")
                self.wi.bottom_right.setStyleSheet("background: transparent")
                self.wi.bottom.setStyleSheet("background: transparent")

        # SHOW LEFT GRIP
        elif position == Qt.LeftEdge:
            self.wi.left(self)
            self.setGeometry(0, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            # RESIZE LEFT
            def resize_left(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
                geo = self.parent.geometry()
                geo.setLeft(geo.right() - width)
                self.parent.setGeometry(geo)
                event.accept()
            self.wi.leftgrip.mouseMoveEvent = resize_left

            # ENABLE COLOR
            if disable_color:
                self.wi.leftgrip.setStyleSheet("background: transparent")

        # RESIZE RIGHT
        elif position == Qt.RightEdge:
            self.wi.right(self)
            self.setGeometry(self.parent.width() - 10, 10, 10, self.parent.height())
            self.setMaximumWidth(10)

            def resize_right(event):
                delta = event.pos()
                width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
                self.parent.resize(width, self.parent.height())
                event.accept()
            self.wi.rightgrip.mouseMoveEvent = resize_right

            # ENABLE COLOR
            if disable_color:
                self.wi.rightgrip.setStyleSheet("background: transparent")


    def mouseReleaseEvent(self, event):
        self.mousePos = None

    def resizeEvent(self, event):
        if hasattr(self.wi, 'container_top'):
            self.wi.container_top.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'container_bottom'):
            self.wi.container_bottom.setGeometry(0, 0, self.width(), 10)

        elif hasattr(self.wi, 'leftgrip'):
            self.wi.leftgrip.setGeometry(0, 0, 10, self.height() - 20)

        elif hasattr(self.wi, 'rightgrip'):
            self.wi.rightgrip.setGeometry(0, 0, 10, self.height() - 20)

class Widgets(object):
    """
    Class used in custom grips. Static class. Template class.
    """    
    def top(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_top = QFrame(Form)
        self.container_top.setObjectName(u"container_top")
        self.container_top.setGeometry(QRect(0, 0, 500, 10))
        self.container_top.setMinimumSize(QSize(0, 10))
        self.container_top.setMaximumSize(QSize(16777215, 10))
        self.container_top.setFrameShape(QFrame.NoFrame)
        self.container_top.setFrameShadow(QFrame.Raised)
        self.top_layout = QHBoxLayout(self.container_top)
        self.top_layout.setSpacing(0)
        self.top_layout.setObjectName(u"top_layout")
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_left = QFrame(self.container_top)
        self.top_left.setObjectName(u"top_left")
        self.top_left.setMinimumSize(QSize(10, 10))
        self.top_left.setMaximumSize(QSize(10, 10))
        self.top_left.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.top_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_left.setFrameShape(QFrame.NoFrame)
        self.top_left.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_left)
        self.top = QFrame(self.container_top)
        self.top.setObjectName(u"top")
        self.top.setCursor(QCursor(Qt.SizeVerCursor))
        self.top.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top)
        self.top_right = QFrame(self.container_top)
        self.top_right.setObjectName(u"top_right")
        self.top_right.setMinimumSize(QSize(10, 10))
        self.top_right.setMaximumSize(QSize(10, 10))
        self.top_right.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.top_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.top_right.setFrameShape(QFrame.NoFrame)
        self.top_right.setFrameShadow(QFrame.Raised)
        self.top_layout.addWidget(self.top_right)

    def bottom(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.container_bottom = QFrame(Form)
        self.container_bottom.setObjectName(u"container_bottom")
        self.container_bottom.setGeometry(QRect(0, 0, 500, 10))
        self.container_bottom.setMinimumSize(QSize(0, 10))
        self.container_bottom.setMaximumSize(QSize(16777215, 10))
        self.container_bottom.setFrameShape(QFrame.NoFrame)
        self.container_bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QHBoxLayout(self.container_bottom)
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left = QFrame(self.container_bottom)
        self.bottom_left.setObjectName(u"bottom_left")
        self.bottom_left.setMinimumSize(QSize(10, 10))
        self.bottom_left.setMaximumSize(QSize(10, 10))
        self.bottom_left.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.bottom_left.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_left.setFrameShape(QFrame.NoFrame)
        self.bottom_left.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_left)
        self.bottom = QFrame(self.container_bottom)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setCursor(QCursor(Qt.SizeVerCursor))
        self.bottom.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom)
        self.bottom_right = QFrame(self.container_bottom)
        self.bottom_right.setObjectName(u"bottom_right")
        self.bottom_right.setMinimumSize(QSize(10, 10))
        self.bottom_right.setMaximumSize(QSize(10, 10))
        self.bottom_right.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.bottom_right.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.bottom_right.setFrameShape(QFrame.NoFrame)
        self.bottom_right.setFrameShadow(QFrame.Raised)
        self.bottom_layout.addWidget(self.bottom_right)

    def left(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.leftgrip = QFrame(Form)
        self.leftgrip.setObjectName(u"left")
        self.leftgrip.setGeometry(QRect(0, 10, 10, 480))
        self.leftgrip.setMinimumSize(QSize(10, 0))
        self.leftgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.leftgrip.setStyleSheet(u"background-color: rgb(255, 121, 198);")
        self.leftgrip.setFrameShape(QFrame.NoFrame)
        self.leftgrip.setFrameShadow(QFrame.Raised)

    def right(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        self.rightgrip = QFrame(Form)
        self.rightgrip.setObjectName(u"right")
        self.rightgrip.setGeometry(QRect(0, 0, 10, 500))
        self.rightgrip.setMinimumSize(QSize(10, 0))
        self.rightgrip.setCursor(QCursor(Qt.SizeHorCursor))
        self.rightgrip.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.rightgrip.setFrameShape(QFrame.NoFrame)
        self.rightgrip.setFrameShadow(QFrame.Raised)
