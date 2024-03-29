# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWereBQ.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1143, 961)
        MainWindow.setMinimumSize(QSize(250, 250))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setCursor(QCursor(Qt.PointingHandCursor))
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	backgrou"
                        "nd-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-backgro"
                        "und-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	border: 2px solid rgb(64, 71, 88)"
                        ";\n"
"}\n"
"QScrollArea  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QScrollArea QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bott"
                        "om-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-lef"
                        "t-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////////////////"
                        "///////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-to"
                        "p-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 25"
                        "5);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	colo"
                        "r: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(225, 225, 225);\n"
"}\n"
"\n"
"QTreeWidget {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	border-radius: 5px;\n"
"	font:10pt \"Segoe UI Semibold\";\n"
"}\n"
"QHeaderView{\n"
"font:10pt \"Segoe UI\";\n"
"font-weight: bold;\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.buttonData = QPushButton(self.topMenu)
        self.buttonData.setObjectName(u"buttonData")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonData.sizePolicy().hasHeightForWidth())
        self.buttonData.setSizePolicy(sizePolicy)
        self.buttonData.setMinimumSize(QSize(0, 45))
        self.buttonData.setFont(font)
        self.buttonData.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonData.setToolTipDuration(5)
        self.buttonData.setLayoutDirection(Qt.LeftToRight)
        self.buttonData.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.buttonData)

        self.buttonLogs = QPushButton(self.topMenu)
        self.buttonLogs.setObjectName(u"buttonLogs")
        sizePolicy.setHeightForWidth(self.buttonLogs.sizePolicy().hasHeightForWidth())
        self.buttonLogs.setSizePolicy(sizePolicy)
        self.buttonLogs.setMinimumSize(QSize(0, 45))
        self.buttonLogs.setFont(font)
        self.buttonLogs.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonLogs.setLayoutDirection(Qt.LeftToRight)
        self.buttonLogs.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.buttonLogs)

        self.buttonDataSettings = QPushButton(self.topMenu)
        self.buttonDataSettings.setObjectName(u"buttonDataSettings")
        sizePolicy.setHeightForWidth(self.buttonDataSettings.sizePolicy().hasHeightForWidth())
        self.buttonDataSettings.setSizePolicy(sizePolicy)
        self.buttonDataSettings.setMinimumSize(QSize(0, 45))
        self.buttonDataSettings.setFont(font)
        self.buttonDataSettings.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDataSettings.setLayoutDirection(Qt.LeftToRight)
        self.buttonDataSettings.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.buttonDataSettings)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.buttonRefresh = QPushButton(self.bottomMenu)
        self.buttonRefresh.setObjectName(u"buttonRefresh")
        sizePolicy.setHeightForWidth(self.buttonRefresh.sizePolicy().hasHeightForWidth())
        self.buttonRefresh.setSizePolicy(sizePolicy)
        self.buttonRefresh.setMinimumSize(QSize(0, 45))
        self.buttonRefresh.setFont(font)
        self.buttonRefresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonRefresh.setLayoutDirection(Qt.LeftToRight)
        self.buttonRefresh.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);")

        self.verticalLayout_5.addWidget(self.buttonRefresh)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy3)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.data = QWidget()
        self.data.setObjectName(u"data")
        sizePolicy3.setHeightForWidth(self.data.sizePolicy().hasHeightForWidth())
        self.data.setSizePolicy(sizePolicy3)
        self.data.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.data)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelData = QLabel(self.data)
        self.labelData.setObjectName(u"labelData")
        self.labelData.setStyleSheet(u"font: 700 30pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.labelData)

        self.line = QFrame(self.data)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background: none")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.scrollArea_2 = QScrollArea(self.data)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1019, 775))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.labelCatalogueDatasets = QLabel(self.frame)
        self.labelCatalogueDatasets.setObjectName(u"labelCatalogueDatasets")
        self.labelCatalogueDatasets.setStyleSheet(u"font: 700 17pt \"Segoe UI Semibold\"; color: rgb(207,249,147)")

        self.verticalLayout_16.addWidget(self.labelCatalogueDatasets)

        self.frameCatalogueDatasets = QFrame(self.frame)
        self.frameCatalogueDatasets.setObjectName(u"frameCatalogueDatasets")
        sizePolicy3.setHeightForWidth(self.frameCatalogueDatasets.sizePolicy().hasHeightForWidth())
        self.frameCatalogueDatasets.setSizePolicy(sizePolicy3)
        self.frameCatalogueDatasets.setFrameShape(QFrame.StyledPanel)
        self.frameCatalogueDatasets.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frameCatalogueDatasets)


        self.verticalLayout_21.addLayout(self.verticalLayout_16)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.labelOtherDatasets = QLabel(self.frame)
        self.labelOtherDatasets.setObjectName(u"labelOtherDatasets")
        self.labelOtherDatasets.setStyleSheet(u"font: 700 17pt \"Segoe UI Semibold\"; color: rgb(207,249,147)")

        self.verticalLayout_19.addWidget(self.labelOtherDatasets)

        self.frameOtherDatasets = QFrame(self.frame)
        self.frameOtherDatasets.setObjectName(u"frameOtherDatasets")
        sizePolicy3.setHeightForWidth(self.frameOtherDatasets.sizePolicy().hasHeightForWidth())
        self.frameOtherDatasets.setSizePolicy(sizePolicy3)
        self.frameOtherDatasets.setFrameShape(QFrame.StyledPanel)
        self.frameOtherDatasets.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frameOtherDatasets)


        self.verticalLayout_21.addLayout(self.verticalLayout_19)


        self.verticalLayout_22.addWidget(self.frame)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.data)
        self.logs = QWidget()
        self.logs.setObjectName(u"logs")
        self.verticalLayout_15 = QVBoxLayout(self.logs)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.labelLogs = QLabel(self.logs)
        self.labelLogs.setObjectName(u"labelLogs")
        self.labelLogs.setStyleSheet(u"font: 700 30pt \"Segoe UI\";")

        self.verticalLayout_15.addWidget(self.labelLogs)

        self.lineLogs = QFrame(self.logs)
        self.lineLogs.setObjectName(u"lineLogs")
        sizePolicy.setHeightForWidth(self.lineLogs.sizePolicy().hasHeightForWidth())
        self.lineLogs.setSizePolicy(sizePolicy)
        self.lineLogs.setStyleSheet(u"background: none")
        self.lineLogs.setFrameShape(QFrame.HLine)
        self.lineLogs.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.lineLogs)

        self.scrollAreaLogsButtons = QScrollArea(self.logs)
        self.scrollAreaLogsButtons.setObjectName(u"scrollAreaLogsButtons")
        self.scrollAreaLogsButtons.setMaximumSize(QSize(16777215, 150))
        self.scrollAreaLogsButtons.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 68, 16))
        self.scrollAreaLogsButtons.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollAreaLogsButtons)

        self.textEditLogs = QTextEdit(self.logs)
        self.textEditLogs.setObjectName(u"textEditLogs")
        self.textEditLogs.setReadOnly(True)

        self.verticalLayout_15.addWidget(self.textEditLogs)

        self.stackedWidget.addWidget(self.logs)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.verticalLayout_20 = QVBoxLayout(self.settings)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.labelSettings = QLabel(self.settings)
        self.labelSettings.setObjectName(u"labelSettings")
        self.labelSettings.setStyleSheet(u"font: 700 30pt \"Segoe UI\";")

        self.verticalLayout_20.addWidget(self.labelSettings)

        self.lineSettings = QFrame(self.settings)
        self.lineSettings.setObjectName(u"lineSettings")
        sizePolicy.setHeightForWidth(self.lineSettings.sizePolicy().hasHeightForWidth())
        self.lineSettings.setSizePolicy(sizePolicy)
        self.lineSettings.setStyleSheet(u"background: none")
        self.lineSettings.setFrameShape(QFrame.HLine)
        self.lineSettings.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.lineSettings)

        self.scrollAreaSettings = QScrollArea(self.settings)
        self.scrollAreaSettings.setObjectName(u"scrollAreaSettings")
        self.scrollAreaSettings.setMinimumSize(QSize(0, 0))
        self.scrollAreaSettings.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaSettings.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1019, 729))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, 0)
        self.frameAllSettings = QFrame(self.scrollAreaWidgetContents_6)
        self.frameAllSettings.setObjectName(u"frameAllSettings")
        self.frameAllSettings.setFrameShape(QFrame.StyledPanel)
        self.frameAllSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameAllSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameUniversalSettings = QFrame(self.frameAllSettings)
        self.frameUniversalSettings.setObjectName(u"frameUniversalSettings")
        self.frameUniversalSettings.setFrameShape(QFrame.StyledPanel)
        self.frameUniversalSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frameUniversalSettings)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_36 = QFrame(self.frameUniversalSettings)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_36)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 700 15pt \"Segoe UI Semibold\"; color: rgb(147, 249, 240); border:none;")

        self.horizontalLayout_39.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_18.addWidget(self.frame_36, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.frameUniversalSettings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(110, 0))
        self.label_18.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\" ; color: rgb(147,189,249)")

        self.horizontalLayout_21.addWidget(self.label_18)

        self.lineEditDownloadFolder = QLineEdit(self.frame_18)
        self.lineEditDownloadFolder.setObjectName(u"lineEditDownloadFolder")
        self.lineEditDownloadFolder.setMinimumSize(QSize(0, 25))
        self.lineEditDownloadFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_21.addWidget(self.lineEditDownloadFolder)

        self.buttonDownloadPath = QPushButton(self.frame_18)
        self.buttonDownloadPath.setObjectName(u"buttonDownloadPath")
        self.buttonDownloadPath.setMinimumSize(QSize(120, 25))
        self.buttonDownloadPath.setMaximumSize(QSize(120, 16777215))
        self.buttonDownloadPath.setFont(font)
        self.buttonDownloadPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDownloadPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDownloadPath.setIcon(icon3)

        self.horizontalLayout_21.addWidget(self.buttonDownloadPath)


        self.verticalLayout_18.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frameUniversalSettings)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(110, 0))
        self.label_19.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\";color: rgb(147,189,249)")

        self.horizontalLayout_22.addWidget(self.label_19)

        self.lineEditArchiveFolder = QLineEdit(self.frame_19)
        self.lineEditArchiveFolder.setObjectName(u"lineEditArchiveFolder")
        self.lineEditArchiveFolder.setMinimumSize(QSize(0, 25))
        self.lineEditArchiveFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_22.addWidget(self.lineEditArchiveFolder)

        self.buttonArchiveFolderPath = QPushButton(self.frame_19)
        self.buttonArchiveFolderPath.setObjectName(u"buttonArchiveFolderPath")
        self.buttonArchiveFolderPath.setMinimumSize(QSize(120, 25))
        self.buttonArchiveFolderPath.setMaximumSize(QSize(120, 16777215))
        self.buttonArchiveFolderPath.setFont(font)
        self.buttonArchiveFolderPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonArchiveFolderPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonArchiveFolderPath.setIcon(icon3)

        self.horizontalLayout_22.addWidget(self.buttonArchiveFolderPath)


        self.verticalLayout_18.addWidget(self.frame_19)

        self.frame_24 = QFrame(self.frameUniversalSettings)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(110, 0))
        self.label_24.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\";color: rgb(147,189,249)")

        self.horizontalLayout_27.addWidget(self.label_24)

        self.lineEditLogFolder = QLineEdit(self.frame_24)
        self.lineEditLogFolder.setObjectName(u"lineEditLogFolder")
        self.lineEditLogFolder.setMinimumSize(QSize(0, 25))
        self.lineEditLogFolder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_27.addWidget(self.lineEditLogFolder)

        self.buttonLogFolderPath = QPushButton(self.frame_24)
        self.buttonLogFolderPath.setObjectName(u"buttonLogFolderPath")
        self.buttonLogFolderPath.setMinimumSize(QSize(120, 25))
        self.buttonLogFolderPath.setMaximumSize(QSize(120, 16777215))
        self.buttonLogFolderPath.setFont(font)
        self.buttonLogFolderPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonLogFolderPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonLogFolderPath.setIcon(icon3)

        self.horizontalLayout_27.addWidget(self.buttonLogFolderPath)


        self.verticalLayout_18.addWidget(self.frame_24)

        self.frame_40 = QFrame(self.frameUniversalSettings)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_36 = QLabel(self.frame_40)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(110, 0))
        self.label_36.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\";color: rgb(147,189,249)")

        self.horizontalLayout_43.addWidget(self.label_36)

        self.lineEditHtgLands = QLineEdit(self.frame_40)
        self.lineEditHtgLands.setObjectName(u"lineEditHtgLands")
        self.lineEditHtgLands.setMinimumSize(QSize(0, 25))
        self.lineEditHtgLands.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_43.addWidget(self.lineEditHtgLands)

        self.buttonHtgLands = QPushButton(self.frame_40)
        self.buttonHtgLands.setObjectName(u"buttonHtgLands")
        self.buttonHtgLands.setMinimumSize(QSize(120, 25))
        self.buttonHtgLands.setMaximumSize(QSize(120, 16777215))
        self.buttonHtgLands.setFont(font)
        self.buttonHtgLands.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonHtgLands.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonHtgLands.setIcon(icon3)

        self.horizontalLayout_43.addWidget(self.buttonHtgLands)


        self.verticalLayout_18.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frameUniversalSettings)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_37 = QLabel(self.frame_41)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(110, 0))
        self.label_37.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\";color: rgb(147,189,249)")

        self.horizontalLayout_44.addWidget(self.label_37)

        self.lineEditSoiAll = QLineEdit(self.frame_41)
        self.lineEditSoiAll.setObjectName(u"lineEditSoiAll")
        self.lineEditSoiAll.setMinimumSize(QSize(0, 25))
        self.lineEditSoiAll.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_44.addWidget(self.lineEditSoiAll)

        self.buttonSoiAll = QPushButton(self.frame_41)
        self.buttonSoiAll.setObjectName(u"buttonSoiAll")
        self.buttonSoiAll.setMinimumSize(QSize(120, 25))
        self.buttonSoiAll.setMaximumSize(QSize(120, 16777215))
        self.buttonSoiAll.setFont(font)
        self.buttonSoiAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSoiAll.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonSoiAll.setIcon(icon3)

        self.horizontalLayout_44.addWidget(self.buttonSoiAll)


        self.verticalLayout_18.addWidget(self.frame_41)

        self.frame_34 = QFrame(self.frameUniversalSettings)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_32 = QLabel(self.frame_34)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(110, 0))
        self.label_32.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_37.addWidget(self.label_32)

        self.lineEditCore = QLineEdit(self.frame_34)
        self.lineEditCore.setObjectName(u"lineEditCore")
        self.lineEditCore.setMinimumSize(QSize(0, 25))
        self.lineEditCore.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_37.addWidget(self.lineEditCore)

        self.buttonCorePath = QPushButton(self.frame_34)
        self.buttonCorePath.setObjectName(u"buttonCorePath")
        self.buttonCorePath.setMinimumSize(QSize(120, 25))
        self.buttonCorePath.setMaximumSize(QSize(120, 16777215))
        self.buttonCorePath.setFont(font)
        self.buttonCorePath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonCorePath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonCorePath.setIcon(icon3)

        self.horizontalLayout_37.addWidget(self.buttonCorePath)


        self.verticalLayout_18.addWidget(self.frame_34)

        self.frame_37 = QFrame(self.frameUniversalSettings)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_33 = QLabel(self.frame_37)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(110, 0))
        self.label_33.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_40.addWidget(self.label_33)

        self.lineEditMarine = QLineEdit(self.frame_37)
        self.lineEditMarine.setObjectName(u"lineEditMarine")
        self.lineEditMarine.setMinimumSize(QSize(0, 25))
        self.lineEditMarine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_40.addWidget(self.lineEditMarine)

        self.buttonMarinePath = QPushButton(self.frame_37)
        self.buttonMarinePath.setObjectName(u"buttonMarinePath")
        self.buttonMarinePath.setMinimumSize(QSize(120, 25))
        self.buttonMarinePath.setMaximumSize(QSize(120, 16777215))
        self.buttonMarinePath.setFont(font)
        self.buttonMarinePath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonMarinePath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonMarinePath.setIcon(icon3)

        self.horizontalLayout_40.addWidget(self.buttonMarinePath)


        self.verticalLayout_18.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frameUniversalSettings)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_34 = QLabel(self.frame_38)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(110, 0))
        self.label_34.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_41.addWidget(self.label_34)

        self.lineEditWha = QLineEdit(self.frame_38)
        self.lineEditWha.setObjectName(u"lineEditWha")
        self.lineEditWha.setMinimumSize(QSize(0, 25))
        self.lineEditWha.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_41.addWidget(self.lineEditWha)

        self.buttonWhaPath = QPushButton(self.frame_38)
        self.buttonWhaPath.setObjectName(u"buttonWhaPath")
        self.buttonWhaPath.setMinimumSize(QSize(120, 25))
        self.buttonWhaPath.setMaximumSize(QSize(120, 16777215))
        self.buttonWhaPath.setFont(font)
        self.buttonWhaPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonWhaPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonWhaPath.setIcon(icon3)

        self.horizontalLayout_41.addWidget(self.buttonWhaPath)


        self.verticalLayout_18.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frameUniversalSettings)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_35 = QLabel(self.frame_39)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(110, 0))
        self.label_35.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_42.addWidget(self.label_35)

        self.lineEditSwBc = QLineEdit(self.frame_39)
        self.lineEditSwBc.setObjectName(u"lineEditSwBc")
        self.lineEditSwBc.setMinimumSize(QSize(0, 25))
        self.lineEditSwBc.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_42.addWidget(self.lineEditSwBc)

        self.buttonSwBcPath = QPushButton(self.frame_39)
        self.buttonSwBcPath.setObjectName(u"buttonSwBcPath")
        self.buttonSwBcPath.setMinimumSize(QSize(120, 25))
        self.buttonSwBcPath.setMaximumSize(QSize(120, 16777215))
        self.buttonSwBcPath.setFont(font)
        self.buttonSwBcPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSwBcPath.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.buttonSwBcPath.setIcon(icon3)

        self.horizontalLayout_42.addWidget(self.buttonSwBcPath)


        self.verticalLayout_18.addWidget(self.frame_39)

        self.frame_17 = QFrame(self.frameUniversalSettings)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(110, 0))
        self.label_17.setMaximumSize(QSize(110, 16777215))
        self.label_17.setStyleSheet(u"font: 700 10pt \"Segoe UI Semibold\"")

        self.horizontalLayout_20.addWidget(self.label_17)

        self.lineEditEmail = QLineEdit(self.frame_17)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setMinimumSize(QSize(200, 25))
        self.lineEditEmail.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_20.addWidget(self.lineEditEmail)


        self.verticalLayout_18.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frameUniversalSettings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 10))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 30, 907, 3))
        self.line_2.setStyleSheet(u"background:none")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frameUniversalSettings)


        self.verticalLayout_17.addWidget(self.frameAllSettings)

        self.scrollAreaSettings.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_20.addWidget(self.scrollAreaSettings)

        self.buttonApplySettings = QPushButton(self.settings)
        self.buttonApplySettings.setObjectName(u"buttonApplySettings")
        self.buttonApplySettings.setMinimumSize(QSize(130, 40))
        self.buttonApplySettings.setMaximumSize(QSize(120, 16777215))
        self.buttonApplySettings.setFont(font)
        self.buttonApplySettings.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonApplySettings.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonApplySettings.setIcon(icon4)

        self.verticalLayout_20.addWidget(self.buttonApplySettings)

        self.stackedWidget.addWidget(self.settings)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
#if QT_CONFIG(tooltip)
        self.buttonData.setToolTip(QCoreApplication.translate("MainWindow", u"Datasets", None))
#endif // QT_CONFIG(tooltip)
        self.buttonData.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.buttonLogs.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.buttonDataSettings.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.buttonRefresh.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"HTG Dataset Updater", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelData.setText(QCoreApplication.translate("MainWindow", u"Datasets", None))
        self.labelCatalogueDatasets.setText(QCoreApplication.translate("MainWindow", u"Catalogue Datasets", None))
        self.labelOtherDatasets.setText(QCoreApplication.translate("MainWindow", u"Other  Datasets", None))
        self.labelLogs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.labelSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Click to hide", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Universal Settings", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Download Folder:", None))
        self.buttonDownloadPath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Archive Folder: ", None))
        self.buttonArchiveFolderPath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Log Folder:", None))
        self.buttonLogFolderPath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"HTG Lands:", None))
        self.buttonHtgLands.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"HTG SOIs All:", None))
        self.buttonSoiAll.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Core:", None))
        self.buttonCorePath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Marine:", None))
        self.buttonMarinePath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"WHA:", None))
        self.buttonWhaPath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"SW BC (Roads):", None))
        self.buttonSwBcPath.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.buttonApplySettings.setText(QCoreApplication.translate("MainWindow", u"Apply Settings", None))
    # retranslateUi

