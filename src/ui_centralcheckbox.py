# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_centralcheckbox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CentralCheckBox(object):
    def setupUi(self, CentralCheckBox):
        if not CentralCheckBox.objectName():
            CentralCheckBox.setObjectName(u"CentralCheckBox")
        CentralCheckBox.resize(116, 23)
        self.horizontalLayout = QHBoxLayout(CentralCheckBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(CentralCheckBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(CentralCheckBox)

        QMetaObject.connectSlotsByName(CentralCheckBox)
    # setupUi

    def retranslateUi(self, CentralCheckBox):
        CentralCheckBox.setWindowTitle(QCoreApplication.translate("CentralCheckBox", u"Form", None))
        self.checkBox.setText("")
    # retranslateUi

