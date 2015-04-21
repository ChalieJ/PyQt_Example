# coding: utf-8
# QPushButton 생성시 인자값에 따른 변화 예제
# QPushButton 토글 기능, 비·활성화 설정

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        """
        위젯 구성 초기화
        """
        self.setGeometry(100, 100, 320, 110) # 창 위치 및 크기 설정
        self.setWindowTitle("QPushButton 예제")

        # QPushButton 생성
        # 토글 버튼 생성
        self.pb_1 = QtWidgets.QPushButton("False", self)
        self.pb_1.setCheckable(True) # Checkable 이 True 상태에만 토글이 가능
        self.pb_1.toggled.connect(self.slot_set_enabled) # 토글 되었을 경우 시그널 발생

        # 누르고 있을때와 땠을 때 반응이 있는 버튼 생성
        # Pressed와 release 때 시그널 발생
        self.pb_2 = QtWidgets.QPushButton("QPushButton", self)
        self.pb_2.setEnabled(False)
        self.pb_2.pressed.connect(self.slot_pb_pressed)
        self.pb_2.released.connect(self.slot_pb_release)

        vbox = QtWidgets.QVBoxLayout() # 버튼들의 정렬을 위한 레이아웃 위젯
        vbox.addWidget(self.pb_1)
        vbox.addWidget(self.pb_2)
        self.setLayout(vbox) # 레이아웃을 Form 위젯에 적용

    # 토글버튼은 눌러졌을 경우 check 상태에 따라 True 또는 False를 준다.
    @pyqtSlot(bool)
    def slot_set_enabled(self, state):
        if state:
            self.pb_1.setText("True") # 라벨 문자 변경
        else:
            self.pb_1.setText("False")
        self.pb_2.setEnabled(state) # state 값에 따라 해당 버튼의 사용가능 여부가 정해진다.

    # 버튼이 눌러졌을 경우
    @pyqtSlot()
    def slot_pb_pressed(self):
        self.pb_2.setText("Pressed")
        self.pb_1.setEnabled(False)

    # 버튼이 클릭 이후 떨어지는 상태, 릴리즈 상태가 될 경우
    @pyqtSlot()
    def slot_pb_release(self):
        self.pb_2.setText("Released")
        self.pb_1.setEnabled(True)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())