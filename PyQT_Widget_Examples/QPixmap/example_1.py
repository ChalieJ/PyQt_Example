# coding: utf-8
# QPixmap의 사용 방법중, QLabel을 이용하여 그림을 출력

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


class Form(QtWidgets.QWidget):
    def __init__(self, parent= None):
        super(Form, self).__init__()
        self.setGeometry(QtCore.QRect(20, 20, 640, 480)) # 창의 크기와 위치를 변경

        # QLabel을 이용한 QPixmap 사용
        lb = QtWidgets.QLabel(self)
        pixmap_1 = QtGui.QPixmap(100, 100) # 100x100 사이즈로 선언
        pixmap_1.load("Penguins.jpg") # 그림을 불러옴

        pixmap_1 = pixmap_1.scaledToWidth(200) # QPixmap의 scaledToWidth는 반환값을 QPixmap의 변경된 그림 준다.
        lb.setPixmap(pixmap_1) # Label에 적용

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())