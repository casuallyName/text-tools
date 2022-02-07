# -*- coding: utf-8 -*-
# @Time     : 2022/2/3 3:04 PM
# @File     : Update.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.9
# @About    : 热更新窗口

import os
import sys
import time
import zipfile
import requests
import traceback
from PySide6 import QtWidgets, QtCore
from uiMainWindowUpdate import Ui_MainWindow


class Windows(Ui_MainWindow):

    def __init__(self):
        super(Windows, self).__init__()
        self.downloadThread = None
        self.MainWindow = None

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        MainWindow.setWindowFlags(QtCore.Qt.Window |
                                  QtCore.Qt.WindowTitleHint |
                                  QtCore.Qt.CustomizeWindowHint |
                                  QtCore.Qt.WindowMinimizeButtonHint
                                  )

        self.progressBar.setValue(0)

    def retranslateUi(self, MainWindow):
        Ui_MainWindow.retranslateUi(self, MainWindow)

    def download(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
            self.downloadThread = Download(url)
            self.downloadThread.barSignal.connect(lambda x: self.progressBar.setValue(x))
            self.downloadThread.messageSignal.connect(lambda x: self.statusbar.showMessage(x))
            self.downloadThread.endSignal.connect(self.end_update)
            self.downloadThread.start()
        else:
            QtWidgets.QMessageBox.critical(MainWindow, '更新', '启动更新失败，请在主程序中检测更新！')
            sys.exit()

    def end_update(self, code):
        if code == 0:
            res = QtWidgets.QMessageBox.information(MainWindow, '提示', '更新完成，是否重新启动程序？',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.Yes)
            if res == QtWidgets.QMessageBox.Yes:
                os.popen('Text Tools.exe')
            sys.exit()
        else:
            QtWidgets.QMessageBox.critical(MainWindow, '更新', '更新失败')
            sys.exit()


class Download(QtCore.QThread):
    barSignal = QtCore.Signal(int)
    endSignal = QtCore.Signal(int)
    messageSignal = QtCore.Signal(str)

    def __init__(self, url):
        super(Download, self).__init__()
        self.url = url

    def run(self) -> None:
        try:
            bar = 0
            down_size = 0
            self.messageSignal.emit(f'正在准备更新')
            res = requests.get(self.url, stream=True)
            while res.headers['Content-Type'] != 'application/zip':
                time.sleep(0.5)
                res = requests.get(self.url, stream=True)
            file_size = int(res.headers['Content-Length']) + 1
            file_name = res.headers['Content-Disposition'].split('=')[-1]
            file_path = os.path.dirname(os.path.realpath(sys.executable))
            self.messageSignal.emit(f'正在下载 {file_name}')
            with open(os.path.join(file_path, file_name), 'wb') as f:
                for chunk in res.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        down_size += len(chunk)
                        new_bar = int(down_size / file_size * 100)
                        if new_bar != bar:
                            bar = new_bar
                            self.barSignal.emit(bar + 1)
            self.messageSignal.emit(f'正在解压 {file_name}')
            try:
                time.sleep(0.5)
                self.unzip_file(os.path.join(file_path, file_name), file_path)
            except:
                traceback.print_tb()
                QtWidgets.QMessageBox.about(MainWindow, 'A', traceback.format_exc())
            self.messageSignal.emit(f'清理缓存')
            try:
                os.remove(os.path.join(file_path, file_name))
            except:
                pass
            self.messageSignal.emit('完成')
            self.barSignal.emit(100)
            self.endSignal.emit(0)
        except:
            self.endSignal.emit(1)

    def unzip_file(self, zip_src, dst_dir):
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, 'r')
            for file in fz.namelist():
                self.messageSignal.emit(f'正在覆盖文件 {file}')
                fz.extract(file, dst_dir)
        else:
            self.messageSignal.emit('解压文件出错')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Windows()
    ui.setupUi(MainWindow)
    ui.download()
    MainWindow.show()
    sys.exit(app.exec())
