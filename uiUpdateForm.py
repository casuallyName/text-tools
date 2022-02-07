# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiUpdateForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        Form.setMinimumSize(QSize(400, 200))
        Form.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_version = QLabel(Form)
        self.label_version.setObjectName(u"label_version")
        font = QFont()
        font.setPointSize(19)
        self.label_version.setFont(font)
        self.label_version.setFrameShape(QFrame.NoFrame)
        self.label_version.setMidLineWidth(4)

        self.gridLayout_2.addWidget(self.label_version, 0, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(70, 30))
        self.pushButton.setMaximumSize(QSize(70, 30))
        icon1 = QIcon()
        icon1.addFile(u"src/img/Clockwise.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label_date = QLabel(Form)
        self.label_date.setObjectName(u"label_date")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_date.setFont(font1)
        self.label_date.setFrameShape(QFrame.NoFrame)
        self.label_date.setMidLineWidth(4)

        self.gridLayout_2.addWidget(self.label_date, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 382, 128))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_info = QLabel(self.scrollAreaWidgetContents)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setFrameShape(QFrame.NoFrame)
        self.label_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_info.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.label_info, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u8f6f\u4ef6\u66f4\u65b0", None))
        self.label_version.setText(QCoreApplication.translate("Form", u"Version", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0", None))
        self.label_date.setText(QCoreApplication.translate("Form", u"Version", None))
        self.label_info.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

