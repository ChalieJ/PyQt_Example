# coding: utf-8
# TableView, TableModel 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# 예제 모델
# 가로 3, 세로 2의 데이터를 가졌다고 가정한 모델
class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

    # TableView가 데이터의 세로줄 수를 요구
    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 2

    # TableView가 데이터의 가로줄 수를 요구
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return 3

    # TableView에서 Data를 표출을 위해 데이터 요구
    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        col = QModelIndex.column()

        if int_role == QtCore.Qt.DisplayRole:
            return "%d, %d" % (QModelIndex.row(), QModelIndex.column())

        if int_role == QtCore.Qt.DecorationRole:
            icon = QtGui.QIcon('air.ico')
            return icon

        if int_role == QtCore.Qt.ToolTipRole:
            return 'Tooltip'

        if int_role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

        if int_role == QtCore.Qt.BackgroundRole:
            return QtGui.QBrush(QtGui.QColor('yellow'))

        return QtCore.QVariant()


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle('QTableModel Example')

        model = MyModel() # 모델 선언, 데이터는 아직 없음
        tbl = QtWidgets.QTableView(self) # 테이블 뷰 선언
        tbl.setModel(model) # 모델 적용

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(tbl)

        self.setLayout(vbox)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())