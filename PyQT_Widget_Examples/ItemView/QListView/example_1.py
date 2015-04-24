# coding: utf-8
# ListView, ListModel 사용예제

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# 예제 모델
# 가로 3, 세로 2의 데이터를 가졌다고 가정한 모델
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
            return "%s" % (self.data[row])

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

        data = ['바나나', '원숭이', '코끼리', '보아뱀']
        model = MyModel(data) # 모델 선언, 데이터는 아직 없음
        lv = QtWidgets.QListView(self) # 테이블 뷰 선언
        lv.setModel(model) # 모델 적용

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(lv)

        self.setLayout(vbox)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())