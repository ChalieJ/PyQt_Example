# coding: utf-8
# QRadioButton 생성 예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100, 100, 320, 105)

        # QRadioButton 생성
        # 생성시 인자값으로 부모만 지정, 아이콘과 텍스트는 생성후 설정
        rb_1 = QtWidgets.QRadioButton(self)
        rb_1.setText("QRadioButton_1")
        icon = QtGui.QIcon("air.ico")
        rb_1.setIcon(icon)

        # 텍스트를 첫번째 인자값으로 지정후, 생성
        rb_2 = QtWidgets.QRadioButton("QRadioButton_2", self)

        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(rb_1)
        vbox.addWidget(rb_2)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())