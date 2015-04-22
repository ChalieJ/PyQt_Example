# coding: utf-8
# QPushButton 생성시 인자값에 따른 변화 예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.init_ui()


    def init_ui(self):
        """
        위젯 구성 초기화
        """
        self.setGeometry(100, 100, 320, 110) # 창 위치 및 크기 설정

        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯

        # QPushButton 선언
        # QPushButton(QWidget* parent=0)
        pb_1 = QtWidgets.QPushButton(self)

        # QPushButton(QString &string, QWidget* parent=0)
        pb_2 = QtWidgets.QPushButton("Button2", self)

        # QPushButton(QIcon &icon, QString &string, QWidget* parent=0)
        icon = QtGui.QIcon("air.ico")
        pb_3 = QtWidgets.QPushButton(icon, "Button2", self)

        vbox.addWidget(pb_1)
        vbox.addWidget(pb_2)
        vbox.addWidget(pb_3)
        self.setLayout(vbox) # 레이아웃을 Form 위젯에 적용


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())