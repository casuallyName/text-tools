# -*- coding: utf-8 -*-
# @Time     : 2022/1/23 7:47 PM
# @File     : formMessage.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 消息窗口

from uiMessageForm import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui


class MessageForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        self.color = QtGui.QColor()
        self.palette = QtGui.QPalette()

        super(MessageForm, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        # self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
        # QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def show(self) -> None:
        super(MessageForm, self).show()
        self.raise_()
