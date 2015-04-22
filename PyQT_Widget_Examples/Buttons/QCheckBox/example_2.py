# coding: utf-8
# QCheckBox 를 이용한 LED 점등

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함

class Led(QtWidgets.QAbstractButton):
    """
    예제를 위하여 만든 LED 위젯
    """
    def __init__(self, parent=None):
        QtWidgets.QAbstractButton.__init__(self, parent)
        self.setMinimumSize(15, 15)
        self.setCheckable(True)

    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_Led(qp)
        qp.end()

    def draw_Led(self, qp):
        state = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(QtCore.Qt.gray)
        if self.isChecked() is True:
            state = QtGui.QBrush(QtCore.Qt.green)
        qp.setBrush(state)
        qp.drawEllipse(0, 0, 10, 10)



class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100, 100, 320, 105)

        self.led_1 = Led(self)
        self.led_1.setChecked(False)
        self.led_2 = Led(self)
        self.led_3 = Led(self)
        self.led_4 = Led(self)

        hbox = QtWidgets.QHBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        hbox.addWidget(self.led_1)
        hbox.addWidget(self.led_2)
        hbox.addWidget(self.led_3)
        hbox.addWidget(self.led_4)
        group_0 = QtWidgets.QGroupBox(self)
        group_0.setLayout(hbox)

        # QCheckBox 그룹 1 생성
        self.chb_1 = QtWidgets.QCheckBox("1", self)
        self.chb_1.clicked.connect(self.slot_chbt_clicked) # 시그널 설정
        self.chb_2 = QtWidgets.QCheckBox("2", self)
        self.chb_2.clicked.connect(self.slot_chbt_clicked) # 시그널 설정
        self.chb_3 = QtWidgets.QCheckBox("3", self)
        self.chb_3.clicked.connect(self.slot_chbt_clicked) # 시그널 설정
        self.chb_4 = QtWidgets.QCheckBox("4", self)
        self.chb_4.clicked.connect(self.slot_chbt_clicked) # 시그널 설정
        # 버튼을 정리해줄 레이어박스 생성,
        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(self.chb_1)
        vbox.addWidget(self.chb_2)
        vbox.addWidget(self.chb_3)
        vbox.addWidget(self.chb_4)
        # 레이어 정리를 위한 그룹박스 생성
        group_1 = QtWidgets.QGroupBox(self)
        group_1.setLayout(vbox)

        # 전체 위젯을 정리
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(group_0)
        vbox.addWidget(group_1)
        self.setLayout(vbox)

    @pyqtSlot()
    def slot_chbt_clicked(self):
        if self.chb_1.isChecked() is True: self.led_1.setChecked(True)
        else: self.led_1.setChecked(False)

        if self.chb_2.isChecked() is True: self.led_2.setChecked(True)
        else: self.led_2.setChecked(False)

        if self.chb_3.isChecked() is True: self.led_3.setChecked(True)
        else: self.led_3.setChecked(False)

        if self.chb_4.isChecked() is True: self.led_4.setChecked(True)
        else: self.led_4.setChecked(False)








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())