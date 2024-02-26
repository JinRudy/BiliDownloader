from PySide2 import QtWidgets, QtCore

from dialogchangelog import show_changelog
from ui_videosubwidget import Ui_VideoSubwidget
from utils import version


class VideoSubWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_VideoSubwidget()
        self.ui.setupUi(self)
        self.ui.label_version.setText("视频剪辑")
        self.connect(
            self.ui.button_changelog,
            QtCore.SIGNAL("clicked()"),
            self.on_button_changelog_clicked
        )

    def on_button_changelog_clicked(self):
        show_changelog(self)

    def update_tab_changes(self, old, now):
        pass
