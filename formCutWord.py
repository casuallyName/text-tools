# -*- coding: utf-8 -*-
# @Time     : 2022/1/19 17:35
# @File     : formCutWord.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 分词设置页面

import traceback
from PySide6.QtCore import Signal
from uiCutWordForm import Ui_Form
from utils import config, default_stopword
from PySide6 import QtWidgets, QtCore, QtGui


class CutWordForm(QtWidgets.QWidget, Ui_Form):
    closeSignal = Signal()

    def __init__(self):
        super(CutWordForm, self).__init__()
        self.setupUi(self)
        self.pos_list = ['a', 'd', 'i', 'n', 'nr', 'ns', 'nt', 'v', 'vn']

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        self.label.setVisible(False)
        self.groupBox_3.setVisible(False)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)
        self.pushButton_addStopWord.clicked.connect(
            lambda: self.add_to_list(self.lineEdit_stopWord, self.listWidget_stopWord, '停用词'))  #
        self.pushButton_addUserWord.clicked.connect(
            lambda: self.add_to_list(self.lineEdit_userWord, self.listWidget_userWord, '自定义词'))

        self.listWidget_stopWord.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_stopWord.customContextMenuRequested.connect(self.stop_word_list_widget_right_menu)
        self.listWidget_stopWord.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.listWidget_userWord.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_userWord.customContextMenuRequested.connect(self.user_word_list_widget_right_menu)
        self.listWidget_userWord.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.checkBox_a.stateChanged.connect(lambda: self.set_pos(self.checkBox_a, 'a'))
        self.checkBox_ad.stateChanged.connect(lambda: self.set_pos(self.checkBox_ad, 'ad'))
        self.checkBox_an.stateChanged.connect(lambda: self.set_pos(self.checkBox_an, 'an'))
        self.checkBox_d.stateChanged.connect(lambda: self.set_pos(self.checkBox_d, 'd'))
        self.checkBox_i.stateChanged.connect(lambda: self.set_pos(self.checkBox_i, 'i'))
        self.checkBox_n.stateChanged.connect(lambda: self.set_pos(self.checkBox_n, 'n'))
        self.checkBox_nr.stateChanged.connect(lambda: self.set_pos(self.checkBox_nr, 'nr'))
        self.checkBox_ns.stateChanged.connect(lambda: self.set_pos(self.checkBox_ns, 'ns'))
        self.checkBox_nt.stateChanged.connect(lambda: self.set_pos(self.checkBox_nt, 'nt'))
        self.checkBox_nz.stateChanged.connect(lambda: self.set_pos(self.checkBox_nz, 'nz'))
        self.checkBox_t.stateChanged.connect(lambda: self.set_pos(self.checkBox_t, 't'))
        self.checkBox_tg.stateChanged.connect(lambda: self.set_pos(self.checkBox_tg, 'tg'))
        self.checkBox_v.stateChanged.connect(lambda: self.set_pos(self.checkBox_v, 'v'))
        self.checkBox_vd.stateChanged.connect(lambda: self.set_pos(self.checkBox_vd, 'vd'))
        self.checkBox_vn.stateChanged.connect(lambda: self.set_pos(self.checkBox_vn, 'vn'))

    def add_to_list(self, line_edit, list_widget, types):
        item = line_edit.text()
        if item != '':
            all_items = [list_widget.item(i).text() for i in range(list_widget.count())]
            if item in all_items:
                QtWidgets.QMessageBox.warning(self, '无法添加', f"'{item}' 已在{types}提取列表中，请勿重复添加。")
            else:
                list_widget.addItem(item)
                # QtWidgets.QMessageBox.information(self, '添加成功', f"'{item}' 已成功添加进{types}列表中。")
                line_edit.clear()

    def stop_word_list_widget_right_menu(self, pos):
        menu = QtWidgets.QMenu()
        menu.popup(QtGui.QCursor.pos())
        select_row = self.listWidget_stopWord.indexAt(pos).row()
        menu_import = menu.addMenu('导入')
        menu_import.addAction('从文件')
        menu_import.addAction('程序预置')
        if select_row > -1:
            menu.addAction('删除')
        if self.listWidget_stopWord.count() != 0:
            menu.addAction('清空')
            menu.addAction('导出')
        action = menu.exec(self.listWidget_stopWord.mapToGlobal(pos))
        if action is not None:
            if action.text() == '清空':
                res = QtWidgets.QMessageBox.question(self,
                                                     '清空',
                                                     '是否清空全部停用词？',
                                                     QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                                     QtWidgets.QMessageBox.No)
                if res == QtWidgets.QMessageBox.Yes:
                    self.listWidget_stopWord.clear()
                return
            if action.text() == '删除':
                self.listWidget_stopWord.takeItem(select_row)
                return
            if action.text() == '从文件':
                self.add_word_from_file(self.listWidget_stopWord)
            if action.text() == '程序预置':
                all_words = [self.listWidget_stopWord.item(i).text() for i in range(self.listWidget_stopWord.count())]
                for stopword in default_stopword:
                    if stopword != '' and stopword not in all_words:
                        all_words.append(stopword)
                        self.listWidget_stopWord.addItem(stopword)
                return
            if action.text() == '导出':
                self.export_word2file(self.listWidget_stopWord, '保存停用词')

    def user_word_list_widget_right_menu(self, pos):
        menu = QtWidgets.QMenu()
        menu.popup(QtGui.QCursor.pos())
        select_row = self.listWidget_userWord.indexAt(pos).row()
        menu.addAction('导入')
        if select_row > -1:
            menu.addAction('删除')
        if self.listWidget_userWord.count() != 0:
            menu.addAction('清空')
            menu.addAction('导出')
        action = menu.exec(self.listWidget_userWord.mapToGlobal(pos))
        if action is not None:
            if action.text() == '清空':
                res = QtWidgets.QMessageBox.question(self,
                                                     '清空',
                                                     '是否清空全部自定义词？',
                                                     QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                                     QtWidgets.QMessageBox.No)
                if res == QtWidgets.QMessageBox.Yes:
                    self.listWidget_userWord.clear()
                return
            if action.text() == '删除':
                self.listWidget_userWord.takeItem(select_row)
                return
            if action.text() == '导入':
                self.add_word_from_file(self.listWidget_userWord)
                return
            if action.text() == '导出':
                self.export_word2file(self.listWidget_stopWord, '保存自定义词')

    def add_word_from_file(self, list_widget):
        file_path, file_type = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                     '打开文件',
                                                                     config.get('Preference', 'work_space_path'),
                                                                     '文本文档 (*.txt)')
        if file_path != '':
            all_words = [list_widget.item(i).text() for i in range(list_widget.count())]
            count = 0
            with open(file_path, encoding='utf-8') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    if line != '' and line not in all_words:
                        all_words.append(line)
                        list_widget.addItem(line)
                        count += 1
            QtWidgets.QMessageBox.information(self, '完成', f'共导入{count}个词语。')

    def export_word2file(self, list_widget, caption):
        file_name, file_type = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                     caption,
                                                                     config.get('Preference', 'work_space_path'),
                                                                     '文本文档 (*.txt)')
        if file_name != '':
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.writelines([list_widget.item(i).text() + '\n' for i in range(list_widget.count())])
                QtWidgets.QMessageBox.information(self, '完成', f"文件已保存至'{file_name}'")
            except:
                QtWidgets.QMessageBox.critical(self, '保存失败', traceback.format_exc())

    def set_pos(self, pos_control, pos):
        if pos_control.isChecked():
            self.pos_list.append(pos)
        else:
            self.pos_list.remove(pos)

    def get_stop_word(self):
        return [self.listWidget_stopWord.item(i).text() for i in range(self.listWidget_stopWord.count())]

    def get_user_word(self):
        return [self.listWidget_userWord.item(i).text() for i in range(self.listWidget_userWord.count())]

    def show(self) -> None:
        super(CutWordForm, self).show()
        self.raise_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        event.accept()
