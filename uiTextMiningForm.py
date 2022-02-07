# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiTextMiningForm.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(260, 240)
        Form.setMinimumSize(QSize(260, 240))
        Form.setMaximumSize(QSize(260, 240))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 35))
        self.label.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox_H = QSpinBox(Form)
        self.spinBox_H.setObjectName(u"spinBox_H")
        self.spinBox_H.setMinimumSize(QSize(0, 35))
        self.spinBox_H.setMaximumSize(QSize(16777215, 35))
        self.spinBox_H.setMaximum(100)
        self.spinBox_H.setValue(20)

        self.gridLayout.addWidget(self.spinBox_H, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_Dop = QSpinBox(Form)
        self.spinBox_Dop.setObjectName(u"spinBox_Dop")
        self.spinBox_Dop.setMinimumSize(QSize(0, 35))
        self.spinBox_Dop.setMaximumSize(QSize(16777215, 35))
        self.spinBox_Dop.setMaximum(100)
        self.spinBox_Dop.setValue(20)

        self.gridLayout.addWidget(self.spinBox_Dop, 1, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))
        self.label_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.spinBox_LeftFree = QSpinBox(Form)
        self.spinBox_LeftFree.setObjectName(u"spinBox_LeftFree")
        self.spinBox_LeftFree.setMinimumSize(QSize(0, 35))
        self.spinBox_LeftFree.setMaximumSize(QSize(16777215, 35))
        self.spinBox_LeftFree.setMaximum(100)
        self.spinBox_LeftFree.setValue(30)

        self.gridLayout.addWidget(self.spinBox_LeftFree, 2, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))
        self.label_4.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.spinBox_RightFree = QSpinBox(Form)
        self.spinBox_RightFree.setObjectName(u"spinBox_RightFree")
        self.spinBox_RightFree.setMinimumSize(QSize(0, 35))
        self.spinBox_RightFree.setMaximumSize(QSize(16777215, 35))
        self.spinBox_RightFree.setMaximum(100)
        self.spinBox_RightFree.setValue(30)

        self.gridLayout.addWidget(self.spinBox_RightFree, 3, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_reset = QPushButton(Form)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setMinimumSize(QSize(100, 35))
        self.pushButton_reset.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.pushButton_reset)

        self.pushButton_close = QPushButton(Form)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(100, 35))
        self.pushButton_close.setMaximumSize(QSize(100, 35))

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Form)
        self.pushButton_close.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u6743\u91cd\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4fe1\u606f\u71b5\u6743\u91cd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6587\u672c\u805a\u5408\u5ea6\u6743\u91cd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5de6\u4fa7\u81ea\u7531\u5ea6\u6743\u91cd", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u53f3\u4fa7\u81ea\u7531\u5ea6\u6743\u91cd", None))
        self.pushButton_reset.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.pushButton_close.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

