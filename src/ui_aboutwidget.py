# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_aboutwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutWidget(object):
    def setupUi(self, AboutWidget):
        if not AboutWidget.objectName():
            AboutWidget.setObjectName(u"AboutWidget")
        AboutWidget.resize(553, 498)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        AboutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(AboutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AboutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_version = QLabel(AboutWidget)
        self.label_version.setObjectName(u"label_version")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_version)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(AboutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(AboutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_3 = QLabel(AboutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(AboutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(AboutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(AboutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(AboutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setOpenExternalLinks(True)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(AboutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button_changelog = QPushButton(AboutWidget)
        self.button_changelog.setObjectName(u"button_changelog")

        self.horizontalLayout_4.addWidget(self.button_changelog)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AboutWidget)

        QMetaObject.connectSlotsByName(AboutWidget)
    # setupUi

    def retranslateUi(self, AboutWidget):
        AboutWidget.setWindowTitle(QCoreApplication.translate("AboutWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AboutWidget", u"BiliDownloader", None))
        self.label_version.setText("")
        self.label_2.setText(QCoreApplication.translate("AboutWidget", u"Copyright (C) 2021-2024 Majjcom", None))
        self.label_3.setText(QCoreApplication.translate("AboutWidget", u"\u53cd\u9988 & \u5f00\u6e90\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("AboutWidget", u"Github:", None))
        self.label_5.setText(QCoreApplication.translate("AboutWidget", u"<html><head/><body><p><a href=\"https://github.com/Majjcom/BiliDownloader\"><span style=\" text-decoration: underline; color:#0000ff;\">Majjcom/BiliDownloader</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("AboutWidget", u"Gitee:", None))
        self.label_7.setText(QCoreApplication.translate("AboutWidget", u"<html><head/><body><p><a href=\"https://gitee.com/majjcom/bili-downloader\"><span style=\" text-decoration: underline; color:#0000ff;\">Majjcom/BiliDownloader</span></a></p></body></html>", None))
        self.button_changelog.setText(QCoreApplication.translate("AboutWidget", u"\u67e5\u770bCHANGELOG", None))
    # retranslateUi

