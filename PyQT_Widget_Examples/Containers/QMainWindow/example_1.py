# coding: utf-8
# QMainWindow
## QMainWindow
## QAction


import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setGeometry(100,100,640,480)
        self.init_ui()

    def init_ui(self):
        # 끝내기
        self.act_quit = QtWidgets.QAction('&Quit', self)
        self.act_quit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.act_quit.triggered.connect(self.slot_quit)
        # 메뉴바 생성 및 액션 적용
        menu = self.menuBar()
        menu_file = menu.addMenu('&File')
        menu_file.addAction(self.act_quit)


    @pyqtSlot()
    def slot_quit(self):
        reply = QtWidgets.QMessageBox.information(
            self,
            u'Exit',u"프로그램을 종료하시겠습니까?",
            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.Save
        )

        if reply == QtWidgets.QMessageBox.Yes:

        elif reply == QtWidgets.QMessageBox.No:
            pass
        app.quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

