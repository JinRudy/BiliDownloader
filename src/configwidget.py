import pickle
import traceback
from os.path import isdir

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QHeaderView

import style
from Lib.bili_api import video, exceptions
from Lib.bili_api.utils.passport import BiliPassport
from centralcheckbox import CentralCheckBox
from checkBoxHeader import CheckBoxHeader
from ui_configwidget import Ui_ConfigWidget
from utils import configUtils
from utils.removeSpecialChars import removeSpecialChars

# codec
video_codec_id = {
    7: "H.264(AVC):☆☆☆",
    12: "H.265(HEVC):☆☆",
    13: "AV1:☆",
}

video_get_id = {
    0: "全部类型",
    1: "读取视频",
    2: "读取音频",
    3: "读取弹幕",
}

video_codec_match = {}
for i in video_codec_id:
    video_codec_match[video_codec_id[i]] = i
video_get_match = {}
for i in video_get_id:
    video_get_match[video_get_id[i]] = i


class ConfigWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_ConfigWidget()
        self.ui.setupUi(self)
        codecs = []
        for i in video_codec_match:
            codecs.append(i)
        self.ui.combo_codec.addItems(codecs)

        getids = []
        for i in video_get_match:
            getids.append(i)
        self.ui.combo_get_type.addItems(getids)

        self.connect(
            self.ui.button_path,
            QtCore.SIGNAL("clicked()"),
            self.on_path_change_button_clicked,
        )
        self.connect(
            self.ui.button_submit,
            QtCore.SIGNAL("clicked()"),
            self.on_submit_button_clicked,
        )
        self.connect(
            self.ui.line_path,
            QtCore.SIGNAL("textChanged(QString)"),
            self.on_path_changed,
        )
        # 设置头部复选
        self.header = CheckBoxHeader()
        self.ui.table_downloads.setHorizontalHeader(self.header)
        self.header.select_all_clicked.connect(self.header.change_state)
        self.header.isOn = configUtils.UserDataHelper().get(configUtils.UserDataHelper().CONFIGS.SAVE_DANMAKU, False)

    # Slot
    def on_path_change_button_clicked(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",
            self.ui.line_path.text(),
            QFileDialog.ShowDirsOnly,
        )
        if len(path) == 0:
            return
        self.ui.line_path.setText(path)

    # Slot
    def on_submit_button_clicked(self):
        self.ui.button_submit.setDisabled(True)
        quality = self.quality_match[self.ui.combo_quality.currentText()]
        codec = video_codec_match[self.ui.combo_codec.currentText()]
        getid = video_get_match[self.ui.combo_get_type.currentText()]
        userdata = configUtils.UserDataHelper()
        # reserveAudio = configUtils.getUserData(configUtils.Configs.RESERVE_AUDIO, False)
        reserveAudio = userdata.get(userdata.CONFIGS.RESERVE_AUDIO, False) or getid == 2
        for i in self.data["download_data"]:
            box_danmaku: CentralCheckBox = i["box_danmaku"]
            push = {
                "path": self.ui.line_path.text(),
                "quality": quality,
                "codec": codec,
                "name": "{:0>3d}-".format(i["page"]) + removeSpecialChars(i["name"]),
                "title": removeSpecialChars(i["title"]),
                "id": i["id"],
                "isbvid": i["isbvid"],
                "cid": i["cid"],
                "reserveAudio": reserveAudio,
                "saveVideo": getid == 1 or getid == 0,
                "saveDanmaku": box_danmaku.get_box().isChecked() and (getid == 3 or getid == 0),
                "onlyOne": 1,
            }
            self.parent().download.push_task(push)
        self.parent().input_finished()

    # Slot
    def on_path_changed(self, path: str):
        ex = isdir(path)
        self.ui.button_submit.setEnabled(ex)
        if not ex:
            self.ui.line_path.setStyleSheet(style.BASIC_FONT_STYLE + style.RED_TEXT)
        else:
            self.ui.line_path.setStyleSheet(style.BASIC_FONT_STYLE)

    # Slot
    def update_info(self, data: QtCore.QByteArray, err: bool):
        data = pickle.loads(data.data())
        if err:
            QMessageBox.critical(self, "错误", data)
            self.ui.widget.setEnabled(False)
            self.ui.button_submit.setEnabled(False)
            return
        self.quality_match = {}
        for i in data:
            self.quality_match[i[1]] = i[0]
            self.ui.combo_quality.addItem(i[1])
        self.ui.widget.setEnabled(True)
        self.ui.button_submit.setEnabled(True)
        self.on_path_changed(self.ui.line_path.text())

    # Slot
    def load_finish(self):
        self.disconnect(self.load_thread)
        del self.load_thread

    def data_update(self, back):
        self.ui.widget.setEnabled(False)
        self.ui.button_submit.setEnabled(False)
        self.ui.combo_quality.clear()
        self.ui.table_downloads.setRowCount(0)
        userdata = configUtils.UserDataHelper()
        codec = userdata.get(userdata.CONFIGS.VIDEO_CODEC, 7)
        # codec = configUtils.getUserData(configUtils.Configs.VIDEO_CODEC, 7)
        self.ui.combo_codec.setCurrentText(video_codec_id[codec])
        self.data = self.parent().input_pages[2].data
        self.ui.line_path.setText(
            userdata.get(
                userdata.CONFIGS.DOWNLOAD_PATH,  # User
                QtCore.QDir("Download").absolutePath()  # Default
            )
        )
        download_danmaku = userdata.get(userdata.CONFIGS.SAVE_DANMAKU, False)
        # download_danmaku = configUtils.getUserData(configUtils.Configs.SAVE_DANMAKU, False)
        self.data["download_data"] = []
        for i in self.data["page_data"]:
            if not i["box"].get_box().isChecked():
                continue
            self.ui.table_downloads.setRowCount(self.ui.table_downloads.rowCount() + 1)
            i["box_danmaku"] = CentralCheckBox()
            i["box_danmaku"].get_box().setChecked(download_danmaku)
            self.header.append(i["box_danmaku"])
            self.ui.table_downloads.setCellWidget(
                self.ui.table_downloads.rowCount() - 1, 0, i["box_danmaku"]
            )
            self.ui.table_downloads.setItem(
                self.ui.table_downloads.rowCount() - 1, 1, QTableWidgetItem(i["name"])
            )
            self.data["download_data"].append(i)
        page = self.data["page_data"][0]
        self.load_thread = GetVideoInfo(page["id"], page["isbvid"], page["cid"], self)
        self.connect(
            self.load_thread,
            QtCore.SIGNAL("update_info(QByteArray, bool)"),
            self.update_info,
        )
        self.connect(
            self.load_thread,
            QtCore.SIGNAL("finished()"),
            self.load_finish,
        )
        self.load_thread.start()


class GetVideoInfo(QtCore.QThread):
    def __init__(
        self, vid, isbvid: bool, cid, parent: QtCore.QObject | None = ...
    ) -> None:
        super().__init__(parent)
        self.vid = vid
        self.isbvid = isbvid
        self.cid = cid
        self.update_info = QtCore.Signal(QtCore.QByteArray, bool)

    def run(self):
        data = None
        err = False
        passport = configUtils.getUserData(configUtils.Configs.PASSPORT)
        if passport is not None:
            passport = BiliPassport(passport["data"])
        try:
            if self.isbvid:
                data = video.get_video_url(bvid=self.vid, cid=self.cid, passport=passport)
            else:
                data = video.get_video_url(avid=self.vid, cid=self.cid, passport=passport)
            quality = []
            for i in range(len(data["accept_quality"])):
                quality.append(
                    (data["accept_quality"][i], data["accept_description"][i])
                )
            data = quality
        except exceptions.NetWorkException as ex:
            data = str(ex)
            err = True
        except Exception as ex:
            data = traceback.format_exc()
            err = True
        data = pickle.dumps(data)
        data = QtCore.QByteArray(data)
        self.emit(QtCore.SIGNAL("update_info(QByteArray,bool)"), data, err)
