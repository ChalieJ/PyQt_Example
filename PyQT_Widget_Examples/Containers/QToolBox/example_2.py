# coding: utf-8
# QToolBox 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QToolBox Example')

        self.lb = QtWidgets.QLabel(self) # 상태표시 라벨

        # 아이템 리스트 생성
        self.item_list_1 = QtWidgets.QListWidget()
        self.item_list_2 = QtWidgets.QListWidget()

        # 툴박스에 넣게될 아이템 생성
        icon = QtGui.QIcon('air.ico')
        QtWidgets.QListWidgetItem(icon, 'Banana', self.item_list_1).setWhatsThis('바나나')
        QtWidgets.QListWidgetItem(icon, 'Apple', self.item_list_1).setWhatsThis('사과')
        QtWidgets.QListWidgetItem(icon, 'Mango', self.item_list_2).setWhatsThis('망고')
        QtWidgets.QListWidgetItem(icon, 'Strawberry', self.item_list_2).setWhatsThis('딸기')


        # 툴박스 생성
        self.tlbox_1 = QtWidgets.QToolBox(self)
        self.tlbox_1.addItem(self.item_list_1, 'QToolBox1') # 아이템 리스트로 설정
        self.tlbox_1.addItem(self.item_list_2, 'QToolBox2')

        # 시그널 연결
        self.tlbox_1.currentChanged.connect(self.slot_selected) # ToolBox 시그널
        self.item_list_1.itemClicked.connect(self.slot_selected_item)
        self.item_list_2.itemClicked.connect(self.slot_selected_item)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.tlbox_1)

        self.setLayout(vbox)

    @pyqtSlot(int)
    def slot_selected(self, value):
        seltd_item = self.tlbox_1.itemText(value)
        self.lb.setText("툴 박스 [%s] 가 선택되었습니다." % seltd_item)

    @pyqtSlot(QtWidgets.QListWidgetItem)
    def slot_selected_item(self, item):
        item_name = item.whatsThis()
        self.lb.setText("아이템 [%s] 가 선택되었습니다." % item_name)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())