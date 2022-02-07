# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiCutWordForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 401)
        Form.setMinimumSize(QSize(800, 401))
        Form.setMaximumSize(QSize(800, 401))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget_stopWord = QListWidget(self.groupBox)
        self.listWidget_stopWord.setObjectName(u"listWidget_stopWord")

        self.gridLayout_2.addWidget(self.listWidget_stopWord, 0, 0, 1, 2)

        self.lineEdit_stopWord = QLineEdit(self.groupBox)
        self.lineEdit_stopWord.setObjectName(u"lineEdit_stopWord")
        self.lineEdit_stopWord.setMinimumSize(QSize(0, 30))
        self.lineEdit_stopWord.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.lineEdit_stopWord, 1, 0, 1, 1)

        self.pushButton_addStopWord = QPushButton(self.groupBox)
        self.pushButton_addStopWord.setObjectName(u"pushButton_addStopWord")
        self.pushButton_addStopWord.setMinimumSize(QSize(80, 30))
        self.pushButton_addStopWord.setMaximumSize(QSize(80, 30))
        icon1 = QIcon()
        icon1.addFile(u"src/img/AddItem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_addStopWord.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_addStopWord, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_addUserWord = QPushButton(self.groupBox_2)
        self.pushButton_addUserWord.setObjectName(u"pushButton_addUserWord")
        self.pushButton_addUserWord.setMinimumSize(QSize(80, 30))
        self.pushButton_addUserWord.setMaximumSize(QSize(80, 30))
        self.pushButton_addUserWord.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_addUserWord, 2, 1, 1, 1)

        self.lineEdit_userWord = QLineEdit(self.groupBox_2)
        self.lineEdit_userWord.setObjectName(u"lineEdit_userWord")
        self.lineEdit_userWord.setMinimumSize(QSize(0, 30))
        self.lineEdit_userWord.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.lineEdit_userWord, 2, 0, 1, 1)

        self.listWidget_userWord = QListWidget(self.groupBox_2)
        self.listWidget_userWord.setObjectName(u"listWidget_userWord")

        self.gridLayout.addWidget(self.listWidget_userWord, 0, 0, 1, 2)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.groupBox_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setMinimumSize(QSize(170, 0))
        self.scrollArea_2.setMaximumSize(QSize(170, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 168, 349))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_a = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_a.setObjectName(u"checkBox_a")
        self.checkBox_a.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_a)

        self.checkBox_ad = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_ad.setObjectName(u"checkBox_ad")

        self.verticalLayout_2.addWidget(self.checkBox_ad)

        self.checkBox_an = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_an.setObjectName(u"checkBox_an")

        self.verticalLayout_2.addWidget(self.checkBox_an)

        self.checkBox_d = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_d.setObjectName(u"checkBox_d")
        self.checkBox_d.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_d)

        self.checkBox_i = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_i.setObjectName(u"checkBox_i")
        self.checkBox_i.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_i)

        self.checkBox_n = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_n.setObjectName(u"checkBox_n")
        self.checkBox_n.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_n)

        self.checkBox_nr = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_nr.setObjectName(u"checkBox_nr")
        self.checkBox_nr.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_nr)

        self.checkBox_ns = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_ns.setObjectName(u"checkBox_ns")
        self.checkBox_ns.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_ns)

        self.checkBox_nt = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_nt.setObjectName(u"checkBox_nt")
        self.checkBox_nt.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_nt)

        self.checkBox_nz = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_nz.setObjectName(u"checkBox_nz")

        self.verticalLayout_2.addWidget(self.checkBox_nz)

        self.checkBox_t = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_t.setObjectName(u"checkBox_t")

        self.verticalLayout_2.addWidget(self.checkBox_t)

        self.checkBox_tg = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_tg.setObjectName(u"checkBox_tg")

        self.verticalLayout_2.addWidget(self.checkBox_tg)

        self.checkBox_v = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_v.setObjectName(u"checkBox_v")
        self.checkBox_v.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_v)

        self.checkBox_vd = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_vd.setObjectName(u"checkBox_vd")

        self.verticalLayout_2.addWidget(self.checkBox_vd)

        self.checkBox_vn = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_vn.setObjectName(u"checkBox_vn")
        self.checkBox_vn.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_vn)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u5206\u8bcd\u5de5\u5177\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u505c\u7528\u8bcd", None))
#if QT_CONFIG(statustip)
        self.pushButton_addStopWord.setStatusTip(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_addStopWord.setWhatsThis(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_addStopWord.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_addStopWord.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u8bcd\u5178", None))
#if QT_CONFIG(statustip)
        self.pushButton_addUserWord.setStatusTip(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_addUserWord.setWhatsThis(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_addUserWord.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_addUserWord.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Form", u"\u6ce8\uff1a\u4f7f\u7528\u8bcd\u6027\u7b5b\u9009\u3001\u5173\u952e\u8bcd\u62bd\u53d6\u6a21\u5f0f\u65f6\u81ea\u5b9a\u4e49\u8bcd\u5178\u9700\u8981\u6807\u8bb0\u8bcd\u6027\u624d\u80fd\u751f\u6548(\u8bcd\u6027\u4f7f\u7528\u7a7a\u683c\u5206\u9694)\uff0c\u8be6\u60c5\u53c2\u8003<a href='https://gitee.com/casuallyName/text-tools/wikis/Home'>\u8bf4\u660e\u6587\u6863</a>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8bcd\u6027\u7ba1\u7406", None))
        self.checkBox_a.setText(QCoreApplication.translate("Form", u"\u5f62\u5bb9\u8bcd", None))
        self.checkBox_ad.setText(QCoreApplication.translate("Form", u"\u526f\u5f62\u8bcd", None))
        self.checkBox_an.setText(QCoreApplication.translate("Form", u"\u540d\u5f62\u8bcd", None))
        self.checkBox_d.setText(QCoreApplication.translate("Form", u"\u526f\u8bcd", None))
        self.checkBox_i.setText(QCoreApplication.translate("Form", u"\u6210\u8bed", None))
        self.checkBox_n.setText(QCoreApplication.translate("Form", u"\u540d\u8bcd", None))
        self.checkBox_nr.setText(QCoreApplication.translate("Form", u"\u4eba\u540d", None))
        self.checkBox_ns.setText(QCoreApplication.translate("Form", u"\u5730\u540d", None))
        self.checkBox_nt.setText(QCoreApplication.translate("Form", u"\u673a\u6784\u56e2\u4f53", None))
        self.checkBox_nz.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6\u4e13\u540d", None))
        self.checkBox_t.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u8bcd", None))
        self.checkBox_tg.setText(QCoreApplication.translate("Form", u"\u65f6\u8bed\u7d20", None))
        self.checkBox_v.setText(QCoreApplication.translate("Form", u"\u52a8\u8bcd", None))
        self.checkBox_vd.setText(QCoreApplication.translate("Form", u"\u526f\u52a8\u8bcd", None))
        self.checkBox_vn.setText(QCoreApplication.translate("Form", u"\u540d\u52a8\u8bcd", None))
    # retranslateUi

