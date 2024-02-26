# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialoglogin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        if not DialogLogin.objectName():
            DialogLogin.setObjectName(u"DialogLogin")
        DialogLogin.resize(500, 538)
        DialogLogin.setMinimumSize(QSize(500, 538))
        DialogLogin.setMaximumSize(QSize(500, 538))
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DialogLogin.setFont(font)
        self.verticalLayout = QVBoxLayout(DialogLogin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 7, 0, 0)
        self.label_status = QLabel(DialogLogin)
        self.label_status.setObjectName(u"label_status")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.label_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_status)

        self.label_qrcode = QLabel(DialogLogin)
        self.label_qrcode.setObjectName(u"label_qrcode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_qrcode.sizePolicy().hasHeightForWidth())
        self.label_qrcode.setSizePolicy(sizePolicy1)
        self.label_qrcode.setScaledContents(True)
        self.label_qrcode.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_qrcode)


        self.retranslateUi(DialogLogin)

        QMetaObject.connectSlotsByName(DialogLogin)
    # setupUi

    def retranslateUi(self, DialogLogin):
        DialogLogin.setWindowTitle(QCoreApplication.translate("DialogLogin", u"\u4e8c\u7ef4\u7801\u767b\u5f55", None))
        self.label_status.setText(QCoreApplication.translate("DialogLogin", u"\u6b63\u5728\u51c6\u5907\u4e8c\u7ef4\u7801", None))
        self.label_qrcode.setText("")
    # retranslateUi

