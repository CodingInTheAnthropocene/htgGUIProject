from modules.settingsWrapper import *
from datetime import timedelta, date
from genericpath import getsize
from modules.universalFunctions import getFileCreatedDate, getCurrency
from modules.catalogueFunctions import *
from os.path import split, splitext
from json import load
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from re import sub
from traceback import print_exc


class datasetFrame(QFrame):
    """ A datasetFrame is the primary intterface for updating datasets in the updater. It consists of a QTree for presenting dataset information, An update button which starts the update process for that dataset, as well as settings button which brings the user to the settings for that particular dataset. Is itself a custom qframe"""

    def __init__(self, parent, dataset, updateFunction, mainWindow, mainWidgets, settingsWidget):
        """Initializes widget with parent widget, A dataset Setttings class, and the process function asssociated with that settings class"""
        super(datasetFrame, self).__init__(parent)

        # Attributes
        self.alias = dataset.alias
        self.name = dataset.name
        self.downloadFolder = dataset.downloadFolder
        self.archiveFolder = dataset.archiveFolder
        self.currentPath = dataset.currentPath
        self.updateFrequency = dataset.updateFrequency
        self.dataCatalogueIdList = dataset.dataCatalogueIdList
        self.xCollapsed= 250
        self.xExpanded = 400
        self.yCollapsed= 115
        self.yExpanded= 200
        self.mainWidgets=mainWidgets
        self.settingsWidget=settingsWidget
        self.mainWindow=mainWindow

        # get data currency from data catalogue API if Data has a data catalogue ID
        if self.dataCatalogueIdList != "N/A":
            try:
                self.hostedFileDate = getCurrency(self.dataCatalogueIdList)
            except:
                self.hostedFileDate = "Not Found"

        else:
            self.hostedFileDate = "N/A"

        # get information about local Current file, display "Not Found" if unable
        try:
            self.fileSize = f"{getsize(self.currentPath)/1000000} mb"
            self.date = getFileCreatedDate(self.currentPath)
        except:
            self.fileSize = "Not Found"
            self.date = "Not Found"

        # functions on init
        self.initFrame()
        try:          
            self.turnPurple()
            self.turnRed()
        except:
            print_exc()

        # Signals and slots
        self.buttonUpdate.clicked.connect(lambda: updateFunction())
        self.buttonSettings.clicked.connect(self.navigateToSettings)
        self.buttonUpdate.clicked.connect(self.turnPurple)
        self.qtree.expanded.connect(self.qtreeExpand)
        self.qtree.collapsed.connect(self.qtreeCollapse)

    def initFrame(self):
        """Starting state for widget""" 


        
        self.setGeometry(QRect(0, 0, self.xCollapsed,self.yCollapsed))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)  
        self.setSizePolicy(sizePolicy)
        
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        #self.setMaximumSize( self.xCollapsed, self.yCollapsed )
        #self.setMinimumSize( self.xCollapsed,self.yCollapsed)


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
        self.animation = QPropertyAnimation(self, b"minimumSize")
        self.animation.setDuration(400)
        self.animation.setStartValue(QSize(self.xCollapsed, self.yCollapsed))
        self.animation.setEndValue(QSize(self.xExpanded, self.yExpanded))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation.start()

    def qtreeCollapse(self):
        self.animationCollapse = QPropertyAnimation(self, b"minimumSize")
        self.animationCollapse.setDuration(400)
        self.animationCollapse.setStartValue(QSize(self.xExpanded, self.yExpanded))
        self.animationCollapse.setEndValue(QSize(self.xCollapsed, self.yCollapsed))
        self.animationCollapse.setEasingCurve(QEasingCurve.InOutQuart)

        self.animationCollapse.start()

    def turnPurple(self):
        """Turns QTree header purple when dataset is out of date"""
        # NOTE, could turn various colours depending on how out-of-date
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
        """Turns qTree headder red if there is a problem accessing the local File or BC data catalogue API Information About the data where applicable"""
        if "Not Found" in (self.date, self.hostedFileDate):
            self.qtree.setStyleSheet(
                "QHeaderView::section {border-radius: 5px; background: rgb(255,153,153); color:black}"
            )
            self.qtree.header().setVisible(True)
    
    def navigateToSettings(self):
        from modules.ui_functions import UIFunctions

        self.mainWidgets.stackedWidget.setCurrentWidget(self.mainWidgets.settings)
        self.mainWidgets.scrollAreaSettings.ensureWidgetVisible(self.settingsWidget)
        btn=self.mainWidgets.buttonDataSettings
        btnName = btn.objectName()
        UIFunctions.resetStyle(self.mainWindow, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  




class logButton(QPushButton):
    """Buttons for switching the view of log information. A custom qpushbutton."""

    def __init__(self, parent, logFile, textEdit):
        """Instantiated with the parent widget , the log file assoociated with the button, and  the QTextedit widget where the information will be displayed"""
        super(logButton, self).__init__(parent)
        self.logFile = logFile
        self.textEdit = textEdit

        # functions on init
        self.initButton()

        # signals and slots
        self.clicked.connect(self.updateTextEdit)

    def initButton(self):
        """ Sttarting state for widget """
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
        """Updates target QTextedit widget with information from log and displays it in a fancy colour coordinated way """

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


class DatasetSettingsWidget(QFrame):
    def __init__(self, parent, dataset):
        super(DatasetSettingsWidget, self).__init__(parent)
        self.widgetParent = parent

        self.datasetSettings = dataset.settingsWrapper
        self.datasetName=dataset.settingsWrapper.name
       

        self.initSettingsWidget()


        self.lineEditSettingsWidgetCurrentPath.setText(dataset.currentPath)
        self.lineEditSettingsWidgetArchiveFolder.setText(dataset.archiveFolder)
        self.lineEditSettingsWidgetUpdateFrequency.setText(str(dataset.updateFrequency))
        self.lineEditSettingsWidgetDownloadFolder.setText(dataset.downloadFolder)
        self.lineEditSettingsWidgetWorkspaceFolder.setText(
            dataset.arcgisWorkspaceFolder
        )

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

        if dataset.settingsWrapper.aoi == "marine":
            self.radioSettingsWidgetMarine.setChecked(True)
        elif dataset.settingsWrapper.aoi == "core":
            self.radioSettingsWidgetCore.setChecked(True)
        elif dataset.settingsWrapper.aoi == "wha":
            self.radioSettingsWidgetWha.setChecked(True)
        elif dataset.settingsWrapper.aoi == "swbc":
            self.radioSettingsWidgetSwBc.setChecked(True)

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

    def outputToSettings(self):
        if self.radioSettingsWidgetMarine.isChecked():
            soiValue = "marine"
        elif self.radioSettingsWidgetCore.isChecked():
            soiValue = "core"
        elif self.radioSettingsWidgetWha.isChecked():
            soiValue = "wha"
        elif self.radioSettingsWidgetSwBc.isChecked():
            soiValue = "swbc"

        dictionaryToSettings = {
            "currentPath": self.lineEditSettingsWidgetCurrentPath.text(),
            "archiveFolder": self.lineEditSettingsWidgetArchiveFolder.text(),
            "downloadFolder": self.lineEditSettingsWidgetDownloadFolder.text(),
            "workspaceFolder": self.lineEditSettingsWidgetWorkspaceFolder.text(),
            "soiArea": soiValue,
            "updateFrequency": int(self.lineEditSettingsWidgetUpdateFrequency.text()),
        }

        self.datasetSettings.settingsWriter(dictionaryToSettings)


    def radioButtonToggle(self, radioButton, lineEdit, fromSettings):
        if radioButton.isChecked():
            lineEdit.setText(fromSettings)
            lineEdit.setReadOnly(True)

        else:
            lineEdit.setReadOnly(False)

    def initSettingsWidget(self):

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

        self.verticalLayout_23.addWidget(self.labelSettingsWidget, 0 , Qt.AlignLeft)

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

    # setupUi

    def retranslateUi(self):

        self.labelSettingsWidget.setToolTip(
            QCoreApplication.translate("Form", "Click to hide", None)
        )
        self.labelSettingsWidget.setText(
            QCoreApplication.translate("Form", f"{self.datasetName}", None)
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

    # retranslateUi

