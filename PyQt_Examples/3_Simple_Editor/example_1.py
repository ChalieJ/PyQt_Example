# coding: utf-8
# 간단한 메모장, 저장 및 불러오기 기능 구형

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = uic.loadUi("ui.ui", self)

    def init_ui(self):
        pass

    @pyqtSlot()
    def slot_open(self):
        fdial = QtWidgets.QFileDialog(self)
        fdial.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        file_name = fdial.getOpenFileName(self, '파일열기', filter='*.txt')[0]
        if file_name == '':
            return
        fd = open(file_name, 'r')
        buf = fd.read()
        fd.close()
        self.ui.textEdit.clear()
        self.ui.textEdit.insertPlainText(buf)

    @pyqtSlot()
    def slot_save(self):
        buf = self.ui.textEdit.toPlainText()
        fdial = QtWidgets.QFileDialog(self)
        fdial.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_name = fdial.getSaveFileName(self, '파일저장', filter='*.txt')[0]
        if file_name == '':
            return
        fd = open(file_name, 'w')
        fd.write(buf)
        fd.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

