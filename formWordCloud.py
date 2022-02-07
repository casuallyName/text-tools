# -*- coding: utf-8 -*-
# @Time     : 2022/1/20 15:12
# @File     : formWordCloud.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 词云图设置页面

import os
from utils import config
from PySide6.QtCore import Signal
from uiWordCloudForm import Ui_Form
from PySide6 import QtWidgets, QtCore, QtGui


class WordCloudForm(QtWidgets.QWidget, Ui_Form):
    closeSignal = Signal()

    def __init__(self):
        self.color = QtGui.QColor()
        self.palette = QtGui.QPalette()

        super(WordCloudForm, self).__init__()
        self.setupUi(self)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.background_colour = [(255, 255, 255), '#FFFFFF']
        self.font_colour = [(255, 255, 255), '#FFFFFF']

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        self.lineEdit_fontPath.setText(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src', 'fonts', 'msyh.ttc'))

        self.label_1.setEnabled(False)
        self.label_backgroundColour.setEnabled(False)
        self.pushButton_selectBackgroundColour.setEnabled(False)

        self.lineEdit_backgroundPath.setEnabled(False)
        self.pushButton_backgroundOpen.setEnabled(False)
        self.pushButton_backgroundShow.setEnabled(False)

        self.label_2.setEnabled(False)
        self.label_fontColour.setEnabled(False)
        self.pushButton_selectFontColour.setEnabled(False)

        self.label_3.setEnabled(False)
        self.comboBox_colourColumn.setEnabled(False)

        self.color.setNamedColor('#FFFFFF')
        self.palette.setColor(QtGui.QPalette.Window, self.color)

        self.label_backgroundColour.setAutoFillBackground(True)
        self.label_backgroundColour.setPalette(self.palette)
        self.label_backgroundColour.setFrameShape(QtWidgets.QFrame.Box)

        self.label_fontColour.setAutoFillBackground(True)
        self.label_fontColour.setPalette(self.palette)
        self.label_fontColour.setFrameShape(QtWidgets.QFrame.Box)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)

        self.radioButton_noBackground.clicked.connect(lambda: self.set_enable(1))
        self.radioButton_setBackgroundColour.clicked.connect(lambda: self.set_enable(2))
        self.checkBox_userBackground.clicked.connect(lambda: self.set_enable(3))
        self.radioButton_randomFontColour.clicked.connect(lambda: self.set_enable(4))
        self.radioButton_setFontColour.clicked.connect(lambda: self.set_enable(5))
        self.radioButton_setUserFontColour.clicked.connect(lambda: self.set_enable(6))

        self.pushButton_selectBackgroundColour.clicked.connect(
            lambda: self.get_and_set_color('backgroundColour'))  # 设置背景颜色
        self.pushButton_selectFontColour.clicked.connect(lambda: self.get_and_set_color('fontColour'))  # 设置字体颜色

        self.pushButton_backgroundOpen.clicked.connect(lambda: self.open_file('image'))
        self.pushButton_fontOpen.clicked.connect(lambda: self.open_file('font'))

    def set_enable(self, index):
        control_dict = {
            2: [self.label_1, self.label_backgroundColour, self.pushButton_selectBackgroundColour],
            3: [self.lineEdit_backgroundPath, self.pushButton_backgroundOpen, self.pushButton_backgroundShow],
            5: [self.label_2, self.label_fontColour, self.pushButton_selectFontColour],
            6: [self.label_3, self.comboBox_colourColumn]
        }
        if index == 1:
            for control in control_dict[2]:
                control.setEnabled(False)
            # for control in control_dict[3]:
            #     control.setEnabled(False)
        elif index == 2:
            for control in control_dict[2]:
                control.setEnabled(True)
            # for control in control_dict[3]:
            #     control.setEnabled(False)
        elif index == 3:
            for control in control_dict[3]:
                control.setEnabled(self.checkBox_userBackground.isChecked())
        elif index == 4:
            for control in control_dict[5]:
                control.setEnabled(False)
            for control in control_dict[6]:
                control.setEnabled(False)
        elif index == 5:
            for control in control_dict[5]:
                control.setEnabled(True)
            for control in control_dict[6]:
                control.setEnabled(False)
        elif index == 6:
            for control in control_dict[5]:
                control.setEnabled(False)
            for control in control_dict[6]:
                control.setEnabled(True)

    def get_and_set_color(self, control) -> None:
        c = QtWidgets.QColorDialog.getColor()
        r, g, b, _ = c.getRgb()
        name = c.name()
        self.color.setNamedColor(name)
        self.palette.setColor(QtGui.QPalette.Window, self.color)
        if control == 'backgroundColour':
            self.background_colour = [(r, g, b), name]
            self.label_backgroundColour.setPalette(self.palette)
        elif control == 'fontColour':
            self.font_colour = [(r, g, b), name]
            self.label_fontColour.setPalette(self.palette)
        elif control == 'contourColour':
            self.contour_color = [(r, g, b), name]
            self.label_label_contourColour.setPalette(self.palette)
        else:
            return

    def open_file(self, file_type):
        if file_type == 'image':
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                 "选择一张底图",
                                                                 config.get('Preference', 'work_space_path'),
                                                                 "PNG 文件(*.png);;JPG 文件(*.jpg)")
            if file_name != '':
                self.lineEdit_backgroundPath.setText(file_name)
        elif file_type == 'font':
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                 "选取字体文件",
                                                                 os.path.join(
                                                                     os.path.dirname(os.path.realpath(__file__)),
                                                                     'src',
                                                                     'fonts'),
                                                                 "全部字体文件(*.tt*);;TrueType 字体文件(*.TTF);;TrueType Collection 字体文件(*.ttc)")
            if file_name != '':
                self.lineEdit_fontPath.setText(file_name)

    def show(self) -> None:
        super(WordCloudForm, self).show()
        self.raise_()

    def closeEvent(self, event) -> None:
        self.closeSignal.emit()
        event.accept()
