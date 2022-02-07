# -*- coding: utf-8 -*-
# @Time     : 2022/1/26 10:38 PM
# @File     : formLicense.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 开源软件协议展示

from uiLicenseForm import Ui_Form
from PySide6 import QtWidgets, QtCore


class LicenseForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(LicenseForm, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def show(self) -> None:
        super(LicenseForm, self).show()
        self.raise_()
