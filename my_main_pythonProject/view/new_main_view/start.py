# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication

from new_main_interface import NewMainInterFace


def main():
    app = QApplication(sys.argv)
    manageview = NewMainInterFace()
    # 先将两个窗口都显示出来
    manageview.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()