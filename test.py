

from modules.functionLib import crownTenuresGeoprocessing, crownTenuresProcess
from modules import *
import arcpy


environmentalRemediationSiteRaw = r"C:\Users\laure\Desktop\test\data\RMDTN_STS_point.shp"
alcAlrRaw = r"C:\Users\laure\Desktop\test\data\TSLRPLS_polygon.shp"

digitalRoadRaw = r"C:\Users\laure\Desktop\test\data\DRA_MPAR_line.shp"

parcelsRaw = r"C:\Users\laure\Desktop\test\PMBC_PARCEL_FABRIC_POLY_SVW.gdb\WHSE_CADASTRE_PMBC_PARCEL_FABRIC_POLY_SVW"
tenuresRaw=r"C:\Users\laure\Desktop\test\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp"

# parcelMapBCGeoprocessing(parcelsRaw)

# digitalRoadAtlasGeoprocessing(digitalRoadRaw)

#alcAlrPolygonsGeoprocessing(alcAlrRaw)

#environmentalRemediationSitesGeoprocessing(environmentalRemediationSiteRaw)

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from modules.customWidgets import *


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()

class Bubble(QtWidgets.QLabel):
    def __init__(self, text):
        super(Bubble, self).__init__(text)
        self.word = text
        self.setContentsMargins(5, 5, 5, 5)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.drawRoundedRect(
            0, 0, self.width() - 1, self.height() - 1, 5, 5)
        super(Bubble, self).paintEvent(event)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, text, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mainArea = QtWidgets.QScrollArea(self)
        self.mainArea.setWidgetResizable(True)
        widget = QtWidgets.QWidget(self.mainArea)
        widget.setMinimumWidth(50)
        layout = FlowLayout(widget)
        self.words = []
        for word in text.split():
            label = Bubble(word)
            label.setFont(QtGui.QFont('SblHebrew', 18))
            label.setFixedWidth(label.sizeHint().width())
            self.words.append(label)
            layout.addWidget(label)
        
        #my tests
        
        test = dataSetFrame(widget, crownTenuresSettings, crownTenuresProcess)
        test.setMinimumSize(QSize(100, 100))
        layout.addWidget(test)
        #button1 = QPushButton(frame)
        #button1.setText("supp")



        layout.addWidget(QPushButton("Hello"))
        layout.addWidget(QLabel("hellohello"))


        self.mainArea.setWidget(widget)
        self.setCentralWidget(self.mainArea)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow('Harry Potter is a series of fantasy literature')
    window.show()
    sys.exit(app.exec_())