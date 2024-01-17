# -*- coding: utf-8 -*-
# !/usr/bin/python
from enum import Enum

from PyQt5.QtWidgets import QMainWindow
from qfluentwidgets import StyleSheetBase, Theme, qconfig

from ui.untitled import Ui_MainWindow as MainMixinS


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    WINDOW = "window"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        print(theme, f"conf/static/qss/{theme.value.lower()}/{self.value}.qss")

        return f"conf/static/qss/{theme.value.lower()}/{self.value}.qss"


class MainWindow(MainMixinS, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.PushButton.clicked.connect(self.my_pushbutton)
        self.Slider.valueChanged.connect(self.my_Slider)
        self.HorizontalFlipView.addImages([
            'conf/static/img/2.jpg', 'conf/static/img/3.jpg', 'conf/static/img/1.png'
        ])
        self.PushButton_4.clicked.connect(self.set_topic)

    def my_pushbutton(self):
        print("按钮被触发")
        print(self.SwitchButton.isChecked())
        self.SwitchButton.setChecked(isChecked=True)
        self.ProgressRing.setValue(80)

        # w = MessageBox(
        #     '支持作者🥰',
        #     '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
        #     self
        # )
        # w.yesButton.setText('来啦老弟')
        # w.cancelButton.setText('下次一定')
        # w.show()

    def my_SwitchButton(self):
        text = self.SwitchButton.getText()
        print(text)

    def my_Slider(self):
        value = int(self.Slider.value())
        self.ProgressRing.setValue(value)

    def set_topic(self):
        print("正在切换主题")
        StyleSheet.WINDOW.apply(self, theme=Theme.DARK)
