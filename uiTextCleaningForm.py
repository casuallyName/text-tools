# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiTextCleaningForm.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 350))
        Form.setMaximumSize(QSize(600, 350))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 75))
        self.groupBox_2.setMaximumSize(QSize(16777215, 75))
        self.gridLayout_47 = QGridLayout(self.groupBox_2)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.checkBox_set_custom_pattern = QCheckBox(self.groupBox_2)
        self.checkBox_set_custom_pattern.setObjectName(u"checkBox_set_custom_pattern")
        self.checkBox_set_custom_pattern.setMinimumSize(QSize(70, 19))
        self.checkBox_set_custom_pattern.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_47.addWidget(self.checkBox_set_custom_pattern, 0, 0, 1, 1)

        self.lineEdit_custom_pattern = QLineEdit(self.groupBox_2)
        self.lineEdit_custom_pattern.setObjectName(u"lineEdit_custom_pattern")
        self.lineEdit_custom_pattern.setMinimumSize(QSize(0, 25))
        self.lineEdit_custom_pattern.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_47.addWidget(self.lineEdit_custom_pattern, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.lineEdit, 1, 2, 1, 2)

        self.pushButton_add = QPushButton(self.groupBox)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(90, 35))
        self.pushButton_add.setMaximumSize(QSize(90, 35))
        icon1 = QIcon()
        icon1.addFile(u"src/img/AddItem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pushButton_add, 1, 4, 1, 1)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 3, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 35))
        self.label.setMaximumSize(QSize(60, 35))

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))
        self.label_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)

        self.lineEdit_join = QLineEdit(self.groupBox)
        self.lineEdit_join.setObjectName(u"lineEdit_join")
        self.lineEdit_join.setMinimumSize(QSize(50, 35))
        self.lineEdit_join.setMaximumSize(QSize(50, 35))

        self.gridLayout_3.addWidget(self.lineEdit_join, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 4, 1, 1)

        self.groupBox_1 = QGroupBox(self.groupBox)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.gridLayout = QGridLayout(self.groupBox_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_1 = QCheckBox(self.groupBox_1)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setMinimumSize(QSize(50, 20))
        self.checkBox_1.setMaximumSize(QSize(50, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(50, 20))
        self.checkBox_2.setMaximumSize(QSize(50, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.checkBox_2.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_1)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(50, 20))
        self.checkBox_3.setMaximumSize(QSize(50, 20))
        self.checkBox_3.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_1)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(50, 20))
        self.checkBox_4.setMaximumSize(QSize(50, 20))
        self.checkBox_4.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_4, 0, 3, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_1)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(50, 20))
        self.checkBox_5.setMaximumSize(QSize(50, 20))
        self.checkBox_5.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_5, 0, 4, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_1)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setMinimumSize(QSize(50, 20))
        self.checkBox_6.setMaximumSize(QSize(50, 20))
        self.checkBox_6.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_6, 1, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_1)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(50, 20))
        self.checkBox_7.setMaximumSize(QSize(50, 20))
        self.checkBox_7.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_1)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setMinimumSize(QSize(50, 20))
        self.checkBox_8.setMaximumSize(QSize(50, 20))
        self.checkBox_8.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_1)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setMinimumSize(QSize(50, 20))
        self.checkBox_9.setMaximumSize(QSize(50, 20))
        self.checkBox_9.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_9, 1, 3, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox_1)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setMinimumSize(QSize(50, 20))
        self.checkBox_10.setMaximumSize(QSize(50, 20))
        self.checkBox_10.setFont(font1)

        self.gridLayout.addWidget(self.checkBox_10, 1, 4, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_1, 0, 1, 1, 4)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u6587\u672c\u6e05\u6d17\u5de5\u5177\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u89c4\u5219", None))
        self.checkBox_set_custom_pattern.setText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7279\u6b8a\u7b26\u53f7\u63d0\u53d6", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_add.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u7b26\uff1a", None))
        self.lineEdit_join.setText(QCoreApplication.translate("Form", u",", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"\u5e38\u7528\u7279\u6b8a\u7b26\u53f7", None))
        self.checkBox_1.setText(QCoreApplication.translate("Form", u"@", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"#", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"$", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"%", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"&&", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"+", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"-", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"*", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"/", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

