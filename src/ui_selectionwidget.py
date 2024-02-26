# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_selectionwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectionWidget(object):
    def setupUi(self, SelectionWidget):
        if not SelectionWidget.objectName():
            SelectionWidget.setObjectName(u"SelectionWidget")
        SelectionWidget.resize(332, 317)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        SelectionWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(SelectionWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(SelectionWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_selection = QLineEdit(SelectionWidget)
        self.line_selection.setObjectName(u"line_selection")

        self.horizontalLayout_2.addWidget(self.line_selection)

        self.button_setSelection = QPushButton(SelectionWidget)
        self.button_setSelection.setObjectName(u"button_setSelection")

        self.horizontalLayout_2.addWidget(self.button_setSelection)

        self.button_help = QToolButton(SelectionWidget)
        self.button_help.setObjectName(u"button_help")
        self.button_help.setCursor(QCursor(Qt.WhatsThisCursor))

        self.horizontalLayout_2.addWidget(self.button_help)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.table_selection = QTableWidget(SelectionWidget)
        if (self.table_selection.columnCount() < 2):
            self.table_selection.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_selection.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_selection.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_selection.setObjectName(u"table_selection")
        self.table_selection.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_selection.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_selection.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_selection.horizontalHeader().setDefaultSectionSize(80)
        self.table_selection.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_selection)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_back = QPushButton(SelectionWidget)
        self.button_back.setObjectName(u"button_back")

        self.horizontalLayout.addWidget(self.button_back)

        self.button_next = QPushButton(SelectionWidget)
        self.button_next.setObjectName(u"button_next")

        self.horizontalLayout.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SelectionWidget)

        QMetaObject.connectSlotsByName(SelectionWidget)
    # setupUi

    def retranslateUi(self, SelectionWidget):
        SelectionWidget.setWindowTitle(QCoreApplication.translate("SelectionWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("SelectionWidget", u"\u9009\u96c6\uff1a", None))
        self.line_selection.setInputMask("")
        self.line_selection.setPlaceholderText(QCoreApplication.translate("SelectionWidget", u"\u8f93\u5165\u9009\u96c6\u914d\u7f6e", None))
        self.button_setSelection.setText(QCoreApplication.translate("SelectionWidget", u"\u8bbe\u7f6e\u9009\u96c6", None))
        self.button_help.setText(QCoreApplication.translate("SelectionWidget", u"?", None))
        ___qtablewidgetitem = self.table_selection.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SelectionWidget", u"\u9009\u62e9", None));
        ___qtablewidgetitem1 = self.table_selection.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SelectionWidget", u"\u540d\u79f0", None));
        self.button_back.setText(QCoreApplication.translate("SelectionWidget", u"\u8fd4\u56de", None))
        self.button_next.setText(QCoreApplication.translate("SelectionWidget", u"\u7ee7\u7eed", None))
    # retranslateUi

