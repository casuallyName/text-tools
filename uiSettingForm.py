# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiSettingForm.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_3 = QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.pushButton_save_1 = QPushButton(self.tab_1)
        self.pushButton_save_1.setObjectName(u"pushButton_save_1")
        self.pushButton_save_1.setMinimumSize(QSize(75, 0))
        self.pushButton_save_1.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_save_1, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.tab_1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_workSpace = QComboBox(self.tab_1)
        self.comboBox_workSpace.addItem("")
        self.comboBox_workSpace.addItem("")
        self.comboBox_workSpace.addItem("")
        self.comboBox_workSpace.setObjectName(u"comboBox_workSpace")

        self.horizontalLayout_3.addWidget(self.comboBox_workSpace)

        self.lineEdit_workSpacePath = QLineEdit(self.tab_1)
        self.lineEdit_workSpacePath.setObjectName(u"lineEdit_workSpacePath")

        self.horizontalLayout_3.addWidget(self.lineEdit_workSpacePath)

        self.pushButton_openWorkSpace = QPushButton(self.tab_1)
        self.pushButton_openWorkSpace.setObjectName(u"pushButton_openWorkSpace")

        self.horizontalLayout_3.addWidget(self.pushButton_openWorkSpace)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.pushButton_check_update = QPushButton(self.tab_1)
        self.pushButton_check_update.setObjectName(u"pushButton_check_update")
        self.pushButton_check_update.setMinimumSize(QSize(75, 0))
        self.pushButton_check_update.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_check_update, 1, 2, 1, 1)

        self.checkBox_checkUpdate = QCheckBox(self.tab_1)
        self.checkBox_checkUpdate.setObjectName(u"checkBox_checkUpdate")
        self.checkBox_checkUpdate.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_checkUpdate, 1, 0, 1, 1)

        icon1 = QIcon()
        icon1.addFile(u"src/img/Gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_JVM_Path = QLineEdit(self.tab_2)
        self.lineEdit_JVM_Path.setObjectName(u"lineEdit_JVM_Path")

        self.horizontalLayout.addWidget(self.lineEdit_JVM_Path)

        self.pushButton_open_jvm = QPushButton(self.tab_2)
        self.pushButton_open_jvm.setObjectName(u"pushButton_open_jvm")

        self.horizontalLayout.addWidget(self.pushButton_open_jvm)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_JVM_XMS = QLineEdit(self.tab_2)
        self.lineEdit_JVM_XMS.setObjectName(u"lineEdit_JVM_XMS")

        self.horizontalLayout_2.addWidget(self.lineEdit_JVM_XMS)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_JVM_XMX = QLineEdit(self.tab_2)
        self.lineEdit_JVM_XMX.setObjectName(u"lineEdit_JVM_XMX")

        self.horizontalLayout_2.addWidget(self.lineEdit_JVM_XMX)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 3)

        self.pushButton_save = QPushButton(self.tab_2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(75, 0))
        self.pushButton_save.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_save, 5, 2, 1, 1)

        self.pushButton_start_JVM = QPushButton(self.tab_2)
        self.pushButton_start_JVM.setObjectName(u"pushButton_start_JVM")
        self.pushButton_start_JVM.setMinimumSize(QSize(75, 0))
        self.pushButton_start_JVM.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_start_JVM, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 5, 1, 1, 1)

        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 4, 0, 1, 3)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 3)

        icon2 = QIcon()
        icon2.addFile(u"src/img/JVM.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u8bbe\u7f6e", None))
        self.pushButton_save_1.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u76ee\u5f55\uff1a", None))
        self.comboBox_workSpace.setItemText(0, QCoreApplication.translate("Form", u"\u684c\u9762", None))
        self.comboBox_workSpace.setItemText(1, QCoreApplication.translate("Form", u"\u6587\u6863", None))
        self.comboBox_workSpace.setItemText(2, QCoreApplication.translate("Form", u"\u5176\u4ed6", None))

        self.pushButton_openWorkSpace.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.pushButton_check_update.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u66f4\u65b0", None))
        self.checkBox_checkUpdate.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u65f6\u68c0\u6d4b\u66f4\u65b0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u9996\u9009\u9879", None))
        self.label.setText(QCoreApplication.translate("Form", u"JVM \u8def\u5f84\uff1a", None))
        self.lineEdit_JVM_Path.setText("")
        self.lineEdit_JVM_Path.setPlaceholderText(QCoreApplication.translate("Form", u"JAVA_HOME", None))
        self.pushButton_open_jvm.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u5206\u914d\u5185\u5b58\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u6700\u5927\u5185\u5b58\uff1a", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.pushButton_start_JVM.setText(QCoreApplication.translate("Form", u"\u542f\u52a8JVM", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8d44\u6e90\u6587\u4ef6\u5217\u8868\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6ce8\uff1aJVM \u8def\u5f84\u4e3a\u7a7a\u65f6\u5c06\u4f7f\u7528\u73af\u5883\u53d8\u91cf\u4e2d\u7684JAVA_HOME", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"JVM\u8bbe\u7f6e", None))
    # retranslateUi

