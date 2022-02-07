# -*- coding: utf-8 -*-
# @Time     : 2022/1/24 10:40
# @File     : formTextMiningSettings.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 词语挖掘设置

from PySide6.QtCore import Signal
from uiTextMiningForm import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui


class TextMiningForm(QtWidgets.QWidget, Ui_Form):
    closeSignal = Signal()

    def __init__(self):
        super(TextMiningForm, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)
        self.pushButton_reset.clicked.connect(self.reset)

    def reset(self):
        self.spinBox_H.setValue(20)
        self.spinBox_Dop.setValue(20)
        self.spinBox_LeftFree.setValue(30)
        self.spinBox_RightFree.setValue(30)

    def show(self) -> None:
        super(TextMiningForm, self).show()
        self.raise_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.closeSignal.emit()
        event.accept()
