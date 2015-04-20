# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("ui.ui", self)
        self.ui.show()

    @pyqtSlot()
    def slot_1st(self):
        pixmap_1 = QtGui.QPixmap(100, 100) # 100x100 사이즈로 선언
        pixmap_1.load("Penguins.jpg") # 그림을 불러옴
        pixmap_1 = pixmap_1.scaledToWidth(200) # QPixmap의 scaledToWidth는 반환값을 QPixmap의 변경된 그림 준다.
        self.ui.label.setPixmap(pixmap_1)


    @pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText("두번째 버튼")

    @pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText("세번째 버튼")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())