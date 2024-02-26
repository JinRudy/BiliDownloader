# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settingswidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(457, 316)
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        SettingsWidget.setFont(font)
        self.gridLayout = QGridLayout(SettingsWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_login = QPushButton(SettingsWidget)
        self.button_login.setObjectName(u"button_login")

        self.gridLayout.addWidget(self.button_login, 1, 2, 1, 1)

        self.combo_codec = QComboBox(SettingsWidget)
        self.combo_codec.setObjectName(u"combo_codec")

        self.gridLayout.addWidget(self.combo_codec, 3, 1, 1, 1)

        self.line_path = QLineEdit(SettingsWidget)
        self.line_path.setObjectName(u"line_path")
        self.line_path.setStyleSheet(u"font: 11pt \"HarmonyOS Sans SC\";")

        self.gridLayout.addWidget(self.line_path, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.label_4 = QLabel(SettingsWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_2 = QLabel(SettingsWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.line = QFrame(SettingsWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 1, 1, 1)

        self.button_reset = QPushButton(SettingsWidget)
        self.button_reset.setObjectName(u"button_reset")

        self.gridLayout.addWidget(self.button_reset, 8, 2, 1, 1)

        self.line_2 = QFrame(SettingsWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)

        self.check_danmaku = QCheckBox(SettingsWidget)
        self.check_danmaku.setObjectName(u"check_danmaku")

        self.gridLayout.addWidget(self.check_danmaku, 6, 1, 1, 1)

        self.line_5 = QFrame(SettingsWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 7, 1, 1, 1)

        self.label_5 = QLabel(SettingsWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.button_path = QPushButton(SettingsWidget)
        self.button_path.setObjectName(u"button_path")

        self.gridLayout.addWidget(self.button_path, 0, 2, 1, 1)

        self.line_login = QLineEdit(SettingsWidget)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setReadOnly(True)

        self.gridLayout.addWidget(self.line_login, 1, 1, 1, 1)

        self.label = QLabel(SettingsWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(SettingsWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.line_4 = QFrame(SettingsWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 1)

        self.line_3 = QFrame(SettingsWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 2, 1, 1)

        self.check_reserve_audio = QCheckBox(SettingsWidget)
        self.check_reserve_audio.setObjectName(u"check_reserve_audio")

        self.gridLayout.addWidget(self.check_reserve_audio, 5, 1, 1, 1)

        self.label_6 = QLabel(SettingsWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.line_6 = QFrame(SettingsWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 7, 2, 1, 1)

        self.label_7 = QLabel(SettingsWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.spin_threads = QSpinBox(SettingsWidget)
        self.spin_threads.setObjectName(u"spin_threads")
        self.spin_threads.setMinimum(1)
        self.spin_threads.setMaximum(8)

        self.gridLayout.addWidget(self.spin_threads, 2, 1, 1, 1)

        self.label_8 = QLabel(SettingsWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.button_login.setText(QCoreApplication.translate("SettingsWidget", u"\u767b\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWidget", u"\u4e0b\u8f7d\u5f39\u5e55", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWidget", u"\u767b\u5f55B\u7ad9", None))
        self.button_reset.setText(QCoreApplication.translate("SettingsWidget", u"\u91cd\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWidget", u"\u91cd\u7f6e\u8bbe\u7f6e", None))
        self.button_path.setText(QCoreApplication.translate("SettingsWidget", u"\u8bbe\u7f6e\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"\u9ed8\u8ba4\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWidget", u"\u4fdd\u7559\u4e0b\u8f7d\u7684\u97f3\u9891\u6587\u4ef6", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWidget", u"\u9ed8\u8ba4\u4f18\u9009\u7f16\u7801", None))
        self.label_7.setText(QCoreApplication.translate("SettingsWidget", u"\u6700\u5927\u4e0b\u8f7d\u7ebf\u7a0b\u6570", None))
        self.label_8.setText(QCoreApplication.translate("SettingsWidget", u"\u91cd\u542f\u751f\u6548", None))
    # retranslateUi

