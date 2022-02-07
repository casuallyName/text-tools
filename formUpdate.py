# -*- coding: utf-8 -*-
# @Time     : 2022/1/28 6:44 PM
# @File     : formUpdate.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 升级提示窗口

import os
import sys
from uiUpdateForm import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui


class UpdateForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(UpdateForm, self).__init__()
        self.download_type = 'patch'
        self.open_link = None
        self.setupUi(self)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)

        self.pushButton.clicked.connect(self.download)

    def download(self):
        if self.download_type == 'Patch':
            res = QtWidgets.QMessageBox.question(self, '更新', '关闭程序并启动更新？',
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                 QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                os.popen(f'Update.exe {self.open_link}')
                sys.exit()
        else:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.open_link))

    def show(self) -> None:
        super(UpdateForm, self).show()
        self.raise_()
