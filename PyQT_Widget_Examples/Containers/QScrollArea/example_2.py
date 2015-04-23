# coding: utf-8
# QScollArea 자식 위젯과 상호작용

import sys
from PyQt5 import QtWidgets

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QScrollArea Example')

        lb = QtWidgets.QLabel("창 크기를 변경해 보세요")

        le_1 = QtWidgets.QLineEdit(self)
        le_2 = QtWidgets.QLineEdit(self)

        # Scroll Area 1 생성
        scrlarea_1 = QtWidgets.QScrollArea(self)
        scrlarea_1.setWidget(le_1) # 피 위젯 적용

        # Scroll Area 2 생성
        scrlarea_2 = QtWidgets.QScrollArea(self)
        scrlarea_2.setWidget(le_2) # 피 위젯 적용
        # Scroll Area 2 설정
        scrlarea_2.setWidgetResizable(True) # 창크기에 따라 자식 위젯도 크기가 변한다.



        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(scrlarea_1)
        vbox.addWidget(scrlarea_2)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())