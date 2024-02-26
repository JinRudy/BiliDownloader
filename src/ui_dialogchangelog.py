# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialogchangelog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogChangeLog(object):
    def setupUi(self, DialogChangeLog):
        if not DialogChangeLog.objectName():
            DialogChangeLog.setObjectName(u"DialogChangeLog")
        DialogChangeLog.resize(680, 420)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DialogChangeLog.setFont(font)
        self.verticalLayout = QVBoxLayout(DialogChangeLog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DialogChangeLog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(DialogChangeLog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(DialogChangeLog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(DialogChangeLog)
        self.buttonBox.accepted.connect(DialogChangeLog.accept)
        self.buttonBox.rejected.connect(DialogChangeLog.reject)

        QMetaObject.connectSlotsByName(DialogChangeLog)
    # setupUi

    def retranslateUi(self, DialogChangeLog):
        DialogChangeLog.setWindowTitle(QCoreApplication.translate("DialogChangeLog", u"\u66f4\u65b0\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("DialogChangeLog", u"\u7248\u672c\u4fe1\u606f\uff1a", None))
    # retranslateUi

