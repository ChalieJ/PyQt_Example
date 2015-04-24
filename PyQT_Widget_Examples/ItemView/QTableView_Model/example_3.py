# coding: utf-8
# TableView, TableModel 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot

# 예제 모델
# 가로 3, 세로 2의 데이터를 가졌다고 가정한 모델
class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, data=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.data = data

    # TableView가 데이터의 세로줄 수를 요구
    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.data)

    # TableView가 데이터의 가로줄 수를 요구
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.data[0])

    # TableView에서 Data를 표출을 위해 데이터 요구
    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        col = QModelIndex.column()

        if int_role == QtCore.Qt.EditRole:
            return "%d" % (self.data[row][col])

        if int_role == QtCore.Qt.DisplayRole:
            return "%d" % (self.data[row][col])

        return QtCore.QVariant()

    def setData(self, QModelIndex, QVariant, int_role=None):
        if int_role == QtCore.Qt.EditRole:
            try:
                self.data[QModelIndex.row()][QModelIndex.column()] = int(QVariant)
            except ValueError:
                pass
            self.dataChanged.emit(QModelIndex, QModelIndex)
        return True

    def flags(self, QModelIndex):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QTableModel Example')

        data = [
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,7],
        ]
        model = MyModel(data) # 모델 선언, 데이터는 아직 없음
        tbl = QtWidgets.QTableView(self) # 테이블 뷰 선언
        tbl.setModel(model) # 모델 적용
        self.lb = QtWidgets.QLabel(self)
        tbl.clicked.connect(self.slot_selected_item)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tbl)
        vbox.addWidget(self.lb)

        self.setLayout(vbox)

    @pyqtSlot(QtCore.QModelIndex)
    def slot_selected_item(self, idx):
        data = idx.data()
        self.lb.setText("선택된 데이터는 %s 입니다." % data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())