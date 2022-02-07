# -*- coding: utf-8 -*-
# @Time     : 2022/1/19 16:29
# @File     : formTextCleaning.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 文本清洗设置页面

from PySide6.QtCore import Signal
from uiTextCleaningForm import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui


class TextCleaningForm(QtWidgets.QWidget, Ui_Form):
    closeSignal = Signal()

    def __init__(self):
        super(TextCleaningForm, self).__init__()
        self.setupUi(self)
        self.check_box_dict = {
            '@': self.checkBox_1,
            '#': self.checkBox_2,
            '$': self.checkBox_3,
            '%': self.checkBox_4,
            '&': self.checkBox_5,
            '+': self.checkBox_6,
            '-': self.checkBox_7,
            '*': self.checkBox_8,
            '/': self.checkBox_9,
            '=': self.checkBox_10
        }

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.lineEdit_custom_pattern.setEnabled(False)  # 设置自定义规则输入区为未激活状态

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)
        self.checkBox_set_custom_pattern.clicked.connect(self.set_enable)  # 启用按钮点击事件对应处理
        self.pushButton_add.clicked.connect(self.add_to_list)
        self.checkBox_1.clicked.connect(lambda: self.check_box_to_list('@'))
        self.checkBox_2.clicked.connect(lambda: self.check_box_to_list('#'))
        self.checkBox_3.clicked.connect(lambda: self.check_box_to_list('$'))
        self.checkBox_4.clicked.connect(lambda: self.check_box_to_list('%'))
        self.checkBox_5.clicked.connect(lambda: self.check_box_to_list('&'))
        self.checkBox_6.clicked.connect(lambda: self.check_box_to_list('+'))
        self.checkBox_7.clicked.connect(lambda: self.check_box_to_list('-'))
        self.checkBox_8.clicked.connect(lambda: self.check_box_to_list('*'))
        self.checkBox_9.clicked.connect(lambda: self.check_box_to_list('/'))
        self.checkBox_10.clicked.connect(lambda: self.check_box_to_list('='))

        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.list_widget_right_menu)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

    # 启用按钮点击事件对应处理
    def set_enable(self):
        '''
        启用按钮被勾选时设定 特殊符号 区域为未激活，并激活自定义规则输入控件
        启用按钮未被勾选时设定 特殊符号 区域为激活，并设定自定义规则输入控件为未激活
        :return:
        '''
        self.groupBox.setEnabled(not self.checkBox_set_custom_pattern.isChecked())
        self.lineEdit_custom_pattern.setEnabled(self.checkBox_set_custom_pattern.isChecked())

    # checkBox 点选添加进(删除)列表
    def check_box_to_list(self, param):
        if self.check_box_dict[param].isChecked():
            all_items = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
            if param not in all_items:
                self.listWidget.addItem(param)
        else:
            all_items_dict = {self.listWidget.item(i).text(): i for i in range(self.listWidget.count())}
            self.listWidget.takeItem(all_items_dict[param])

    # 手动输入添加进列表
    def add_to_list(self):
        item = self.lineEdit.text()
        if item != '':
            all_items = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
            if item in all_items:
                QtWidgets.QMessageBox.warning(self, '无法添加', f"'{item}' 已在特殊符号提取列表中，请勿重复添加。")
            else:
                self.listWidget.addItem(item)
                QtWidgets.QMessageBox.information(self, '添加成功', f"'{item}' 已成功添加进特殊符号提取列表中。")
                self.lineEdit.clear()

    # 右键菜单
    def list_widget_right_menu(self, pos) -> None:
        menu = QtWidgets.QMenu()
        menu.popup(QtGui.QCursor.pos())
        select_row = self.listWidget.indexAt(pos).row()
        if select_row > -1:
            delete_item = menu.addAction('删除')
        else:
            delete_item = ''
        if self.listWidget.count() != 0:
            clean_item = menu.addAction('清空')
        else:
            clean_item = ''
        action = menu.exec(self.listWidget.mapToGlobal(pos))
        if action == clean_item:
            res = QtWidgets.QMessageBox.question(self,
                                                 '清空',
                                                 '是否清空全部特殊符号？',
                                                 QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                                 QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                self.checkBox_1.setChecked(False)
                self.checkBox_2.setChecked(False)
                self.checkBox_3.setChecked(False)
                self.checkBox_4.setChecked(False)
                self.checkBox_5.setChecked(False)
                self.checkBox_6.setChecked(False)
                self.checkBox_7.setChecked(False)
                self.checkBox_8.setChecked(False)
                self.checkBox_9.setChecked(False)
                self.checkBox_10.setChecked(False)
                self.listWidget.clear()
            return
        if action == delete_item:
            if self.check_box_dict.get(self.listWidget.item(select_row).text(), None) is not None:
                self.check_box_dict[self.listWidget.item(select_row).text()].setChecked(False)
            else:
                self.listWidget.takeItem(select_row)
            return

    def show(self) -> None:
        super(TextCleaningForm, self).show()
        self.raise_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        event.accept()

