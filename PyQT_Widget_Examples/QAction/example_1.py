# coding: utf-8
# QMainWindow
## QMainWindow
## QAction

# QAction은 menu와 toolbar 에서 사용할 수 있다.

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setGeometry(100,100,140,180)
        self.init_ui()

    def init_ui(self):
        # 액션선언
        # 끝내기
        self.act_quit = QtWidgets.QAction('&Quit', self)
        self.act_quit.setText('Quit')
        self.act_quit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.act_quit.hovered.connect(self.slot_quit)

        menu_bar = self.menuBar()
        menu_hello = menu_bar.addMenu('&Hello')
        menu_hello.addAction(self.act_quit)






    @pyqtSlot()
    def slot_quit(self):
        reply = QtWidgets.QMessageBox.information(
            self,
            u'Exit',u"프로그램을 종료하시겠습니까?",
            QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel,
            QtWidgets.QMessageBox.Save
        )

        if reply == QtWidgets.QMessageBox.Yes:
            app.quit()
        elif reply == QtWidgets.QMessageBox.No:
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

