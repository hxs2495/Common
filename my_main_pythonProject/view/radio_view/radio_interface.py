#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from conf import setting
from lib.common_function import load_urlview
from .radio_untitled import Ui_MainWindow as radioMixinS


class RadioInterFace(radioMixinS, QMainWindow):
    switch_main_interface = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        load_urlview(widget=self.music_widget, url=setting.radio_url)
        # self.PushButton.clicked.connect(lambda: self.switch_main_interface.emit())
