# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic # Qt Designer로 만든 UI 파일을 읽어올때 사용

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        # 두번째 인자에 QDialog 즉, self를 부모인자에 넣는다.
        self.ui = uic.loadUi("ui.ui", self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form() # 폼 Instance를 생성, 생성자인 __init__()가 실행된다.
    w.show() # QDialog가 가진 show() 멤버 함수를 이용하여 창을 표출
    # 부모에 속한 자식 위젯은 모두 보여지게 된다.

    sys.exit(app.exec())
