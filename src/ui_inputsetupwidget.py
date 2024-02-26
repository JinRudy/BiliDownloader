# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inputsetupwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InputSetupWidget(object):
    def setupUi(self, InputSetupWidget):
        if not InputSetupWidget.objectName():
            InputSetupWidget.setObjectName(u"InputSetupWidget")
        InputSetupWidget.resize(355, 247)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        InputSetupWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(InputSetupWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(InputSetupWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(InputSetupWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.line_input = QLineEdit(InputSetupWidget)
        self.line_input.setObjectName(u"line_input")
        self.line_input.setStyleSheet(u"font: 11pt \"HarmonyOS Sans SC\";")

        self.verticalLayout.addWidget(self.line_input)

        self.label_hint = QLabel(InputSetupWidget)
        self.label_hint.setObjectName(u"label_hint")
        self.label_hint.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_hint)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_next = QPushButton(InputSetupWidget)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setEnabled(False)

        self.verticalLayout.addWidget(self.button_next)


        self.retranslateUi(InputSetupWidget)

        QMetaObject.connectSlotsByName(InputSetupWidget)
    # setupUi

    def retranslateUi(self, InputSetupWidget):
        InputSetupWidget.setWindowTitle(QCoreApplication.translate("InputSetupWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("InputSetupWidget", u"\u8f93\u5165\u60f3\u8981\u4e0b\u8f7d\u7684\u89c6\u9891\u53f7\u6216\u94fe\u63a5\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("InputSetupWidget", u"\u9700\u8981\u5305\u542bAV\u3001BV\u3001MD\u3001\u548cEP\u53f7", None))
        self.label_hint.setText("")
        self.button_next.setText(QCoreApplication.translate("InputSetupWidget", u"\u7ee7\u7eed", None))
    # retranslateUi

