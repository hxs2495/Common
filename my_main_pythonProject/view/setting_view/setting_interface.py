#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from .setting_untitled import Ui_MainWindow as settingMixinS


class Setting_InterFace(settingMixinS, QMainWindow):
    switch_main_interface = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.init_setup()
        # self.init_conf()

    # def init_setup(self):
    #     """初始化系统函数绑定"""
    #     self.NavigationBar.addItem(
    #         routeKey="chat",
    #         icon=FluentIcon.CHAT,
    #         text="聊天",
    #         position=NavigationItemPosition.TOP,
    #         onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(0)
    #
    #     )
    #
    #     self.NavigationBar.addItem(
    #         routeKey="setting",
    #         icon=FluentIcon.SETTING,
    #         text="设置",
    #         position=NavigationItemPosition.BOTTOM,
    #         onClick=lambda: self.PopUpAniStackedWidget.setCurrentIndex(1)
    #     )
    #
    #     self.CommandBar.addActions([Action(FluentIcon.PHONE, '音频通话', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.VIDEO, '视频通话', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.ACCEPT, '接听来电', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.REMOVE_FROM, '拒绝来电', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.CHAT, '随机聊一聊', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.REMOVE, '拉黑用户', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.VIEW, '查看黑名单', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.DELETE, '删除记录', triggered=self.on_CommandBar_clicked),
    #                                 Action(FluentIcon.ADD, '更多记录', triggered=self.on_CommandBar_clicked)])
    #
    #     self.SegmentedWidget.addItem(routeKey="contacts_people", text="联系人", onClick=self.load_contacts_people_list)
    #
    #     self.SegmentedWidget.addItem(routeKey="recent_contacts", text="最近联系", onClick=self.recent_contacts_list)
    #
    #     self.linkpeople_name_listWidget.itemClicked.connect(self.on_listWidget_clicked)
    #
    #     # 信号与槽
    #     self.PrimaryPushButton.clicked.connect(self.sendLeftMessage)  # 左侧发送按钮点击事件
    #     self.pushButtonLeft.clicked.connect(self.sendRightMessage)  # 右侧发送按钮点击事件
    #
    # def init_conf(self):
    #     # 初始化加载数据
    #     self.recent_contacts_list()
    #
    # def load_contacts_people_list(self):
    #     self.linkpeople_name_listWidget.clear()
    #     self.linkpeople_name_listWidget.addItems(setting.contacts_people_list)
    #
    # def recent_contacts_list(self):
    #     self.linkpeople_name_listWidget.clear()
    #
    #     self.linkpeople_name_listWidget.addItems(setting.recent_contacts_list)
    #
    # def on_listWidget_clicked(self, item):
    #     print(item.text())
    #     self.target_name.setText(item.text())
    #
    # def on_CommandBar_clicked(self):
    #     print("触发")
    #
    # def sendLeftMessage(self):
    #     self.text = self.chat_TextEdit.toPlainText()
    #     self.chat_TextEdit.setPlainText("")
    #     TEXT = MessageType.Text
    #
    #     receive_avatar = 'conf/static/material/7.jpg'
    #     bubble_message = BubbleMessage(self.text, receive_avatar, Type=TEXT, is_send=True)
    #     self.w1.add_message_item(bubble_message)
    #
    #
    # def sendRightMessage(self):
    #     self.text = self.chat_TextEdit.toPlainText()
    #     self.chat_TextEdit.setPlainText("")
    #     send_avatar = 'conf/static/material/8.jpg'
    #     IMAGE = MessageType.Image
    #     TEXT = MessageType.Text
    #     bubble_message = BubbleMessage(self.text, send_avatar, Type=TEXT, is_send=False)
    #     self.w1.add_message_item(bubble_message)
