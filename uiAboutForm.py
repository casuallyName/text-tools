# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiAboutForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 288)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(3045, 4000))
        icon = QIcon()
        icon.addFile(u"src/img/QIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(48, 48))
        self.label.setMaximumSize(QSize(48, 48))
        self.label.setPixmap(QPixmap(u"src/img/QIcon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 48))
        self.label_2.setMaximumSize(QSize(16777215, 47))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(13, 38, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_version = QLabel(Form)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMinimumSize(QSize(0, 30))
        self.label_version.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_version)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(30, 30))
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u"src/img/Qt_for_Python.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_homePage = QLabel(Form)
        self.label_homePage.setObjectName(u"label_homePage")
        self.label_homePage.setMinimumSize(QSize(0, 30))
        self.label_homePage.setMaximumSize(QSize(16777215, 30))
        self.label_homePage.setStyleSheet(u"")
        self.label_homePage.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_homePage)

        self.label_DocumentPage = QLabel(Form)
        self.label_DocumentPage.setObjectName(u"label_DocumentPage")
        self.label_DocumentPage.setMinimumSize(QSize(0, 30))
        self.label_DocumentPage.setMaximumSize(QSize(16777215, 30))
        self.label_DocumentPage.setStyleSheet(u"")
        self.label_DocumentPage.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_DocumentPage)

        self.label_issuesPage = QLabel(Form)
        self.label_issuesPage.setObjectName(u"label_issuesPage")
        self.label_issuesPage.setMinimumSize(QSize(0, 30))
        self.label_issuesPage.setMaximumSize(QSize(16777215, 30))
        self.label_issuesPage.setStyleSheet(u"")
        self.label_issuesPage.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_issuesPage)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_open_source_software = QLabel(Form)
        self.label_open_source_software.setObjectName(u"label_open_source_software")
        self.label_open_source_software.setMinimumSize(QSize(0, 30))
        self.label_open_source_software.setMaximumSize(QSize(16777215, 30))
        self.label_open_source_software.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_open_source_software)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Text Tools - \u5173\u4e8e", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Text tools", None))
        self.label_version.setText(QCoreApplication.translate("Form", u"\u7248\u672c : beta", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Built with Qt for Python", None))
        self.label_5.setText("")
        self.label_homePage.setText(QCoreApplication.translate("Form", u"\u4e3b\u9875 : <a href=\"https://gitee.com/casuallyName/text-tools\">Gitee</a> | <a href=\"https://github.com/casuallyName/text-tools\">Github</a>", None))
        self.label_DocumentPage.setText(QCoreApplication.translate("Form", u"\u6587\u6863 : <a href=\"https://gitee.com/casuallyName/text-tools/wikis/Home\">Gitee</a> | <a href=\"https://github.com/casuallyName/text-tools/wiki\">Github</a>\n"
"", None))
        self.label_issuesPage.setText(QCoreApplication.translate("Form", u"\u53cd\u9988 : <a href=\"https://gitee.com/casuallyName/text-tools/issues\">Gitee</a> | <a href=\"https://github.com/casuallyName/text-tools/issues\">Github</a>", None))
        self.label_open_source_software.setText(QCoreApplication.translate("Form", u"Powered by <a href='a'>open-source software</a>", None))
    # retranslateUi

