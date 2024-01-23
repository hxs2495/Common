#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QMainWindow, QLabel
from .secord_untitled import Ui_MainWindow as secordMixinS


class Secord_Interface(secordMixinS, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
