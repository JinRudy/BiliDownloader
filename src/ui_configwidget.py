# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_configwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigWidget(object):
    def setupUi(self, ConfigWidget):
        if not ConfigWidget.objectName():
            ConfigWidget.setObjectName(u"ConfigWidget")
        ConfigWidget.resize(501, 520)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        ConfigWidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(ConfigWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(ConfigWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.combo_quality = QComboBox(self.widget)
        self.combo_quality.setObjectName(u"combo_quality")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_quality.sizePolicy().hasHeightForWidth())
        self.combo_quality.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_quality, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.combo_codec = QComboBox(self.widget)
        self.combo_codec.setObjectName(u"combo_codec")
        sizePolicy.setHeightForWidth(self.combo_codec.sizePolicy().hasHeightForWidth())
        self.combo_codec.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.combo_codec, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_path = QLineEdit(self.widget)
        self.line_path.setObjectName(u"line_path")
        self.line_path.setStyleSheet(u"font: 11pt \"HarmonyOS Sans SC\";")

        self.horizontalLayout.addWidget(self.line_path)

        self.button_path = QPushButton(self.widget)
        self.button_path.setObjectName(u"button_path")

        self.horizontalLayout.addWidget(self.button_path)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.combo_get_type = QComboBox(self.widget)
        self.combo_get_type.setObjectName(u"combo_get_type")

        self.gridLayout.addWidget(self.combo_get_type, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.table_downloads = QTableWidget(self.widget)
        if (self.table_downloads.columnCount() < 2):
            self.table_downloads.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_downloads.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_downloads.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_downloads.setObjectName(u"table_downloads")
        self.table_downloads.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_downloads.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_downloads.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_downloads.setRowCount(0)
        self.table_downloads.setColumnCount(2)
        self.table_downloads.horizontalHeader().setVisible(True)
        self.table_downloads.horizontalHeader().setCascadingSectionResizes(False)
        self.table_downloads.horizontalHeader().setDefaultSectionSize(100)
        self.table_downloads.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_downloads)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_back = QPushButton(ConfigWidget)
        self.button_back.setObjectName(u"button_back")

        self.horizontalLayout_2.addWidget(self.button_back)

        self.button_submit = QPushButton(ConfigWidget)
        self.button_submit.setObjectName(u"button_submit")
        self.button_submit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.button_submit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ConfigWidget)

        QMetaObject.connectSlotsByName(ConfigWidget)
    # setupUi

    def retranslateUi(self, ConfigWidget):
        ConfigWidget.setWindowTitle(QCoreApplication.translate("ConfigWidget", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("ConfigWidget", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("ConfigWidget", u"\u4f18\u9009\u683c\u5f0f", None))
        self.label_4.setText(QCoreApplication.translate("ConfigWidget", u"\u6293\u53d6\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("ConfigWidget", u"\u6700\u5927\u6e05\u6670\u5ea6", None))
        self.button_path.setText(QCoreApplication.translate("ConfigWidget", u"\u8bbe\u7f6e\u5f53\u524d\u4fdd\u5b58\u4f4d\u7f6e", None))
        ___qtablewidgetitem = self.table_downloads.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ConfigWidget", u"\u4e0b\u8f7d\u5f39\u5e55", None));
        ___qtablewidgetitem1 = self.table_downloads.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ConfigWidget", u"\u4e0b\u8f7d\u9879", None));
        self.button_back.setText(QCoreApplication.translate("ConfigWidget", u"\u8fd4\u56de", None))
        self.button_submit.setText(QCoreApplication.translate("ConfigWidget", u"\u63d0\u4ea4", None))
    # retranslateUi

