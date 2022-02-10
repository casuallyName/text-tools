# -*- coding: utf-8 -*-
# @Time     : 2022/1/17 14:16
# @File     : Main_Window.py
# @Author   : Zhou Hang
# @email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 主窗口

import os
import sys
import jpype
from formAbout import AboutForm
from formCutWord import CutWordForm
from formMessage import MessageForm
from formSetting import SettingForm
from formTextCleaning import TextCleaningForm
from formTextMining import TextMiningForm
from formUpdate import UpdateForm
from formView import ViewForm
from formWordCloud import WordCloudForm
from threads import CutWordThread
from threads import MakeWordCloudThread
from threads import ReadFileThread
from threads import ReadImageThread
from threads import SaveImageThread
from threads import TextCleaningThread
from threads import TextClusteringThread
from threads import TextMiningThread
from threads import WriteExcelThread
from uiMainWindow import Ui_MainWindow
from PySide6 import QtWidgets, QtCore, QtGui
from utils import Args, config, built_version, built_date


class Window(Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.data = None
        self.wc_gen = None
        self.show_data = None
        self.select_column_dict = {'All': {}, 'Text': {}, 'Rank': {}, 'Color': {}}
        self.all_pages = 1
        self.head_index = 0

        self.check_update_click = False

        self.icon_run = QtGui.QIcon()
        self.icon_run.addFile(u"src/img/Run.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_wait = QtGui.QIcon()
        self.icon_wait.addFile(u"src/img/Wait.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_stop = QtGui.QIcon()
        self.icon_stop.addFile(u"src/img/Stop.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.about_form = AboutForm()
        self.text_cleaning_form = TextCleaningForm()
        self.cut_word_form = CutWordForm()
        self.word_cloud_form = WordCloudForm()
        self.view_form = ViewForm()
        self.message_form = MessageForm()
        self.text_mining_form = TextMiningForm()
        self.setting_form = SettingForm()
        self.update_form = UpdateForm()

        self._read_file_thread = None
        self._show_table_thread = None
        self._read_image_thread = None
        self._write_excel_thread = None
        self._text_cleaning_thread = None
        self._text_mining_thread = None
        self._cut_word_thread = None
        self._text_clustering_thread = None
        self._make_word_cloud_thread = None
        self._save_image_thread = None

        if config.getboolean('Preference', 'check_update'):
            self.setting_form.check_update_thread.start()

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        self.about_form.label_version.setText(
            f"版本 : v{built_version} (built on {built_date})")
        self.label_cutModelExtraction.setVisible(False)
        self.spinBox_cutModelExtraction.setVisible(False)
        self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 95))

    def retranslateUi(self, MainWindow):
        Ui_MainWindow.retranslateUi(self, MainWindow)

        self.action_about.triggered.connect(lambda: self.about_form.show())  # 关于
        self.action_check_update.triggered.connect(self.check_update)
        self.action_cutWordSetting.triggered.connect(  # menu 分词 对应处理
            lambda: self.show_model_setting_form(self.cut_word_form, self.action_cutWordSetting, 2)
        )
        self.actionJVM.triggered.connect(lambda: self.show_setting_form(page=1))  # 设置 JVM
        self.action_open.triggered.connect(self.open_file)  # 打开文件
        self.action_preference.triggered.connect(lambda: self.show_setting_form(page=0))  # 设置 首选项
        self.action_textCleaningSetting.triggered.connect(  # menu 文本清洗 对应处理
            lambda: self.show_model_setting_form(self.text_cleaning_form, self.action_textCleaningSetting, 0))
        self.action_textMiningSetting.triggered.connect(  # menu 词语挖掘 对应处理
            lambda: self.show_model_setting_form(self.text_mining_form, self.action_textMiningSetting, 1)
        )
        self.action_wordCloudImage.triggered.connect(self.save_image)  # 导出词云图
        self.action_wordCloudSetting.triggered.connect(  # menu 词云图 对应处理
            lambda: self.show_model_setting_form(self.word_cloud_form, self.action_wordCloudSetting, 4)
        )

        self.comboBox_selectColumn.currentIndexChanged.connect(self.record_select_column)  # 记录输入列选择
        self.comboBox_wordCloudText.currentIndexChanged.connect(self.record_select_column)  # 记录输入列选择
        self.comboBox_wordCloudRank.currentIndexChanged.connect(self.record_select_column)  # 记录输入列选择
        self.comboBox_textClusteringModelSelect.currentIndexChanged.connect(self.set_spin_box_type)  # 聚类模型参数整形浮点切换
        self.comboBox_cutWordModelSelect.currentIndexChanged.connect(self.set_spin_box_enabled)  # 分词模型参数输入Enabled切换
        self.cut_word_form.closeSignal.connect(lambda: self.action_cutWordSetting.setChecked(False))

        self.pushButton_Up.clicked.connect(lambda: self.turn_pages('+'))  # 下一页按钮对应处理
        self.pushButton_UpTop.clicked.connect(lambda: self.turn_pages('++'))  # 尾页对应处理
        self.pushButton_Down.clicked.connect(lambda: self.turn_pages('-'))  # 上一页对应处理
        self.pushButton_DownTop.clicked.connect(lambda: self.turn_pages('--'))  # 首页对应处理
        self.pushButton_viewWordCloud.clicked.connect(lambda: self.view_image(image_type='self'))  # 主程序预览按钮对应处理
        self.pushButton_start.clicked.connect(self.get_parma_and_run_thread)  # 开始按钮响应事件
        self.pushButton_makeWordCloud.clicked.connect(self.get_parma_and_make_thread)  # 制作按钮响应事件
        self.pushButton_textCleaningSetting.clicked.connect(
            lambda: self.show_model_setting_form(self.text_cleaning_form,
                                                 self.action_textCleaningSetting,
                                                 0))  # 文本清洗模型高级设置按钮点击事件
        self.pushButton_cutWordSetting.clicked.connect(
            lambda: self.show_model_setting_form(self.cut_word_form, self.action_cutWordSetting, 2))  # 分词页高级设置按钮响应函数
        self.pushButton_wordMiningSetting.clicked.connect(  # 词语挖掘页高级设置响应按钮
            lambda: self.show_model_setting_form(self.text_mining_form, self.action_textMiningSetting,
                                                 1))
        self.pushButton_wordCloudSetting.clicked.connect(
            lambda: self.show_model_setting_form(self.word_cloud_form, self.action_wordCloudSetting, 4))  # 词云图高级设置响应函数

        self.setting_form.UpdateSignal.connect(self.show_update_info)
        self.spinBox_everyPage.valueChanged.connect(self.change_every_page)  # 页内显示数据量变化对应处理
        self.spinBox_pageNow.valueChanged.connect(self.change_table_show)  # 数据预览当前页数变化对应处理

        self.tabWidget.currentChanged.connect(self.update_combo_box)  # 表格选择改变对应处理
        self.tabWidget_modelChoice.currentChanged.connect(self.model_choice_change)  # 模型选择对应处理函数
        self.tableWidget.itemChanged.connect(self.change_table_value)  # 修改表格对应的处理函数

        self.text_cleaning_form.closeSignal.connect(lambda: self.action_textCleaningSetting.setChecked(False))
        self.text_cleaning_form.checkBox_set_custom_pattern.clicked.connect(  # 分词模型设置页启用按钮对应主页处理函数
            self.set_custom_pattern)
        self.text_mining_form.closeSignal.connect(lambda: self.action_textMiningSetting.setChecked(False))

        self.word_cloud_form.comboBox_colourColumn.currentIndexChanged.connect(self.record_select_column)  # 记录输入列选择
        self.word_cloud_form.closeSignal.connect(lambda: self.action_wordCloudSetting.setChecked(False))
        self.word_cloud_form.pushButton_backgroundShow.clicked.connect(self.read_image)  # 底图预览
        self.word_cloud_form.checkBox_userBackground.clicked.connect(
            self.set_enable_width_height_enable)  # 词云图 宽高 控件状态设定
        self.word_cloud_form.radioButton_noBackground.clicked.connect(
            self.set_enable_width_height_enable)  # 词云图 宽高 控件状态设定
        self.word_cloud_form.radioButton_setBackgroundColour.clicked.connect(
            self.set_enable_width_height_enable)  # 词云图 宽高 控件状态设定

    # 展示模型奢者页面 并至于程序最前
    def show_model_setting_form(self, form, action, idx):
        action.setChecked(True)
        self.tabWidget_modelChoice.setCurrentIndex(idx)
        form.show()

    # 展示设置页面
    def show_setting_form(self, page):
        if jpype.isJVMStarted():
            self.setting_form.pushButton_start_JVM.setEnabled(False)
        self.setting_form.tabWidget.setCurrentIndex(page)
        self.setting_form.show()

    # 选择文件
    def open_file(self):
        '''
        选择文件， 启动读取文件线程
        :return:
        '''
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
                                                                     "选取文件",
                                                                     config.get('Preference', 'work_space_path'),
                                                                     "所有 Excel 文件(*.xl*);;"
                                                                     "Excel 工作簿(*.xlsx);;"
                                                                     "Excel 97-2003(*.xls);;"
                                                                     "CSV UTF-8 (逗号分隔) (*.csv)")
        if file_name != '':
            self.menubar.setEnabled(False)
            self._read_file_thread = ReadFileThread(file_path=file_name, file_type=file_type)
            self._read_file_thread.endSignal.connect(self.get_table_file)
            self.statusbar.showMessage('正在读取文件')
            self.message_form.label.setText('正在读取文件 ...')
            self.message_form.show()
            self._read_file_thread.endSignal.connect(lambda: self.message_form.close())
            self._read_file_thread.start()

    # 保存数据
    def save_data(self, data):
        if len(data) == 1:
            file_name, file_type = QtWidgets.QFileDialog.getSaveFileName(MainWindow,
                                                                         "选取文件",
                                                                         os.path.join(config.get('Preference',
                                                                                                 'work_space_path'),
                                                                                      list(data.keys())[0]),
                                                                         "Excel 工作簿(*.xlsx);;"
                                                                         "CSV UTF-8 (逗号分隔) (*.csv)")
        else:
            file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
                                                                         "选取文件",
                                                                         config.get('Preference', 'work_space_path'),
                                                                         "Excel 工作簿(*.xlsx);;")
        if file_name != '':
            self._write_excel_thread = WriteExcelThread(file_name=file_name, file_type=file_type, data_dict=data)
            self._write_excel_thread.errorSignal.connect(self.show_critical)
            self._write_excel_thread.endSignal.connect(lambda: self.message_form.close())
            self.message_form.label.setText('正在保存文件 ...')
            self.message_form.show()
            self._write_excel_thread.start()
        else:
            self.statusbar.showMessage('未选择文件', 5)

    # 保存图片
    def save_image(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(MainWindow,
                                                             "选择一张底图",
                                                             config.get('Preference', 'work_space_path'),
                                                             "PNG 文件(*.png);;JPG 文件(*.jpg)")
        if file_name != '':
            self._save_image_thread = SaveImageThread(save_func=self.wc_gen.to_file, file_path=file_name)
            self._save_image_thread.errorSignal.connect(self.show_critical)
            self._save_image_thread.endSignal.connect(lambda: self.message_form.close())
            self.message_form.label.setText('正在保存图片 ...')
            self.message_form.show()
            self._save_image_thread.start()

    # 接收读取文件线程的结果，并开启展示数据线程
    def get_table_file(self):
        '''
        接收读取文件线程的结果，并开启展示数据线程

        :return:
        '''

        self.data = self._read_file_thread.data
        self.statusbar.showMessage('')
        self.menubar.setEnabled(True)
        self.tabWidget.blockSignals(True)
        self.tabWidget.clear()
        for i in self.data:
            self.tabWidget.addTab(QtWidgets.QWidget(), str(i))
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.blockSignals(False)
        self.update_save_menu()
        items = ['请选择一列数据'] + self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].columns.tolist()
        self.select_column_dict = {'All': {}, 'Text': {}, 'Rank': {}, 'Color': {}}
        self.comboBox_selectColumn.blockSignals(True)
        self.comboBox_selectColumn.clear()
        self.comboBox_selectColumn.addItems(items)
        self.comboBox_selectColumn.blockSignals(False)
        self.comboBox_wordCloudText.blockSignals(True)
        self.comboBox_wordCloudText.clear()
        self.comboBox_wordCloudText.addItems(items)
        self.comboBox_wordCloudText.blockSignals(False)
        self.comboBox_wordCloudRank.blockSignals(True)
        self.comboBox_wordCloudRank.clear()
        self.comboBox_wordCloudRank.addItems(items)
        self.comboBox_wordCloudRank.blockSignals(False)
        self.word_cloud_form.comboBox_colourColumn.blockSignals(True)
        self.word_cloud_form.comboBox_colourColumn.clear()
        self.word_cloud_form.comboBox_colourColumn.addItems(items)
        self.word_cloud_form.comboBox_colourColumn.blockSignals(False)
        self.change_table_show()

    # 依据tabWidget选择对应文件
    def select_data(self) -> bool:
        '''
        依据tabWidget选择对应文件

        :return:
        '''
        if self.data is None:
            return False
        else:
            self.show_data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())]
            self.all_pages = self.show_data.shape[0] / self.spinBox_everyPage.value()
            self.all_pages = int(self.all_pages) + (0 if int(self.all_pages) == self.all_pages else 1)
            return True

    # 更新保存列表
    def update_save_menu(self):
        if self.data is None:
            self.save_action_list = []
            self.menu_table.clear()
            action = QtGui.QAction(MainWindow)
            action.setObjectName(u"action")
            action.setText('无文件可保存')
            action.setEnabled(False)
            self.save_action_list.append(action)
            self.menu_table.addAction(action)
        else:
            self.save_action_list = []
            self.menu_table.clear()
            if len(self.data) > 1:
                action = QtGui.QAction(MainWindow)
                action.setObjectName(u"action")
                action.setText('保存全部表格')
                action.triggered.connect(lambda: self.save_data(self.data))
                action.setEnabled(True)
                self.save_action_list.append(action)
                self.menu_table.addAction(action)
            for k, v in self.data.items():
                action = QtGui.QAction(MainWindow)
                action.setObjectName(u"action_" + str(k))
                action.setText(str(k))
                action.triggered.connect(lambda: self.save_data({k: v}))
                action.setEnabled(True)
                self.save_action_list.append(action)
                self.menu_table.addAction(action)
        if self.wc_gen is None:
            self.action_wordCloudImage.setText('无图片可保存')
            self.action_wordCloudImage.setEnabled(False)
        else:
            self.action_wordCloudImage.setText('保存词云图')
            self.action_wordCloudImage.setEnabled(True)

    # 页内显示数据量变化对应处理函数
    def change_every_page(self):
        '''
        重制spinBox_pageNow，并再次开启数据显示线程

        :return:
        '''
        if self.head_index == 0:
            self.spinBox_pageNow.blockSignals(True)
            self.spinBox_pageNow.setValue(1)
            self.spinBox_pageNow.blockSignals(False)
        else:
            self.spinBox_pageNow.blockSignals(True)
            self.spinBox_pageNow.setValue(int(self.head_index / self.spinBox_everyPage.value()) + 1)
            self.spinBox_pageNow.blockSignals(False)
        self.change_table_show()

    #  sheet表名选择对应处理 comboBox
    def update_combo_box(self):
        '''
        依据 tabWidget 选择修改 comboBox 列名选择

        :return:
        '''
        self.update_save_menu()
        items = ['请选择一列数据'] + self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].columns.tolist()
        select_text = self.select_column_dict['All'].get(self.tabWidget.tabText(self.tabWidget.currentIndex()),
                                                         '请选择一列数据')
        self.comboBox_selectColumn.blockSignals(True)
        self.comboBox_selectColumn.clear()
        self.comboBox_selectColumn.addItems(items)
        for i, item in enumerate(items):
            if item == select_text:
                self.comboBox_selectColumn.setCurrentIndex(i)
                break
        else:
            self.comboBox_selectColumn.setCurrentIndex(0)
        self.comboBox_selectColumn.blockSignals(False)
        select_text = self.select_column_dict['Text'].get(self.tabWidget.tabText(self.tabWidget.currentIndex()),
                                                          '请选择一列数据')
        self.comboBox_wordCloudText.blockSignals(True)
        self.comboBox_wordCloudText.clear()
        self.comboBox_wordCloudText.addItems(items)
        for i, item in enumerate(items):
            if item == select_text:
                self.comboBox_wordCloudText.setCurrentIndex(i)
                break
        else:
            self.comboBox_wordCloudText.setCurrentIndex(0)
        self.comboBox_wordCloudText.blockSignals(False)
        select_text = self.select_column_dict['Rank'].get(self.tabWidget.tabText(self.tabWidget.currentIndex()),
                                                          '请选择一列数据')
        self.comboBox_wordCloudRank.blockSignals(True)
        self.comboBox_wordCloudRank.clear()
        self.comboBox_wordCloudRank.addItems(items)
        for i, item in enumerate(items):
            if item == select_text:
                self.comboBox_wordCloudRank.setCurrentIndex(i)
                break
        else:
            self.comboBox_wordCloudRank.setCurrentIndex(0)
        self.comboBox_wordCloudRank.blockSignals(False)
        select_text = self.select_column_dict['Color'].get(self.tabWidget.tabText(self.tabWidget.currentIndex()),
                                                           '请选择一列数据')
        self.word_cloud_form.comboBox_colourColumn.blockSignals(True)
        self.word_cloud_form.comboBox_colourColumn.clear()
        self.word_cloud_form.comboBox_colourColumn.addItems(items)
        for i, item in enumerate(items):
            if item == select_text:
                self.word_cloud_form.comboBox_colourColumn.setCurrentIndex(i)
                break
        else:
            self.word_cloud_form.comboBox_colourColumn.setCurrentIndex(0)
        self.word_cloud_form.comboBox_colourColumn.blockSignals(False)
        self.change_table_show()

    # 记录每个sheet表选择的列名
    def record_select_column(self):
        self.select_column_dict['All'][
            self.tabWidget.tabText(self.tabWidget.currentIndex())] = self.comboBox_selectColumn.currentText()
        self.select_column_dict['Text'][
            self.tabWidget.tabText(self.tabWidget.currentIndex())] = self.comboBox_wordCloudText.currentText()
        self.select_column_dict['Rank'][
            self.tabWidget.tabText(self.tabWidget.currentIndex())] = self.comboBox_wordCloudRank.currentText()
        self.select_column_dict['Color'][
            self.tabWidget.tabText(
                self.tabWidget.currentIndex())] = self.word_cloud_form.comboBox_colourColumn.currentText()

    # 修改页面数据显示内容
    def change_table_show(self):
        '''
        修改页面数据显示内容

        :return:
        '''
        if self.select_data():
            self.set_enabled(False)
            self.spinBox_pageNow.setMaximum(self.all_pages)
            self.label_pageMax.setText(f'/{self.all_pages} (每页')
            self.head_index = self.spinBox_everyPage.value() * (self.spinBox_pageNow.value() - 1)

            self.tableWidget.blockSignals(True)
            data = self.show_data.iloc[
                   self.spinBox_everyPage.value() * (
                           self.spinBox_pageNow.value() - 1):
                   self.spinBox_everyPage.value() * self.spinBox_pageNow.value()]
            row_shape, column_shape = data.shape
            self.tableWidget.setRowCount(data.shape[0])
            self.tableWidget.setColumnCount(data.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(data.columns)
            sample_data = data.values
            for row in range(row_shape):
                for column in range(column_shape):
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(
                        '' if str(sample_data[row][column]) == 'nan' else str(sample_data[row][column])))
            self.tableWidget.blockSignals(False)
            self.set_enabled(True)

    # 词云图制作时屏蔽开始按钮和数据输入选择
    def model_choice_change(self):
        if self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '文本清洗':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 95))
        elif self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '词语挖掘':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 85))
        elif self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '文本分词':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 85))
        elif self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '文本聚类':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 85))
        elif self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '词云图制作':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 125))
        elif self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '地址标准化':
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 85))
        else:
            self.tabWidget_modelChoice.setMaximumSize(QtCore.QSize(16777215, 125))
        if self.tabWidget_modelChoice.tabText(self.tabWidget_modelChoice.currentIndex()) == '词云图制作':
            self.comboBox_selectColumn.setVisible(False)
            self.pushButton_start.setVisible(False)
            self.progressBar.setVisible(False)
        else:
            self.comboBox_selectColumn.setVisible(True)
            self.pushButton_start.setVisible(True)
            self.progressBar.setVisible(True)

    # 设置控件状态
    def set_enabled(self, enable):
        if not enable:
            MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.tabWidget_modelChoice.setEnabled(enable)
        self.comboBox_selectColumn.setEnabled(enable)
        self.pushButton_start.setEnabled(enable)
        self.tableWidget.setEnabled(enable)
        self.pushButton_UpTop.setEnabled(enable)
        self.pushButton_Up.setEnabled(enable)
        self.spinBox_pageNow.setEnabled(enable)
        self.spinBox_everyPage.setEnabled(enable)
        self.pushButton_Down.setEnabled(enable)
        self.pushButton_DownTop.setEnabled(enable)
        self.tabWidget.setEnabled(enable)
        if enable:
            self.pushButton_start.setText('开始')
            self.pushButton_start.setIcon(self.icon_run)
        if enable:
            self.statusbar.showMessage('')
            MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    # 词云图 宽高 控件状态设定
    def set_enable_width_height_enable(self):
        if self.word_cloud_form.checkBox_userBackground.isChecked():
            self.spinBox_wordCloudImgWidth.setEnabled(False)
            self.spinBox_wordCloudImgHeight.setEnabled(False)
        else:
            self.spinBox_wordCloudImgWidth.setEnabled(True)
            self.spinBox_wordCloudImgHeight.setEnabled(True)

    # 翻页按钮对应处理函数
    def turn_pages(self, flag):
        '''
        翻页按钮对应处理函数

        :param flag:
        :return:
        '''
        if flag == '++':
            self.spinBox_pageNow.setValue(1)
        elif flag == '-':
            if self.spinBox_pageNow.value() + 1 <= self.all_pages:
                self.spinBox_pageNow.setValue(self.spinBox_pageNow.value() + 1)
        elif flag == '+':
            if self.spinBox_pageNow.value() - 1 > 0:
                self.spinBox_pageNow.setValue(self.spinBox_pageNow.value() - 1)
        elif flag == '--':
            self.spinBox_pageNow.setValue(self.all_pages)

    # 修改表格对应的处理函数
    def change_table_value(self, item):
        '''
        页面修改数据时对应修改底层数据

        :param item:
        :return:
        '''
        if ('' if str(self.show_data.iloc[item.row(), item.column()]) == 'nan' else str(
                self.show_data.iloc[item.row(), item.column()])) != item.text():
            self.data[list(self.data.keys())[self.tabWidget.currentIndex()]].iloc[self.spinBox_everyPage.value() * (
                    self.spinBox_pageNow.value() - 1) + item.row(), item.column()] = eval(
                item.text()) if item.text().isdigit() else item.text()

    # 聚类模型参数整形浮点切换
    def set_spin_box_type(self):
        '''
        comboBox_textClusteringModelSelect.currentIndex() 为 2 时切换至整形类型，其余为浮点类型

        :return:
        '''
        if self.comboBox_textClusteringModelSelect.currentIndex() == 1:
            self.spinBox_textClusteringParam = QtWidgets.QDoubleSpinBox(self.tab_3)
            self.spinBox_textClusteringParam.setObjectName(u"spinBox_textClusteringParam")
            self.spinBox_textClusteringParam.setMinimumSize(QtCore.QSize(70, 35))
            self.spinBox_textClusteringParam.setMaximumSize(QtCore.QSize(70, 35))
            self.spinBox_textClusteringParam.setValue(1.000000000000000)
            self.spinBox_textClusteringParam.setSingleStep(0.01)
            self.gridLayout_2.addWidget(self.spinBox_textClusteringParam, 0, 3, 1, 1)
        else:
            self.spinBox_textClusteringParam = QtWidgets.QSpinBox(self.tab_3)
            self.spinBox_textClusteringParam.setObjectName(u"spinBox_textClusteringParam")
            self.spinBox_textClusteringParam.setMinimumSize(QtCore.QSize(70, 35))
            self.spinBox_textClusteringParam.setMaximumSize(QtCore.QSize(70, 35))
            self.spinBox_textClusteringParam.setValue(2)
            self.gridLayout_2.addWidget(self.spinBox_textClusteringParam, 0, 3, 1, 1)

    # 分词模型参数输入Enabled切换
    def set_spin_box_enabled(self):
        if self.comboBox_cutWordModelSelect.currentText() in ['关键词抽取模式 (TextRank)', '关键词抽取模式 (TF-IDF)']:
            self.label_cutModelExtraction.setVisible(True)
            self.spinBox_cutModelExtraction.setVisible(True)
            self.cut_word_form.groupBox_3.setVisible(True)
            self.cut_word_form.label.setVisible(True)
        elif self.comboBox_cutWordModelSelect.currentText() == '词性筛选模式':
            self.cut_word_form.groupBox_3.setVisible(True)
            self.cut_word_form.label.setVisible(True)
        else:
            self.label_cutModelExtraction.setVisible(False)
            self.spinBox_cutModelExtraction.setVisible(False)
            self.cut_word_form.groupBox_3.setVisible(False)
            self.cut_word_form.label.setVisible(False)

    # 分词模型设置页启用按钮对应主页处理函数
    def set_custom_pattern(self):
        '''
        基于分词设置页面 启用按钮 状态调整主页留个按钮的激活状态

        :return:
        '''
        self.checkBox_Chinese.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())
        self.checkBox_ChinesePunctuation.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())
        self.checkBox_Number.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())
        self.checkBox_EnglishUpper.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())
        self.checkBox_EnglishLower.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())
        self.checkBox_EnglishPunctuation.setEnabled(not self.text_cleaning_form.checkBox_set_custom_pattern.isChecked())

    # 读取图片
    def read_image(self):
        if self.word_cloud_form.lineEdit_backgroundPath.text() != '':
            if os.path.exists(self.word_cloud_form.lineEdit_backgroundPath.text()):
                self._read_image_thread = ReadImageThread(file_name=self.word_cloud_form.lineEdit_backgroundPath.text(),
                                                          view_form=self.view_form)
                self._read_image_thread.errorSignal.connect(self.show_critical)
                self._read_image_thread.endSignal.connect(lambda: self.view_image('background'))
                self.word_cloud_form.pushButton_backgroundShow.setEnabled(False)
                self._read_image_thread.start()
            else:
                QtWidgets.QMessageBox.warning(MainWindow, '文件不存在', '图片文件不存在，请检查路径。')
        else:
            QtWidgets.QMessageBox.warning(self.word_cloud_form, '预览失败', '预览失败，请先选择一张图片。')

    # 预览图片
    def view_image(self, image_type):
        if image_type == 'background':
            img = self._read_image_thread.image
            self.word_cloud_form.pushButton_backgroundShow.setEnabled(True)
        elif image_type == 'word_cloud':
            self.wc_gen = self._make_word_cloud_thread.wc
            img = self._make_word_cloud_thread.img
            self.update_save_menu()
        else:
            if self.wc_gen is None:
                QtWidgets.QMessageBox.warning(MainWindow, '预览失败', '还没有生成词云图。')
                return
            else:
                self.wc_gen = self._make_word_cloud_thread.wc
                img = self._make_word_cloud_thread.img
        self.view_form.image_array = img.copy()
        self.view_form.image_pix = img.toqpixmap()
        self.view_form.image.setPixmap(img.toqpixmap())
        self.view_form.show()

    # 开始按钮响应
    def get_parma_and_run_thread(self):
        if self.data is None:
            QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '无可用数据，程序无法运行，请先导入数据。')
        else:
            model_choice_id = self.tabWidget_modelChoice.currentIndex()
            column_id = self.comboBox_selectColumn.currentIndex()
            # 文本清洗
            if column_id != 0 and model_choice_id == 0:
                if self.pushButton_start.text() == '开始':
                    if self.text_cleaning_form.checkBox_set_custom_pattern.isChecked():
                        pattern = self.text_cleaning_form.lineEdit_custom_pattern.text()
                    else:
                        pattern = "["
                        pattern += '\u4e00-\u9fa5' if self.checkBox_Chinese.isChecked() else ''
                        pattern += '。？！，、;：“”（）——……《》、－-～·' if self.checkBox_ChinesePunctuation.isChecked() else ''
                        pattern += '0-9' if self.checkBox_Number.isChecked() else ''
                        pattern += 'A-Z' if self.checkBox_EnglishUpper.isChecked() else ''
                        pattern += 'a-z' if self.checkBox_EnglishLower.isChecked() else ''
                        pattern += '\.\?!,:;\-–—()\[\]\{\}"\'`' if self.checkBox_EnglishPunctuation.isChecked() else ''
                        pattern += ''.join([self.text_cleaning_form.listWidget.item(i).text() for i in
                                            range(self.text_cleaning_form.listWidget.count())])
                        pattern += ']+'
                    text_cleaning_args = Args('文本清洗参数')
                    text_cleaning_args.data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].copy()
                    text_cleaning_args.sheet_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
                    text_cleaning_args.input_column = self.comboBox_selectColumn.currentText()
                    text_cleaning_args.pattern = pattern
                    text_cleaning_args.join_symbol = self.text_cleaning_form.lineEdit_join.text()
                    self._text_cleaning_thread = TextCleaningThread(args=text_cleaning_args)
                    self._text_cleaning_thread.endSignal.connect(self.get_text_cleaning_thread_result)
                    self._text_cleaning_thread.errorSignal.connect(self.show_critical)
                    self._text_cleaning_thread.barSignal.connect(lambda x: self.progressBar.setValue(x))
                    self.progressBar.setValue(0)
                    self.set_enabled(False)
                    self.pushButton_start.setEnabled(True)
                    self.pushButton_start.setText('停止')
                    self.pushButton_start.setIcon(self.icon_stop)
                    self.progressBar.setValue(0)
                    self.statusbar.showMessage('正在处理')
                    self._text_cleaning_thread.start()
                else:
                    self._text_cleaning_thread.terminate()
                    self.statusbar.showMessage('已中断执行', 5)
                    self.set_enabled(True)
            # 词语挖掘
            elif column_id != 0 and model_choice_id == 1:
                if self.pushButton_start.text() == '开始':
                    word_mining_args = Args('词语挖掘参数')
                    word_mining_args.data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].copy()
                    word_mining_args.sheet_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
                    word_mining_args.input_column = self.comboBox_selectColumn.currentText()
                    word_mining_args.parma = self.spinBox_wordMining.value()
                    word_mining_args.H = self.text_mining_form.spinBox_H.value() / (
                            self.text_mining_form.spinBox_H.value() +
                            self.text_mining_form.spinBox_Dop.value() +
                            self.text_mining_form.spinBox_LeftFree.value() +
                            self.text_mining_form.spinBox_RightFree.value())
                    word_mining_args.Dop = self.text_mining_form.spinBox_Dop.value() / (
                            self.text_mining_form.spinBox_H.value() +
                            self.text_mining_form.spinBox_Dop.value() +
                            self.text_mining_form.spinBox_LeftFree.value() +
                            self.text_mining_form.spinBox_RightFree.value())
                    word_mining_args.LeftFree = self.text_mining_form.spinBox_LeftFree.value() / (
                            self.text_mining_form.spinBox_H.value() +
                            self.text_mining_form.spinBox_Dop.value() +
                            self.text_mining_form.spinBox_LeftFree.value() +
                            self.text_mining_form.spinBox_RightFree.value())
                    word_mining_args.RightFree = self.text_mining_form.spinBox_RightFree.value() / (
                            self.text_mining_form.spinBox_H.value() +
                            self.text_mining_form.spinBox_Dop.value() +
                            self.text_mining_form.spinBox_LeftFree.value() +
                            self.text_mining_form.spinBox_RightFree.value())
                    self._text_mining_thread = TextMiningThread(args=word_mining_args)
                    self._text_mining_thread.barSignal.connect(lambda x: self.progressBar.setValue(x))
                    self._text_mining_thread.errorSignal.connect(self.show_critical)
                    self._text_mining_thread.endSignal.connect(self.get_text_mining_thread_result)
                    self.set_enabled(False)
                    self.pushButton_start.setEnabled(True)
                    self.pushButton_start.setText('停止')
                    self.pushButton_start.setIcon(self.icon_stop)
                    self.progressBar.setValue(0)
                    self.statusbar.showMessage('正在处理')
                    self._text_mining_thread.start()
                else:
                    self._text_mining_thread.terminate()
                    self.statusbar.showMessage('已中断执行', 5)
                    self.set_enabled(True)
            # 分词
            elif column_id != 0 and model_choice_id == 2:
                if self.pushButton_start.text() == '开始':
                    cut_word_args = Args('分词参数')
                    cut_word_args.data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].copy()
                    cut_word_args.sheet_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
                    cut_word_args.input_column = self.comboBox_selectColumn.currentText()
                    cut_word_args.model_select = self.comboBox_cutWordModelSelect.currentText()
                    cut_word_args.extraction = self.spinBox_cutModelExtraction.value()
                    cut_word_args.word_frequency = self.checkBox_wordFrequency.isChecked()
                    cut_word_args.stop_word = self.cut_word_form.get_stop_word()
                    cut_word_args.user_word = self.cut_word_form.get_user_word()
                    cut_word_args.pos = self.cut_word_form.pos_list
                    self._cut_word_thread = CutWordThread(args=cut_word_args)
                    self._cut_word_thread.barSignal.connect(lambda x: self.progressBar.setValue(x))
                    self._cut_word_thread.errorSignal.connect(self.show_critical)
                    self._cut_word_thread.endSignal.connect(self.get_cut_word_thread_result)
                    self.set_enabled(False)
                    self.pushButton_start.setEnabled(True)
                    self.pushButton_start.setText('停止')
                    self.pushButton_start.setIcon(self.icon_stop)
                    self.progressBar.setValue(0)
                    self.statusbar.showMessage('正在处理')
                    self._cut_word_thread.start()
                else:
                    self._cut_word_thread.terminate()
                    self.statusbar.showMessage('已中断执行')
                    self.set_enabled(True)
            # 聚类
            elif column_id != 0 and model_choice_id == 3:
                if self.pushButton_start.text() == '开始':
                    text_clustering_args = Args('聚类参数')
                    text_clustering_args.data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].copy()
                    text_clustering_args.sheet_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
                    text_clustering_args.input_column = self.comboBox_selectColumn.currentText()
                    text_clustering_args.select_model = self.comboBox_textClusteringModelSelect.currentText()
                    text_clustering_args.parma = self.spinBox_textClusteringParam.value()
                    res = QtWidgets.QMessageBox.question(MainWindow, '开始聚类', '该过程不可中断，请确认输入参数没有问题\n点击OK继续执行',
                                                         QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                    if res == QtWidgets.QMessageBox.Ok:
                        self._text_clustering_thread = TextClusteringThread(args=text_clustering_args)
                        if self._text_clustering_thread.JVM_status:
                            self._text_clustering_thread.barSignal.connect(lambda x: self.progressBar.setValue(x))
                            self._text_clustering_thread.errorSignal.connect(self.show_critical)
                            self._text_clustering_thread.endSignal.connect(self.get_text_clustering_thread_result)
                            self.set_enabled(False)
                            self.progressBar.setValue(0)
                            self.statusbar.showMessage('正在处理')
                            self.pushButton_start.setIcon(self.icon_wait)
                            self.pushButton_start.setText('正在处理')
                            self._text_clustering_thread.start()
                        else:
                            res = QtWidgets.QMessageBox.critical(MainWindow, 'JVM 启动失败',
                                                                 'JVM 启动失败，请前往"设置-JVM设置"中手动启动JVM',
                                                                 QtWidgets.QMessageBox.Ok)
                            if res == QtWidgets.QMessageBox.Ok:
                                pass
                                return
                            else:
                                return
                    else:
                        return
                else:
                    self._text_clustering_thread.terminate()
                    self.statusbar.showMessage('已中断执行')
                    self.set_enabled(True)
            # 词云图 弃用
            elif model_choice_id == 4:
                # 对应词云图制作，暂时使用另一个按钮启动
                pass
            # 地址标准化 暂缓
            elif column_id != 0 and model_choice_id == 5:
                if self.pushButton_start.text() == '开始':
                    # thread.start()
                    self.set_enabled(False)
                    self.pushButton_start.setEnabled(True)
                    self.pushButton_start.setText('停止')
                    self.pushButton_start.setIcon(self.icon_stop)
                else:
                    # thread.terminate()
                    self.set_enabled(True)
            else:
                QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入数据为空，请选择一列数据作为模型输入。')

    # 制作按钮响应
    def get_parma_and_make_thread(self):
        if self.data is None:
            QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '无可用数据，程序无法运行，请先导入数据。')
        else:
            text_id = self.comboBox_wordCloudText.currentIndex()
            rank_id = self.comboBox_wordCloudRank.currentIndex()
            colour_id = self.word_cloud_form.comboBox_colourColumn.currentIndex()
            if self.word_cloud_form.radioButton_setUserFontColour.isChecked():
                if text_id == 0:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入文本数据为空，请选择一列数据作为模型输入。')
                    return
                elif rank_id == 0:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入词频数据为空，请选择一列数据作为模型输入。')
                    return
                elif colour_id == 0:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入颜色数据为空，请选择一列数据作为模型输入。')
                    return
                elif text_id == rank_id:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入文本数据与词频数据相同，请重新选择。')
                    return
                elif text_id == colour_id:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入文本数据与颜色数据相同，请重新选择。')
                    return
                elif rank_id == colour_id:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入词频数据与颜色数据相同，请重新选择。')
                    return
                else:
                    pass
            else:
                if text_id == 0:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入文本数据为空，请选择一列数据作为模型输入。')
                    return
                elif rank_id == 0:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入词频数据为空，请选择一列数据作为模型输入。')
                    return
                elif text_id == rank_id:
                    QtWidgets.QMessageBox.warning(MainWindow, '无法运行', '输入文本数据与词频数据相同，请重新选择。')
                    return
                else:
                    pass

            data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].loc[:,
                   [self.comboBox_wordCloudText.currentText(),
                    self.comboBox_wordCloudRank.currentText()]]
            data[self.comboBox_wordCloudText.currentText()] = data[self.comboBox_wordCloudText.currentText()].astype(
                'str')
            data[self.comboBox_wordCloudRank.currentText()] = data[self.comboBox_wordCloudRank.currentText()].astype(
                'int')
            word_count_dict = data.set_index(self.comboBox_wordCloudText.currentText()).to_dict()[
                self.comboBox_wordCloudRank.currentText()]
            if self.word_cloud_form.radioButton_setUserFontColour.isChecked():
                colour_data = self.data[self.tabWidget.tabText(self.tabWidget.currentIndex())].loc[:,
                              [self.comboBox_wordCloudText.currentText(),
                               self.word_cloud_form.comboBox_colourColumn.currentText()]]
                colour_data[self.comboBox_wordCloudText.currentText()] = data[
                    self.comboBox_wordCloudText.currentText()].astype('str')
                colour_data[self.word_cloud_form.comboBox_colourColumn.currentText()] = colour_data[
                    self.word_cloud_form.comboBox_colourColumn.currentText()].astype('str')

                color_to_words = {c: w.values.tolist()[0] for c, w in colour_data.groupby(
                    self.word_cloud_form.comboBox_colourColumn.currentText())}
            else:
                color_to_words = None
            if self.word_cloud_form.checkBox_userBackground.isChecked():
                if os.path.exists(self.word_cloud_form.lineEdit_backgroundPath.text()):
                    background_path = self.word_cloud_form.lineEdit_backgroundPath.text()
                else:
                    QtWidgets.QMessageBox.warning(MainWindow, '文件不存在', '蒙版文件不存在，请检查路径。')
                    return
            else:
                background_path = None
            if os.path.exists(self.word_cloud_form.lineEdit_fontPath.text()):
                font_file_path = self.word_cloud_form.lineEdit_fontPath.text()
            else:
                QtWidgets.QMessageBox.warning(MainWindow, '文件不存在', '字体文件不存在，请检查路径。')
                return

            word_cloud_args = Args('词云图参数')
            word_cloud_args.data = word_count_dict
            word_cloud_args.width = self.spinBox_wordCloudImgWidth.value()
            word_cloud_args.height = self.spinBox_wordCloudImgHeight.value()
            word_cloud_args.no_background = self.word_cloud_form.radioButton_noBackground.isChecked()
            word_cloud_args.background_mask = self.word_cloud_form.checkBox_userBackground.isChecked()
            word_cloud_args.background_colour = self.word_cloud_form.background_colour
            word_cloud_args.background_img_path = background_path
            word_cloud_args.font_file_path = font_file_path
            word_cloud_args.FontModel = [self.word_cloud_form.radioButton_randomFontColour.isChecked(),
                                         self.word_cloud_form.radioButton_setFontColour.isChecked(),
                                         self.word_cloud_form.radioButton_setUserFontColour.isChecked()]
            word_cloud_args.font_colour = self.word_cloud_form.font_colour
            word_cloud_args.font_colour_dict = color_to_words
            word_cloud_args.max_word = self.word_cloud_form.spinBox_max_word_count_wordCloud.value()
            word_cloud_args.relative_scaling = self.word_cloud_form.doubleSpinBox_relative_scaling_wordCloud.value()
            word_cloud_args.margin = self.word_cloud_form.spinBox_max_word_margin_wordCloud.value()
            word_cloud_args.prefer_horizontal = self.word_cloud_form.doubleSpinBox_prefer_horizontal_wordCloud.value()

            self._make_word_cloud_thread = MakeWordCloudThread(args=word_cloud_args)
            self._make_word_cloud_thread.endSignal.connect(lambda: self.message_form.close())
            self._make_word_cloud_thread.endSignal.connect(lambda: self.pushButton_makeWordCloud.setIcon(self.icon_run))
            self._make_word_cloud_thread.endSignal.connect(lambda: self.view_image('word_cloud'))
            self._make_word_cloud_thread.errorSignal.connect(self.show_critical)
            self.message_form.label.setText('正在制作词云图... ')
            # self.set_enabled(False)
            self.message_form.show()
            self.pushButton_makeWordCloud.setIcon(self.icon_wait)
            self._make_word_cloud_thread.start()

    # 显示异常信息
    def show_critical(self, error):
        QtWidgets.QMessageBox.critical(MainWindow, "错误", error, QtWidgets.QMessageBox.Cancel)
        self.set_enabled(True)

    # 文本清洗线程结果处理
    def get_text_cleaning_thread_result(self):
        self.data[self._text_cleaning_thread.args.sheet_name] = self._text_cleaning_thread.args.data.copy()
        # self.change_table_show()
        self.update_combo_box()

    # 词语挖掘线程结果
    def get_text_mining_thread_result(self):
        sheet_name = f'词语挖掘结果_{self._text_mining_thread.args.input_column}'
        self.data[sheet_name] = self._text_mining_thread.result_data.copy()
        sheets = {self.tabWidget.tabText(i): i for i in range(self.tabWidget.count())}
        index = sheets.get(sheet_name, -1)
        if index != -1:
            self.set_enabled(True)
            self.tabWidget.setCurrentIndex(index)
        else:
            self.tabWidget.addTab(QtWidgets.QWidget(), sheet_name)
            self.set_enabled(True)
            self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

    # 分词线程结果
    def get_cut_word_thread_result(self):
        self.data[self._cut_word_thread.args.sheet_name] = self._cut_word_thread.args.data.copy()
        if self.checkBox_wordFrequency.isChecked():
            sheet_name = f'词频统计结果_{self._cut_word_thread.args.input_column}'
            self.data[sheet_name] = self._cut_word_thread.args.word_count_data.copy()
            sheets = {self.tabWidget.tabText(i): i for i in range(self.tabWidget.count())}
            index = sheets.get(sheet_name, -1)
            if index != -1:
                self.set_enabled(True)
                self.tabWidget.setCurrentIndex(index)
            else:
                self.tabWidget.addTab(QtWidgets.QWidget(), sheet_name)
                self.set_enabled(True)
                self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
        else:
            self.update_combo_box()

    # 文本聚类线程结果
    def get_text_clustering_thread_result(self):
        self.data[self._text_clustering_thread.args.sheet_name] = self._text_clustering_thread.args.data.copy()
        self._text_clustering_thread.terminate()
        self._text_clustering_thread = None
        self.update_combo_box()

    # 手动点击启动检查更新
    def check_update(self):
        self.check_update_click = True
        self.setting_form.check_update_thread.start()

    # 显示新版本信息
    def show_update_info(self, code, new_version, version_date, update_info, status_code):
        if code == 0:
            if self.check_update_click:
                QtWidgets.QMessageBox.information(MainWindow, 'Text Tools - 更新', '已是最新版本。')
            else:
                return
        elif code == 1:
            self.update_form.label_version.setText(new_version)
            self.update_form.label_date.setText(version_date)
            self.update_form.label_info.setText(update_info)
            self.update_form.open_link = self.setting_form.check_update_thread.download_link
            self.update_form.download_type = None
            self.update_form.show()
        elif code == 2:
            self.update_form.label_version.setText(new_version)
            self.update_form.label_date.setText(version_date)
            self.update_form.label_info.setText(update_info)
            self.update_form.open_link = self.setting_form.check_update_thread.download_link
            self.update_form.download_type = 'Patch'
            self.update_form.show()
        elif code == -1:
            QtWidgets.QMessageBox.warning(MainWindow, 'Text Tools - 更新', f'更新失败，错误代码 {status_code} 。')
        else:
            QtWidgets.QMessageBox.critical(MainWindow, 'Text Tools - 更新', f'更新失败。')
        self.check_update_click = False


class MyMainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,
                                               '关闭',
                                               '关闭程序后一切未保存的处理结果都将丢失，\n是否要退出程序？',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            # event.accept()
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
            sys.exit(0)  # 关闭所以窗口
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    # MainWindow = QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
