# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import time
from PyQt5.QtCore import pyqtSlot
import random

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setGeometry(QtCore.QRect(10, 10, 640, 480))

        scene = QtWidgets.QGraphicsScene(self)
        view = QtWidgets.QGraphicsView(scene, self)
        view.setGeometry(100, 0, 400, 400)


        text = scene.addText("Hello, World!")
        text.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

        blueBrush = QtGui.QBrush(QtCore.Qt.blue)
        outlinePen = QtGui.QPen(QtCore.Qt.black)
        outlinePen.setWidth(2)
        ellipse = scene.addEllipse(100, 0, 80, 100, outlinePen, blueBrush)



        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents(QtCore.QEventLoop.AllEvents)
    w = Form()
    sys.exit(app.exec())