# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import QApplication

from lib.common_function import day_logger
from view.view_manage.manage_interface import Manage_InterFace


def apply_stylesheet(app):
    style_file = QFile("conf/static/qss/QScrollArea.qss")  # 替换为你的QSS文件路径
    if style_file.open(QIODevice.ReadOnly | QIODevice.Text):
        style_data = style_file.readAll()
        style_file.close()
        app.setStyleSheet(str(style_data, encoding='utf-8'))
    else:
        print("无法打开QSS文件")


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app)
    manageview = Manage_InterFace()
    # 先将两个窗口都显示出来
    manageview.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    day_logger()
    main()
