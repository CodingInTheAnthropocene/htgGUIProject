# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datasetSettingsWidgetTemplate.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(791, 613)
        self.frameSettingsWidget = QFrame(Form)
        self.frameSettingsWidget.setObjectName(u"frameSettingsWidget")
        self.frameSettingsWidget.setGeometry(QRect(110, 70, 630, 395))
        self.frameSettingsWidget.setFrameShape(QFrame.StyledPanel)
        self.frameSettingsWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frameSettingsWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelSettingsWidget = QFrame(self.frameSettingsWidget)
        self.labelSettingsWidget.setObjectName(u"labelSettingsWidget")
        self.labelSettingsWidget.setFrameShape(QFrame.StyledPanel)
        self.labelSettingsWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.labelSettingsWidget)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.pushButton_2 = QPushButton(self.labelSettingsWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"font: 700 15pt \"Segoe UI Semibold\"; color: rgb(147, 249, 240); border:none;")

        self.horizontalLayout_43.addWidget(self.pushButton_2, 0, Qt.AlignLeft)


        self.verticalLayout_23.addWidget(self.labelSettingsWidget)

        self.frame_3 = QFrame(self.frameSettingsWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEditSettingsWidgetCurrentPath = QLineEdit(self.frame_3)
        self.lineEditSettingsWidgetCurrentPath.setObjectName(u"lineEditSettingsWidgetCurrentPath")
        self.lineEditSettingsWidgetCurrentPath.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetCurrentPath.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEditSettingsWidgetCurrentPath)

        self.buttonSettingWidgetCurrentPath = QPushButton(self.frame_3)
        self.buttonSettingWidgetCurrentPath.setObjectName(u"buttonSettingWidgetCurrentPath")
        self.buttonSettingWidgetCurrentPath.setMinimumSize(QSize(120, 25))
        self.buttonSettingWidgetCurrentPath.setMaximumSize(QSize(120, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.buttonSettingWidgetCurrentPath.setFont(font)
        self.buttonSettingWidgetCurrentPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingWidgetCurrentPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSettingWidgetCurrentPath.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.buttonSettingWidgetCurrentPath)


        self.verticalLayout_23.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frameSettingsWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(110, 0))
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_5.addWidget(self.label)

        self.radioSettingsWidgetDownloadFolder = QRadioButton(self.frame_2)
        self.radioSettingsWidgetDownloadFolder.setObjectName(u"radioSettingsWidgetDownloadFolder")

        self.horizontalLayout_5.addWidget(self.radioSettingsWidgetDownloadFolder)

        self.lineEditSettingsWidgetDownloadFolder = QLineEdit(self.frame_2)
        self.lineEditSettingsWidgetDownloadFolder.setObjectName(u"lineEditSettingsWidgetDownloadFolder")
        self.lineEditSettingsWidgetDownloadFolder.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetDownloadFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEditSettingsWidgetDownloadFolder)

        self.buttonSettingsWidgetDownloadFolder = QPushButton(self.frame_2)
        self.buttonSettingsWidgetDownloadFolder.setObjectName(u"buttonSettingsWidgetDownloadFolder")
        self.buttonSettingsWidgetDownloadFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetDownloadFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetDownloadFolder.setFont(font)
        self.buttonSettingsWidgetDownloadFolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingsWidgetDownloadFolder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonSettingsWidgetDownloadFolder.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.buttonSettingsWidgetDownloadFolder)


        self.verticalLayout_23.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frameSettingsWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(110, 0))
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.radioSettingsWidgetArchiveFolder = QRadioButton(self.frame_4)
        self.radioSettingsWidgetArchiveFolder.setObjectName(u"radioSettingsWidgetArchiveFolder")

        self.horizontalLayout_7.addWidget(self.radioSettingsWidgetArchiveFolder)

        self.lineEditSettingsWidgetArchiveFolder = QLineEdit(self.frame_4)
        self.lineEditSettingsWidgetArchiveFolder.setObjectName(u"lineEditSettingsWidgetArchiveFolder")
        self.lineEditSettingsWidgetArchiveFolder.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetArchiveFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEditSettingsWidgetArchiveFolder)

        self.buttonSettingsWidgetArchiveFolder = QPushButton(self.frame_4)
        self.buttonSettingsWidgetArchiveFolder.setObjectName(u"buttonSettingsWidgetArchiveFolder")
        self.buttonSettingsWidgetArchiveFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetArchiveFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetArchiveFolder.setFont(font)
        self.buttonSettingsWidgetArchiveFolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingsWidgetArchiveFolder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonSettingsWidgetArchiveFolder.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.buttonSettingsWidgetArchiveFolder)


        self.verticalLayout_23.addWidget(self.frame_4)

        self.frame_14 = QFrame(self.frameSettingsWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.radioSettingsWidgetWorkspaceFolder = QRadioButton(self.frame_14)
        self.radioSettingsWidgetWorkspaceFolder.setObjectName(u"radioSettingsWidgetWorkspaceFolder")

        self.horizontalLayout_17.addWidget(self.radioSettingsWidgetWorkspaceFolder)

        self.lineSettingsWidgetWorkspaceFolder = QLineEdit(self.frame_14)
        self.lineSettingsWidgetWorkspaceFolder.setObjectName(u"lineSettingsWidgetWorkspaceFolder")
        self.lineSettingsWidgetWorkspaceFolder.setMinimumSize(QSize(0, 25))
        self.lineSettingsWidgetWorkspaceFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_17.addWidget(self.lineSettingsWidgetWorkspaceFolder)

        self.buttonSettingsWidgetWorkspaceFolder = QPushButton(self.frame_14)
        self.buttonSettingsWidgetWorkspaceFolder.setObjectName(u"buttonSettingsWidgetWorkspaceFolder")
        self.buttonSettingsWidgetWorkspaceFolder.setMinimumSize(QSize(120, 25))
        self.buttonSettingsWidgetWorkspaceFolder.setMaximumSize(QSize(120, 16777215))
        self.buttonSettingsWidgetWorkspaceFolder.setFont(font)
        self.buttonSettingsWidgetWorkspaceFolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettingsWidgetWorkspaceFolder.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonSettingsWidgetWorkspaceFolder.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.buttonSettingsWidgetWorkspaceFolder)


        self.verticalLayout_23.addWidget(self.frame_14)

        self.frame_5 = QFrame(self.frameSettingsWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(110, 16777215))
        self.label_5.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.radioSettingsWidgetCore = QRadioButton(self.frame_5)
        self.radioSettingsWidgetCore.setObjectName(u"radioSettingsWidgetCore")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetCore)

        self.radioSettingsWidgetMarine = QRadioButton(self.frame_5)
        self.radioSettingsWidgetMarine.setObjectName(u"radioSettingsWidgetMarine")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetMarine)

        self.radioSettingsWidgetWha = QRadioButton(self.frame_5)
        self.radioSettingsWidgetWha.setObjectName(u"radioSettingsWidgetWha")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetWha)

        self.radioSettingsWidgetSwBc = QRadioButton(self.frame_5)
        self.radioSettingsWidgetSwBc.setObjectName(u"radioSettingsWidgetSwBc")

        self.horizontalLayout_8.addWidget(self.radioSettingsWidgetSwBc)


        self.verticalLayout_23.addWidget(self.frame_5)

        self.frame_15 = QFrame(self.frameSettingsWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(110, 16777215))
        self.label_15.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_18.addWidget(self.label_15)

        self.lineEditSettingsWidgetUpdateFrequency = QLineEdit(self.frame_15)
        self.lineEditSettingsWidgetUpdateFrequency.setObjectName(u"lineEditSettingsWidgetUpdateFrequency")
        self.lineEditSettingsWidgetUpdateFrequency.setMinimumSize(QSize(0, 25))
        self.lineEditSettingsWidgetUpdateFrequency.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_18.addWidget(self.lineEditSettingsWidgetUpdateFrequency)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)


        self.verticalLayout_23.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frameSettingsWidget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.verticalLayout_23.addWidget(self.frame_16)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Form", u"Click to hide", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Some Dataset", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Current Path:  ", None))
        self.buttonSettingWidgetCurrentPath.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label.setText(QCoreApplication.translate("Form", u"Download Folder: ", None))
        self.radioSettingsWidgetDownloadFolder.setText(QCoreApplication.translate("Form", u"Universal", None))
        self.buttonSettingsWidgetDownloadFolder.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Archive Folder: ", None))
        self.radioSettingsWidgetArchiveFolder.setText(QCoreApplication.translate("Form", u"Universal", None))
        self.buttonSettingsWidgetArchiveFolder.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Workspace Folder:", None))
        self.radioSettingsWidgetWorkspaceFolder.setText(QCoreApplication.translate("Form", u"Download", None))
        self.buttonSettingsWidgetWorkspaceFolder.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Area of Interest:", None))
        self.radioSettingsWidgetCore.setText(QCoreApplication.translate("Form", u"Core", None))
        self.radioSettingsWidgetMarine.setText(QCoreApplication.translate("Form", u"Marine", None))
        self.radioSettingsWidgetWha.setText(QCoreApplication.translate("Form", u"WHA", None))
        self.radioSettingsWidgetSwBc.setText(QCoreApplication.translate("Form", u"SW BC", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Update Frequency:", None))
        self.lineEditSettingsWidgetUpdateFrequency.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"Days after last posted update", None))
    # retranslateUi

