# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWordCloudForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 550)
        Form.setMinimumSize(QSize(780, 550))
        Form.setMaximumSize(QSize(780, 550))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_colourColumn = QComboBox(self.groupBox_2)
        self.comboBox_colourColumn.setObjectName(u"comboBox_colourColumn")
        self.comboBox_colourColumn.setMinimumSize(QSize(0, 35))
        self.comboBox_colourColumn.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.comboBox_colourColumn, 3, 5, 1, 5)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))
        self.label_4.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.pushButton_fontOpen = QPushButton(self.groupBox_2)
        self.pushButton_fontOpen.setObjectName(u"pushButton_fontOpen")
        self.pushButton_fontOpen.setMinimumSize(QSize(110, 35))
        self.pushButton_fontOpen.setMaximumSize(QSize(110, 35))
        icon1 = QIcon()
        icon1.addFile(u"src/img/Open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_fontOpen.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_fontOpen, 0, 9, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 3, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 2, 1, 2)

        self.radioButton_randomFontColour = QRadioButton(self.groupBox_2)
        self.radioButton_randomFontColour.setObjectName(u"radioButton_randomFontColour")
        self.radioButton_randomFontColour.setMinimumSize(QSize(0, 30))
        self.radioButton_randomFontColour.setMaximumSize(QSize(16777215, 30))
        self.radioButton_randomFontColour.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_randomFontColour, 1, 0, 1, 3)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_2, 2, 6, 1, 1)

        self.radioButton_setFontColour = QRadioButton(self.groupBox_2)
        self.radioButton_setFontColour.setObjectName(u"radioButton_setFontColour")
        self.radioButton_setFontColour.setMinimumSize(QSize(0, 35))
        self.radioButton_setFontColour.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.radioButton_setFontColour, 2, 0, 1, 2)

        self.radioButton_setUserFontColour = QRadioButton(self.groupBox_2)
        self.radioButton_setUserFontColour.setObjectName(u"radioButton_setUserFontColour")
        self.radioButton_setUserFontColour.setMinimumSize(QSize(130, 35))
        self.radioButton_setUserFontColour.setMaximumSize(QSize(130, 35))

        self.gridLayout_2.addWidget(self.radioButton_setUserFontColour, 3, 0, 1, 2)

        self.lineEdit_fontPath = QLineEdit(self.groupBox_2)
        self.lineEdit_fontPath.setObjectName(u"lineEdit_fontPath")
        self.lineEdit_fontPath.setMinimumSize(QSize(0, 35))
        self.lineEdit_fontPath.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.lineEdit_fontPath, 0, 1, 1, 8)

        self.pushButton_selectFontColour = QPushButton(self.groupBox_2)
        self.pushButton_selectFontColour.setObjectName(u"pushButton_selectFontColour")
        self.pushButton_selectFontColour.setMinimumSize(QSize(110, 35))
        self.pushButton_selectFontColour.setMaximumSize(QSize(110, 35))
        icon2 = QIcon()
        icon2.addFile(u"src/img/Brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_selectFontColour.setIcon(icon2)

        self.gridLayout_2.addWidget(self.pushButton_selectFontColour, 2, 8, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))
        self.label_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.label_3, 3, 4, 1, 1)

        self.label_fontColour = QLabel(self.groupBox_2)
        self.label_fontColour.setObjectName(u"label_fontColour")
        self.label_fontColour.setMinimumSize(QSize(30, 30))
        self.label_fontColour.setMaximumSize(QSize(30, 30))
        self.label_fontColour.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_fontColour, 2, 7, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_1 = QLabel(self.groupBox)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 30))
        self.label_1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_1, 1, 5, 1, 1)

        self.pushButton_backgroundShow = QPushButton(self.groupBox)
        self.pushButton_backgroundShow.setObjectName(u"pushButton_backgroundShow")
        self.pushButton_backgroundShow.setMinimumSize(QSize(110, 35))
        self.pushButton_backgroundShow.setMaximumSize(QSize(110, 35))
        icon3 = QIcon()
        icon3.addFile(u"src/img/Preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_backgroundShow.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton_backgroundShow, 2, 8, 1, 1)

        self.pushButton_backgroundOpen = QPushButton(self.groupBox)
        self.pushButton_backgroundOpen.setObjectName(u"pushButton_backgroundOpen")
        self.pushButton_backgroundOpen.setMinimumSize(QSize(110, 35))
        self.pushButton_backgroundOpen.setMaximumSize(QSize(110, 35))
        self.pushButton_backgroundOpen.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_backgroundOpen, 2, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(609, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 7)

        self.pushButton_selectBackgroundColour = QPushButton(self.groupBox)
        self.pushButton_selectBackgroundColour.setObjectName(u"pushButton_selectBackgroundColour")
        self.pushButton_selectBackgroundColour.setMinimumSize(QSize(110, 35))
        self.pushButton_selectBackgroundColour.setMaximumSize(QSize(110, 35))
        self.pushButton_selectBackgroundColour.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_selectBackgroundColour, 1, 7, 1, 1)

        self.radioButton_setBackgroundColour = QRadioButton(self.groupBox)
        self.radioButton_setBackgroundColour.setObjectName(u"radioButton_setBackgroundColour")
        self.radioButton_setBackgroundColour.setMinimumSize(QSize(0, 35))
        self.radioButton_setBackgroundColour.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.radioButton_setBackgroundColour, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.label_backgroundColour = QLabel(self.groupBox)
        self.label_backgroundColour.setObjectName(u"label_backgroundColour")
        self.label_backgroundColour.setMinimumSize(QSize(30, 30))
        self.label_backgroundColour.setMaximumSize(QSize(30, 30))
        self.label_backgroundColour.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_backgroundColour, 1, 6, 1, 1)

        self.radioButton_noBackground = QRadioButton(self.groupBox)
        self.radioButton_noBackground.setObjectName(u"radioButton_noBackground")
        self.radioButton_noBackground.setMinimumSize(QSize(0, 35))
        self.radioButton_noBackground.setMaximumSize(QSize(16777215, 35))
        self.radioButton_noBackground.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_noBackground, 0, 1, 1, 1)

        self.lineEdit_backgroundPath = QLineEdit(self.groupBox)
        self.lineEdit_backgroundPath.setObjectName(u"lineEdit_backgroundPath")
        self.lineEdit_backgroundPath.setMinimumSize(QSize(0, 35))
        self.lineEdit_backgroundPath.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_backgroundPath, 2, 3, 1, 4)

        self.checkBox_userBackground = QCheckBox(self.groupBox)
        self.checkBox_userBackground.setObjectName(u"checkBox_userBackground")
        self.checkBox_userBackground.setMinimumSize(QSize(0, 35))
        self.checkBox_userBackground.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.checkBox_userBackground, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(130, 35))
        self.label_8.setMaximumSize(QSize(130, 35))

        self.horizontalLayout_4.addWidget(self.label_8)

        self.doubleSpinBox_prefer_horizontal_wordCloud = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_prefer_horizontal_wordCloud.setObjectName(u"doubleSpinBox_prefer_horizontal_wordCloud")
        self.doubleSpinBox_prefer_horizontal_wordCloud.setMinimumSize(QSize(55, 35))
        self.doubleSpinBox_prefer_horizontal_wordCloud.setMaximumSize(QSize(55, 35))
        self.doubleSpinBox_prefer_horizontal_wordCloud.setMinimum(0.100000000000000)
        self.doubleSpinBox_prefer_horizontal_wordCloud.setMaximum(0.900000000000000)
        self.doubleSpinBox_prefer_horizontal_wordCloud.setSingleStep(0.100000000000000)
        self.doubleSpinBox_prefer_horizontal_wordCloud.setValue(0.900000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_prefer_horizontal_wordCloud)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(130, 35))
        self.label_5.setMaximumSize(QSize(130, 35))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.spinBox_max_word_count_wordCloud = QSpinBox(self.groupBox_3)
        self.spinBox_max_word_count_wordCloud.setObjectName(u"spinBox_max_word_count_wordCloud")
        self.spinBox_max_word_count_wordCloud.setMinimumSize(QSize(55, 35))
        self.spinBox_max_word_count_wordCloud.setMaximumSize(QSize(55, 35))
        self.spinBox_max_word_count_wordCloud.setMinimum(100)
        self.spinBox_max_word_count_wordCloud.setMaximum(1000)
        self.spinBox_max_word_count_wordCloud.setSingleStep(10)
        self.spinBox_max_word_count_wordCloud.setValue(200)

        self.horizontalLayout_2.addWidget(self.spinBox_max_word_count_wordCloud)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(130, 35))
        self.label_6.setMaximumSize(QSize(130, 35))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.spinBox_max_word_margin_wordCloud = QSpinBox(self.groupBox_3)
        self.spinBox_max_word_margin_wordCloud.setObjectName(u"spinBox_max_word_margin_wordCloud")
        self.spinBox_max_word_margin_wordCloud.setMinimumSize(QSize(55, 35))
        self.spinBox_max_word_margin_wordCloud.setMaximumSize(QSize(55, 35))
        self.spinBox_max_word_margin_wordCloud.setValue(2)

        self.horizontalLayout_5.addWidget(self.spinBox_max_word_margin_wordCloud)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 3)

        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(130, 35))
        self.label_7.setMaximumSize(QSize(130, 35))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.doubleSpinBox_relative_scaling_wordCloud = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_relative_scaling_wordCloud.setObjectName(u"doubleSpinBox_relative_scaling_wordCloud")
        self.doubleSpinBox_relative_scaling_wordCloud.setMinimumSize(QSize(55, 35))
        self.doubleSpinBox_relative_scaling_wordCloud.setMaximumSize(QSize(55, 35))
        self.doubleSpinBox_relative_scaling_wordCloud.setMinimum(0.100000000000000)
        self.doubleSpinBox_relative_scaling_wordCloud.setMaximum(1.000000000000000)
        self.doubleSpinBox_relative_scaling_wordCloud.setSingleStep(0.100000000000000)
        self.doubleSpinBox_relative_scaling_wordCloud.setValue(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_relative_scaling_wordCloud)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u8bcd\u4e91\u56fe\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u5b57\u4f53\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u8def\u5f84\uff1a", None))
        self.pushButton_fontOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.radioButton_randomFontColour.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u5b57\u4f53\u989c\u8272", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u989c\u8272\u9884\u89c8\uff1a", None))
        self.radioButton_setFontColour.setText(QCoreApplication.translate("Form", u"\u56fa\u5b9a\u989c\u8272", None))
        self.radioButton_setUserFontColour.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u989c\u8272", None))
        self.pushButton_selectFontColour.setText(QCoreApplication.translate("Form", u"\u8c03\u8272\u677f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u989c\u8272\u5217\uff1a", None))
        self.label_fontColour.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u80cc\u666f\u8bbe\u7f6e", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u989c\u8272\u9884\u89c8\uff1a", None))
        self.pushButton_backgroundShow.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
        self.pushButton_backgroundOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
#if QT_CONFIG(statustip)
        self.pushButton_selectBackgroundColour.setStatusTip(QCoreApplication.translate("Form", u"\u8c03\u8272\u677f", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_selectBackgroundColour.setWhatsThis(QCoreApplication.translate("Form", u"\u8c03\u8272\u677f", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.pushButton_selectBackgroundColour.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_selectBackgroundColour.setText(QCoreApplication.translate("Form", u"\u8c03\u8272\u677f", None))
        self.radioButton_setBackgroundColour.setText(QCoreApplication.translate("Form", u"\u56fa\u5b9a\u989c\u8272\u5e95\u56fe", None))
        self.label_backgroundColour.setText("")
        self.radioButton_noBackground.setText(QCoreApplication.translate("Form", u"\u900f\u660e\u5e95\u56fe", None))
        self.checkBox_userBackground.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u8499\u7248", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5176\u4ed6\u53c2\u6570", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6c34\u5e73\u65b9\u5411\u6392\u7248\u9891\u7387\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u8bcd\u8bed\u6570\u91cf\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8bcd\u95f4\u9694\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8bcd\u9891\u4e0e\u5b57\u53f7\u6620\u5c04\u6bd4\uff1a", None))
    # retranslateUi

