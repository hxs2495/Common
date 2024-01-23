from PyQt5.QtWidgets import QMainWindow, QLabel
from .setting_untitled import Ui_MainWindow as settingMixinS


class Setting_InterFace(settingMixinS, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Pivot.addItem(routeKey="基础设置", text="基础设置", onClick=lambda: self.load_page(0))
        self.Pivot.addItem(routeKey="高级设置", text="高级设置", onClick=lambda: self.load_page(1))
        self.Pivot.addItem(routeKey="关于本机", text="关于本机", onClick=lambda: self.load_page(2))

    def load_page(self, index):
        self.PopUpAniStackedWidget.setCurrentIndex(index)
