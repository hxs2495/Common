#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QMainWindow, QLabel
from .init_untitled import Ui_MainWindow as initializeMixinS


class Init_InterFace(initializeMixinS, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lastsetup_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(0))
        self.lastsetup_pushButton_2.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(1))
        self.lastsetup_pushButton_3.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(2))
        self.lastsetup_pushButton_4.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(3))
        self.lastsetup_pushButton_5.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(4))
        self.lastsetup_pushButton_6.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(5))
        self.lastsetup_pushButton_7.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(6))
        self.lastsetup_pushButton_8.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(7))
        self.lastsetup_pushButton_9.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(8))

        # 下一步
        self.start_init_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(1))
        self.nextsetup_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(2))
        self.nextsetup_pushButton_2.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(3))
        self.nextsetup_pushButton_3.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(4))
        self.nextsetup_pushButton_4.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(5))

        self.nextsetup_pushButton_8.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(9))
        # self.nextsetup_pushButton_9.clicked.connect(self.open_init_progressBar)
