# coding: utf-8
# QComboBox 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QComboBox')
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)

        # 리스트에 있는 데이터 사용
        self.data = [
            {'name':'바나나', 'pic_filename': 'banana.jpg'},
            {'name':'원숭이', 'pic_filename': 'monkey.jpg'},
            {'name':'코끼리', 'pic_filename': 'elephant.jpg'},
            {'name':'보아뱀', 'pic_filename': 'boa.jpg'}
        ]
        self.cb_1 = QtWidgets.QComboBox(self)
        self.cb_1.addItem(self.data[0]['name'], self.data[0])
        self.cb_1.addItem(self.data[1]['name'], self.data[1])
        self.cb_1.addItem(self.data[2]['name'], self.data[2])
        self.cb_1.addItem(self.data[3]['name'], self.data[3])

        self.lb = QtWidgets.QLabel(self)
        self.lb.setMinimumWidth(200)

        self.cb_1.activated.connect(self.slot_cb_activated)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.cb_1)
        vbox.addWidget(self.lb)

        self.setLayout(vbox)

    @pyqtSlot(int)
    def slot_cb_activated(self, idx):
        pixmap = QtGui.QPixmap(self.data[idx]['pic_filename'])
        pixmap = pixmap.scaledToWidth(250)
        self.lb.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())