# coding: utf-8
# ListView, ListModel 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

# 예제 모델
class MyModel(QtCore.QAbstractListModel):
    def __init__(self, data=[], parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.data = data

    # TableView가 데이터의 세로줄 수를 요구
    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.data)

    # TableView에서 Data를 표출을 위해 데이터 요구
    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()

        if int_role == QtCore.Qt.DisplayRole:
            return "%s" % (self.data[row]['name'])

        if int_role == QtCore.Qt.DecorationRole:
            icon = QtGui.QIcon('air.ico')
            return icon

        if int_role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignLeft

        return QtCore.QVariant()





class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QTableModel Example')
        self.setMinimumWidth(240)

        # 데이터
        data = [
            {'name':'바나나', 'pic_filename': 'banana.jpg'},
            {'name':'원숭이', 'pic_filename': 'monkey.jpg'},
            {'name':'코끼리', 'pic_filename': 'elephant.jpg'},
            {'name':'보아뱀', 'pic_filename': 'boa.jpg'}
        ]

        model = MyModel(data) # 모델 선언, 데이터는 아직 없음
        lv = QtWidgets.QListView(self) # 테이블 뷰 선언
        lv.setModel(model) # 모델 적용

        self.lb_pic = QtWidgets.QLabel(self)
        self.lb_pic.setMinimumHeight(150)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lv)
        vbox.addWidget(self.lb_pic)

        self.setLayout(vbox)

        lv.clicked.connect(self.slot_selected)

    @pyqtSlot(QtCore.QModelIndex)
    def slot_selected(self, m_idx):
        f = m_idx.model()
        pixmap = QtGui.QPixmap(f.data[m_idx.row()]['pic_filename'])
        pixmap = pixmap.scaledToWidth(250)
        self.lb_pic.setPixmap(pixmap)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())