# coding: utf-8
# QIcon 사용 예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100,100,200,180)

        icon = QtGui.QIcon('save.ico')

        pb = QtWidgets.QPushButton('아이콘', self)

        act_1 = QtWidgets.QAction()
        cb = QtWidgets.QComboBox(self)
        cb.addAction()

        self.setWindowIcon(icon) # 윈도우 타이틀 아이콘
        pb.setIcon(icon) # 버튼 아이콘

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(pb)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

