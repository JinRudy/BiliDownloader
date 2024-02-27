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
        VideoSubwidget.resize(539, 548)
        VideoSubwidget.setLayoutDirection(Qt.LeftToRight)
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
        self.horizontalLayoutWidget.setGeometry(QRect(30, 50, 174, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.button_videosub_submit = QPushButton(self.horizontalLayoutWidget)
        self.button_videosub_submit.setObjectName(u"button_videosub_submit")

        self.horizontalLayout_3.addWidget(self.button_videosub_submit)

        self.horizontalLayoutWidget_2 = QWidget(VideoSubwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 170, 471, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.time_startsub = QTimeEdit(self.horizontalLayoutWidget_2)
        self.time_startsub.setObjectName(u"time_startsub")
        self.time_startsub.setContextMenuPolicy(Qt.NoContextMenu)
        self.time_startsub.setLayoutDirection(Qt.RightToLeft)
        self.time_startsub.setInputMethodHints(Qt.ImhPreferNumbers|Qt.ImhTime)
        self.time_startsub.setCurrentSection(QDateTimeEdit.SecondSection)
        self.time_startsub.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.time_startsub)

        self.time_endsub = QTimeEdit(self.horizontalLayoutWidget_2)
        self.time_endsub.setObjectName(u"time_endsub")
        self.time_endsub.setContextMenuPolicy(Qt.NoContextMenu)
        self.time_endsub.setInputMethodHints(Qt.ImhPreferNumbers|Qt.ImhTime)
        self.time_endsub.setCurrentSection(QDateTimeEdit.HourSection)
        self.time_endsub.setCalendarPopup(True)
        self.time_endsub.setTime(QTime(0, 0, 0))

        self.horizontalLayout.addWidget(self.time_endsub)

        self.time_startsub.raise_()
        self.time_endsub.raise_()
        self.label_2.raise_()

        self.retranslateUi(VideoSubwidget)

        QMetaObject.connectSlotsByName(VideoSubwidget)
    # setupUi

    def retranslateUi(self, VideoSubwidget):
        VideoSubwidget.setWindowTitle(QCoreApplication.translate("VideoSubwidget", u"Form", None))
        self.label_version.setText(QCoreApplication.translate("VideoSubwidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("VideoSubwidget", u"TextLabel", None))
        self.button_videosub_submit.setText(QCoreApplication.translate("VideoSubwidget", u"\u5f00\u59cb\u622a\u53d6", None))
        self.label_2.setText(QCoreApplication.translate("VideoSubwidget", u"\u622a\u53d6\u65f6\u95f4", None))
        self.time_startsub.setDisplayFormat(QCoreApplication.translate("VideoSubwidget", u"HH:mm:ss", None))
        self.time_endsub.setDisplayFormat(QCoreApplication.translate("VideoSubwidget", u"HH:mm:ss", None))
    # retranslateUi

