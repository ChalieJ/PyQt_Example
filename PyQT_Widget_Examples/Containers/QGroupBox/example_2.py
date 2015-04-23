# coding: utf-8
# QGroupBox Properties 및 Public Function 이용
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QGroupBox Example')

        # 첫 번째 그룹
        grpbox_1 = QtWidgets.QGroupBox(self) # 그룹박스 생성
        le_1 = QtWidgets.QLineEdit(self) # 그룹박스에 넣을 위젯
        vbox = QtWidgets.QVBoxLayout() # 그룹박스안을 정리해줄 레이아웃
        vbox.addWidget(le_1)
        grpbox_1.setLayout(vbox) # 그룹박스의 레이아웃 지정

        # 첫번째 그룹 세부 설정
        grpbox_1.setTitle('QGroupBox')
        grpbox_1.setCheckable(True)
        grpbox_1.setAlignment(QtCore.Qt.AlignCenter)


        # 두 번째 그룹
        grpbox_2 = QtWidgets.QGroupBox('QGroupBox_2', self)
        le_2 = QtWidgets.QLineEdit(self) # 그룹박스에 넣을 위젯
        vbox = QtWidgets.QVBoxLayout() # 그룹박스안을 정리해줄 레이아웃
        vbox.addWidget(le_2)
        grpbox_2.setLayout(vbox) # 그룹박스의 레이아웃 지정


        # 메인 폼 레이아웃 정리
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(grpbox_1)
        vbox.addWidget(grpbox_2)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())