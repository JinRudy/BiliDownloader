# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_videosubwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VideoSubwidget(object):
    def setupUi(self, VideoSubwidget):
        if not VideoSubwidget.objectName():
            VideoSubwidget.setObjectName(u"VideoSubwidget")
        VideoSubwidget.resize(540, 483)
        self.verticalLayoutWidget = QWidget(VideoSubwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 10, 361, 31))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_version = QLabel(self.verticalLayoutWidget)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout_4.addWidget(self.label_version)

        self.verticalLayoutWidget_3 = QWidget(VideoSubwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(30, 100, 361, 54))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(VideoSubwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 50, 141, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.button_changelog = QPushButton(self.horizontalLayoutWidget)
        self.button_changelog.setObjectName(u"button_changelog")

        self.horizontalLayout_3.addWidget(self.button_changelog)


        self.retranslateUi(VideoSubwidget)

        QMetaObject.connectSlotsByName(VideoSubwidget)
    # setupUi

    def retranslateUi(self, VideoSubwidget):
        VideoSubwidget.setWindowTitle(QCoreApplication.translate("VideoSubwidget", u"Form", None))
        self.label_version.setText(QCoreApplication.translate("VideoSubwidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("VideoSubwidget", u"TextLabel", None))
        self.button_changelog.setText(QCoreApplication.translate("VideoSubwidget", u"PushButton", None))
    # retranslateUi

