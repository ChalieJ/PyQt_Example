# coding: utf-8
# QRadioButton 그룹별 반응 예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot # pyqtSlot 프로퍼티를 사용하기 위함


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setGeometry(100, 100, 320, 105)

        self.lb = QtWidgets.QLabel("버튼을 클릭해 주세요.", self)

        # QRadioButton 그룹 1 생성
        self.rb_1 = QtWidgets.QRadioButton("Monkey", self)
        self.rb_1.clicked.connect(self.slot_rbt_clicked) # 시그널 설정
        self.rb_2 = QtWidgets.QRadioButton("Zebra", self)
        self.rb_2.clicked.connect(self.slot_rbt_clicked) # 시그널 설정
        # 버튼을 정리해줄 레이어박스 생성,
        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(self.rb_1)
        vbox.addWidget(self.rb_2)
        # 레이어 정리를 위한 그룹박스 생성
        group_1 = QtWidgets.QGroupBox(self)
        group_1.setLayout(vbox)


        # QRadioButton 그룹 2 생성
        self.rb_3 = QtWidgets.QRadioButton("banana", self)
        self.rb_3.setChecked(True) # 체크를 미리 해두었음
        self.rb_3.clicked.connect(self.slot_rbt_clicked) # 시그널 설정
        self.rb_4 = QtWidgets.QRadioButton("carrot", self)
        self.rb_4.clicked.connect(self.slot_rbt_clicked) # 시그널 설정
        # 버튼을 정리해줄 레이어박스 생성,
        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(self.rb_3)
        vbox.addWidget(self.rb_4)
        # 레이어 정리를 위한 그룹박스 생성
        group_2 = QtWidgets.QGroupBox(self)
        group_2.setLayout(vbox)


        # 전체 위젯을 정리
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(group_1)
        vbox.addWidget(group_2)
        self.setLayout(vbox)

    def slot_rbt_clicked(self):
        data_1 = ''
        data_2 = ''
        if self.rb_1.isChecked() is True:
            data_1 += self.rb_1.text()
        if self.rb_2.isChecked() is True:
            data_1 += self.rb_2.text()
        if self.rb_3.isChecked() is True:
            data_2 += self.rb_3.text()
        if self.rb_4.isChecked() is True:
            data_2 += self.rb_4.text()

        self.lb.setText(data_1 + ' likes ' + data_2)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())