# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("ui.ui", self)

    # Qt Designer에서 버튼의 Clicked와 연결해둔 Slot들
    @pyqtSlot()
    def slot_1st(self):
        self.ui.label.setText("첫번째 버튼") # 라벨의 문구만 변경

    @pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText("두번째 버튼")

    @pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText("세번째 버튼")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())