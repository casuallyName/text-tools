# -*- coding: utf-8 -*-
# @Time     : 2022/1/20 20:01
# @File     : formView.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 预览窗口

from utils import config
from uiViewForm import Ui_Form
from threads import SaveImageThread
from PySide6 import QtWidgets, QtCore, QtGui


class ViewForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(ViewForm, self).__init__()
        self.setupUi(self)
        self.image_array = None
        self.image_pix = None
        self._save_image_thread = None

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.image.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.image.customContextMenuRequested.connect(self.right_menu)

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)

        self.pushButton_ZoomIn.clicked.connect(lambda: self.zoom_picture(zoom='In'))
        self.pushButton_ZoomOut.clicked.connect(lambda: self.zoom_picture(zoom='Out'))
        self.spinBox_zoom.valueChanged.connect(self.resize_image)

    def zoom_picture(self, zoom):
        if zoom == 'In':
            self.spinBox_zoom.setValue(self.spinBox_zoom.value() + 1)
        elif zoom == 'Out':
            self.spinBox_zoom.setValue(self.spinBox_zoom.value() - 1)
        else:
            pass

    def resize_image(self):
        scaled_pixmap = self.image_pix.scaled(self.image_pix.size() * self.spinBox_zoom.value() / 100,
                                              QtGui.Qt.KeepAspectRatio, QtGui.Qt.SmoothTransformation)
        self.image.setPixmap(scaled_pixmap)

    def right_menu(self, pos) -> None:
        '''
        listWidget 控件右键菜单

        :param pos:
        :return:
        '''
        menu = QtWidgets.QMenu()
        menu.popup(QtGui.QCursor.pos())
        save_img = menu.addAction('图片另存为')
        action = menu.exec_(self.image.mapToGlobal(pos))
        if action == save_img:
            file_name, file_type = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                         '图片另存为',
                                                                         config.get('Preference', 'work_space_path'),
                                                                         "PNG 文件(*.png);;JPG 文件(*.jpg)"
                                                                         )
            self._save_image_thread = SaveImageThread(self.image_array.copy().save, file_name)
            self._save_image_thread.errorSignal.connect(self.show_critical)
            self._save_image_thread.endSignal.connect(lambda: self.show_message(file_path=file_name))
            self._save_image_thread.start()

        # 显示异常信息

    def show_critical(self, error):
        QtWidgets.QMessageBox.critical(self, "错误", error, QtWidgets.QMessageBox.Cancel)

    def show_message(self, file_path):
        QtWidgets.QMessageBox.information(self, "成功成功", f"图片已保存至 '{file_path}' ")

    def show(self) -> None:
        self.spinBox_zoom.setValue(100)
        super(ViewForm, self).show()
        self.raise_()
