# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_downloaditem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DownloadItem(object):
    def setupUi(self, DownloadItem):
        if not DownloadItem.objectName():
            DownloadItem.setObjectName(u"DownloadItem")
        DownloadItem.resize(500, 111)
        DownloadItem.setMinimumSize(QSize(0, 111))
        DownloadItem.setMaximumSize(QSize(16777215, 111))
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DownloadItem.setFont(font)
        self.verticalLayout = QVBoxLayout(DownloadItem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_title = QLabel(DownloadItem)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_3.addWidget(self.label_title)

        self.label_part = QLabel(DownloadItem)
        self.label_part.setObjectName(u"label_part")

        self.horizontalLayout_3.addWidget(self.label_part)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_status = QLabel(DownloadItem)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout_2.addWidget(self.label_status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_progress = QLabel(DownloadItem)
        self.label_progress.setObjectName(u"label_progress")

        self.horizontalLayout_2.addWidget(self.label_progress)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.progressBar = QProgressBar(DownloadItem)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        self.button_open = QPushButton(DownloadItem)
        self.button_open.setObjectName(u"button_open")
        self.button_open.setEnabled(False)

        self.gridLayout.addWidget(self.button_open, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(DownloadItem)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(DownloadItem)

        QMetaObject.connectSlotsByName(DownloadItem)
    # setupUi

    def retranslateUi(self, DownloadItem):
        DownloadItem.setWindowTitle(QCoreApplication.translate("DownloadItem", u"Form", None))
        self.label_title.setText("")
        self.label_part.setText("")
        self.label_status.setText(QCoreApplication.translate("DownloadItem", u"\u7b49\u5f85\u4e0b\u8f7d", None))
        self.label_progress.setText(QCoreApplication.translate("DownloadItem", u"0 / 0", None))
        self.button_open.setText(QCoreApplication.translate("DownloadItem", u"\u91cd\u65b0\u4e0b\u8f7d", None))
    # retranslateUi

