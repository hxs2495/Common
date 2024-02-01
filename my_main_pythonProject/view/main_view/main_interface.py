#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from .main_untitled import Ui_MainWindow as MainMixinS


class Main_Interface(MainMixinS, QMainWindow):
    switch_interface = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 加载图标
        self.load_icon()
        # 绑定触发函数
        self.init_setup()

    def load_icon(self):
        # 设置按钮图标
        buttons = [(self.telephonecall_pushButton, 'chat.png'),
                   (self.music_player_pushButton, 'support.png'),
                   (self.video_player_pushButton, 'video.png'),
                   (self.enter_second_view_pushButton, 'enter2.png'),
                   (self.internet_rudion_pushButton, 'warehouse.png'),
                   (self.alarm_clock_pushButton, 'alarm.png'),
                   (self.wificonnect_pushButton, 'free-wifi.png'),
                   (self.blutooth_pushButton, 'bluetooth.png'),
                   (self.select_weather_pushButton, 'clouds.png'),
                   (self.healthydata_pushButton, 'heartbeat.png'),
                   (self.calendar_pushButton, 'schedule.png'),
                   (self.schedule_pushButton, 'calendar.png'),
                   (self.smart_chat_pushButton, 'smart_chat.png'),
                   (self.volume_brightness_pushButton, 'sound.png'),
                   (self.shutdown_pushButton, 'shutdown.png'),
                   (self.set_base_pushButton, 'settings.png'),
                   (self.sound_phonechat_pushButton, 'microphone.png'),
                   (self.set_add_pushButton, 'add.png'),

                   ]
        common_button_style = """
            QPushButton {
                border: none;
                background-color: transparent;
            }
        """

        for button, icon in buttons:
            button.setStyleSheet(common_button_style)
            button.setIcon(QIcon(f'conf/static/icon/{icon}'))
            button.setIconSize(button.size())

    def init_setup(self):
        """初始化系统函数绑定"""
        # 绑定主显示界面按钮
        self.time_label.clicked.connect(self.open_setview)
        self.tips_label.clicked.connect(self.open_setview)
        self.telephonecall_pushButton.clicked.connect(lambda: self.switch_interface.emit("chat"))
        self.music_player_pushButton.clicked.connect(lambda: self.switch_interface.emit("music"))

        self.enter_second_view_pushButton.clicked.connect(self.open_setview)
        # 绑定返回按钮
        self.home_pushButton.clicked.connect(self.open_mainview)
        self.home_pushButton_2.clicked.connect(self.open_setview)
        self.home_pushButton_3.clicked.connect(self.open_setview)
        self.home_pushButton_4.clicked.connect(self.open_mainview)
        # 绑定功能界面
        self.set_base_pushButton.clicked.connect(self.open_basesetview)
        self.alarm_clock_pushButton.clicked.connect(lambda: self.open_minor_functionview(0))
        self.wificonnect_pushButton.clicked.connect(lambda: self.open_minor_functionview(1))
        self.blutooth_pushButton.clicked.connect(lambda: self.open_minor_functionview(2))
        self.select_weather_pushButton.clicked.connect(lambda: self.open_minor_functionview(3))
        self.calendar_pushButton.clicked.connect(lambda: self.open_minor_functionview(4))
        self.healthydata_pushButton.clicked.connect(lambda: self.open_minor_functionview(5))
        self.shutdown_pushButton.clicked.connect(lambda: self.open_minor_functionview(6))
        self.volume_brightness_pushButton.clicked.connect(lambda: self.open_minor_functionview(7))
        self.smart_chat_pushButton.clicked.connect(lambda: self.open_minor_functionview(10))
        self.schedule_pushButton.clicked.connect(lambda: self.open_minor_functionview(8))

    # def load_htmlview(self):
    #     # 加载主页日期
    #     common_function.load_htmlview(frame=self.weather_pushButton,
    #                                   file_path=r"conf/static/html/mainview_weather.html")
    #     # 加载天气预报
    #     # common_function.load_htmlview(frame=self.weather_widget, file_path=r"conf/static/html/weather.html")
    #     # # 加载音乐
    #     # common_function.load_urlview(widget=self.music_widget, url=setting.music_url)
    #     # # 加载电台
    #     # common_function.load_urlview(widget=self.radio_widget, url=setting.rudion_url)
    #     # # 加载视频
    #     # common_function.load_urlview(widget=self.video_widget, url=setting.video_url)

    # # 窗口大小发生变化时自动触发该函数，重置背景
    # def resizeEvent(self, event):
    #     # 设置窗体背景图片
    #     palette = QPalette()
    #     brush = QBrush(QPixmap("conf/static/material/14.jpg").scaled(self.width(), self.height()))
    #     # brush = QBrush(QPixmap(config.get('imagepath', 'path')).scaled(self.width(), self.height()))
    #     palette.setBrush(QPalette.Background, brush)
    #     self.setPalette(palette)
    #     # 设置不影响其他控件背景
    #     self.setAutoFillBackground(True)

    def open_mainview(self):
        """
        返回主界面
        """
        self.PopUpAniStackedWidget.setCurrentIndex(0)

    def open_setview(self):
        """打开次界面"""
        self.PopUpAniStackedWidget.setCurrentIndex(1)

    def open_minor_functionview(self, index):
        """打开辅助功能界面视图"""
        self.PopUpAniStackedWidget.setCurrentIndex(2)
        self.tabWidget_function.setCurrentIndex(index)

    def open_basesetview(self):
        """打开设置界面视图"""
        self.PopUpAniStackedWidget.setCurrentIndex(3)
