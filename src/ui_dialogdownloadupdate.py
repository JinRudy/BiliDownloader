# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialogdownloadupdate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogDownloadUpdate(object):
    def setupUi(self, DialogDownloadUpdate):
        if not DialogDownloadUpdate.objectName():
            DialogDownloadUpdate.setObjectName(u"DialogDownloadUpdate")
        DialogDownloadUpdate.resize(500, 85)
        DialogDownloadUpdate.setMinimumSize(QSize(500, 85))
        DialogDownloadUpdate.setMaximumSize(QSize(500, 85))
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        DialogDownloadUpdate.setFont(font)
        DialogDownloadUpdate.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout = QVBoxLayout(DialogDownloadUpdate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DialogDownloadUpdate)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(DialogDownloadUpdate)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(DialogDownloadUpdate)

        QMetaObject.connectSlotsByName(DialogDownloadUpdate)
    # setupUi

    def retranslateUi(self, DialogDownloadUpdate):
        DialogDownloadUpdate.setWindowTitle(QCoreApplication.translate("DialogDownloadUpdate", u"\u83b7\u53d6\u66f4\u65b0", None))
        self.label.setText(QCoreApplication.translate("DialogDownloadUpdate", u"\u6b63\u5728\u83b7\u53d6\u66f4\u65b0...", None))
    # retranslateUi

