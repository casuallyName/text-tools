# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiViewForm.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QSize(400, 300))
        Form.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox_zoom = QSpinBox(Form)
        self.spinBox_zoom.setObjectName(u"spinBox_zoom")
        self.spinBox_zoom.setMinimumSize(QSize(0, 25))
        self.spinBox_zoom.setMaximumSize(QSize(16777215, 25))
        self.spinBox_zoom.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_zoom.setStyleSheet(u"background:transparent;")
        self.spinBox_zoom.setWrapping(False)
        self.spinBox_zoom.setFrame(False)
        self.spinBox_zoom.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_zoom.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_zoom.setAccelerated(False)
        self.spinBox_zoom.setKeyboardTracking(True)
        self.spinBox_zoom.setProperty("showGroupSeparator", False)
        self.spinBox_zoom.setMinimum(1)
        self.spinBox_zoom.setMaximum(500)
        self.spinBox_zoom.setValue(100)
        self.spinBox_zoom.setDisplayIntegerBase(10)

        self.gridLayout_2.addWidget(self.spinBox_zoom, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pushButton_ZoomOut = QPushButton(Form)
        self.pushButton_ZoomOut.setObjectName(u"pushButton_ZoomOut")
        self.pushButton_ZoomOut.setMinimumSize(QSize(0, 25))
        self.pushButton_ZoomOut.setMaximumSize(QSize(16777215, 25))
        icon1 = QIcon()
        icon1.addFile(u"src/img/ZoomOut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_ZoomOut.setIcon(icon1)
        self.pushButton_ZoomOut.setAutoRepeat(True)

        self.gridLayout_2.addWidget(self.pushButton_ZoomOut, 1, 1, 1, 1)

        self.pushButton_ZoomIn = QPushButton(Form)
        self.pushButton_ZoomIn.setObjectName(u"pushButton_ZoomIn")
        self.pushButton_ZoomIn.setMinimumSize(QSize(0, 25))
        self.pushButton_ZoomIn.setMaximumSize(QSize(16777215, 25))
        icon2 = QIcon()
        icon2.addFile(u"src/img/ZoomIn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_ZoomIn.setIcon(icon2)
        self.pushButton_ZoomIn.setAutoRepeat(True)

        self.gridLayout_2.addWidget(self.pushButton_ZoomIn, 1, 4, 1, 1)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 380, 249))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image = QLabel(self.scrollAreaWidgetContents_2)
        self.image.setObjectName(u"image")
        self.image.setMaximumSize(QSize(16777215, 16777215))
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 6)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u9884\u89c8", None))
        self.pushButton_ZoomOut.setText(QCoreApplication.translate("Form", u"\u7f29\u5c0f", None))
        self.pushButton_ZoomIn.setText(QCoreApplication.translate("Form", u"\u653e\u5927", None))
        self.image.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"%", None))
    # retranslateUi

