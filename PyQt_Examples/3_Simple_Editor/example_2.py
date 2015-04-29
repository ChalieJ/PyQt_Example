# coding: utf-8
# 윈도우 메모장을 따라 만들기, 새 파일, 저장 및 불러오기 기능 구형
# 아래의 선행 학습이 필요
## QMainWindow
## QAction
## QIcon
## QMessageBox

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot


class Form(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setGeometry(100,100,640,480)
        self.file_name = '제목없음'
        self.program_name = 'PyQt 메모장'
        self.is_saved = True

        self.init_ui()


    # Qt Designer를 사용하지 않았으므로 따로 Ui 코드 작성
    def init_ui(self):
        # Action 설정
        # 새 파일
        self.act_new_file = QtWidgets.QAction('&New', self)
        self.act_new_file.setShortcut(QtGui.QKeySequence('Ctrl+N'))
        self.act_new_file.triggered.connect(self.slot_new)
        # 저장
        self.act_save_file = QtWidgets.QAction('&Save', self)
        icon = QtGui.QIcon('save.ico')
        self.act_save_file.setIcon(icon)
        self.act_save_file.setShortcut(QtGui.QKeySequence('Ctrl+S'))
        self.act_save_file.triggered.connect(self.slot_save)
        # 열기
        self.act_open_file = QtWidgets.QAction('&Open', self)
        self.act_open_file.setShortcut(QtGui.QKeySequence('Ctrl+O'))
        self.act_open_file.triggered.connect(self.slot_open)
        # 끝내기
        self.act_quit = QtWidgets.QAction('&Quit', self)
        self.act_quit.setShortcut(QtGui.QKeySequence('Ctrl+Q'))
        self.act_quit.triggered.connect(self.slot_quit)
        # 메뉴바 생성 및 액션 적용
        menu = self.menuBar()
        menu_file = menu.addMenu('&File')
        menu_file.addAction(self.act_new_file)
        menu_file.addAction(self.act_save_file)
        menu_file.addAction(self.act_open_file)
        menu_file.addSeparator()
        menu_file.addAction(self.act_quit)

        # 텍스트 에디터 생성 및 시그널 연결
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.textChanged.connect(self.slot_content_changed)

        # 초기 설정
        self.act_save_file.setEnabled(False)
        self.set_title()
        self.setCentralWidget(self.text_edit)


    # 윈도우 타이틀 변경
    def set_title(self):
        self.setWindowTitle(self.file_name + ' - ' + self.program_name)

    @pyqtSlot()
    def slot_content_changed(self):
        self.is_saved = False
        self.act_save_file.setEnabled(True)

    @pyqtSlot()
    def slot_new(self):
        if self.is_saved is not True:
            reply = QtWidgets.QMessageBox.information(
                self,
                u'Save',u"작성한 내용을 저장하시겠습니까?",
                QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel,
                QtWidgets.QMessageBox.Save
            )

            if reply == QtWidgets.QMessageBox.Yes:
                self.slot_save()
            elif reply == QtWidgets.QMessageBox.No:
                return

        self.text_edit.clear()
        self.act_save_file.setEnabled(False)
        self.file_name = '제목없음'
        self.set_title()




    @pyqtSlot()
    def slot_open(self):
        fdial = QtWidgets.QFileDialog(self)
        fdial.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        file_name = fdial.getOpenFileName(self, '파일열기', filter='*.txt')[0]
        if file_name == '':
            return
        fd = open(file_name, 'r')
        buf = fd.read()
        fd.close()
        self.text_edit.clear()
        self.text_edit.insertPlainText(buf)
        self.file_name = file_name
        self.set_title()


    @pyqtSlot()
    def slot_save(self):
        buf = self.text_edit.toPlainText()
        fdial = QtWidgets.QFileDialog(self)
        fdial.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_name = fdial.getSaveFileName(self, '파일저장', filter='*.txt')[0]
        if file_name == '':
            return
        fd = open(file_name, 'w')
        fd.write(buf)
        fd.close()
        self.file_name = file_name
        self.act_save_file.setEnabled(False)
        self.set_title()

    @pyqtSlot()
    def slot_quit(self):
        if self.is_saved is not True:
            reply = QtWidgets.QMessageBox.information(
                self,
                u'Save',u"작성한 내용을 저장하시겠습니까?",
                QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel,
                QtWidgets.QMessageBox.Save
            )

            if reply == QtWidgets.QMessageBox.Yes:
                self.slot_save()
            elif reply == QtWidgets.QMessageBox.No:
                pass
        app.quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())

