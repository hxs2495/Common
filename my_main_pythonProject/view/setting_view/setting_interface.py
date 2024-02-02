#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from .setting_untitled import Ui_MainWindow as settingMixinS


class SettingInterFace(settingMixinS, QMainWindow):
    switch_main_interface = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_setup()
        # self.init_conf()

    def init_setup(self):
        """初始化系统函数绑定"""
        self.Pivot.addItem("base_setting_view", text="基础设置",
                           onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(0))
        self.Pivot.addItem("senior_setting_view", text="高级设置",
                           onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(1))
        self.Pivot.addItem("update_setting_view", text="软件更新",
                           onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(2))
