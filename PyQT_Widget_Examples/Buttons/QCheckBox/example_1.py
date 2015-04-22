# coding: utf-8
# QCheckBox 생성 예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100, 100, 320, 105)

        # QRadioButton 생성
        # 생성시 인자값으로 부모만 지정, 아이콘과 텍스트는 생성후 설정
        chb_1 = QtWidgets.QCheckBox(self)
        chb_1.setText("QCheckBox_1")
        icon = QtGui.QIcon("air.ico")
        chb_1.setIcon(icon)

        # 텍스트를 첫번째 인자값으로 지정후, 생성
        chb_2 = QtWidgets.QCheckBox("QCheckBox_2", self)

        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(chb_1)
        vbox.addWidget(chb_2)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())