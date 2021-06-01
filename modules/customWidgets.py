from datetime import timedelta, date
from genericpath import getsize
from modules.functionLib import getFileCreatedDate, getCurrency
from os.path import split, splitext
from json import load
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from re import sub


class datasetFrame(QFrame):
    ''' A datasetFrame is the primary intterface for updating datasets in the updater. It consists of a QTree for presenting dataset information, An update button which starts the update process for that dataset, as well as settings button which brings the user to the settings for that particular dataset. Is itself a custom qframe'''
    def __init__(self, parent, settingsClass, processFunction):
        '''Initializes widget with parent widget, A dataset Setttings class, and the process function asssociated with that settings class'''
        super(datasetFrame, self).__init__(parent)

        # Attributes
        self.alias = settingsClass.alias
        self.name = settingsClass.name
        self.downloadFolder = settingsClass.downloadFolder
        self.archiveFolder = settingsClass.archiveFolder
        self.currentPath = settingsClass.currentPath
        self.updateDays = settingsClass.updateDays
        self.dataCatalogueId = settingsClass.dataCatalogueId
        self.multiplySizeCollapsed = 250
        self.multiplySizeExpanded = 400

        # get data currency from data catalogue API if Data has a data catalogue ID
        if self.dataCatalogueId != "N/A":
            try:
                self.hostedFileDate = getCurrency(self.dataCatalogueId)
            except:
                self.hostedFileDate = "Not Found"

        else:
            self.hostedFileDate = "N/A"

        # get information about local Current file, display "Not Found" if unable
        try:
            self.fileSize = f"{getsize(self.currentPath)/1000000:.2} mb"
            self.date = getFileCreatedDate(self.currentPath)
        except:
            self.fileSize = "Not Found"
            self.date = "Not Found"

        # functions on init
        self.initFrame()
        self.turnPurple()
        self.turnRed()

        # Signals and slots
        self.buttonUpdate.clicked.connect(processFunction)
        self.buttonUpdate.clicked.connect(self.turnPurple)
        self.qtree.expanded.connect(self.qtreeExpand)
        self.qtree.collapsed.connect(self.qtreeCollapse)

    def initFrame(self):
        '''Starting state for widget'''
        self.resize(QSize(self.multiplySizeCollapsed, 111))
        self.setObjectName(f"frame_{self.alias}")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QSize(500, 200))
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
        self.qtree.setMaximumSize(QSize(16777215, 16777212))
        self.qtree.header().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.qtree)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(f"layoutButtons_{self.alias}")
        self.buttonUpdate = QPushButton(self)
        self.buttonUpdate.setObjectName(f"buttonUpdate_{self.alias}")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
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
        self.buttonSettings.setMaximumSize(QSize(100, 16777215))

        self.layoutButtons.addWidget(self.buttonSettings)
        self.verticalLayout_4.addLayout(self.layoutButtons)
        self.setMinimumSize(QSize(self.multiplySizeCollapsed, 111))

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

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
        self.animation.setStartValue(QSize(self.multiplySizeCollapsed, 111))
        self.animation.setEndValue(QSize(self.multiplySizeExpanded, 200))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation.start()

    def qtreeCollapse(self):
        self.animationCollapse = QPropertyAnimation(self, b"minimumSize")
        self.animationCollapse.setDuration(400)
        self.animationCollapse.setStartValue(QSize(self.multiplySizeExpanded, 200))
        self.animationCollapse.setEndValue(QSize(self.multiplySizeCollapsed, 111))
        self.animationCollapse.setEasingCurve(QEasingCurve.InOutQuart)

        self.animationCollapse.start()

    def turnPurple(self):
        '''Turns QTree header purple when dataset is out of date'''
        # NOTE, could turn various colours depending on how out-of-date it is safe
        if (
            isinstance(self.date, date) == True
            and isinstance(self.hostedFileDate, date) == True
        ):
            if self.date < self.hostedFileDate - timedelta(days=self.updateDays):
                self.qtree.setStyleSheet(
                    "QHeaderView::section {border-radius: 5px; background: rgb(189, 147, 249); color: black}"
                )
                self.qtree.header().setVisible(True)

    def turnRed(self):
        '''Turns qTree headder red if there is a problem accessing the local File or BC data catalogue API Information About the data where applicable'''
        if "Not Found" in (self.date, self.hostedFileDate):
            self.qtree.setStyleSheet(
                "QHeaderView::section {border-radius: 5px; background: rgb(255,153,153); color:black}"
            )
            self.qtree.header().setVisible(True)


class logButton(QPushButton):
    '''Buttons for switching the view of log information. A custom qpushbutton.'''
    def __init__(self, parent, logFile, textEdit):
        '''Instantiated with the parent widget , the log file assoociated with the button, and  the QTextedit widget where the information will be displayed'''
        super(logButton, self).__init__(parent)
        self.logFile = logFile
        self.textEdit = textEdit

        #functions on init
        self.initButton()

        # signals and slots
        self.clicked.connect(self.updateTextEdit)

    def initButton(self):
        ''' Sttarting state for widget '''
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
        '''Updates target QTextedit widget with information from log and displays it in a fancy colour coordinated way '''
        
        # Read JSON Log into Python dictionary
        with open(self.logFile, "r") as log:
            logDictionary = load(log)["dates"]
        #clear textedit widget
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
                
                #Space between update events
                self.textEdit.append("\n")

