# coding: utf-8
# QTabWidget 사용예제


import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QTabWidget Example')

        # Tab 단위로 들어갈 페이지 1 위젯 생성
        page_1 = QtWidgets.QWidget() # 빈 여백으로 사용할 QWidget 선언
        icon = QtGui.QIcon('air.ico') # Tab에 사용할 icon
        lb = QtWidgets.QLabel(page_1) # Tab의 요소로 사용
        le = QtWidgets.QLineEdit(page_1)  # Tab의 요소로 사용
        le.textChanged.connect(lb.setText) # 요소들 끼리의 시그널
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(le)
        page_1.setLayout(vbox)

        # Tab 단위로 들어갈 페이지 2 위젯 생성
        page_2 = QtWidgets.QWidget() # 빈 여백으로 사용할 QWidget 선언
        icon = QtGui.QIcon('air.ico') # Tab에 사용할 icon
        pixmap = QtGui.QPixmap('qt_banner.png')
        pixmap = pixmap.scaledToHeight(100)
        lb = QtWidgets.QLabel(page_2)
        lb.setPixmap(pixmap)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb)
        page_2.setLayout(vbox)

        # QTabWidget(QWidget * parent = 0)
        tabw = QtWidgets.QTabWidget(self) # 탭 위젯 선언
        tabw.addTab(page_1, icon, 'Page_1') # 페이지를 탭 안에 넣으면서 생성
        tabw.addTab(page_2, icon, 'Page_2')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tabw)

        self.setLayout(vbox)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())