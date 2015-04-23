# coding: utf-8
# QTabWidget 사용예제, Page용 위젯을 따로 만들어 사용


import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

class page_1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # Tab 단위로 들어갈 페이지 1 위젯 생성
        lb = QtWidgets.QLabel(self) # Tab의 요소로 사용
        le = QtWidgets.QLineEdit(self)  # Tab의 요소로 사용
        le.textChanged.connect(lb.setText) # 요소들 끼리의 시그널
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb)
        vbox.addWidget(le)
        self.setLayout(vbox)



class page_2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # Tab 단위로 들어갈 페이지 2 위젯 생성
        pixmap = QtGui.QPixmap('qt_banner.png')
        pixmap = pixmap.scaledToHeight(100)
        lb = QtWidgets.QLabel(self)
        lb.setPixmap(pixmap)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lb)
        self.setLayout(vbox)


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QTabWidget Example')

        # QTabWidget(QWidget * parent = 0)
        self.tabw = QtWidgets.QTabWidget(self) # 탭 위젯 선언
        self.tabw.setMinimumWidth(250) # 탭 위젯 가로 최소 길이 설정
        self.tabw.setUsesScrollButtons(True) # 탭의 수가 위젯 길이를 벗아날 경우 스크롤 제공

        self.le = QtWidgets.QLineEdit(self)
        self.rb_1 = QtWidgets.QRadioButton('에디터',self)
        self.rb_2 = QtWidgets.QRadioButton('그림',self)
        self.rb_1.setWhatsThis('editor')
        self.rb_2.setWhatsThis('picture')
        self.rb_grp = QtWidgets.QButtonGroup(self)
        self.rb_grp.addButton(self.rb_1)
        self.rb_grp.addButton(self.rb_2)
        self.pb_new = QtWidgets.QPushButton('New Tab', self)
        self.pb_remove = QtWidgets.QPushButton('Remove Tab', self)

        # 시그널연결
        self.pb_new.clicked.connect(self.slot_new_tab)
        self.pb_remove.clicked.connect(self.slot_remove_tab)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.le)
        vbox.addWidget(self.rb_1)
        vbox.addWidget(self.rb_2)
        vbox.addWidget(self.pb_new)
        vbox.addWidget(self.pb_remove)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.tabw)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def slot_new_tab(self):
        icon = QtGui.QIcon('air.ico') # Tab에 사용할 icon
        tab_name = self.le.text() if self.le.text() != '' else 'Unknown'
        item = self.rb_grp.checkedButton().whatsThis()
        page = None
        if item == 'editor':
           page = page_1()
        elif item == 'picture':
           page = page_2()

        self.tabw.addTab(page, icon, tab_name) # 페이지를 탭 안에 넣으면서 생성



    def slot_remove_tab(self):
        c_idx =self.tabw.currentIndex()
        self.tabw.removeTab(c_idx)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())