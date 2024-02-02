#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from conf import setting
from lib import common_function
from .init_untitled import Ui_MainWindow as initializeMixinS


class InitInterFace(initializeMixinS, QMainWindow):
    switch_main_interface = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_setup()
        self.init_conf()

    def init_setup(self):
        """初始化系统函数绑定"""
        # 下一步
        self.start_init_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(1))
        self.nextsetup_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(2))
        self.nextsetup_pushButton_2.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(3))
        self.nextsetup_pushButton_3.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(4))
        self.nextsetup_pushButton_4.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(5))
        self.add_linkpeople_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(6))
        self.nextsetup_pushButton_5.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(8))
        self.nextsetup_pushButton_6.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(7))
        self.add_linkpeople_pushButton2.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(7))
        self.nextsetup_pushButton_7.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(8))
        self.nextsetup_pushButton_8.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(9))
        self.nextsetup_pushButton_9.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(10))
        self.nextsetup_pushButton_9.clicked.connect(self.open_init_progressBar)
        # 上一步
        self.lastsetup_pushButton.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(0))
        self.lastsetup_pushButton_2.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(1))
        self.lastsetup_pushButton_3.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(2))
        self.lastsetup_pushButton_4.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(3))
        self.lastsetup_pushButton_5.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(4))
        self.lastsetup_pushButton_6.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(5))
        self.lastsetup_pushButton_7.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(6))
        self.lastsetup_pushButton_8.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(5))
        self.lastsetup_pushButton_9.clicked.connect(lambda: self.PopUpAniStackedWidget.setCurrentIndex(8))

        self.country_ListWidget.itemClicked.connect(self.on_listWidget_clicked)
        self.language_ListWidget.itemClicked.connect(self.on_listWidget_clicked)
        self.wifi_listWidget.itemClicked.connect(self.on_listWidget_clicked)

    def init_conf(self):
        # 默认显示首页
        self.PopUpAniStackedWidget.setCurrentIndex(0)
        # 加载配置数据
        common_function.load_file_content(filepath=setting.user_agreement_path,
                                          controlname=self.user_agreement_textEdit)

        self.country_ListWidget.addItems(setting.country_list)
        self.language_ListWidget.addItems(setting.language_list)
        self.wifi_listWidget.addItems(setting.wifi_name_list)

        self.linkpeople_relationship_comboBox_1.addItems(setting.contact_relationship_list)
        self.linkpeople_relationship_comboBox_2.addItems(setting.contact_relationship_list)
        self.linkpeople_relationship_comboBox_3.addItems(setting.contact_relationship_list)
        self.linkpeople_relationship_comboBox_4.addItems(setting.contact_relationship_list)
        self.linkpeople_relationship_comboBox_5.addItems(setting.contact_relationship_list)
        self.linkpeople_relationship_comboBox_6.addItems(setting.contact_relationship_list)

    def on_listWidget_clicked(self, item):
        print(item.text())
        if item.text() == setting.test_wifi_name:
            self.wifipassword_lineEdit.setText(setting.test_wifi_password)
        else:
            self.wifipassword_lineEdit.clear()
        self.wifiname_lineEdit.setText(item.text())

    def open_init_progressBar(self):
        self.PopUpAniStackedWidget.setCurrentIndex(10)
        # 使用QTimer实现3秒后跳转
        QTimer.singleShot(3000, self.open_mainview)

    def open_mainview(self):
        # 关闭当前窗口
        self.close()
        # 打开新的mainview窗口
        # 发送信号
        self.switch_main_interface.emit()
