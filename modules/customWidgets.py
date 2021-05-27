from datetime import timedelta, date
from genericpath import exists, getsize
from modules.functionLib import getFileCreatedDate
from modules.dataCurrency import getCurrency
from traceback import print_exc
from PySide6.QtWidgets import * 
from PySide6.QtGui import *
from PySide6.QtCore import *


class datasetFrame(QFrame):
    def __init__(self, parent, settingsClass, processFunction):
        super(datasetFrame, self).__init__(parent)
        
        #Attributes
        self.alias = settingsClass.alias
        self.name = settingsClass.name
        self.downloadFolder = settingsClass.downloadFolder       
        self.archiveFolder = settingsClass.archiveFolder
        self.currentPath = settingsClass.currentPath
        self.updateDays = settingsClass.updateDays
        self.multiplySizeCollapsed = len(self.name)*1.5+250
        self.multiplySizeExpanded = len(max([self.downloadFolder, self.currentPath, self.archiveFolder]))+400

        try:
            self.hostedFileDate = getCurrency(settingsClass.dataCatalogueId)
        except:
            self.hostedFileDate = "Not Found or N/A"   

        try:
            self.fileSize = getsize(self.currentPath)/1000000
            self.date = getFileCreatedDate(self.currentPath)
        except:
            self.fileSize = "Not Found"
            self.date = "Not Found"   
        
        #functions on init
        self.initFrame()
        self.turnPurple()

        #Signals and slots
        self.buttonUpdate.clicked.connect(processFunction)
        self.qtree.expanded.connect(self.qtreeExpand)
        self.qtree.collapsed.connect(self.qtreeCollapse)

    def initFrame(self):
        self.setMinimumSize(QSize(self.multiplySizeCollapsed, 111))
        self.frame = QFrame(self)
        self.frame.setObjectName(f"frame_{self.alias}")
        self.frame.setGeometry(QRect(0, 0, self.multiplySizeCollapsed, 111))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(500, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(f"verticalLayout_{self.alias}")
        self.qtree = QTreeWidget(self.frame)
        font = QFont()
        font.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
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
        #self.qtree.setStyleSheet(u"QHeaderView::section {border-radius: 5px; background: rgb(189, 147, 249);}")
        #self.qtree.header().setVisible(True)
        self.qtree.header().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.qtree)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(f"layoutButtons_{self.alias}")
        self.buttonUpdate = QPushButton(self.frame)
        self.buttonUpdate.setObjectName(f"buttonUpdate_{self.alias}")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonUpdate.sizePolicy().hasHeightForWidth())
        self.buttonUpdate.setSizePolicy(sizePolicy1)
        self.buttonUpdate.setMinimumSize(QSize(0, 0))
        self.buttonUpdate.setMaximumSize(QSize(16772155, 16777215))

        self.layoutButtons.addWidget(self.buttonUpdate)

        self.buttonSettings = QPushButton(self.frame)
        self.buttonSettings.setObjectName(f"buttonSettings_{self.alias}")
        self.buttonSettings.setMaximumSize(QSize(100, 16777215))

        self.layoutButtons.addWidget(self.buttonSettings)
        self.verticalLayout_4.addLayout(self.layoutButtons)
        
        
        self.retranslateUi()            

        QMetaObject.connectSlotsByName(self)
    

    def retranslateUi(self):
        ___qtreewidgetitem = self.qtree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", f"{self.name}", None));

        __sortingEnabled = self.qtree.isSortingEnabled()
        self.qtree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.qtree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Info:", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", f"Hosted File Date: {self.hostedFileDate}", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", f"Date: {self.date}", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", f"Size: {self.fileSize:.2} mb", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", f"File Path: {self.currentPath}", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", f"Archive Folder: {self.archiveFolder}", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Form", f"Download Folder: {self.downloadFolder}", None));
        self.qtree.setSortingEnabled(__sortingEnabled)
        

        self.buttonUpdate.setText(QCoreApplication.translate("Form", u"Update", None))
        self.buttonSettings.setText(QCoreApplication.translate("Form", u"Settings", None))
    
    def qtreeExpand(self):
        self.setMinimumSize(QSize(self.multiplySizeExpanded,175))
        self.frame.resize(self.multiplySizeExpanded,175)
        

    def qtreeCollapse(self):
        self.setMinimumSize(QSize(self.multiplySizeCollapsed,111))
        self.frame.resize(self.multiplySizeCollapsed, 111)

    def turnPurple(self):
        if isinstance(self.date, date) == True and isinstance(self.hostedFileDate, date) == True:
            if self.date < self.hostedFileDate - timedelta(days=self.updateDays):
                self.qtree.setStyleSheet("QHeaderView::section {border-radius: 5px; background: rgb(189, 147, 249);}")
                self.qtree.header().setVisible(True)


