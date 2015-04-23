# coding: utf-8
# QScollArea 생성

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QScrollArea Example')

        # Scroll Area에 적용할 위젯 생성
        lb = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('qt_banner.png')
        pixmap = pixmap.scaledToHeight(100)
        lb.setPixmap(pixmap)

        # Scroll Area 생성
        scrlarea = QtWidgets.QScrollArea(self)
        scrlarea.setWidget(lb) # 피 위젯 적용

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(scrlarea)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())