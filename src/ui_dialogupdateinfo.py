# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialogupdateinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogUpdateInfo(object):
    def setupUi(self, DialogUpdateInfo):
        if not DialogUpdateInfo.objectName():
            DialogUpdateInfo.setObjectName(u"DialogUpdateInfo")
        DialogUpdateInfo.resize(671, 501)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DialogUpdateInfo.setFont(font)
        self.verticalLayout = QVBoxLayout(DialogUpdateInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_version = QLabel(DialogUpdateInfo)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout.addWidget(self.label_version)

        self.text_info = QTextEdit(DialogUpdateInfo)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_info)

        self.buttonBox = QDialogButtonBox(DialogUpdateInfo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogUpdateInfo)
        self.buttonBox.accepted.connect(DialogUpdateInfo.accept)
        self.buttonBox.rejected.connect(DialogUpdateInfo.reject)

        QMetaObject.connectSlotsByName(DialogUpdateInfo)
    # setupUi

    def retranslateUi(self, DialogUpdateInfo):
        DialogUpdateInfo.setWindowTitle(QCoreApplication.translate("DialogUpdateInfo", u"BiliDownloader - \u65b0\u7248\u672c", None))
        self.label_version.setText("")
    # retranslateUi

