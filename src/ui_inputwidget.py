# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inputwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InputWidget(object):
    def setupUi(self, InputWidget):
        if not InputWidget.objectName():
            InputWidget.setObjectName(u"InputWidget")
        InputWidget.resize(264, 113)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        InputWidget.setFont(font)
        self.gridLayout = QGridLayout(InputWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(InputWidget)

        QMetaObject.connectSlotsByName(InputWidget)
    # setupUi

    def retranslateUi(self, InputWidget):
        InputWidget.setWindowTitle(QCoreApplication.translate("InputWidget", u"Form", None))
    # retranslateUi

