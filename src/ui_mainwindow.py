# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from inputwidget import InputWidget
from settingswidget import SettingsWidget
from downloadwidget import DownloadWidget
from aboutwidget import AboutWidget
from videosubwidget import VideoSubWidget

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_input = QWidget()
        self.tab_input.setObjectName(u"tab_input")
        self.gridLayout_2 = QGridLayout(self.tab_input)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_input = InputWidget(self.tab_input)
        self.widget_input.setObjectName(u"widget_input")

        self.gridLayout_2.addWidget(self.widget_input, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_input, "")
        self.tab_download = QWidget()
        self.tab_download.setObjectName(u"tab_download")
        self.gridLayout_4 = QGridLayout(self.tab_download)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_download = DownloadWidget(self.tab_download)
        self.widget_download.setObjectName(u"widget_download")

        self.gridLayout_4.addWidget(self.widget_download, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_download, "")
        self.tab_video = QWidget()
        self.tab_video.setObjectName(u"tab_video")
        self.gridLayout_6 = QGridLayout(self.tab_video)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_videosub = VideoSubWidget(self.tab_video)
        self.widget_videosub.setObjectName(u"widget_videosub")

        self.gridLayout_6.addWidget(self.widget_videosub, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_video, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_3 = QGridLayout(self.tab_settings)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_settings = SettingsWidget(self.tab_settings)
        self.widget_settings.setObjectName(u"widget_settings")

        self.gridLayout_3.addWidget(self.widget_settings, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_settings, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.gridLayout_5 = QGridLayout(self.tab_about)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_about = AboutWidget(self.tab_about)
        self.widget_about.setObjectName(u"widget_about")

        self.gridLayout_5.addWidget(self.widget_about, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_about, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BiliDownloader", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_input), QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_download), QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_video), QCoreApplication.translate("MainWindow", u"\u526a\u8f91", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

