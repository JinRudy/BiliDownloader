# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_confirmwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from imagelabel import ImageLabel

import res_rc

class Ui_ConfirmWidget(object):
    def setupUi(self, ConfirmWidget):
        if not ConfirmWidget.objectName():
            ConfirmWidget.setObjectName(u"ConfirmWidget")
        ConfirmWidget.resize(297, 277)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        ConfirmWidget.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(ConfirmWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(ConfirmWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_info = QTextEdit(ConfirmWidget)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.text_info)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.cover_label = ImageLabel(ConfirmWidget)
        self.cover_label.setObjectName(u"cover_label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover_label.sizePolicy().hasHeightForWidth())
        self.cover_label.setSizePolicy(sizePolicy)
        self.cover_label.setScaledContents(True)
        self.cover_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cover_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_back = QPushButton(ConfirmWidget)
        self.button_back.setObjectName(u"button_back")

        self.horizontalLayout.addWidget(self.button_back)

        self.button_next = QPushButton(ConfirmWidget)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setEnabled(False)

        self.horizontalLayout.addWidget(self.button_next)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(ConfirmWidget)

        QMetaObject.connectSlotsByName(ConfirmWidget)
    # setupUi

    def retranslateUi(self, ConfirmWidget):
        ConfirmWidget.setWindowTitle(QCoreApplication.translate("ConfirmWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("ConfirmWidget", u"\u8bf7\u786e\u8ba4\u4fe1\u606f\uff1a", None))
        self.cover_label.setText("")
        self.button_back.setText(QCoreApplication.translate("ConfirmWidget", u"\u8fd4\u56de", None))
        self.button_next.setText(QCoreApplication.translate("ConfirmWidget", u"\u7ee7\u7eed", None))
    # retranslateUi

