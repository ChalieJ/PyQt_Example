# coding: utf-8
# QToolBox 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QToolBox Example')

        # 툴박스에 들어갈 아이템 생성 1
        icon = QtGui.QIcon('air.ico')
        pb_1 = QtWidgets.QPushButton(icon, "Item 1", self)
        pb_1.setFlat(True)

        # 툴박스 1 생성
        tlbox_1 = QtWidgets.QToolBox(self)
        tlbox_1.addItem(pb_1, 'QToolBox1')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tlbox_1)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())