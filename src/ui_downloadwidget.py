# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_downloadwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DownloadWidget(object):
    def setupUi(self, DownloadWidget):
        if not DownloadWidget.objectName():
            DownloadWidget.setObjectName(u"DownloadWidget")
        DownloadWidget.resize(256, 232)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DownloadWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(DownloadWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(DownloadWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setSpacing(0)
        self.listWidget.setGridSize(QSize(0, 111))

        self.verticalLayout.addWidget(self.listWidget)

        self.button_clean = QPushButton(DownloadWidget)
        self.button_clean.setObjectName(u"button_clean")

        self.verticalLayout.addWidget(self.button_clean)


        self.retranslateUi(DownloadWidget)

        QMetaObject.connectSlotsByName(DownloadWidget)
    # setupUi

    def retranslateUi(self, DownloadWidget):
        DownloadWidget.setWindowTitle(QCoreApplication.translate("DownloadWidget", u"Form", None))
        self.button_clean.setText(QCoreApplication.translate("DownloadWidget", u"\u6e05\u7a7a\u5df2\u5b8c\u6210", None))
    # retranslateUi

