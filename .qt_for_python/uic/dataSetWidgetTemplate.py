# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataSetWidgetTemplate.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.frameDataset = QFrame(Form)
        self.frameDataset.setObjectName(u"frameDataset")
        self.frameDataset.setGeometry(QRect(70, 90, 251, 111))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameDataset.sizePolicy().hasHeightForWidth())
        self.frameDataset.setSizePolicy(sizePolicy)
        self.frameDataset.setMaximumSize(QSize(300, 200))
        self.frameDataset.setFrameShape(QFrame.StyledPanel)
        self.frameDataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameDataset)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qTreeDataset = QTreeWidget(self.frameDataset)
        font = QFont()
        font.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        self.qTreeDataset.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.qTreeDataset)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        self.qTreeDataset.setObjectName(u"qTreeDataset")
        self.qTreeDataset.setMaximumSize(QSize(16777215, 16777212))
        self.qTreeDataset.setStyleSheet(u"")
        self.qTreeDataset.header().setVisible(True)
        self.qTreeDataset.header().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.qTreeDataset)

        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.setObjectName(u"layoutButtons")
        self.buttonUpdate = QPushButton(self.frameDataset)
        self.buttonUpdate.setObjectName(u"buttonUpdate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonUpdate.sizePolicy().hasHeightForWidth())
        self.buttonUpdate.setSizePolicy(sizePolicy1)
        self.buttonUpdate.setMinimumSize(QSize(0, 0))
        self.buttonUpdate.setMaximumSize(QSize(16772155, 16777215))

        self.layoutButtons.addWidget(self.buttonUpdate)

        self.buttonSettings = QPushButton(self.frameDataset)
        self.buttonSettings.setObjectName(u"buttonSettings")
        self.buttonSettings.setMaximumSize(QSize(100, 16777215))

        self.layoutButtons.addWidget(self.buttonSettings)


        self.verticalLayout_4.addLayout(self.layoutButtons)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.qTreeDataset.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Dataset", None));

        __sortingEnabled = self.qTreeDataset.isSortingEnabled()
        self.qTreeDataset.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.qTreeDataset.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Info:", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"Hosted File Date:", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"Date:", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"Size: ", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"File Path: ", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"Archive Folder:", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Form", u"Download Folder:", None));
        self.qTreeDataset.setSortingEnabled(__sortingEnabled)

        self.buttonUpdate.setText(QCoreApplication.translate("Form", u"Update", None))
        self.buttonSettings.setText(QCoreApplication.translate("Form", u"Settings", None))
    # retranslateUi

