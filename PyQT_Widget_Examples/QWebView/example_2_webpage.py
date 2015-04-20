# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super(Form, self).__init__()
        self.ui = uic.loadUi("ui.ui", self)
        self.show()

    @pyqtSlot()
    def slot_setAddress(self):
        value = self.ui.lineEdit.text()
        if 0 != value.find("http"):
            value = 'http://' + value

        self.ui.lineEdit.setText(value)
        self.ui.webView.load(QtCore.QUrl(value))
        print(value)

    @pyqtSlot(int)
    def slot_zoomFactor(self, value):
        value = value * 0.01
        self.ui.webView.setZoomFactor(value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents(QtCore.QEventLoop.AllEvents)
    w = Form()
    sys.exit(app.exec())