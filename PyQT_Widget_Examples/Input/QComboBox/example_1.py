# coding: utf-8
# QComboBox 사용예제

import sys
from PyQt5 import QtWidgets


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QComboBox')
        self.setMinimumWidth(250)

        # 리스트에 있는 데이터 사용
        value_list = ['data_1', 'data_2']
        cb_1 = QtWidgets.QComboBox(self)
        cb_1.addItems(value_list)

        # 하나씩 아이템 넣기
        cb_2 = QtWidgets.QComboBox(self)
        cb_2.addItem('data_3')
        cb_2.addItem('data_4')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(cb_1)
        vbox.addWidget(cb_2)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())