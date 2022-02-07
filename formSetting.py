# -*- coding: utf-8 -*-
# @Time     : 2022/1/27 5:58 PM
# @File     : formSetting.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 设置窗口

import os
import jpype
import traceback
from formUpdate import UpdateForm
from uiSettingForm import Ui_Form
from utils import config, start_jvm
from threads import CheckUpdateThread
from PySide6 import QtWidgets, QtCore, QtGui


class SettingForm(QtWidgets.QWidget, Ui_Form):
    UpdateSignal = QtCore.Signal(int, str, str, str, int)

    def __init__(self):
        super(SettingForm, self).__init__()
        self.check_update_thread = CheckUpdateThread()
        self.update_form = UpdateForm()
        self.setupUi(self)
        self.check_update_thread.endSignal.connect(self.show_update)

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.CustomizeWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.checkBox_checkUpdate.setChecked(config.getboolean('Preference', 'check_update'))

        if config.getint('Preference', 'work_space') == 0:
            self.comboBox_workSpace.setCurrentIndex(0)
            self.pushButton_openWorkSpace.setEnabled(False)
        elif config.getint('Preference', 'work_space') == 1:
            self.comboBox_workSpace.setCurrentIndex(1)
            self.pushButton_openWorkSpace.setEnabled(False)
        elif config.getint('Preference', 'work_space') == 2:
            self.comboBox_workSpace.setCurrentIndex(2)
            self.pushButton_openWorkSpace.setEnabled(True)
        else:
            self.comboBox_workSpace.setCurrentIndex(2)
            self.pushButton_openWorkSpace.setEnabled(True)
        work_space_path = config.get('Preference', 'work_space_path')
        if work_space_path != '':
            self.lineEdit_workSpacePath.setText(work_space_path)
        else:
            self.lineEdit_workSpacePath.setText('')
            config.set('Preference', 'work_space_path', os.path.dirname(os.path.realpath(__file__)))

        if jpype.isJVMStarted():
            self.pushButton_start_JVM.setEnabled(False)

        self.lineEdit_JVM_Path.setText('' if config.get('JVM', 'JVM_PATH') == 'null' else config.get('JVM', 'JVM_PATH'))
        self.lineEdit_JVM_XMS.setText(config.get('JVM', 'JVM_XMS'))
        self.lineEdit_JVM_XMX.setText(config.get('JVM', 'JVM_XMX'))
        self.listWidget.clear()
        for _, v in config.items('JAR'):
            if v.startswith('/'):
                self.listWidget.addItem(v)
            else:
                self.listWidget.addItem(os.path.abspath(v))

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)

        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.right_menu)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_start_JVM.clicked.connect(self.start_JVM)
        self.pushButton_save.clicked.connect(self.save_jdk_config)
        self.pushButton_save_1.clicked.connect(self.save_config)
        self.comboBox_workSpace.currentIndexChanged.connect(self.select_work_space_enable)
        self.pushButton_check_update.clicked.connect(lambda: self.check_update_thread.start())
        self.pushButton_openWorkSpace.clicked.connect(self.open_workspace)
        self.pushButton_open_jvm.clicked.connect(self.opem_jvm)

    def right_menu(self, pos):
        menu = QtWidgets.QMenu()
        menu.popup(QtGui.QCursor.pos())
        select_row = self.listWidget.indexAt(pos).row()
        import_file = menu.addAction('导入jar文件')
        import_path = menu.addAction('导入目录')
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
                                                 '是否清空全部资源文件？',
                                                 QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes,
                                                 QtWidgets.QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                self.listWidget.clear()
            return
        if action == delete_item:
            self.listWidget.takeItem(select_row)
            return
        if action == import_file:
            file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, '导入jar文件', './src', 'JAR 文件(*.jar)')
            if file_name != '':
                if file_name not in [self.listWidget.item(i).text() for i in range(self.listWidget.count())]:
                    self.listWidget.addItem(file_name)
                else:
                    QtWidgets.QMessageBox.warning(self, '添加失败', '添加失败，资源已存在')
            return
        if action == import_path:
            file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '导入jar文件', './src')
            if file_path not in [self.listWidget.item(i).text() for i in range(self.listWidget.count())]:
                self.listWidget.addItem(file_path)
            else:
                QtWidgets.QMessageBox.warning(self, '添加失败', '添加失败，资源已存在')
            return

    def open_workspace(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(self, '选择工作目录', '.')
        if file_path != '':
            self.lineEdit_workSpacePath.setText(file_path)
            config.set('Preference', 'work_space_path', file_path)

    def opem_jvm(self):
        file_name, file_path = QtWidgets.QFileDialog.getOpenFileName(self, '选择 jvm.dll 文件', './', 'jvm.dll')
        if file_name != '':
            self.lineEdit_JVM_Path.setText(file_name)
            config.set('JVM', 'jvm_path', file_name)

    def start_JVM(self):
        try:
            jvm_path = jpype.getDefaultJVMPath() if self.lineEdit_JVM_Path.text() == '' else self.lineEdit_JVM_Path.text()
            jars = os.pathsep.join([self.listWidget.item(i).text() for i in range(self.listWidget.count())])
            jvm_xms = self.lineEdit_JVM_XMS.text()
            jvm_xmx = self.lineEdit_JVM_XMX.text()
            start_jvm(jvm_path=jvm_path, jars=jars, jvm_xms=jvm_xms, jvm_xmx=jvm_xmx)
            if jpype.isJVMStarted():
                QtWidgets.QMessageBox.information(self, '提示', 'JVM 启动成功，已自动保存设置。')
                self.pushButton_start_JVM.setEnabled(False)

        except:
            QtWidgets.QMessageBox.critical(self, 'JVM 启动失败',
                                           f'JVM 启动失败\n{traceback.format_exc()}')

    def save_jdk_config(self):
        try:
            config.remove_section("JAR")
            config.add_section("JAR")
            for i in range(self.listWidget.count()):
                config.set("JAR", f"item_{i}", self.listWidget.item(i).text().replace(
                    os.path.dirname(os.path.realpath(__file__)) + '/', ''))
            config.set('JVM', 'jvm_xms', self.lineEdit_JVM_XMS.text())
            config.set('JVM', 'jvm_xmx', self.lineEdit_JVM_XMX.text())
            config.set('JVM', 'jvm_path', self.lineEdit_JVM_Path.text())
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src', 'config.ini'),
                      'w') as file:
                config.write(file)
            if jpype.isJVMStarted():
                QtWidgets.QMessageBox.information(self, '提示', 'JVM配置已保存，修改内容需重启软件才能后生效。')
            else:
                QtWidgets.QMessageBox.information(self, '提示', 'JVM配置已保存。')
        except:
            QtWidgets.QMessageBox.critical(self, '保存失败', traceback.format_exc())

    def save_config(self):
        try:
            if self.comboBox_workSpace.currentIndex() == 2 and self.lineEdit_workSpacePath.text() == '':
                QtWidgets.QMessageBox.warning(self, '保存失败', '工作目录不能为空')
            else:
                if self.comboBox_workSpace.currentIndex() == 0:
                    config.set('Preference', 'work_space_path', os.path.join(os.path.expanduser('~'), "Desktop"))
                elif self.comboBox_workSpace.currentIndex() == 1:
                    config.set('Preference', 'work_space_path', os.path.join(os.path.expanduser('~'), "Documents"))
                elif self.comboBox_workSpace.currentIndex() == 2:
                    config.set('Preference', 'work_space_path', self.lineEdit_workSpacePath.text())
                else:
                    config.set('Preference', 'work_space_path', os.path.dirname(os.path.realpath(__file__)))
                config.set('Preference', 'work_space', str(self.comboBox_workSpace.currentIndex()))
                config.set('Preference', 'check_update', str(self.checkBox_checkUpdate.isChecked()))

                with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src', 'config.ini'),
                          'w') as file:
                    config.write(file)
                QtWidgets.QMessageBox.information(self, '提示', '设置已保存')
        except:
            QtWidgets.QMessageBox.critical(self, '保存失败', traceback.format_exc())

    def select_work_space_enable(self):
        if self.comboBox_workSpace.currentIndex() == 0:
            self.lineEdit_workSpacePath.setText(os.path.join(os.path.expanduser('~'), "Desktop"))
            self.pushButton_openWorkSpace.setEnabled(False)
        elif self.comboBox_workSpace.currentIndex() == 1:
            self.lineEdit_workSpacePath.setText(os.path.join(os.path.expanduser('~'), "Document"))
            self.pushButton_openWorkSpace.setEnabled(False)
        elif self.comboBox_workSpace.currentIndex() == 2:
            self.lineEdit_workSpacePath.setText('')
            self.pushButton_openWorkSpace.setEnabled(True)

    def show_update(self, code):
        if self.window().isActiveWindow():
            if code == 0:
                QtWidgets.QMessageBox.information(self, 'Text Tools - 更新', '已是最新版本，无需更新')
            elif code == 1:
                self.update_form.label_version.setText(self.check_update_thread.new_version)
                self.update_form.label_date.setText(self.check_update_thread.version_date)
                self.update_form.label_info.setText(self.check_update_thread.update_info)
                self.update_form.download_type = None
                self.update_form.show()
            elif code == 2:
                self.update_form.label_version.setText(self.check_update_thread.new_version)
                self.update_form.label_date.setText(self.check_update_thread.version_date)
                self.update_form.label_info.setText(self.check_update_thread.update_info)
                self.update_form.open_link = self.check_update_thread.download_link
                self.update_form.download_type = 'Patch'
                self.update_form.show()
            elif code == -1:
                QtWidgets.QMessageBox.warning(self, 'Text Tools - 更新',
                                              f'更新失败，错误代码{self.check_update_thread.status_code}')
            else:
                QtWidgets.QMessageBox.critical(self, 'Text Tools - 更新', f'更新失败。')
        else:
            self.UpdateSignal.emit(code,
                                   self.check_update_thread.new_version,
                                   self.check_update_thread.version_date,
                                   self.check_update_thread.update_info,
                                   self.check_update_thread.status_code)

    def show(self) -> None:
        super(SettingForm, self).show()
        self.raise_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.comboBox_workSpace.setCurrentIndex(config.getint('Preference', 'work_space'))
        if config.getint('Preference', 'work_space') == 2:
            self.lineEdit_workSpacePath.setText(config.get('Preference', 'work_space_path'))
        else:
            self.lineEdit_workSpacePath.setText('')
        self.checkBox_checkUpdate.setChecked(config.getboolean('Preference', 'check_update'))
        self.lineEdit_JVM_Path.setText(config.get('JVM', 'jvm_path'))
        self.lineEdit_JVM_XMS.setText(config.get('JVM', 'jvm_xms'))
        self.lineEdit_JVM_XMX.setText(config.get('JVM', 'jvm_xmx'))
        for _, v in config.items('JAR'):
            if v.startswith('/'):
                self.listWidget.addItem(v)
            else:
                self.listWidget.addItem(os.path.abspath(v))
