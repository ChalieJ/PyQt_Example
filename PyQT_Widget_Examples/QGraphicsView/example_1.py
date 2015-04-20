# coding: utf-8
# QGraphicsView를 이용하여 Hello World 출력

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setGeometry(QtCore.QRect(10, 10, 640, 480))

        scene = QtWidgets.QGraphicsScene()
        scene.addText("Hello, World!")

        view = QtWidgets.QGraphicsView(scene, self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents(QtCore.QEventLoop.AllEvents)
    w = Form()
    sys.exit(app.exec())