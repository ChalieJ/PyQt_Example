# coding: utf-8
# QLineEdit 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QLineEdit')
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)

        self.lb = QtWidgets.QLabel(self)
        self.le_pass = QtWidgets.QLineEdit(self)
        self.le_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le = QtWidgets.QLineEdit(self)
        self.le.setClearButtonEnabled(True) # Clear 버튼 유무

        self.le.textChanged.connect(self.lb.setText)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.le_pass)
        vbox.addWidget(self.le)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())