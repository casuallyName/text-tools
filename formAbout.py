# -*- coding: utf-8 -*-
# @Time     : 2022/1/24 11:38
# @File     : formAbout.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 关于界面

from uiAboutForm import Ui_Form
from formLicense import LicenseForm
from PySide6 import QtWidgets, QtCore


class AboutForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(AboutForm, self).__init__()
        self.setupUi(self)
        self.license_form = LicenseForm()

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)

        self.label_open_source_software.linkActivated.connect(lambda: self.license_form.show())

    def show(self) -> None:
        super(AboutForm, self).show()
        self.raise_()
