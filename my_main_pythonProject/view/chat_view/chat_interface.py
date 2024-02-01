#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from qfluentwidgets import FluentIcon, NavigationItemPosition, Action

from conf import setting
from .bubble_message import BubbleMessage, ChatWidget, MessageType, Notice
from .chat_untitled import Ui_MainWindow as chatMixinS


class Chat_InterFace(chatMixinS, QMainWindow):
    switch_main_interface = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.message_view = ChatWidget()

        time_message = Notice(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
        self.message_view.add_message_item(time_message)

        self.verticalLayout_3.addWidget(self.message_view)
        # self.frame.setLayout(layout)

        self.init_setup()
        self.init_conf()

    def init_setup(self):
        """初始化系统函数绑定"""
        self.NavigationBar.addItem(
            routeKey="chat",
            icon=FluentIcon.CHAT,
            text="聊天",
            position=NavigationItemPosition.TOP,
            onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(0)

        )

        self.NavigationBar.addItem(
            routeKey="setting",
            icon=FluentIcon.SETTING,
            text="设置",
            position=NavigationItemPosition.SCROLL,
            onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(1)
        )
        self.NavigationBar.addItem(
            routeKey="return",
            icon=FluentIcon.RETURN,
            text="返回",
            position=NavigationItemPosition.BOTTOM,
            onClick=lambda: self.switch_main_interface.emit()
        )
        self.CommandBar.addActions([Action(FluentIcon.PHONE, '音频通话', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.VIDEO, '视频通话', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.ACCEPT, '接听来电', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.REMOVE_FROM, '挂断电话', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.PHOTO, '发送图片',
                                           triggered=lambda: self.send_message(avatar_path='conf/static/material/7.jpg',
                                                                               imges='conf/static/material/8.jpg',
                                                                               message_type=MessageType.Image,
                                                                               is_send=True)),
                                    Action(FluentIcon.CHAT, '随机聊一聊', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.REMOVE, '拉黑用户', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.VIEW, '查看黑名单', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.DELETE, '删除记录', triggered=self.on_CommandBar_clicked),
                                    Action(FluentIcon.ADD, '更多记录', triggered=self.on_CommandBar_clicked)])

        self.SegmentedWidget.addItem(routeKey="contacts_people", text="通讯录", onClick=self.load_contacts_people_list)

        self.SegmentedWidget.addItem(routeKey="recent_contacts", text="最近", onClick=self.recent_contacts_list)

        self.linkpeople_name_listWidget.itemClicked.connect(self.on_listWidget_clicked)

        # 信号与槽
        self.PrimaryPushButton.clicked.connect(
            lambda: self.send_message(avatar_path='conf/static/material/7.jpg', text=self.chat_TextEdit.toPlainText(),
                                      message_type=MessageType.Text, is_send=True))  # 左侧发送按钮点击事件
        self.pushButtonLeft.clicked.connect(
            lambda: self.send_message(avatar_path='conf/static/material/8.jpg', text=self.chat_TextEdit.toPlainText(),
                                      message_type=MessageType.Text, is_send=False))  # 右侧发送按钮点击事件

    def init_conf(self):
        # 初始化加载数据
        self.recent_contacts_list()

    def load_contacts_people_list(self):
        self.linkpeople_name_listWidget.clear()
        self.linkpeople_name_listWidget.addItems(setting.contacts_people_list)

    def recent_contacts_list(self):
        self.linkpeople_name_listWidget.clear()

        self.linkpeople_name_listWidget.addItems(setting.recent_contacts_list)

    def on_listWidget_clicked(self, item):
        print(item.text())
        self.target_name.setText(item.text())

    def on_CommandBar_clicked(self):
        print("触发")

    def send_message(self, avatar_path, text=None, imges=None, message_type=MessageType.Text, is_send=True):
        self.chat_TextEdit.setPlainText("")

        if message_type == MessageType.Text:
            bubble_message = BubbleMessage(str_content=text, avatar=avatar_path, Type=message_type, is_send=is_send)
            self.message_view.add_message_item(bubble_message)
            self.message_view.verticalScrollBar().setValue(self.message_view.verticalScrollBar().maximum())
            return

        bubble_message = BubbleMessage(str_content=imges, avatar=avatar_path, Type=MessageType.Image, is_send=False)
        self.message_view.add_message_item(bubble_message)

        self.message_view.verticalScrollBar().setValue(self.message_view.verticalScrollBar().maximum())
